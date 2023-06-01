def rabin_karp_search(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    prime = 101
    operations = 0

    if pattern_len > text_len:
        return -1, operations

    # Вычисляем хэши для паттерна и первой подстроки текста
    pattern_hash = 0
    text_hash = 0
    for i in range(pattern_len):
        pattern_hash += ord(pattern[i]) * (prime ** i)
        text_hash += ord(text[i]) * (prime ** i)
        operations += 2

    # Ищем паттерн в тексте
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash:
            # Если хэши совпадают, проверяем символы
            found = True
            for j in range(pattern_len):
                operations += 1
                if text[i + j] != pattern[j]:
                    found = False
                    break
            if found:
                return i, operations

        # Обновляем хэш текста для следующей подстроки
        if i < text_len - pattern_len:
            text_hash = (text_hash - ord(text[i])) // prime
            text_hash += ord(text[i + pattern_len]) * (prime ** (pattern_len - 1))
            operations += 3

    return -1, operations


text = "amcambamv"
pattern = "amb"
index, operations = rabin_karp_search(text, pattern)
print(f"Index: {index}, count operations: {operations}")