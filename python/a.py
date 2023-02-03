if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    max = arr[0]
    i = 1
    temp = 0
    while i < len(arr)-1:
        if(arr[i] > max):
            print(arr[i])
        i = i+1

    print(temp)
