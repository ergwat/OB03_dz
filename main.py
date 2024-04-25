# Создайте базовый класс Animal, который будет содержать общие атрибуты (например, name, age)
# и методы (make_sound(), eat()) для всех животных.
# Реализуйте наследование, создав подклассы Bird, Mammal, и Reptile, которые наследуют от класса Animal.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для make_sound()).

# Продемонстрируйте полиморфизм: создайте функцию animal_sound(animals),
# которая принимает список животных и вызывает метод make_sound() для каждого животного.
# Используйте композицию для создания класса Zoo, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

# Создайте классы для сотрудников, например, ZooKeeper, Veterinarian,
# которые могут иметь специфические методы (например, feed_animal() для ZooKeeper и heal_animal() для Veterinarian).


class Animal():
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food


    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, food, can_fly):
        super().__init__(name, age, food)
        self.can_fly = can_fly

    def make_sound(self):
        print(f"Птичка {self.name} говорит: 'Чик-чирик'")

    def eat(self):
        print(f"Птичка {self.name} покушала {self.food}")


class Mammal(Animal):
    def __init__(self, name, age, food, has_tail):
        super().__init__(name, age, food)
        self.has_tail = has_tail

    def make_sound(self):
        print(f"Млекопитающее {self.name} говорит: 'Муууу'")

    def eat(self):
        print(f"Млекопитающее {self.name} покушало {self.food}")

class Reptile(Animal):
    def __init__(self, name, age, food, can_swim):
        super().__init__(name, age, food)
        self.can_swim = can_swim

    def make_sound(self):
        print(f"Рептилия {self.name} ничего не говорит, только молча таращится на тебя")

    def eat(self):
        print(f"Рептилия {self.name} съела {self.food})")


class Employee():
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

class ZooKeeper(Employee):
    def __init__(self, name, job, salary):
        super().__init__(name, job, salary)

    def feed_animal(self, animal):
        print(f"Смотритель {self.name} покормил {animal.name}")

class Veterinarian(Employee):
    def __init__(self, name, job, salary):
        super().__init__(name, job, salary)

    def heal_animal(self, animal):
        print(f"У собачки боли, у кошечки боли, у {animal.name} всё пройди. Ветеринар {self.name} вылечил {animal.name}")


animals = [Bird("Кукушка", 2, "Семечки", True),
               Mammal("Вол", 3, "Сено", False),
               Reptile("Крокодил", 1, "Мяяясо", True)]
emploees = [ZooKeeper("Вася", "Смотритель животных", 35000),
            Veterinarian("Петя", "Ветеринар", 45000)]