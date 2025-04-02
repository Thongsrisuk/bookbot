
def stringtext(text):
 tes = text.split()
 return tes

def count_chars(num):
    char_counts = {}
    for char in num:
        lowercase_char = char.lower()
        if lowercase_char in char_counts:
            char_counts[lowercase_char] += 1
        else:
            char_counts[lowercase_char] = 1
    return char_counts

def sort_chars(char_count):
    chars_list = []
    
    for char, count in char_count.items():
        chars_list.append({"char": char, "count": count})
    
    # Sort the list by the count value
    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list





