q=int(input())
total=[[1,-1]]
head=0

def insert(ori_node,new_code,cur):
    total.append([new_code,-1])
    while total[cur][0]!=ori_node:
        cur=total[cur][1]
    total[len(total)-1][1]=total[cur][1]
    total[cur][1]=len(total)-1
    return

def query(ori_node,cur):
    while total[cur][0]!=ori_node and total[cur][1]!=-1:
        cur=total[cur][1]
    if total[cur][0]==ori_node  and total[cur][1]!=-1 :
        print(total[total[cur][1]][0])
        return
    print(0)

def dl(ori_node,cur):
    while total[cur][0] != ori_node:
        cur = total[cur][1]
    total[cur][1]=total[total[cur][1]][1]
    return



for i in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        insert(que[1], que[2], head)
    elif que[0] == 2:
        query(que[1], head)
    elif que[0] == 3:
        dl(que[1], head)

