#Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that takes a some numbers in the tuple as input and returns a tuple in which contains odd index values in the input tuple  



def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    odd_tup = ()
    odd_tup = aTup[::2]
    return odd_tup

def main():
	data=input()
	for i in range(int(data)):
		a = input()
		l=a.split()
		aTup=()
		for j in range(len(l)):
			aTup+=(int(l[j]),)
		print(oddTuples(aTup))

if __name__== "__main__":
	main()