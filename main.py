import itertools
from math import log2, ceil
import functions
choise = int(input("Ввести своё сообщение - 1\nИспользовать сообщение из варианта - 2\n"))
inf_word = []
if choise == 1:
    inf_word = list(map(int, input().split()))
else:
    inf_word = [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1]

print("Исходное слово: " + str(inf_word) + "\n\n")


count_test_bs = ceil(log2(len(inf_word))) + 1

print("Количество проверочных бит: " + str(count_test_bs) + "\n\n")
code_word_length = len(inf_word) + count_test_bs
matrix = functions.create_matrix(code_word_length)
code_word = functions.code(inf_word, matrix, count_test_bs)
indexes = list(range(code_word_length))
functions.count_errs(code_word, indexes, matrix)



