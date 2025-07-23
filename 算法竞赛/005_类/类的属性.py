class Dog:
    # 这是初始化方法
    def __init__(self, Name, Age):
        # self 代表正在被创建的那个对象
        print(f"一只叫做 {Name} 的小狗被创建了！")

        # 将传入的参数值，绑定到对象自身的属性上
        self.name = Name
        self.age = Age


# 实例化时，在类名后面的括号里传入 __init__ 方法需要的参数 (self 除外)
dog1 = Dog("旺财", 2)
dog2 = Dog("大黄", 3)

# 访问对象的属性
print(f"{dog1.name} 今年 {dog1.age} 岁了。")  # 输出: 旺财 今年 2 岁了。
print(f"{dog2.name} 今年 {dog2.age} 岁了。")  # 输出: 大黄 今年 3 岁了。
