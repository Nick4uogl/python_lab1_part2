import os


class ReadFile:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("File type must be string")
        if not os.path.exists(name):
            raise Exception("This file does not exists")
        self.__name = name

    def __str__(self):
        return f"{self.__name}"

    def count_words(self):
        num_words = 0

        with open(self.__name, 'r') as f:
            for line in f:
                line = line.strip(os.linesep)
                words_list = line.split()
                num_words = num_words + len(words_list)

        return num_words

    def count_chars(self):
        num_chars = 0

        with open(self.__name, 'r') as f:
            for line in f:
                num_chars = num_chars + len(line)

        return num_chars

    def count_lines(self):
        num_lines = 0

        with open(self.__name, 'r') as f:
            for line in f:
                num_lines = num_lines + 1

        return num_lines

    def count_sentences(self):
        num_sentences = 0

        with open(self.__name, 'r') as f:
            for line in f:
                num_sentences += line.count('.')

        return num_sentences


file_name = 'text.txt'
file = ReadFile(file_name)
print(file)
print(file.count_words())
print(file.count_chars())
print(file.count_lines())
print(file.count_sentences())
