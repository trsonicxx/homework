#homework
def pstr(a,b):
    if a.endswith(b):
	    return True
    else:
        return False
a=str(input())
b=str(input())
pstr(a,b)

'''23. Complete the solution so that it returns true if the first argument(string) 
passed in ends with the 2nd argument (also a string).
Examples:
solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false'''
