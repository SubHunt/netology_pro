import json
import collections


def logger(old_function):
    def new_function(*args, **kwargs):
        print(f'вызвана функция {old_function.__name__} с аргументами')
        print(f'{args = }')
        print(f'{kwargs = }')
        value = old_function(*args, **kwargs)
        return value
    return new_function


def test_3():

    @logger
    def read_json(file_path, max_len_word=6, top_words=10):
        """ Функция подсчитывает кол-во встречаемых слов в файле json """
        with open(file_path, encoding='utf-8') as news_file:
            news = json.load(news_file)
            description_word = []
            for item in news['rss']['channel']['items']:
                description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
                description_word.extend(description)
                counter_words = collections.Counter(description_word)
            print('Вариант работы с JSON:')
            print(counter_words.most_common(top_words))

    read_json('newsafr.json')


if __name__ == '__main__':
    test_3()
