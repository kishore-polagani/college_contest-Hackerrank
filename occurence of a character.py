Given a sentence S and a character ch, count occurrence of the given character in the sentence

Input Format

First line of input contains a sentence - S and second line of input contains a single lowercase character - ch.

Constraints

1 <= len(S) <= 100

Output Format

Print count of the given character in the sentence.

Sample Input 0

Data Structures & Algorithms
s
Sample Output 0

2
...
s=input()
k=input()
c=0
for i in range(len(s)):
    if k==s[i]:
        c=c+1
print(c)
