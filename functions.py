import itertools


def create_matrix(length):
    matrix = [0] * (length)
    for i in range(length):
        bin_list = []
        str_bin = bin(i + 1)[2:]
        str_bin = '0' * (length) + str_bin
        bin_list = [int(str_bin[j]) for j in range(len(str_bin) - 1, -1, -1)]
        matrix[i] = bin_list
    return matrix


def code(word, matr, c_t_b):
    new_word = copy_list(word)
    for i in range(c_t_b):
        new_word.insert(2 ** i - 1, 0)
    summ = 0
    kontr = []
    for i in range(c_t_b):
        for j3 in range(len(matr)):
            summ += new_word[j3] * matr[j3][i]
        kontr.append(summ % 2)
        summ = 0
    for i in range(c_t_b):
        new_word[2 ** i - 1] = kontr[i]
    return new_word


def make_lists_of_err(word, list_of_inds, i):
    file = open("comb_of_errors_" + str(i) + ".txt", "a")
    list_of_errs = []
    l_err = list(itertools.combinations(list_of_inds, r=i))
    for j in range(len(l_err)):
        new_list = inverse(word, l_err[j])
        list_of_errs.append(new_list)
        file.write(str(new_list))
        file.write("\n")
    file.write("Всего комбинаций - " + str(len(list_of_errs)))
    file.write("\n")
    file.close()
    return list_of_errs


def copy_list(list):
    new_list = []
    for i in list:
        new_list.append(i)
    return new_list


def inverse(l, indexes):
        tmp_list = copy_list(l)
        for j2 in range(len(indexes)):
            tmp_list[indexes[j2]] = 0 if tmp_list[indexes[j2]] == 1 else 1
        return tmp_list


def decode(f_list, matr):
    err_vec = []
    for i in range(len(matr[0])):
        summ = 0
        for j1 in range(len(matr)):
            summ += f_list[j1] * matr[j1][i]
        err_vec.append(summ % 2)
    if sum(err_vec) > 0:
        return False
    else:
        return True


def count_errs(c_word, inds, matr):
    f2 = open("errors.txt", "a")
    for kr in range(1, len(inds)):
        count = 0
        fake_list = make_lists_of_err(c_word, inds, kr)
        for j in range(len(fake_list)):
            if not(decode(fake_list[j], matr)):
                count += 1
        f2.write("Ошибок кратности " + str(kr) + " обнаружено " + str(count))
        f2.write("\n")
        f2.write("Всего ошибок кратности " + str(kr) + " - " + str(len(fake_list)) + "\n")
        f2.write("Обнаруживающая способность кода: " + str(count / len(fake_list)))
        f2.write("\n" + " \n")
