'''
    Assignment-1 Create Social Network
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''

    # remove the pass below and start writing your code
    persons_data = data.split('\n')
    follow_list = []
    for each_person in persons_data:
    	follow_list.append(each_person.split('follows'))
    print(follow_list)
    
    new_list2 = []
    for j in follow_list:
    	new_list = []
    	if j[0] != '':
    		new_list.append(j[0].strip(' '))
    		j[1] = j[1].strip(' ')
    		new_list.append(j[1].split(','))
    		new_list2.append(new_list)
    adict= {}
    for m in range(len(new_list2)):
    	if new_list2[m][0] in adict:
    		adict[new_list2[m][0]] += new_list2[m][1]
    	else:
    		adict[new_list2[m][0]] = new_list2[m][1]
    return adict

def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    print(create_social_network(string))

if __name__ == "__main__":
    main()
