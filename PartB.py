import sys


def tokenizeFile(file_path):
    """
    This function takes a file path or file name as an input and return a list
    of words tokenized from the file. Any characters beside a-z, A-Z, and 0-9
    will not be considered, and all valid characters are turned into lower case.

    Time complexity: O(n), with n is the number of characters in the input file.
    The function runs in linear time relative to the size of the input since every
    submethod it uses (such as read, replace, lower, split) checks through each characters
    in the input
    """
    try:
        with open(file_path, encoding="utf-8") as file:
            content = file.read()  # content has type string
            for character in content:
                if (not character.isascii()) or (
                    not character.isalnum() and not character.isspace()
                ):
                    content = content.replace(character, " ")
            formatted_content = content.lower()
            words_list = formatted_content.split()
            return words_list
    except FileNotFoundError:
        print("Cannot open the file")
        return False


def countTokenFrequencies(words_list):
    """
    This function takes a list of words as input and return a dictionary with
    key - value pair as token - frequency.

    Time complexity: O(n), with n is the number of words in words_list. This is
    because the function uses a for loop to checks through every word in the
    words_list input.
    """
    token_frequencies = dict()
    for word in words_list:
        if word in token_frequencies:
            token_frequencies[word] += 1
        else:
            token_frequencies[word] = 1
    return token_frequencies


def countCommonToken(token_dict_1, token_dict_2):
    """
    This function takes input as 2 dictionaries and return the number of
    common keys between those dicts.

    Time complexity: O(n), with n is number of items in token_dict_1, because
    the function uses a for loop to iterate through each item in the dict
    """
    common_token_count = 0
    for item in token_dict_1.items():
        if token_dict_2.get(item[0]):
            common_token_count += 1
    return common_token_count


def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    words_list_1 = tokenizeFile(file1)
    words_list_2 = tokenizeFile(file2)
    if words_list_1 == False or words_list_2 == False:
        return 0

    token_freq_1 = countTokenFrequencies(words_list_1)
    token_freq_2 = countTokenFrequencies(words_list_2)

    num_common_token = countCommonToken(token_freq_1, token_freq_2)
    print(num_common_token)


if __name__ == "__main__":
    main()
