def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))


max_sum = 0
max_num = 0

while True:
    try:
        num = int(input("Введите целое число (или 0 для выхода): "))
    except ValueError:
        print("Это не целое число. Пожалуйста, попробуйте еще раз.")
        continue

    if num == 0:
        break
    elif sum_of_digits(num) > max_sum:
        max_sum = sum_of_digits(num)
        max_num = num

print("Число с максимальной суммой цифр:", max_num)
