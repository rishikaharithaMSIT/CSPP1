'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
	'''this is main function'''
	in_strs = input()
	# the input string is in s
	# remove pass and start your code here
	count_1 = 0
	count_max = 0
	end_index=0
	for index_strs in range(len(in_strs)-1):
		if ord(in_strs[index_strs]) <= ord(in_strs[index_strs+1]):
			count_1 += 1
		else: 
			count_1= 0
				
		if count_max <= count_1:
			count_max = count_1
			end_index = index_strs+1
			

	print(in_strs[end_index - count_max:end_index+1])	

if __name__== "__main__":
	main()
