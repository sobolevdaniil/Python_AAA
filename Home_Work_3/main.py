class CountVectorizer:
    def __init__(self):
        self._vocabulary = []

    def fit_transform(self, corpus_of_texts):
        """Функция возвращает мешок слов в виде матрицы"""

        # Кокатенируем все тексты в один, изменяя регистр на нижний
        full_text = ''
        for text in corpus_of_texts:
            full_text += text.lower() + ' '

        # Ищем уникальные слова во всем тексте
        unique_words = []
        for word in full_text.split():
            if word not in unique_words:
                unique_words.append(word)
        self._vocabulary = unique_words

        def count_words(txt: str) -> dict:
            """Функция считает количество различных слов в тексте"""
            result = {}
            for wd in txt.split():
                if wd not in result:
                    wd.lower()
                    result[wd] = 1
                else:
                    result[wd] += 1
            return result

        # Подсчитываем количество слов в каждом из текстов корпуса
        list_of_dicts = []
        for text in [text.lower() for text in corpus_of_texts]:
            list_of_dicts.append(count_words(text))

        # Создаем мешок слов в виде матрицы
        big_list = []
        for some_dict in list_of_dicts:
            list_for_one = []
            for unique_word in unique_words:
                if unique_word in some_dict.keys():
                    list_for_one.append(some_dict[unique_word])
                else:
                    list_for_one.append(0)
            big_list.append(list_for_one)

        return big_list

    def get_feature_names(self):
        """Функция возвращает уникальные слова в корпусе"""
        return self._vocabulary


if __name__ == '__main__':

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
