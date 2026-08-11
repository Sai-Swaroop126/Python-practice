#Slicing in Lists

nums = [10, 20, 30, 40, 50]
print(nums[1:4:-1])  
#syntax:list[start:stop:step] Here the indexing starts from 1 and ends at 4 but u have to move backwards as its given -1.Thats why []
print(nums[::-2])
#No start, no stop just -2 since negative start from either side of the list and move 2 steps backwards
print(nums[10:20])  
#Out of the box
nums = [10, 20, 30, 40, 50, 60, 70]
print(nums[5:1:-2])

#List Comprehesion
#List comprehension is just a short way of creating a new list using a for loop.
nums = [1,2,3,4,5]
even = [x for x in nums if x % 2 == 0]#[x for x in nums if x % 2 == 0]
print(even)

#List Squares
nums = [1,2,3,4,5]
squares = [x**2 for x in nums]
print(squares)

#Max and Min element in a list
nums = [10,30,70,40,50]
nums.sort()
print(nums[0]) #min
print(nums[-1])#max

nums = [10, 30, 70, 40, 50]

smallest = nums[0]
largest = nums[0]

for x in nums:
    if x < smallest:
        smallest = x

    if x > largest:
        largest = x

print("Min:", smallest)
print("Max:", largest)

#append() → one element at the end
#extend() → multiple elements
#insert() - one element at specific index. Syntax: list.insert(index,element)
#remove elements()- list.remove(element)
#pop()- remove element at specifif inndex.list.pop(idx)
#sort()
#reverse()
#len()
#count() count how many times an element is present
#for loop = for x in nums:

nums=[10,20,30]
nums.append(40)
print(nums)

nums = [10,20,30]
nums.insert(2,25)
print(nums)

nums = [10,20,30]
nums.remove(30)
print(nums)

nums=[10,20,30,40,50]
nums = nums[2:5:1]
print(nums)

nums = [10,20,30,40,50]
even_nums = [x for x in nums if x%2==0] # in these for loops like for x in nums it directly access the x element inside the list not the index its the value
print(even_nums)

#if u want the loop by index just go for i in range (len(nums)) and then access the element by nums[i]

nums = [1,2,2,3,4,5]
freq = {}
for x in nums:
    freq[x]= freq.get(x,0)+1
for x in freq:
    if(freq[x]>1):
        print(x,"is repeated",freq[x],"times")

nums = [1,2,2,3,4,5]
nums = nums.count(2)
print(nums)

nums = [30,10,50,20]
nums.sort()
print(nums[::-1])

nums = [1,2,3,45]
nums.reverse()
print(nums)

nums = [1, 2, 2, 3, 3, 4, 4, 5]
freq = {}

#Remove Duplicates by preserving order
# Step 1: Build frequency map
for x in nums:
    freq[x] = freq.get(x, 0) + 1

# Step 2: Extract unique keys into a list
duplicate_free = []
for x in freq:
    duplicate_free.append(x)

print(duplicate_free)  # Output: [1, 2, 3, 4, 5]

#PYTHONIC WAY - list(dict.fromkeys(nums)) - this will removev duplicates and maintain the order of first occurence of the elements in the list.
nums = [10,20,30,30]
unique_nums = list(dict.fromkeys(nums))
print(unique_nums)

#Frequency of each element
nums = [1,2,2,3,3,4,4,5]
freq = {}
for x in nums:
    freq[x] = freq.get(x,0)+1
print(freq)

#Second Largest element
nums = [10,20,30,40,30,50]
for i in range (len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]>nums[j]):
            nums[i],nums[j]=nums[j],nums[i]
print(nums[-2])
#Exactly. You don't need an else here. 👍
#So Python naturally continues to the next iteration when the if condition is false.
#Python lets you swap two variables directly:
#2 pointer doesnt work here because the list is not sorted.

#Positive and negative numbers
nums = [10,-20,30,-40,50]
positive = [x for x in nums if x>=0]
negative = [x for x in nums if x<0]
print(positive)
print(negative)

#List of squares for even numbers
nums = [1,2,3,4,5,6]
list_of_squares_for_even_numbers = [x**2 for x in nums if x%2==0]
print(list_of_squares_for_even_numbers)

#print elements which are greater than 1
nums=[1,2,2,3,3,3,4,4,4,4,5]
freq = {}
for x in nums:
    freq[x] = freq.get(x,0)+1
for x in freq:
    if(freq[x]>1):
         print(x)

#Flatten a nested list
nums = [[1, 2], [3, 4], [5, 6]]

result = []

for x in nums: #this indicates like for ex [1,2] is x and then for y in x means 1 and 2 like individual elements of the list
    for y in x:
        result.append(y)

print(result)

#Longest list in nested list
nums = [[1,2],[3,4,5,6],[7,8]]
max_len = 0
longest = []
for x in nums:
    len_nums = len(x)
    if len_nums>max_len:
        max_len = len_nums
        longest = x
print(longest)

#Common elements from list1 and list 2
list1 = [1,2,3,4,5]
list2 = [4,5,6,78,8]
common = []

for x in list1:
    if x in list2:
        common.append(x)

print(common)
