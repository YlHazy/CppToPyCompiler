if __name__ == '__main__':
    n = None
    print("请输入数组的长度：")
    n= input()
    arr = [0] * 100
    print("请输入 " << n << " 个整数：")
    i = 0
    for i in range(i, n):
        i += 1
        arr[i]= input()
    i = 0
    for i in range(i, n-1):
        i += 1
        j = 0
        for j in range(j, n-i-1):
            j += 1
            temp=arr[j] = =arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
    print("排序后的数组是：")
    i = 0
    for i in range(i, n):
        i += 1
        print(arr[i] + " ")
    print("\n")
