def count_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def get_char_freq(text):
    char_freq = {}
    for char in text:
        char = char.lower()
        if char in char_fre:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq

def sorted_char_freq(text):
    char_freq_list = []
    for char in text:
        char = char.lower()
        if char_freq[{"char":char}]:

