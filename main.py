# Git Repository: https://github.com/TheDevFruit/AICourse

arr = ['Иван', 'Алиса', 'Петр', 'Ольга', 'Евгения', 'Дмитрий', 'Ли']

for_first = lambda x: x[0]
arr.sort(key=for_first)

for i in range(len(arr)):
    print(f"{i} {arr[i]}")
