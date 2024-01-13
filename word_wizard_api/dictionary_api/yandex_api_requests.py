import requests
import json
import random

from word_wizard_api.assets.words_10000 import words


class YandexWordsFetcher:
    def __init__(self):
        self.api_key = 'dict.1.1.20240110T134658Z.42bf471f4889a06f.663f79b97e4b477f78483d9a1f0c6ba0b2156ac2'
        self.base_url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'

    def fetch_word_info(self, word):
        url = f'{self.base_url}?key={self.api_key}&lang=en-ru&text={word}'
        response = requests.get(url)
        json_content = json.loads(response.text)
        return json_content

    def get_random_word_info(self, words):
        random_word = random.choice(words)
        return self.fetch_word_info(random_word)

    def process_word_info(self, json_content):
        word = json_content.get('def', [{}])[0].get('text', '')
        transcription = json_content.get('def', [{}])[0].get('ts', '')

        try:
            synonyms = [synonym['text'] for synonym in json_content['def'][0]['tr'][0]['syn']]
        except KeyError:
            synonyms = []

        try:
            examples_eng = [example['text'] for example in json_content['def'][0]['tr'][0]['ex']]
            examples_rus = [item['tr'][0]['text'] for item in
                            json_content.get('def', [{}])[0].get('tr', [{}])[0].get('ex', [])]
            dict_eng_rus = {eng: rus for rus, eng in zip(examples_rus, examples_eng)}
        except KeyError:
            examples_eng, examples_rus, dict_eng_rus = [], [], []

        return word, transcription, synonyms, examples_eng, examples_rus, dict_eng_rus


yandex_words_fetcher = YandexWordsFetcher()
json_content = yandex_words_fetcher.get_random_word_info(words)
word, transcription, synonyms, examples_eng, examples_rus, dict_eng_rus = yandex_words_fetcher.process_word_info(
    json_content)

print(json_content)

print(word, transcription)
