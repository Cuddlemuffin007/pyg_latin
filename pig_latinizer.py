# program to transform strings to pig-latin version
#import re


PIG_ENDING = 'ay'
VOWEL_ENDING = 'say'

user_input = input("Pig-latinize it!\n>> ")

# checks to see if string starts with a vowel, returns True or False
def starts_with_vowel(test_str):
    vowels = "aeiouAEIOU"
    #vowel = re.compile(r'[aeiou]', re.IGNORECASE)
    #if vowel.match(test_string):
    if test_str[0] in vowels:
        return True
    return False

# checks to see if string starts with a digraph or trigraph
# Returns False if not, else digraphs return 2, trigraphs return 3
def start_or_end_with_di_or_trigraph(test_str):
    digraphs = ['bl', 'br', 'ch', 'ck', 'cl',
                'cr', 'dr', 'fl', 'fr', 'gh',
                'gl', 'gr', 'ng', 'ph', 'pl',
                'pr', 'qu', 'sc', 'sh', 'sk',
                'sl', 'sm', 'sn', 'sp', 'st',
                'sw', 'th', 'tr', 'tw', 'wh', 'wr']

    trigraphs = ['scr', 'shr', 'spl', 'spr',
                 'squ', 'str', 'thr']

    words = test_str.lower().split()
    for word in words:
        if word[0:3] in trigraphs:
            return 3
        elif word[0:2] in digraphs:
            return 2
        elif word[-5:-2] in trigraphs:
            return -5
        elif word[-4:-2] in digraphs:
            return -4
    return False

def pig_latinizer(test_str):
    result_list = []
    word_list = test_str.split()
    print(word_list)
    for word in word_list:
        # for testing
        #print("Word: ", word, "\n",
        #      "Starts with vowel?: ", starts_with_vowel(word), "\n",
        #      "Starts with digraph or trigraph?", starts_with_di_or_trigraph(word))
        if starts_with_vowel(word):
            result_list.append(word + VOWEL_ENDING)
        elif start_or_end_with_di_or_trigraph(word):
            result_list.append(
                word[start_or_end_with_di_or_trigraph(word):] +
                word[0:start_or_end_with_di_or_trigraph(word)] + PIG_ENDING)
        else:
            result_list.append(word[1:] + word[0] + PIG_ENDING)

    return ' '.join(result_list)

#reverses pig-latinization, also takes into account di or trigraphs
def depig(test_str):
    word_list = test_str.split()
    print(word_list)
    result_list = []
    for word in word_list:
        if word[-3:] == VOWEL_ENDING:
            result_list.append(word[:-3])
        elif start_or_end_with_di_or_trigraph(word):
            result_list.append(word[start_or_end_with_di_or_trigraph(word):-2] +
                               word[:start_or_end_with_di_or_trigraph(word)])
        else:
            result_list.append(word[-3:-2] + word[:-3])

    return ' '.join(result_list)

print(pig_latinizer(user_input))

print(depig(pig_latinizer(user_input)))