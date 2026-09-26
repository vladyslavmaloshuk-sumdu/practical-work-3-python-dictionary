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


# Виведення всіх автомобілів
def print_cars(cars):
    print("\nСписок усіх автомобілів")

    for car in cars:
        print(
            car,
            "Потужність:", cars[car][0],
            "к. с., Вартість:", cars[car][1], "$"
        )


# Додавання нового автомобіля
def add_cars(cars):
    print("\nДодавання авто:")
    name = input("Введіть назву авто: ")

    while True:
        try:
            power = float(input("Введіть потужність (к. с.): "))
            price = float(input("Введіть вартість ($): "))

            cars[name] = [power, price]
            print("Запис успішно додано")
            break

        except ValueError:
            print(
                "Помилка: потрібно вводити лише числа! "
                "Спробуйте ще раз."
            )


# Видалення автомобіля
# Додано перевірку порожнього введення,
# очищення пробілів та пошук без урахування регістру.
def delete_cars(cars):
    print("\nВидалення авто:")

    name = input(
        "Введіть назву авто для видалення: "
    ).strip()

    if not name:
        print("ПОМИЛКА: Назва авто не може бути порожньою!")
        return

    # Пошук без урахування регістру
    matched_key = None

    for car_key in cars:
        if car_key.lower() == name.lower():
            matched_key = car_key
            break

    if matched_key:
        del cars[matched_key]

        print(
            f"Автомобіль '{matched_key}' "
            "успішно знайдено та видалено зі словника."
        )
    else:
        print(
            f"ПОМИЛКА: Автомобіля з назвою "
            f"'{name}' не знайдено в базі!"
        )


# Виведення автомобілів у відсортованому порядку
def print_sorted_cars(cars):
    print("\nВідсортований список автомобілів (за алфавітом):")

    sorted_keys = sorted(cars.keys())

    for key in sorted_keys:
        print(key, "->", cars[key][0])


# Пошук автомобілів за потужністю
def search_car(cars):
    print("\nПошук автомобіля за потужністю")

    while True:
        try:
            min_power = float(
                input(
                    "Введіть мінімальну потужність автомобіля: "
                )
            )
            break

        except ValueError:
            print(
                "Помилка: потрібно вводити лише число! "
                "Спробуйте ще раз."
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
        print(
            "Автомобілів із такою потужністю не знайдено."
        )


# Підрахунок загальної вартості автомобілів
# з потужністю більше 100 к. с.
def calc_powerful_cars_total(cars):
    print(
        "\nЗагальна вартість авто "
        "з двигуном > 100 к.с."
    )

    total_price = 0

    for car, data in cars.items():
        power = data[0]
        price = data[1]

        if power > 100:
            total_price += price

    print(
        f"Сумарна вартість таких авто: "
        f"{total_price} $"
    )


# Головне меню
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