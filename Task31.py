class MyData:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return MyData(self.value + other)
        elif isinstance(other, str):
            return MyData(str(self.value) + other)
        elif isinstance(other, list):
            return MyData(other + [self.value])
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return MyData(self.value - other)
        elif isinstance(other, str):
            if isinstance(self.value, str):
                return MyData(self.value.replace(other, ""))
            return NotImplemented
        elif isinstance(other, list):
            if isinstance(self.value, list):
                new_list = [x for x in self.value if x not in other]
                return MyData(new_list)
            return NotImplemented
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return MyData(self.value * other)
        elif isinstance(other, str):
            if isinstance(self.value, str):
                return MyData(self.value.count(other))
            return NotImplemented
        elif isinstance(other, list):
            if isinstance(self.value, list) and len(self.value) == len(other):
                return MyData([a * b for a, b in zip(self.value, other)])
            return NotImplemented
        else:
            return NotImplemented

    def __str__(self):
        return f"{self.value}"

print("Числа")
num = MyData(10)
print(f"Исходное: {num}")
print(f"{num} + 5 = {num + 5}")  # 15
print(f"num - 3 = {num - 3}")  # 7
print(f"num * 4 = {num * 4}")  # 40

print("Строки")
s = MyData("Hello")
print(f"{s} + World = {s + ' World'}")  # Hello World
print(f"{s} - l = {s - 'l'}")  # Heo
print(f"{s} * 3 = {s * 3}")  # HelloHelloHello
print(f"{s} * l = {s * 'l'}")  # 2 вхождения

print("Списки")
lst = MyData([1, 2, 3])
print(f"{lst} + [4,5] = {lst + [4, 5]}")  # [1,2,3] + [4,5] = [4,5,1,2,3]
print(f"{lst} - [2] = {lst - [2]}")  # [1,3]
print(f"{lst} * 2 = {lst * 2}")  # [1,2,3,1,2,3]
print(f"{lst} * [10,20,30] = {lst * [10, 20, 30]}")  # [10, 40, 90]