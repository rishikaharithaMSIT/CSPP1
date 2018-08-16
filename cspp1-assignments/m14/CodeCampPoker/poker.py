'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def make_dict(hand):
    """Convert hand to dictionary"""
    dict_val = {}
    for i in hand:
        if i in dict_val:
            dict_val[i] += 1
        else:
            dict_val[i] = 1
    return dict_val

def is_four_of_kind(hand):
    """Check for four of a kind"""
    dict_val = make_dict(hand)
    is_four_count = 0
    for i in dict_val:
        if dict_val[i] == 4:
            is_four_count += 1
    if is_four_count == 0:
        return False
    return True
def is_three_of_kind(hand):
    """Check for three of a kind"""
    dict_val = make_dict(hand)
    #print(dict_val)
    is_three_count = 0
    for i in dict_val:
        if dict_val[i] == 3:
            is_three_count += 1
            #print(dict_val[i], dict_val, is_three_count)
    if is_three_count == 0:
        return False
    return True

def is_one_pair(hand):
    """Check for a pair"""
    dict_val = make_dict(hand)
    is_four_count = 0
    for i in dict_val:
        if dict_val[i] == 2:
            is_four_count += 1
    if is_four_count == 1:
        return True
    return False
def is_two_pair(hand):
    """Check for two pairs"""
    dict_val = make_dict(hand)
    is_four_count = 0
    for i in dict_val:
        if dict_val[i] == 2:
            is_four_count += 1
    if is_four_count == 2:
        return True
    return False

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    len_hand = len(hand)
    for i in range(len_hand):
        if hand[i] == 'A':
            hand[i] = 1
        if hand[i] == 'J':
            hand[i] = 11
        if hand[i] == 'Q':
            hand[i] = 12
        if hand[i] == 'K':
            hand[i] = 13
        if hand[i] == 'T':
            hand[i] = 10
        hand[i] = int(hand[i])
    #print(hand)
    hand.sort()
    #print(hand)
    seq_hand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    flag = False
    if hand[0] == 1:
        #print(hand[1:5] , seq_hand[9:14])
        if hand[1:5] == seq_hand[9:14]:
            #print(hand[1:5], "try try try", seq_hand[9:14])
            return True
    else:
        len_seq = len(seq_hand)
        for i in range(len_seq):
            if hand == seq_hand[i:(i+5)]:
                #print(hand, "try try try", seq_hand[i:(i+5)])
                flag = True
    if flag is True:
        return True
    return False



def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    flag = False
    len_hand = len(hand)
    for i in range(len_hand-1):
        if hand[i] is not hand[i+1]:
            flag = True
            break
    if flag:
        return False
    return True

def is_no_same(hands):
    ok = []
    len_hand = len(hands)
    for j in range(len_hand):
        hand_val = []
        for k in range(len(hands[j])):
            hand_val.append(hands[j][k])
        for i in range(len_hand):
        if hand[i] == 'A':
            hand[i] = 14
        if hand[i] == 'J':
            hand[i] = 11
        if hand[i] == 'Q':
            hand[i] = 12
        if hand[i] == 'K':
            hand[i] = 13
        if hand[i] == 'T':
            hand[i] = 10
        hand[i] = int(hand[i])
    #print(hand)
        ok.append(hand_val)

    k = max(ok)
    print("k is",k)

def is_same(com_list):
    def isone_pair(hand):
        """Check for a pair"""
        check = False
        o = []
        dict_val = make_dict(hand)
        #print("dictval ",dict_val)
        is_four_count = 0
        for i in dict_val:
            if dict_val[i] == 2:
                check = True
                q = i
                o.append(q)

        #print("o", o)
        return o

    max_r = 0
    for i in com_list:
        if com_list[i] > 0:
            max_r = com_list[i]
    #print(max_r)
    s_rank = []
    #print("com list : ",com_list)
    for i in com_list:
        if max_r == com_list[i]:
            i = i.strip("[]")
            i = i.split(",")
            for j in range(len(i)):
                i[j] = i[j].strip(" ''")
            #print("i is : ",i)
            hand_val = []
            len_hand = len(i)
            for j in range(len_hand):
                hand_val.append(i[j][0])
            g = [i ,isone_pair(hand_val)]
            s_rank.append(g)
    #print("srank : ",s_rank)
    #print("after: ",com_list)
    maxv = 0
    maxh = []
    for i in range(len(s_rank)):
        if int(s_rank[i][1][0]) > maxv:
            maxv = int(s_rank[i][1][0])
            maxh = s_rank[i][0]
    #print("max h", maxh)
    return maxh

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    hand_val = []
    len_hand = len(hand)
    for i in range(len_hand):
        hand_val.append(list(hand[i])[0])
    hand_suit = []
    for i in range(len_hand):
        hand_suit.append(list(hand[i])[1])
    #print(hand_suit, hand_val)
    if is_straight(hand_val) and is_flush(hand_suit):
        #print("sf")

        return 8
    if is_four_of_kind(hand_val):
        #print("4k")
        return 7
    if is_flush(hand_suit):
        #print("f")
        return 5
    if is_straight(hand_val):
        #print("s")
        return 4
    if is_three_of_kind(hand_val) and is_one_pair(hand_val):
        #print("fh")
        return 6
    if is_three_of_kind(hand_val):
        #print("3k")
        return 3
    if is_two_pair(hand_val):
        return 2
    if is_one_pair(hand_val):
        return 1

    return 0

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    com_list = {}
    hand_list =[]
    #print("hands", hands)
    for i in range(len(hands)):
        com_list[str(hands[i])] = hand_rank(hands[i])  
    
    n = max(hands, key=hand_rank)
    r = hand_rank(n)
    if r == 1:
        h = is_same(com_list)
        return h
    if r == 0:
        h = is_no_same(hands)
    return n

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    #print(HANDS)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
