import sys
from stats import *

def main():
 try:
    Path = sys.argv[1]
    text = get_book_text(Path)
 except Exception as e:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)
 num = stringtext(text)
 count = count_chars(text)
 char = sort_chars(count)
 print("============ BOOKBOT ============")
 print(f"Analyzing book found at {Path}...")
 print("----------- Word Count ----------")
 print(f"Found {len(num)} total words")
 print("--------- Character Count -------")
 for item in char:
        character = item["char"]
        # Only print alphabetical characters
        if character.isalpha():
            print(f"{character}: {item['count']}")
    
 print("============= END ===============")

def get_book_text(Path):
  with open(Path) as f:  
    frank = f.read()
    return frank
 
main()
