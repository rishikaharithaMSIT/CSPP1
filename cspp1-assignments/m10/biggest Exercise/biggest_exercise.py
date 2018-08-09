#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    max_vals = len(aDict[list(aDict.keys())[0]])
    max_key = list(aDict.keys())[0]
    for i in aDict:
        if max_vals < len(aDict[i]):
            max_vals = len(aDict[i])
            max_key = i
    return max_key

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
        
    print(biggest(aDict))


if __name__== "__main__":
    main()