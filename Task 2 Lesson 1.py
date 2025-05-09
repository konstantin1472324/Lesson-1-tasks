import math
def task2():
    a = float(input("Введите угол a в радианах: 
        if abs(math.cos(a)) == 1:
        print("Ошибка: знаменатель обращается в ноль")
        return
    sqrt1 = math.sqrt((1 - math.cos(a)) / (1 + math.cos(a)))
    sqrt2 = math.sqrt((1 + math.cos(a)) / (1 - math.cos(a)))
    z = sqrt1 + sqrt2
    print(f"Результат z = {z}")
task2()