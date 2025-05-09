def task3():
    x = float(input("Введите действительное число x: "))
    result = x * (x * (x * (2 * x - 3) + 4) - 5) + 6
    print(f"Значение полинома: {result}")
task3()