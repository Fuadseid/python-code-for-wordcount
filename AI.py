def count_char_frequency(input_str):
    """
    Counts the frequency of each character in the input string.
    
    Args:
        input_str (str): The input string.
    
    Returns:
        dict: A dictionary where the keys are the characters and the values are their frequencies.
    """
    char_freq = {}
    for char in input_str:
        if char.isalpha():
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
    return char_freq

# Example usage
input_string = input("Enter a string: ")
char_frequency = count_char_frequency(input_string)

print("Character Frequency:")
for char, freq in char_frequency.items():
    print(f"{char}: {freq}")
