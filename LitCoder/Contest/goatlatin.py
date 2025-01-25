def goat_latin_conversion(sentence):
    """
    Converts a given sentence into Goat Latin as per the specified rules.

    :param sentence: str, input sentence consisting of words separated by spaces.
    :return: str, the Goat Latin converted sentence.
    """
    # Helper function to check if a character is a vowel
    def is_vowel(ch):
        return ch.lower() in {'a', 'e', 'i', 'o', 'u'}

    words = sentence.split()  # Split the sentence into words
    goat_latin_words = []  # List to store converted words

    for index, word in enumerate(words, start=1):
        if is_vowel(word[0]):
            # Rule 1: If the word starts with a vowel, append 'ma'
            converted_word = word + "ma"
        else:
            # Rule 2: If the word starts with a consonant, move the first letter to the end, then add 'ma'
            converted_word = word[1:] + word[0] + "ma"

        # Rule 3: Add 'a' repeated based on the word's index
        converted_word += "a" * index

        goat_latin_words.append(converted_word)

    # Join the converted words with spaces to form the final sentence
    return " ".join(goat_latin_words)

# Get input from the user
if __name__ == "__main__":
    user_input = input("Enter a sentence to convert to Goat Latin: ").strip()
    if user_input:
        result = goat_latin_conversion(user_input)
        print("Goat Latin Conversion:", result)
    else:
        print("Invalid input! Please enter a valid sentence.")
