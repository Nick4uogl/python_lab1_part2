class Product:
    def __init__(self, product: str, price: int, description: str):
        if price < 0:
            raise ValueError('price can not be negative')
        self.product = product
        self.price = price
        self.description = description

    def __str__(self):
        return print(f"{self.product} price:{self.price} description:{self.description}")


class Customer:
    def __init__(self, surname: str, name: str, patronymic: str, mobile: str):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile = mobile

    def __str__(self):
        return print(f"{self.surname} {self.name} {self.patronymic} mobile: {self.mobile}")


class Order:
    def __init__(self, customer: Customer):
        self.customer = customer
        self.products = dict()

    def add_product(self, product: Product, amount: int):
        whole_amount = amount + self.products.get(product, 0)
        self.products[product] = whole_amount

    def del_product(self, product: Product, amount: int):
        current_amount = self.products.get(product, 0)
        whole_amount = current_amount - amount
        if whole_amount < 0:
            raise ValueError(f"You can delete only {current_amount} items")
        self.products[product] = whole_amount

    def calculate_price(self):
        return sum(product.price * self.products[product] for product in self.products)

    def __str__(self):
        return print(f"{self.customer} {self.products}")


customer1 = Customer("Nick", "Pylypchuk", "Igorovych", '+380960981783')
bananas = Product("banana", 70, "A kilo of bananas")
apple = Product("apple", 20, "A kilo of apples")
cookies_cow = Product("cookies cow", 30, "a bundle of cookies")

order1 = Order(customer1)
order1.add_product(apple, 3)
order1.del_product(apple, 2)
print(order1.calculate_price())

