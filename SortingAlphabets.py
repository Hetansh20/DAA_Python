def counting_sort_alphabets(s):
    # Define valid alphabet characters (A-Z, a-z)
    alphabet_chars = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

    # Initialize count map
    count = {char: 0 for char in alphabet_chars}

    # Count the letters in input string
    for char in s:
        if char in count:
            count[char] += 1

    # Construct sorted string
    sorted_str = ''.join(char * count[char] for char in alphabet_chars)

    return sorted_str

# Example usage
input_string = "b3A2c1aB9Z"
sorted_result = counting_sort_alphabets(input_string)
print("Sorted Alphabets:", sorted_result)