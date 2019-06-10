# Задача 1. Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
# Записывает в файл пару: страна – ссылка.

import json

class Country_iter:
    def __init__(self, path):
        with open(path) as file:
            countries = json.load(file)
            self.country_list = [country['name']['common'] for country in countries]
        self.cursor = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor < len(self.country_list):
          with open('wiki_links.txt', 'a') as file:
            file.write(f'{self.country_list[self.cursor]} - https://en.wikipedia.org/wiki/{self.country_list[self.cursor].replace(" ", "_")}\n')
        else:
          raise StopIteration
        return self.cursor


countries = Country_iter('countries.json')
for country in countries:
  pass

# Задача 2. Написать генератор, который принимает путь к файлу.
# При каждой итерации возвращает md5 хеш каждой строки файла.


import hashlib

def md5_generator(path):
    with open(path, 'rb') as file:
        strings = file.readlines()
        for string in strings:
            yield hashlib.md5(string)

for string in md5_generator('countries.json'):
    print(string.hexdigest())