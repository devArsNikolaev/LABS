numbers = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
inp = input('Введите строку')
for i in inp:
    if int(i) in numbers.keys():
        numbers[int(i)] += 1
result_value = numbers[0]
result_char = 0
for j in range(9):
    if result_value < numbers[j]:
        result_char = j
        result_value = numbers[j]

print('больше всего цифр', result_char)