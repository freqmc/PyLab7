class Product:
    def __init__(self, name, price, count, weight, desc):
        self.name = name
        self.__price = price
        self.__count = count
        self.weight = weight
        self.desc = desc

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, pr):
        if pr < 0:
            print("Ошибка: Цена не может быть меньше нуля!")
        else:
            self.__price = pr

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, c):
        if c < 0:
            print("Ошибка: Количество не может быть меньше нуля!")
        else:
            self.__count = c

    def info(self):
        print(f"Товар: {self.name}, "
              f"Кол-во: {self.__count}, "
              f"Цена: {self.__price}, "
              f"Вес: {self.weight} кг, "
              f"Описание: {self.desc}")


class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.products = []

    def add_product(self, product):
        for pr in self.products:
            if pr.name == product.name:
                print(f"Внимание: Товар '{product.name}' уже есть на складе. Обновляем данные.")
                pr.count = pr.count + product.count
                pr.price = product.price
                return
        self.products.append(product)
        print(f"Товар '{product.name}' успешно добавлен на склад.")

    def remove_product(self, name):
        for pr in self.products:
            if pr.name == name:
                self.products.remove(pr)
                print(f"Товар '{name}' удален со склада.")
                return
        print(f"Товар '{name}' не найден на складе.")

    def show_all(self):
        if not self.products:
            print("На складе нет товаров.")
            return
        print(f"Список товаров на складе {self.name}")
        for pr in self.products:
            pr.info()  # Вызываем метод, он сам выводит информацию
        print()

    def find(self, name):
        for pr in self.products:
            if pr.name == name:
                print("\nНайденный товар:")
                pr.info()
                return pr
        print(f"Товар '{name}' не найден.")
        return None

    def update_quantity(self, name, amount):
        product = self.find(name)
        if product:
            new_count = product.count + amount
            if new_count >= 0:
                product.count = new_count
                print(f"Количество товара '{name}' обновлено. Новое кол-во: {product.count}")
            else:
                print("Ошибка: Недостаточно товара на складе для списания.")


def main():
    my_store = Store("Центральный Склад", "ул. Ленина, 1")

    while True:
        print("\n=== МЕНЮ СКЛАДА ===")
        print("1. Добавить товар")
        print("2. Удалить товар")
        print("3. Показать все товары")
        print("4. Найти товар по названию")
        print("5. Изменить количество товара (приход/расход)")
        print("6. Изменить цену товара")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        match choice:
            case '1':
                print("\n--- Добавление нового товара ---")
                name = input("Название товара: ")
                try:
                    price = float(input("Цена: "))
                    count = int(input("Количество: "))
                    weight = float(input("Вес (кг): "))
                except ValueError:
                    print("Ошибка: Введите корректные числовые значения для цены, количества и веса!")
                    continue

                desc = input("Описание: ")
                new_prod = Product(name, price, count, weight, desc)
                my_store.add_product(new_prod)

            case '2':
                name = input("\nВведите название товара для удаления: ")
                my_store.remove_product(name)

            case '3':
                my_store.show_all()

            case '4':
                name = input("\nВведите название товара для поиска: ")
                my_store.find(name)

            case '5':
                name = input("\nВведите название товара: ")
                try:
                    amount = int(input("Введите количество (положительное - приход, отрицательное - расход): "))
                    my_store.update_quantity(name, amount)
                except ValueError:
                    print("Ошибка: Введите целое число!")

            case '6':
                name = input("\nВведите название товара: ")
                prod = my_store.find(name)
                if prod:
                    try:
                        new_price = float(input("Введите новую цену: "))
                        prod.price = new_price  # Используется сеттер с проверкой
                        print(f"Цена товара '{name}' обновлена.")
                    except ValueError:
                        print("Ошибка: Введите корректное числовое значение!")

            case '0':
                print("Выход из программы.")
                break

            case _:
                print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()