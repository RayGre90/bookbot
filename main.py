def main():
    file_path = "books/frankenstein.txt"
    with open(file_path, "r") as file:
        file_contents = file.read()
    
    char_counts = count_char(file_contents)
    
    # Create char_list here
    char_list = []
    for char, count in char_counts.items():
        # Only include letters
        if char.isalpha():
            char_dict = {"char": char, "num": count}
            char_list.append(char_dict)

    char_list.sort(reverse=True, key=sort_on)

    # Print report
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(file_contents.split())} words found in the document\n")
    
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

def count_char(text):
    low_case = {}
    for char in text:
        char = char.lower()
        if char.isalpha():  # Only count letters
            if char not in low_case:
                low_case[char] = 1 
            else:
                low_case[char] = low_case[char] + 1
    return low_case

def sort_on(dict):
    return dict["num"]

main()