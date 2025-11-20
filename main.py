from stats import count_words,get_sorted_char_freq
import sys

def get_book_text(path_to_file):
    with open(path_to_file,"r",encoding = "utf-8-sig") as f:
        file_contents = f.read()
        return file_contents
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path_to_file = sys.argv[1]
text = get_book_text(path_to_file)
count = count_words(text)
sorted_char_freq = get_sorted_char_freq(text)
print(f"Found {count} total words")
for i in sorted_char_freq:
    print(f"{i["char"]}: {i["num"]}",end = "\n")
