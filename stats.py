def count_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def get_char_freq(text):
    char_freq = {}
    for char in text:
        if not(char.isalpha()):
            continue
        char = char.lower()
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq

def helper_sort(char_list):
    return char_list["num"]

def get_sorted_char_freq(text):
    text = text.lower()
    temp_list = get_char_freq(text)
    sorted_char_list = []
    for char in temp_list:
        char_freq = {"char":char,"num":temp_list[char]}
        sorted_char_list.append(char_freq)
    sorted_char_list.sort(reverse=True, key=helper_sort)
    return sorted_char_list
