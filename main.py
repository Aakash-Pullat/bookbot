from stats import count_words,get_word_freq,get_sorted_char_freq

def get_book_text(path_to_file):
    with open(path_to_file,"r",encoding = "utf-8-sig") as f:
        file_contents = f.read()
        return file_contents

path_to_file = "./books/frankenstein.txt"
text = get_book_text(path_to_file)
sorted_char_freq = get_sorted_char_freq(text)
print(sorted_char_freq)
