def smallest_ones_length(k: int) -> int:
    # Если k делится на 2 или 5 — ответа не существует
    if k % 2 == 0 or k % 5 == 0:
        return -1

    remainder = 0
    for length in range(1, k + 1):
        remainder = (remainder * 10 + 1) % k
        if remainder == 0:
            return length

    return -1
print(smallest_ones_length(7))