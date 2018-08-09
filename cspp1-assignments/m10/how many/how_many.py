'''
Author: Rishika Haritha - 20186041
Encoding: Utf-8
'''

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count_vals = 0
    for i in aDict:
        count_vals += len(aDict[i])
    return count_vals
    

def main():
    aDict={}
    test_cases = int(input())
    for i in range(test_cases):
        s=input()
        l=s.split()
        if l[0][0] not in aDict:
            aDict[l[0][0]]=[l[1]]
        else:
            aDict[l[0][0]].append(l[1])
    print(how_many(aDict))


if __name__== "__main__":
    main()