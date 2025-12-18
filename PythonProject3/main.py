def my_sqrt(num: int) -> bool:
    odd = 1
    while num > 0:
        num -= odd
        odd += 2
    return num == 0


print(my_sqrt(5))