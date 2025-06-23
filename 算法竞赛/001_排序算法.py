def Selection_Sort(a):

    for i in range(len(a)):
        min = a[i]
        min_index = i
        for j in range(i+1,len(a)):
            if a[j] < min:
                min = a[j]
                min_index = j
        a[i],a[min_index] = a[min_index],a[i]
        print(a)
    return a
def Bubble_Sort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

def Insertion_Sort(a):
    for i in range(1,len(a)):
        j = i
        while j > 0 and a[j] < a[j-1]:
            a[j],a[j-1] = a[j-1],a[j]
            j -= 1
        print(a)
    return a
a = [5,2,8,1,9]
# a = Selection_Sort(a)
# a = Bubble_Sort(a)
a = Insertion_Sort(a)
print(a)