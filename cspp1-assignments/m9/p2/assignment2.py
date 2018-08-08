'''
Exercise: Assignment-2
Next, implement the function getGuessedWord that takes in two parameters
a string, secret_word, and a list of letters, letters_guessed. This function
returns a string that is comprised of letters and underscores, based on what
letters in letters_guessed are in secret_word. This shouldn't be too different from isWordGuessed!
'''
def replace_by(secret_word, secret_word_copy):
    #print(secret_word)
    for item in secret_word_copy:
        loc = secret_word.index(item)
        secret_word.remove(item)
        secret_word.insert(loc, '_')
        
    #print(secret_word)
    return secret_word

def convert_list_to_string(secret_word):
    str1 = ''.join(str(e) for e in secret_word)
    return str1

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secret_word = list(secret_word)
    secret_word_copy = secret_word[:]
    secret_word1 = secret_word[:]
    for i in letters_guessed:
        if i in secret_word:
            secret_word_copy =  replace_by(secret_word, i):
            secret_word =  list(filter(lambda a: a != i, secret_word))
        if len(secret_word) == 0:
            return convert_list_to_string(secret_word1)
        
    
    if len(secret_word) != 0:
        #secret_word_copy = replace_by(secret_word1,secret_word_copy)
        #print(secret_word_copy)
        return convert_list_to_string(secret_word_copy)
    else:
        return ""

def main():
    '''
    Main function for current assignment
    '''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(get_guessed_word(secret_word, list1))

if __name__ == "__main__":
    main()
