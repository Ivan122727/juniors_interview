# Объединяем отрезки [1, 2, 2, 3, 4, 6, 5, 12] -> [1, 3, 4, 12]
def union_intervals(intervals: list[int]) -> list[int]:
    res = list()
    for i in range(1, len(intervals), 2):
        if len(res) and res[-1] >= intervals[i - 1]:
            res[-2] = min(res[-2], intervals[i - 1])
            res[-1] = max(res[-1], intervals[i])
        else:
            res.append(intervals[i - 1])
            res.append(intervals[i])
    return res

# Удаляем интервалы до начала урока
def delete_before_lesson(arr: list[int], start: int) -> list[int]:
    while len(arr) and arr[1] < start:
        arr.pop(0)
        arr.pop(0)
    if len(arr):
        arr[0] = max(start, arr[0])
    return arr

# Удаляем интервалы после окончания урока
def delete_after_lesson(arr: list[int], finish: int) -> list[int]:
    while len(arr) and arr[-2] >= finish:
        arr.pop(-1)
        arr.pop(-1)
    if len(arr):
        arr[-1] = min(finish, arr[-1])
    return arr

# Удаляем интервалы вне урока
def delete_out_of_lesson(intervals: list[int], start: int, finish: int) -> list[int]:
    intervals = delete_before_lesson(intervals, start)
    intervals = delete_after_lesson(intervals, finish)
    return intervals


def normalize_intervals(intervals: list[int], start: int, finish: int) -> list[int]:
    normalized_intervals = union_intervals(intervals)
    normalized_intervals = delete_out_of_lesson(normalized_intervals, start, finish)
    return normalized_intervals


def appearance(intervals: dict[str, list[int]]) -> int:
    start = intervals['lesson'][0]
    finish = intervals['lesson'][1]
    tutor = normalize_intervals(intervals['tutor'], start, finish)
    pupil = normalize_intervals(intervals['pupil'], start, finish)
    p_index = 1
    count = 0
    for t_index in range(1, len(tutor), 2):
        while p_index < len(pupil) and tutor[t_index] > pupil[p_index - 1]:
            left = max(tutor[t_index - 1], pupil[p_index - 1])
            right = min(tutor[t_index], pupil[p_index])
            count += max(right - left, 0)
            if tutor[t_index] >= pupil[p_index]:
                p_index += 2
            else:
                break
    return count


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
      {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594691500, 1594692000, 1594695600, 1594695800],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 0
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
