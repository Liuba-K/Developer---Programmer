#Сортировка кучей(пирамида, сортирующее дерево.):: Heapsort
#Сложность по дополнительной памяти O(1), всё происходит сразу на месте.
#Итоговая сложность по времени: O(n log n) + O(n log n) = O(n log n).

import random
from heapq import heappop, heappush

def Heapsort(spisok):
    h = []
    for value in spisok:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

def HeapSift(spisok, start, end):
    largest = end
    l = 2 * end + 1
    r = 2 * end + 2

    if l < start and spisok[end] < spisok[l]:
        largest = l

    if r < start and spisok[largest] < spisok[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != end:
        spisok[end], spisok[largest] = spisok[largest], spisok[end]

        # Применяем heapify к корню.
        HeapSift(spisok, start, largest)

def Heapsort_2(spisok):
    n= len(spisok)
    for start in range(n, -1, -1):   #range(старт, стоп, шаг)
        HeapSift(spisok, n, start)

    for end in range(n - 1, 0, -1):
        spisok[end], spisok[0] = spisok[0], spisok[end]
        HeapSift(spisok, end, 0)
    return spisok


if __name__ == '__main__':
    s = [random.randrange(0, 100) for i in range(100)]
    print(f'Исходный массив {s}')
    print(Heapsort(s))
    print(Heapsort_2(s))


