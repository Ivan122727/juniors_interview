import asyncio
import csv
import unittest
import aiohttp
from aiounittest import AsyncTestCase

from solution import get_links_by_url

# Словарь с правильным количеством на каждую букву
count_animal_titles_dict = {
    "А": 1167,
    "Б": 1158,
    "В": 496,
    "Г": 874,
    "Д": 802,
    "Е": 105,
    "Ё": 2,
    "Ж": 339,
    "З": 644,
    "И": 367,
    "Й": 4,
    "К": 1056,
    "Л": 724,
    "М": 771,
    "Н": 495,
    "О": 752,
    "П": 1384,
    "Р": 518,
    "С": 1369,
    "Т": 978,
    "У": 281,
    "Ф": 200,
    "Х": 296,
    "Ц": 240,
    "Ч": 288,
    "Ш": 289,
    "Щ": 160,
    "Ъ": 0,
    "Ы": 0,
    "Ь": 0,
    "Э": 234,
    "Ю": 148,
    "Я": 224,
}


class TestAsyncFunctions(AsyncTestCase):
    # Проверка на получение ссылок
    async def test_get_links_by_url(self):
        async with aiohttp.ClientSession() as session:
            links = await get_links_by_url(session)
            self.assertEqual(len(links), 392)

    # Проверка на порядок букв и на наличие лишних букв
    async def test_csv_order_and_letters(self):
        expected_order = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        actual_order = []
        with open('beasts.csv', 'r', encoding='utf8', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                letter = row[0]
                actual_order.append(letter)
        actual_order_str = ''.join(actual_order)
        self.assertEqual(actual_order_str, expected_order)

    # Проверка на количество Букв
    async def test_csv_counts(self):
        actual_counts = {}
        with open('beasts.csv', 'r', encoding='utf8', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                letter, count = row
                actual_counts[letter] = int(count)
        self.assertEqual(actual_counts, count_animal_titles_dict)


if __name__ == "__main__":
    asyncio.run(unittest.main())
