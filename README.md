Вариант 3

С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].Формируется матрица F следующим образом: скопировать в нее А и если в С количество положительных элементов в четных столбцах больше, чем количество отрицательных  элементов в нечетных столбцах, то поменять местами В и С симметрично, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*A^T – K * F^(-1), иначе вычисляется выражение (A^(-1) +G-F^(-1))*K, где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А, F и все матричные операции последовательно.Работу выполнила студентка группы ИСТбд-12, Грачева Дарья.
