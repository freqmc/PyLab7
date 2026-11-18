import math


class Vector:
    def __init__(self, components):
        if not isinstance(components, (list, tuple)):
            raise TypeError("Компоненты вектора должны быть списком или кортежем")
        self.components = list(components)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self.components) != len(other.components):
            return False
        for a, b in zip(self.components, other.components):
            if a != b:
                return False
        return True

    def __lt__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.norm() < other.norm()

    def norm(self):
        return math.sqrt(sum(x * x for x in self.components))

    def __str__(self):
        return f"Vector({self.components})"

    def __repr__(self):
        return f"Vector({self.components})"

v1 = Vector([1, 2, 3])
v2 = Vector([1, 2, 3])
v3 = Vector([3, 2, 1])
v4 = Vector([10, 20])

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v3 = {v3}")
print(f"v4 = {v4}\n")

print("Проверка на равенство")
print(f"v1 == v2 : {v1 == v2}")
print(f"v1 == v3 : {v1 == v3}")

print("Сравнение длин")
print(f"Длина v1 = {v1.norm():.2f}")
print(f"Длина v3 = {v3.norm():.2f}")
print(f"Длина v4 = {v4.norm():.2f}")

print(f"v1 < v3 : {v1 < v3}")  # True
print(f"v1 < v4 : {v1 < v4}")  # True
print(f"v4 < v1 : {v4 < v1}")  # False