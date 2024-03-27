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


def sortFrequencies(token_frequencies):
    """
    This function takes a dictionary of token - frequency pairs as input
    and return a dictionary in sorted order (order by decreasing frequency
    of token)

    Time complexity: O(n*logn), with n is number of item in the input dictionary,
    because this function use sorted() and dict(), which have complexity
    O(nlogn) and O(n) respectively. As a result, the time complexity of
    the function is dominated by O(nlogn)
    """
    token_frequency_tuples = token_frequencies.items()
    sorted_token_frequencies = sorted(
        token_frequency_tuples, key=lambda item: item[0]
    )  # sort on secondary key (alphabet)
    sorted_token_frequencies = sorted(
        sorted_token_frequencies, key=lambda item: item[1], reverse=True
    )  # sort on primary key (frequency) in reverse order
    sorted_token_frequencies_dict = dict(sorted_token_frequencies)
    return sorted_token_frequencies_dict


def printResult(token_frequencies):
    """
    This function takes a dictionary as input and print out the content of
    the dictionary in format "token\tfrequency"

    Time complexity: O(n), with n is the number of items in the token_frequencies
    dictionary. This is because the function uses a for loop to iterate through
    each item in the input.
    """
    for token, frequency in token_frequencies.items():
        print(f"{token}\t{frequency}")


def main():
    file_path = sys.argv[1]
    words_list = tokenizeFile(file_path)
    if words_list == False:
        return 0
    token_frequencies = countTokenFrequencies(words_list)
    ordered_token_frequencies = sortFrequencies(token_frequencies)
    printResult(ordered_token_frequencies)


if __name__ == "__main__":
    main()
