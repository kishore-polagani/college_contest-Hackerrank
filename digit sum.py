Given a non-negative integer - N, print the sum of digits of the given number.

Input Format

First and only line of input contains a non-negative integer N.

Constraints

0 <= length(N) <= 103

Output Format

Print the sum of digits of the given number.

Sample Input 0

164
Sample Output 0

11
....
n=int(input())
s=0
while(n>0):
    t=n%10
    s=s+t
    n=n//10
print(s)
