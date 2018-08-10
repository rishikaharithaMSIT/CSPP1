#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player. We'll be implementing the playHand function. This function allows the user to play out a single hand. First, though, you'll need to implement the helper calculateHandlen function, which can be done in under five lines of code.


def calculate_handlen(player_hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    hand_length = sum(list(player_hand.values()))
    return hand_length

def main():
	i_n = input()
	a_dict = {}
	for i in range(int(i_n)):
		da_ta = input()
		l_1 = da_ta.split()
		a_dict[l_1[0]] = int(l_1[1])
	print(calculate_handlen(a_dict))
		


if __name__ == "__main__":
	main()