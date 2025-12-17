def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


print(plusOne([9]))
print(plusOne([9,9,9,9,9]))
print(plusOne([1,2,3]))
print(plusOne([1,2,9]))
print(plusOne([8,9,9,9]))