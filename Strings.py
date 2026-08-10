print ("Hello,Swaroop")

s = "Harshitha"
s=s[::-1]
print(s)

s="MoM"
if(s==s[::-1]):
    print("Yes")

s="Harshitha"
count=0
for ch in s:
    if ch in "aeiouAEIOU":
        count+=1
print(count)

#Character Frequency
from collections import Counter
a = "harshitha"
print(Counter(a))

#First Non Repeating Character
s = "swiss"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break

#Remove Duplicate Characters
s = "Swarooop"
seen = set()
result = ""
for ch in s:
    if ch  not in seen:
        result+=ch
        seen.add(ch)
print(seen)

#check Anagram
s1="listen"
s2="silent"
if(sorted(s1)==sorted(s2)):
    print("Yes")

#Reverse order of words in a string
s="Harshitha is a good girl"
words = s.split()
words.reverse()
result = " ".join(words)
print(result)

#Find the longest word in a string
s = "I love Java and Python"
count = 0
max_len= 0
for ch in s:
    if ch!=" ":
        count+=1
    else:
        max_len = max(max_len,count)
        count = 0

max_len = max(max_len,count)
print(max_len)

#First Repeating Character
s = "swiss"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
for ch in s:
    if freq[ch] > 1:
        print(ch)
        break

#Check Unique Characters in a string
s = "python"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0) +1
for ch in s:
    if(freq[ch]==1):
     print("Yes")
     break

# Longest Substring Without Repeating Characters
s=abcabccc
seen = set()
left = 0
max_len = 0
for right in range(len(s)):

    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    max_len = max(max_len, right - left + 1)
    print(max_len)