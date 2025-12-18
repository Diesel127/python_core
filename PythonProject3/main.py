def is_polindrom(s):
    cleaned = []
    for ch in s:
        if ch.isalnum():
            cleaned.append(ch.lower())
    return cleaned == cleaned[::-1]

print(is_polindrom(" Kazak"))