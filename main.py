from random import randint # функция генерации случайных чисел

# индекс минимального
def index_min(values):
    min_value = min(values) # минимальный в списке
    idx = values.index(min_value) # его индекс
    return idx

# индекс заданного значения
def index_of(values, value):
    idx = -1 # если не найдем, индекс -1
    for i in range(len(values)):
        if values[i] == value: # если нашли совпадающее
            idx = i
            break # прекращаем поиск
    return idx

# сортировка массива
def sort(values):
    l = len(values)  # длина массива
    # алгоритм пузырьковой сортировки
    for i in range(l):
        for j in range(l-1-i):
            if (values[j] > values[j+1]):
                t = values[j]
                values[j] = values[j+1]
                values[j+1] = t

# самая длинная последовательность одинаковых (результат в виде списка)
def longest_serie(values):
    max_a = max_b = 0 # индексы последовательности
    for i in range(len(values) - 1):
        if values[i] == values[i+1]: # если нашли повторение
            a = i
            b = i + 1
            # увеличиваем индекс, пока идут повторяющиеся
            while (b < len(values)) and (values[b] == values[i]):
                b += 1
            if b - a > max_b - max_a: # если новая последовательность больше ранее найденной
                max_a = a
                max_b = b
    return values[max_a:max_b]

# три максимальных
def max_three(values):
    if len(values) < 3: # если длина меньше 3, то вернем весь список
        return values
    a = values.copy() # получаем копию массива
    maxes = []
    for i in range(3):
        maxi = max(a) # получаем текущий максимальный
        maxes.append(maxi) # добавляем в результирующий список
        a.remove(maxi) # удаляем из рассматриваемого
    return maxes

# сравнение массивов на равенство
def equals(a, b):
    if (len(a) == len(b)): # если совпадают по размеру
        for i in range(len(a)):
            if a[i] != b[i]: # если не соответствующие не совпали
                return False # массивы не равны
        return True # если оказались равны
    else:
        return False # не совпадают по размеру

# функция для создания и заполнения массивов
def create_array():
    n = int(input('Введите размер массива: '))
    A = [0] * n
    print('\n1 - заполнить случайными')
    print('2 - заполнить с клавиатуры')
    t = int(input('Введите способ заполнения массива: '))
    print()
    if t == 1: # случайные
        for i in range(n):
            A[i] = randint(-10, 10) # -10..10
    else: # с клавиатуры
        for i in range(n):
            A[i] = int(input('Введите элемент A[%d]: ' % i))
    return A

# основная программа - работа с массивами
def main():
    print('Массив A')
    A = create_array() # создаем массив
    print('Получен массив:', *A)
    # проверяем все функции
    print('\nИндекс минимального:', index_min(A))
    x = int(input('\nВведите значение для определения индекса: '))
    idx = index_of(A, x)
    if (idx != -1):
        print('Индекс искомого:', idx)
    else:
        print('Указанного элемента нет в массиве')
    # самая длинная серия одинаковых
    serie = longest_serie(A)
    print('\nСамая длинная последовательность одинаковых:', serie)
    sort(A) # сортируем
    print('\nСортировка массива:', *A)
    # три наибольших
    maxes = max_three(A)
    print('\nНаибольшие элементы: (до трёх шт)', maxes)
    serie = longest_serie(A)
    print('\nСамая длинная последовательность после сортировки', serie)
    print('\nСравнение с другим массивом')
    B = create_array() # создаем новый массив
    print('\nПолучен массив:', *B)
    if equals(A, B):
        print('Массивы совпадают')
    else:
        print('Массивы не совпадают')

main()
input('Нажмите Enter, чтобы выйти')