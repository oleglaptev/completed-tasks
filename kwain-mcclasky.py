#функция для склеивания строк
def combine(m, n):
    a = len(m)
    c = ''
    count = 0
    for i in range(a):
        if m[i] == n[i]:
            c += m[i]
        elif m[i] != n[i]:
            c += '-'
            count += 1
    if count > 1:
        return None
    else:
        return c

#функция, представляющая собой один проход алгоритма (получения списка n из списка n-1)
def alg(dnf):
    newList = list(dnf)
    size = len(newList)
    res_implicants = []
    alg_implicants = []
    cross_implicants = []
    mark = [0] * size
    m = 0
    #последовательное склеивание интервалов первого множества и их отметка
    for i in range(size):
        for j in range(i + 1, size):
            c = combine(str(newList[i]), str(newList[j]))
            if c != None:
                alg_implicants.append(str(c))
                mark[i] = 1
                mark[j] = 1
    #отметка одинаковых интервалов в получившемся множестве (втором)
    mark2 = [0] * len(alg_implicants)
    for i in range(len(alg_implicants)):
        for j in range(i + 1, len(alg_implicants)):
            if i != j and mark2[j] == 0:
                if alg_implicants[i] == alg_implicants[j]:
                    mark2[j] = 1
    #добавление неотмеченных интервалов из второго множества в промежуточное множество между уровнями рекурсии
    for r in range(len(alg_implicants)):
        if mark2[r] == 0:
            cross_implicants.append(alg_implicants[r])
    #добавление неотмеченных интервалов из первого множества в результат
    for q in range(size):
        if mark[q] == 0:
            res_implicants.append(str(newList[q]))
            m += 1
    if m == size or size == 1:
        return res_implicants
    else:
        return res_implicants + alg(cross_implicants)

def result_conversion(result):
    lets = 'abcd'
    res1 = ['' for i in range(len(result))]
    for i in range(len(result)):
        for j in range(4):
            if result[i][j] == '1':
                res1[i] += result[i][j].replace('1', lets[j])
            elif result[i][j] == '0':
                res1[i] += result[i][j].replace('0', '\033[4m' + lets[j] + '\033[0m')
            else:
                res1[i] += result[i][j].replace('-', '')
    return res1


sovdnf = {'0001', '0101', '0111', '1101', '1111', '1110', '1011'}
print(*result_conversion(alg(sovdnf)), sep=' v ')
sovdnf1 = {'0001', '0011', '0101', '0111', '1110', '1111'}
print(*result_conversion(alg(sovdnf1)), sep=' v ')
sovdnf2 = {'0000', '0001', '0010', '0011', '0110', '0111', '1000', '1001', '1011', '1111'}
print(*result_conversion(alg(sovdnf2)), sep=' v ')