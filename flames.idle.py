def remove_common_letters(str1, str2):
    common_letters = set(str1) & set(str2)
    for letter in common_letters:
        str1 = str1.replace(letter, '', 1)
        str2 = str2.replace(letter, '', 1)
    return str1, str2

def calculate_flames_count(name1, name2):
    name1, name2 = remove_common_letters(name1, name2)
    total_length = len(name1) + len(name2)
    flames_count = total_length % 6
    return flames_count

def get_flames_result(flames_count):
    flames_dict = {
        1: "FRIENDS",
        2: "LOVE",
        3: "AFFECTION",
        4: "MARRIAGE",
        5: "ENEMY",
        0: "SIBLING"
    }
    return flames_dict[flames_count]

def play_flames_game():
    print("!!!FLAMES TIME!!!")
    name1 = input("NamE 1: ").lower()
    name2 = input("NamE 2: ").lower()

    flames_count = calculate_flames_count(name1, name2)
    result = get_flames_result(flames_count)

    print(f"The relationship between {name1.capitalize()} and {name2.capitalize()} is: {result}")


play_flames_game()
