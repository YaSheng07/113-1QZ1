# @package 物件導向設計
class Person:
    name: str
    age: int
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        pass

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."
        pass
    
    def haveBirthday(self):
        self.age += 1
        print(f"Happy birthday, {self.name}! You are now {self.age} years old.")
        pass
    pass

# 創建 Person 類的實例
person1 = Person(name="Alice", age=30)

# 呼叫 greet 方法
print(person1.greet())  # 輸出: Hello, my name is Alice and I am 30 years old.

# 呼叫 haveBirthday 方法
person1.haveBirthday()  # 輸出: Happy birthday, Alice! You are now 31 years old.

# 呼叫 greet 方法
print(person1.greet())  # 輸出: Hello, my name is Alice and I am 31 years old.

person2 = Person(name="Andy", age=20)


print(person2.greet())  # 輸出: Hello, my name is Andy and I am 20 years old.


person2.haveBirthday()  # 輸出: Happy birthday, Andy! You are now 21 years old.


print(person2.greet())  # 輸出: Hello, my name is Andy and I am 21 years old.