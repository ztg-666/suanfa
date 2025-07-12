# Python：
# dict 是字典的实现，底层使用哈希表。
# 因此在该语言中两者通常被视为等价。

# 创建字典
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Physics"]
}

# 1. 访问元素
print(f"学生姓名: {student['name']}")  # 输出: Alice
print(f"年龄: {student.get('age')}")   # 使用 get 方法安全访问

# 2. 修改元素
student["age"] = 21  # 更新年龄
student["university"] = "MIT"  # 添加新键值对
print(f"更新后: {student}")

# 3. 删除元素
removed_courses = student.pop("courses")  # 删除并返回被删值
print(f"已删除课程: {removed_courses}")
print(f"删除后字典: {student}")

# 4. 遍历字典
print("\n遍历字典:")
for key, value in student.items():
    print(f"{key}: {value}")

# 5. 检查存在性
print("\n检查键是否存在:")
print("'age' in student:", 'age' in student)  # 输出: True
print("'grade' in student:", 'grade' in student)  # 输出: False

# 6. 字典合并
additional_info = {"grade": "A", "country": "USA"}
student.update(additional_info)
print(f"\n合并后字典: {student}")

# 7. 特殊方法
print("\n字典视图对象:")
print("所有键:", student.keys())
print("所有值:", student.values())
