def task5():
    A = int(input("Введите число A: "))
    B = int(input("Введите число B: "))
    C = int(input("Введите число C: "))
    positive_count = 0
    if A > 0:
        positive_count += 1
    if B > 0:
        positive_count += 1
    if C > 0:
        positive_count += 1
    is_true = (positive_count == 2)
    print(f"Ровно два из чисел A, B, C являются положительными: {is_true}")
task5()