def get_word_count(text):
    words = text.split()
    word_count_int = len(words)
    return word_count_int

def get_char_count(text):
    t_count = 0
    p_count = 0
    c_count = 0

    for char in text.lower():
        if char == "t":
            t_count += 1
        elif char == "p":
            p_count += 1
        elif char == "c":
            c_count += 1

    print(f"'t': {t_count}, 'p': {p_count}, 'c': {c_count}")
    return t_count, p_count, c_count
