def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    counts = {}

    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1


    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    return sorted_counts
