def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    counts = {}
    for character in text:
        if character.isalpha():
            lowered = character.lower()
            counts[lowered] = counts.get(lowered, 0) + 1
    return [{"char": char, "num": total} for char, total in counts.items()]


def sort_on(items):
    return items["num"]


def sort_counts(counts):
    return sorted(counts, reverse=True, key=sort_on)
