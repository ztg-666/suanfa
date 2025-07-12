list = [-1,-1,-1,-1,-1,-1]
l = 0
r = 0
while True:
    opt = int(input("1.入队 2.出队 3.查看队尾元素"))
    if opt == 1:
        num = int(input("请输入数字"))
        if r < len(list):
            list[r] = num
            r += 1
        else:
            print("队列已满")
    elif opt == 2:
        if l < r:
            print(list[l])
            l += 1
        else:
            print("队列已空")
    else:
        if l < r:
            print(list[r-1])
