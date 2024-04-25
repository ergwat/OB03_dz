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

import random
import pickle

class Animal:
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food

    def info(self):
        print(f"Название: {self.name}, Возраст: {self.age}, Пища: {self.food}")

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
        print(f"Рептилия {self.name} съела {self.food}")


class Employee:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

    def info(self):
        print(f"Имя: {self.name}, Должность: {self.job}, Зарплата: {self.salary}")


class ZooKeeper(Employee):
    def __init__(self, name, job, salary):
        super().__init__(name, job, salary)

    def feed(self, animal):
        print(f"Смотритель {self.name} покормил {animal.name}")
        animal.eat()


class Veterinarian(Employee):
    def __init__(self, name, job, salary):
        super().__init__(name, job, salary)

    def heal(self, animal):
        print(f"У собачки боли, у кошечки боли, у {animal.name} всё пройди. Ветеринар {self.name} вылечил {animal.name}")


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_bird(self, name, age, food, can_fly):
        new_bird = Bird(name, age, food, can_fly)
        self.animals.append(new_bird)
        print(f"Птица добавлена: {new_bird.name}")

    def add_mammal(self, name, age, food, has_tail):
        new_mammal = Mammal(name, age, food, has_tail)
        self.animals.append(new_mammal)
        print(f"Млекопитающее добавлено: {new_mammal.name}")

    def add_reptile(self, name, age, food, can_swim):
        new_reptile = Reptile(name, age, food, can_swim)
        self.animals.append(new_reptile)
        print(f"Рептилия добавлена: {new_reptile.name}")

    def add_ZooKeeper(self, name, job, salary):
        new_zookeeper = ZooKeeper(name, job, salary)
        self.employees.append(new_zookeeper)
        print(f"Сотрудник добавлен: {new_zookeeper.name}")

    def add_vererenarian(self, name, job, salary):
        new_vererenarian = Veterinarian(name, job, salary)
        self.employees.append(new_vererenarian)
        print(f"Сотрудник добавлен: {new_vererenarian.name}, {new_vererenarian.job}")

    def list_animals(self):
        print("\nЖивотные в зоопарке:")
        for animal in self.animals:
            print(animal.info())

    def list_employees(self):
        print("\nСотрудники зоопарка:")
        for employee in self.employees:
            print(employee.info())


def save_zoo(zoo):
    with open('Save/zoo_data.pkl', 'wb') as file:
        pickle.dump(zoo, file)
    print("Zoo data saved successfully.")


def load_zoo():
    try:
        with open('Save/zoo_data.pkl', 'rb') as file:
            zoo = pickle.load(file)
        print("Zoo data loaded successfully.")
        return zoo
    except FileNotFoundError:
        print("No saved zoo data found.")
        return None


birds_list = ["Кукушка", "Соловей", "Сова", "Пингвин", "Курица", "Киви", "Гагара", "Орёл", "Коршун", "Воробей"]
mammals_list = ["Крокодил", "Лев", "Лиса", "Слон", "Кошка", "Собака", "Кот", "Панда", "Коза", "Кролик"]
reptiles_list = ["Крокодил", "Черепаха", "Ящерица", "Лягушка", "Геккон", "Динозавр", "Игуана"]
names_list = ["Вася", "Петя", "Маша", "Коля", "Ваня", "Саша", "Ваня", "Коля", "Ваня", "Саша"]


try:
    zoo = load_zoo()
except FileNotFoundError:
    print("No saved zoo data found.")
    zoo = Zoo()

zoo.add_bird(random.choice(birds_list), random.randint(1,5), "Семечки", True)
zoo.add_bird(random.choice(birds_list), random.randint(1,5), "Семечки", False)
zoo.add_mammal(random.choice(mammals_list), random.randint(1,15), "Сено", False)
zoo.add_reptile(random.choice(reptiles_list), random.randint(1,50), "Мяяясо", True)
zoo.add_ZooKeeper(random.choice(names_list), "Смотритель животных", random.randint(30000,50000))
zoo.add_vererenarian(random.choice(names_list), "Ветеринар", random.randint(30000,50000))

zoo.list_animals()
zoo.list_employees()

print("\nВремя ухаживать за животными")
for i in zoo.employees:
    if i.job == "Смотритель животных":
        for j in zoo.animals:
            i.feed(j)
    elif i.job == "Ветеринар":
        for j in zoo.animals:
            i.heal(j)

print("\n")
for i in zoo.animals:
    i.make_sound()
print("\n")
for i in zoo.animals:
    i.eat()

save_zoo(zoo)

'''


    text = task_list_in_progress.get(0, tk.END)
    with open("in_progress_tasks.txt", "w") as file:
        for text in text:
            new_text = str(text) + "\n"
            file.write(new_text)

    text = task_list_done.get(0, tk.END)
    with open("done_tasks.txt", "w") as file:
        for text in text:
            new_text=str(text)+"\n"
            file.write(new_text)


def load_data():
    with open("new_tasks.txt", "r") as file:
        for line in file: #каждая строчка читается отдельно
            if line != "\n": task_list_new.insert(tk.END, line)

    with open("in_progress_tasks.txt") as file:
        for line in file:
            if line != "\n": task_list_in_progress.insert(tk.END, line)

    with open("done_tasks.txt") as file:
        for line in file:
            if line != "\n": task_list_done.insert(tk.END, line)
'''