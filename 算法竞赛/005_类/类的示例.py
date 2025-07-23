# 汽车设计蓝图 (Class)
class Car:
    # 初始化方法，定义汽车的基本属性
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0  # 初始速度为0
        self.is_running = False  # 初始状态为熄火

    # 启动汽车的方法
    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.color}的{self.brand} {self.model} 启动了！")
        else:
            print("汽车已经在运行中了。")

    # 加速的方法
    def accelerate(self, value):
        if self.is_running:
            self.speed += value
            print(f"加速 {value} km/h, 当前速度: {self.speed} km/h")
        else:
            print("请先启动汽车！")

    # 刹车的方法
    def brake(self, value):
        if self.speed >= value:
            self.speed -= value
        else:
            self.speed = 0
            self.is_running = False
        print(f"减速 {value} km/h, 当前速度: {self.speed} km/h")

    # 显示汽车信息的方法
    def get_info(self):
        if self.is_running:
            status = "运行中"
        else:
            status = "已熄火"
        return f"品牌: {self.brand}, 型号: {self.model}, 颜色: {self.color}, 状态: {status}"


# --- 开始使用这个蓝图创建汽车 ---

# 创建一辆特斯拉 (Object/Instance)
my_tesla = Car("特斯拉", "Model 3", "红色")

# 创建另一辆宝马 (Object/Instance)
my_bmw = Car("宝马", "X5", "黑色")

# 操作特斯拉
print(my_tesla.get_info())
my_tesla.accelerate(50)  # 提示先启动
my_tesla.start()
my_tesla.accelerate(80)
my_tesla.brake(30)
print(f"特斯拉当前速度: {my_tesla.speed} km/h")

print("-" * 20)

# 操作宝马
print(my_bmw.get_info())
my_bmw.start()
my_bmw.accelerate(100)
print(f"宝马当前速度: {my_bmw.speed} km/h")

