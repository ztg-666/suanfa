a = [-1,-1,-1,-1,-1]

top = 0

while True:
    opt = int(input("1.入栈 2.出栈 3.查看栈顶元素"))
    if opt == 1:
        num = int(input("请输入数字"))
        if top < len(a):
            a[top] = num
            top += 1
        else:
            print("栈已满")
    elif opt == 2:
        if top > 0:
            print(a[top-1])
            top -= 1
            print("出栈成功")

        else:
            print("栈已空")
    elif opt == 3:
        if top > 0:
            print("栈顶元素为:",a[top-1])
    elif opt == 4:
        print(a)
    else:
        break