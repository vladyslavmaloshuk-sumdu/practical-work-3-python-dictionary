from random import choice

cars = {
    "Toyota Camry": [180, 25000],
    "Daewo Lanos": [86, 3500],
    "Ford Focus": [120, 15000],
    "BMW X5": [340, 60000],
    "Skoda Octavia": [150, 22000],
    "Kia Rio": [100, 12000],
    "Audi A4": [190, 35000],
    "Renault Logan": [90, 8000],
    "Honda Civic": [140, 20000],
    "Mazda 3": [120, 18000],
}


def print_cars(cars):
    print("\nСписок усіх автомобілів")
    for car in cars:
        print(
            car,
            "Потужність:", cars[car][0],
            "к. с., Вартість:", cars[car][1], "$"
        )


def add_cars(cars):
    print("\nДодавання авто:")
    name = input("Введіть назву авто: ")
    power = float(input("Введіть потужність (к. с.): "))
    price = float(input("Введіть вартість ($): "))

    cars[name] = [power, price]
    print("Запис успішно додано")


def delete_cars(cars):
    print("\nВидалення авто:")
    name = input("Введіть назву авто для видалення: ")

    try:
        del cars[name]
        print(f"Автомобіль {name} видалено зі словника")
    except KeyError:
        print(f"ПОМИЛКА: Автомобіля з назвою {name} не знайдено в базі!")


def print_sorted_cars(cars):
    print("\nВідсортований список автомобілів (за алфавітом):")
    sorted_keys = sorted(cars.keys())

    for key in sorted_keys:
        print(key, "->", cars[key][0])


# Пошук автомобілів за потужністю
def search_car(cars):
    print("\nПошук автомобіля за потужністю")
    min_power = float(
        input("Введіть мінімальну потужність автомобіля: ")
    )

    found = False

    for car in cars:
        if cars[car][0] >= min_power:
            print(
                car,
                "Потужність:", cars[car][0],
                "к. с., Вартість:", cars[car][1], "$"
            )
            found = True

    if not found:
        print("Автомобілів із такою потужністю не знайдено.")


def calc_powerful_cars_total(cars):
    print("\nЗагальна вартість авто з двигуном > 100 к.с.")

    total_price = 0

    for car, data in cars.items():
        power = data[0]
        price = data[1]

        if power > 100:
            total_price += price

    print(f"Сумарна вартість таких авто: {total_price} $")


while True:
    print("\nГОЛОВНЕ МЕНЮ")
    print("1. Вивести всі авто")
    print("2. Додати авто")
    print("3. Видалити авто")
    print("4. Вивести відсортований список")
    print("5. Підрахувати вартість потужних авто (> 100 к.с.)")
    print("6. Пошук автомобіля за потужністю")
    print("7. Вийти")

    choice = input("Оберіть дію: ")

    if choice == "1":
        print_cars(cars)

    elif choice == "2":
        add_cars(cars)

    elif choice == "3":
        delete_cars(cars)

    elif choice == "4":
        print_sorted_cars(cars)

    elif choice == "5":
        calc_powerful_cars_total(cars)

    elif choice == "6":
        search_car(cars)

    elif choice == "7":
        print("Роботу завершено")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз")