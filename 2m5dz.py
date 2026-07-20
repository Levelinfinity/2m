class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance += amount

    def withdraw(self, amount):
        if BankAccount.is_valid_amount(amount) and self.balance >= amount:
            self.balance -= amount

    def __str__(self):
        return f"BankAccount(balance={self.balance})"
    
    def __add__(self, other):
        return BankAccount(self.balance + other.balance) 
    
    @staticmethod 
    def is_valid_amount(amount):
        return amount > 0 
    
    @classmethod
    def create_default_account(cls):
        return cls(1000)
    

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} лет"
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
    

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Студент {self.name} (ID: {self.student_id})"
    

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    @classmethod
    def create_math_teacher(cls, name, age):
        return cls(name, age, "Математика")
    
    @staticmethod
    def is_adult(age):
        return age >= 18
    

class Researcher:
    def __init__(self, Field):
        self.field = Field

    def research(self):
        print(f"Проводится исследование в области {self.field}")


class Assistant(Student, Researcher):
    def __init__(self, name, age, student_id, field):
        Student.__init__(self, name, age, student_id)
        Researcher.__init__(self, field)


acc1 = BankAccount(500)
acc2 = BankAccount.create_default_account()

print(acc1)
print(acc2)

acc1.deposit(2000)
acc1.withdraw(1000)
print(acc1)

acc3 = acc1 + acc2
print(acc3)

print(BankAccount.is_valid_amount(-50))
print(BankAccount.is_valid_amount(100))

print("-" * 30)

p1 = Person("Боб", 20)
p2 = Person("Боб", 20)
print(p1 == p2)

student = Student("Алиса", 19, "A77")
print(student)

teacher = Teacher.create_math_teacher("Олег Петрович", 45)
print(f"Учитель ведёт: {teacher.subject}")
print(Teacher.is_adult(52))

assistant = Assistant("Слава", 22, "A99", "Физика")
print(assistant)
assistant.research()

print("-" * 30)
print("Порядок MRO для Assistant:")
for i in Assistant.mro():
    print(i)