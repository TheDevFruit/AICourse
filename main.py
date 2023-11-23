# Git Repository: https://github.com/TheDevFruit/AICourse

arr = [0, 1]
n = int(input("Введите N-Число: "))
for i in arr:
    arr.append(arr[len(arr)-1] + arr[len(arr)-2])
    if len(arr)-1 == n:
        print(arr[len(arr)-1])
        break
