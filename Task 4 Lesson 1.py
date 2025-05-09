def task4():
    K = int(input("Введите день года K (1-365): "))
    if K < 1 or K > 365:
        print("Ошибка: K должно быть в диапазоне 1-365")
        return
    day_of_week = (K + 5) % 7 
    if day_of_week == 0:
        day_of_week = 7
    days = {1: "понедельник", 2: "вторник", 3: "среда", 
            4: "четверг", 5: "пятница", 6: "суббота", 7: "воскресенье"}
    print(f"День недели для {K}-го дня года: {day_of_week} ({days[day_of_week]})")
task4()