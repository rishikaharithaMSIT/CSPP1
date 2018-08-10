'''
Author: Rishika Haritha - 20186041
Encoding: Utf-8
'''

def is_validword(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    is_in_hand = False
    is_in_wordlist = False
    flag = 0
    for w in word:
        if w not in hand:
            flag = 1
    if not flag:
        is_in_hand = True
    if word in wordList:
        is_in_wordlist = True

    if is_in_hand and is_in_wordlist:
        return True
    return False


    


def main():
    '''in main function'''
    input_word = input()
    test_cases = int(input())
    a_dict={}
    for i in range(test_cases):
        da_ta = input()
        l_1 = da_ta.split()
        a_dict[l_1[0]] = int(l_1[1])
    l_2 = input().split()
    print(is_validword(input_word, a_dict, l_2))
        


if __name__ == "__main__":
    main()
