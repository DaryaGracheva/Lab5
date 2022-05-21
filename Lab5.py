import time
import random
import numpy as np

print("Результат работы программы:")
try :
    rows = int(input("Введите количество строк (столбцов) квадратной матрицы больше 3: "))
    while rows < 4 :
        rows = int(input("Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы больше 3:"))
    K = int(input("Введите число К: "))
    start = time.time()
    A = np.zeros((rows,rows),dtype = int)
    F = np.zeros((rows,rows), dtype = int)

    for i in range (rows):                                                                                              # формируем матрицу А с помощью генератора случайных чисел
        for j in range(rows):
            A[i][j] = np.random.randint(-10,10)

    time1 = time.time()
    print("\nМатрица A: \n",A)

    for i in range (rows):                                                                                              # формируем матрицу F, копируя из матрицы А
        for j in range(rows):
            F[i][j] = A[i][j]

    count_nechet = 0
    count_chet = 0

    for i in range(rows//2, rows):                                                                                       # считаем кол-во положительных элементов в четных столбцах и кол-во отрицательных элементов в нечетных столбцах матрицы С
        for j in range(rows//2, rows):
            if j % 2 == 1 and A[i][j] < 0:
                count_nechet += 1
            elif j % 2 == 0 and A[i][j] > 0:
                count_chet += 1
                
    if count_nechet < count_chet:                                                                                       # в С кол-во положительных элементов в четных столбцах матрицы больше,чем отрицательных элементов в нечетных столбцах матрицы, то меняем местами B и C симметрично
        print("\nМеняем B и C симметрично")
        F[0:rows // 2, rows // 2 + rows % 2:rows] = A[rows // 2 + rows % 2:rows, rows // 2 + rows % 2:rows]
        F[rows // 2 + rows % 2:rows, rows // 2 + rows % 2:rows] = A[0:rows // 2, rows // 2 + rows % 2:rows]
    else:                                                                                                               # иначе С и Е меняем местами несимметрично
        print("\nМеняем С и Е несимметрично")
        F[0:rows // 2, 0:rows // 2] = A[rows // 2 + rows % 2:rows, rows // 2 + rows % 2:rows]
        F[rows // 2 + rows % 2:rows, rows // 2 + rows % 2:rows] = A[0:rows // 2, 0:rows // 2]

    time2 = time.time()
    print("\nМатрица F: \n", F)

    if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:
        print("\nНельзя вычислить, поскольку матрица А или F вырождена")
    elif np.linalg.det(A) > sum(F.diagonal()):
        A =  np.dot(A, np.transpose(A)) - (K * np.transpose(F))                                                         # A*A^T - K*F^(-1)
        finish = time.time()
        print("\nОпределитель матрицы А больше суммы диагональных элементов матрицы F\n")
        print("\nВычисление выражения: A*A^T - K*F^(-1)")
    else:
        A = (np.linalg.inv(A) + np.tril(A) - np.linalg.inv(F))                                                          # A^(-1) + G - F^(-1)
        finish = time.time()
        print("\nOпределитель матрицы А меньше суммы диагональных элементов матрицы F")
        print("\nВычисление выражения: A^(-1) + G - F^(-1)")
        print("\nТреугольная матрица из А :\n",np.tril(A))
    
    print("\nРезультат:")
    for i in A:                                                                                                         # выполняем перебор всех строк матрицы
        for j in i:                                                                                                     # вяполняем перебор всех элементов в строке
            print("%5d" % j, end=' ')
        print()

    finish = time.time()
    result = finish - start
    print("\nProgram time: " + str(result) + " seconds.")

except ValueError:
    print("\nЭто не число")

except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
