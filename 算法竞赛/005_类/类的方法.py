class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义一个方法（行为）
    def bark(self):
        # 方法内部可以通过 self 访问到对象自身的属性
        print(f"{self.name} 正在汪汪叫！")

    # 定义另一个方法
    def get_human_age(self):
        # 假设狗的1岁等于人的7岁
        human_age = self.age * 7
        print(f"如果 {self.name} 是人，它已经 {human_age} 岁了。")

# 创建对象
my_dog = Dog("小白", 4)

# 调用对象的方法
my_dog.bark()          # 输出: 小白 正在汪汪叫！
my_dog.get_human_age() # 输出: 如果 小白 是人，它已经 28 岁了。
