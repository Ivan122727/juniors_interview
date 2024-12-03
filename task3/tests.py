import unittest
from solution import appearance


class TestStrictDecorator(unittest.TestCase):
    # Базовый тест где интераллы "нормализованны"
    def test_base(self):
        test = {
            'intervals': {
                'lesson': [10, 60],
                'pupil': [11, 15, 17, 55],
                'tutor': [10, 14, 16, 60],
            },
            'answer': 41
        }
        self.assertEqual(appearance(test['intervals']), test['answer'])

    # Тест где ученик был только до начала урока
    def test_pupil_only_before_lesson(self):
        test = {
            'intervals': {
                'lesson': [10, 60],
                'pupil': [0, 5, 4, 10],
                'tutor': [10, 14, 16, 60],
            },
            'answer': 0
        }
        self.assertEqual(appearance(test['intervals']), test['answer'])

    # Тест где ученик был только после окончания урока
    def test_pupil_only_after_lesson(self):
        test = {
            'intervals': {
                'lesson': [10, 60],
                'pupil': [60, 65, 64, 70],
                'tutor': [10, 14, 16, 60],
            },
            'answer': 0
        }
        self.assertEqual(appearance(test['intervals']), test['answer'])

    # Тест где ученик заходил до начала урока и только после окончания
    def test_pupil_after_and_beffor_lesson(self):
        test = {
            'intervals': {
                'lesson': [10, 60],
                'pupil': [0, 5, 4, 10, 60, 65, 64, 70],
                'tutor': [10, 14, 16, 60],
            },
            'answer': 0
        }
        self.assertEqual(appearance(test['intervals']), test['answer'])

     # Тест где учитель был только до начала урока
    def test_tutor_only_before_lesson(self):
        test = {
            'intervals': {
                'lesson': [10, 60],
                'pupil': [10, 14, 16, 60],
                'tutor': [0, 5, 4, 10],
            },
            'answer': 0
        }
        self.assertEqual(appearance(test['intervals']), test['answer'])

    # Тест где учитель был только после окончания урока
    def test_tutor_only_after_lesson(self):
        test = {
            'intervals': {
                'lesson': [10, 60],
                'pupil': [10, 14, 16, 60],
                'tutor': [60, 65, 64, 70],
            },
            'answer': 0
        }
        self.assertEqual(appearance(test['intervals']), test['answer'])

    # Тест где учитель заходил до начала урока и только после окончания
    def test_tutor_after_and_beffor_lesson(self):
        test = {
            'intervals': {
                'lesson': [10, 60],
                'pupil': [10, 14, 16, 60],
                'tutor': [0, 5, 4, 10, 60, 65, 64, 70],
            },
            'answer': 0
        }
        self.assertEqual(appearance(test['intervals']), test['answer'])


    # Тест где все вместе(зашел, вышел до и после урока + во время урока сидел с двух вкладок) для ученика
    def test_mixed_pupil(self):
        test = {
            'intervals': {
                'lesson': [2765, 6365],
                'pupil': [2754, 4465, 2772, 4507, 4477, 4478, 4529, 5115, 4546, 4547, 4699, 4974, 5060, 5061, 5071, 6445, 5123, 5738, 5814, 6445, 6465, 6840, 6467, 6468, 6489, 6489, 6544, 6606],
                'tutor': [0, 329, 2714, 5113, 5114, 6428]
            },
            'answer': 3577
        }
        self.assertEqual(appearance(test['intervals']), test['answer'])

     # Тест где все вместе(зашел, вышел до и после урока + во время урока сидел с двух вкладок) для учителя
    def test_mixed_tutor(self):
        test = {
            'intervals': {
                'lesson': [2765, 6365],
                'pupil': [0, 329, 2714, 5113, 5114, 6428],
                'tutor': [2754, 4465, 2772, 4507, 4477, 4478, 4529, 5115, 4546, 4547, 4699, 4974, 5060, 5061, 5071, 6445, 5123, 5738, 5814, 6445, 6465, 6840, 6467, 6468, 6489, 6489, 6544, 6606],
            },
            'answer': 3577
        }
        self.assertEqual(appearance(test['intervals']), test['answer'])

     # Тест где все вместе(зашел, вышел до и после урока + во время урока сидел с двух вкладок) для учителя
    def test_mixed_tutor_and_pupil(self):
        test = {
            'intervals': {
                'lesson': [2765, 6365],
                'pupil': [0, 2740, 2714, 2780, 5114, 5145, 5116, 5143, 5144, 5149, 5146, 6379],
                'tutor': [2754, 4465, 2772, 4507, 4477, 4478, 4529, 5115, 4546, 4547, 4699, 4974, 5060, 5061, 5071, 6445, 5123, 5738, 5814, 6445, 6465, 6840, 6467, 6468, 6489, 6489, 6544, 6606],
            },
            'answer': 1266
        }
        self.assertEqual(appearance(test['intervals']), test['answer'])

    def test_out_lesson_pupil_tutor(self):
        test = {
            'intervals': {
                'lesson': [10, 60],
                'pupil': [0, 5, 4, 10, 60, 65, 64, 70],
                'tutor': [0, 5, 4, 10, 60, 65, 64, 70],
            },
            'answer': 0
        }
        self.assertEqual(appearance(test['intervals']), test['answer'])


if __name__ == "__main__":
    unittest.main()
