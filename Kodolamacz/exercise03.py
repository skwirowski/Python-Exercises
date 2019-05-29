# 1. Smart Exponentiation
#    Example: 2^7 = 2^3 * 2^3 * 2 = 128
#    Write recursive function calculating exponentiation based on preceding example


def smart_exponentiation(base, power):
    if power == 1:
        return base
    if power == 0:
        return 1
    half = smart_exponentiation(base, power // 2)
    if power % 2 == 0:
        return half * half
    else:
        return half * half * base


print("===== smart_exponentiation function =====")
print(smart_exponentiation(2, 7))

# 2. Palindrome
#    Create function that returns True when argument string is palindrome otherwise it should return False


def is_palindrome(string):
    return string == string[::-1]


def is_palindrome_another_take(string):
    n = len(string)
    for i in range(len(string)//2):
        if string[i] != string[n-i-1]:
            return False
    return True


print("===== is_palindrome function =====")
print(is_palindrome("ready to check for palindromes"))
print(is_palindrome("abcdefedcba"))
print("===== is_palindrome_another_take function =====")
print(is_palindrome_another_take("aaccddeeefhiklmnoooprrrsty"))
print(is_palindrome_another_take("abcdefedcba"))

# 3. Anagram
#    Create function that checks if two string arguments are anagrams


def is_anagram_sorting(base_string, tested_string):
    if len(base_string) != len(tested_string):
        return False

    sorted_base_string = "".join(sorted(base_string))
    sorted_tested_string = "".join(sorted(tested_string))

    if sorted_base_string == sorted_tested_string:
        return True
    else:
        return False


print("===== is_anagram_sorting function =====")
print(is_anagram_sorting("gbcdefa", "gfedcba"))
print(is_anagram_sorting("gbcdefaz", "gfedcbay"))


def is_anagram_dictionary(base_string, tested_string):
    length = len(base_string)

    if length != len(tested_string):
        return False

    base_dictionary = dict()
    tested_dictionary = dict()

    for i in range(length):
        if base_string[i] in base_dictionary:
            base_dictionary[base_string[i]] += 1
        else:
            base_dictionary[base_string] = 1
        if tested_string[i] in tested_dictionary:
            tested_dictionary[tested_string] += 1
        else:
            tested_dictionary[tested_string] = 1

    return base_dictionary == tested_dictionary


print("===== is_anagram_dictionary function =====")
print(is_anagram_sorting("abcdefghijklmnop", "ponmlkjihgfedcba"))
print(is_anagram_sorting("ponmlkjihgfedcbar", "abcdefghijklmnop"))


# 5. Characters occurrence
#    Write a function that checks if at least the same number of each character from first string appears in another one


def do_all_characters_occur(base_string, tested_string):
    if len(tested_string) < len(base_string):
        return False

    initial_letter_count = len(base_string)
    letter_count = len(base_string)
    loop_passes = 0

    def check_for_occurrences(string, character):
        return string.count(character)

    while letter_count > 0:
        base_character_occurrence = check_for_occurrences(base_string, base_string[0])
        tested_character_occurrence = check_for_occurrences(tested_string, base_string[0])

        if tested_character_occurrence < base_character_occurrence:
            break

        letter_count -= base_character_occurrence
        base_string = base_string.replace(base_string[0], "")
        loop_passes += 1

    print("Loop passes")
    print(loop_passes)
    print("Initial letter count")
    print(initial_letter_count)

    if letter_count == 0:
        return True
    else:
        return False


print("===== do_all_characters_occur function =====")
print(do_all_characters_occur("aabbccddxx", "axbcdefaghidjklmnboprstuqcwxyz"))
print(do_all_characters_occur("aabbccddxx", "abcdeabcdefgaabbccddeefx"))