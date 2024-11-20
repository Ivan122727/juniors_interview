import asyncio
import csv
import aiohttp
from bs4 import BeautifulSoup


BASE_URL = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
RUSSIAN_ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


async def get_links_by_url(session: aiohttp.ClientSession) -> set[str]:
    async with session.get(BASE_URL) as response:
        soup = BeautifulSoup(await response.text(), 'html.parser')
        links_container = soup.select_one(
            'div.ts-module-Индекс_категории-container'
        )
        links = set()
        for letter_category in links_container:
            for link in letter_category:
                links.add(link.find('a')['href'])
        return links


async def get_animal_titles_by_link(link: str, session: aiohttp.ClientSession) -> set[str]:
    async with session.get(link) as response:
        soup = BeautifulSoup(await response.text(), 'html.parser')
        content = soup.select('div.mw-content-ltr')[-1]
        animal_titles = set()
        for animal_title in content.find_all('a'):
            animal_titles.add(animal_title['title'])
        return animal_titles


async def main():
    founded_animal_titles = set()
    # Парсим данные
    async with aiohttp.ClientSession() as session:
        links = await get_links_by_url(session)
        tasks = [get_animal_titles_by_link(link, session) for link in links]
        for task in asyncio.as_completed(tasks):
            titles = await task
            founded_animal_titles |= titles
    # Обрабатываем полученные данные
    count_animal_titles_dict = dict()
    for animal_title in founded_animal_titles:
        first_letter = animal_title[0]
        count_animal_titles_dict[first_letter] = count_animal_titles_dict.get(first_letter, 0) + 1
    # Записываем результат в файл
    with open('beasts.csv', 'w', encoding='utf8', newline='') as file:
        writer = csv.writer(file)
        for letter in RUSSIAN_ALPHABET:
            writer.writerow([letter, count_animal_titles_dict.get(letter, 0)])

if __name__ == "__main__":
    asyncio.run(main())
