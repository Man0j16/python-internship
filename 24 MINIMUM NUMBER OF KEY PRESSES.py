'''Title
MINIMUM NUMBER OF KEY PRESSES

Description
George has a setup which includes a special keyboard and a monitor , that initially displays 0. The special keyboard has 11
numeric keys (0,1,2,3,4,5,6,7,8,9,00). If he presses 00, the previously displayed value will be multiplied by 100. Whereas, if he
presses any other numeric key, the previously displayed value will be firstly multiplied by 10 and then the number on the key
will be added to it
You are given a numeric string S. Your task is to help George find and return an integer value, representing the minimum
number of key presses to reach the number.
Input Specification:
input: A numeric string s. representing the final number,
Output Specification:
Return an integer value, representing the minimum number of key presses to reach the number.
Sample Input:
100
Sample Output:
2'''
SourceCode:
def min_key_presses(s):
 target = int(s)
 presses = 0
 
 while target > 0:
    if target % 100 == 0:
        target //= 100
 else:
        target //= 10
 presses += 1
 
 return presses
# Example usage:
s = input().strip() 
print(min_key_presses(s))

