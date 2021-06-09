def set_gen(lst):
    i= 0
    while i < len(lst):
        cnt = lst.count(lst[i])
        if cnt > 1:
            lst[i] = str(lst[i]) * cnt
        i+= 1
    return set(lst)
l = []
n = int(input('Введите желаемое количество элементов списка: '))
for i in range(n):
    l.append(int(input('Введите значение элемента, который хотите добавить в список: ')))
print("Список: ",l)

print('Измененный список: ',set_gen(l))