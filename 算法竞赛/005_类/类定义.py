# 定义一个最简单的“狗”的蓝图
class Dog:
    pass # pass 是一个占位符，表示这个类里面暂时什么都没有

# 现在，我们根据这个蓝图来“创建”一只具体的狗（对象）
# 这个过程叫做 “实例化” (Instantiation)
my_dog = Dog()

# my_dog 就是一个 Dog 类的对象（或实例）
print(my_dog)
# 输出: <__main__.Dog object at 0x...>  (表示这是一个Dog对象，后面是它在内存中的地址)
