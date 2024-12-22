def convert_input(user_input):
    try:
        return int(user_input)
    except ValueError:
        try:
            return float(user_input)
        except ValueError:
            return user_input
if __name__ == '__main__':
    n = None
    n= input()
    n = convert_input(n)
    arr = [0] * 100
    i = 0
    for i in range(int(i), int(n)):
        arr[i]= input()
        arr[i] = convert_input(arr[i])
    i = 0
    for i in range(int(i), int(n-1)):
        j = 0
        for j in range(int(j), int(n-i-1)):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    i = 0
    for i in range(int(i), int(n)):
        print(arr[i])
    print("\n")