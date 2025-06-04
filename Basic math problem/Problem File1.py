# 1 Swap of two number using thired variable and with third variable 
a = 3 ,
b = 5 ,
# method 1 
temp = a
a = b
b = temp 
# method 2 
a,b = b,a

#------------------------------------------------------------------------------------------------
# check the leap year 
year  = int(input("Enter a year -->" ))

if (year % 4 == 0 and  year % 100 != 0) or (year % 400 == 0 ):
	print("Leap year")
else:
	print("Not leap year ")
	
	
#------------------------------------------------------------------------------------------------ 
# check the prime number 

num = int(input("Enter a numbert"))

flag = False

if num == 1:
	print("Not prime number")
elif num > 1:
	# check the factors 
	for i in range (2,num):
		if num % i == 0 :
			flag = True 
			break
			
if flag:
	print("Not prime")
else:
	print("Prime Number")
	
#------------------------------------------------------------------------------------------------ 
# check the print all prime number  1 to 10

lower = 1
higher = 10

for num in range(lower, higher+1):
	if num > 1:
		for i in range(2,num):
			if num % i == 0:
				break
		else:
			print(num)
				
#------------------------------------------------------------------------------------------------ 
# Print the Factorial of number 

num  = int(input ("Enter num "))
factorial = 1

if num < 0:
	print("Factorial not exist in -negative number ")
elif num == 0:
	print("Factorial of 0 is 1")
else:
	for i in range(1,num+1):
		factorial = factorial* i
	print("Factorial")
	
#------------------------------------------------------------------------------------------------ 
# Print the Factorial of number using recursive

def recur_fact(n):
	if n == 1 and n == 0 :
		return n
	else:
		return n * recur_fact(n-1)
	
num  = int(input ("Enter num "))

if num < 0:
	print("Factorial not exist in -negative number ")
elif num == 0:
	print("Factorial of 0 is 1")
else:
	print("The factorial num is" , recur_fact(num))


#------------------------------------------------------------------------------------------------ 
# Print the Fibonacci sequences by iterative method

nterm = int(input("How many terms -->"))

# first two terms
n1,n2 = 0,1 
count = 0

# check the number is valid or not 
if nterm <= 0:
	print('Enter a positive number')
elif nterm == 1:
	print("Series is " , n1)
else:
	print("Fibonancy series ")
	while count < nterm:
		print(n1)
		nth = n1 + n2
		# updating the values
		n1 = n2
		n2 = nth
		count +=1

#***************1.Fibonnci series  ****************
def Fibonnci():
	a,b = 0,1
	while True:
		yield a
		a,b = b,a+b
	
f1 = Fibonnci()
# if use the this loop it will run infinite 
for i in f1:
	print(i)
	
# insted of running this we can print
print(next(f1))
print(next(f2))
print(next(f1))
print(next(f2))	
print(next(f1))
print(next(f2))
		
#------------------------------------------------------------------------------------------------ 
# Print the Fibonacci sequences by Recursive method

def recur_fibb(n):
	if n <= 1:
		return n
	else:
		return(recur_fibb(n-1)-recur_fibb(n-2))
		
nterm = int(input("How many terms -->"))
		
#check the number is a valid state or not 
if nterm <= 0:
	print("Enter a positive number")
else:
	print("Fibbonancy sequency")
	for i in range(nterm):
		print(recur_fibb(i))
		
#------------------------------------------------------------------------------------------------ 
# Print the Armstrong number 

num  = int(input ("Enter num "))
#calculate the number of digit of num

num_digit = len(str(num))

#initialize the variable
sum_of_power = 0
temp_num = num

# calculate the sum of digits raised tyo trhe power of num_digit

while temp_num > 0:
	digit = temp_num % 10
	sum_of_power += digit ** num_digit
	temp_num // 10
	
#check trhe armstrong number 
if sum_of_power == num:
	print("This is a armstrong number")
else:
	print("This is a not armstrong number")

#------------------------------------------------------------------------------------------------ 
# Program to Print the Sum of give number 

limit  = int(input("Enter a limit"))

sum = 0
for i in range(1,limit+1):
	sum +=i

print("Sum of number is " )

#------------------------------------------------------------------------------------------------ 
# Program to find the LCM 

def compute_lcm(x,y):
	if x > y:
		greater = x
	else:
		greater = y
	while(True):
		if ((greater % x == 0) and (greater % y == 0)):
			lcm = greater
			break
		greater +=1
	return greater 
	
num1 = input ("Enter a num 1")
num2 = input ("Enter a num 2")
print("The LCM is " , compute_lcm(num1,num2))

#------------------------------------------------------------------------------------------------ 
# Program to find the HCF 

def compute_hcf(x,y):
	if x > y:
		smaller = y
	else:
		smaller = x 
	hcf = 1 
	for i in range(1,smaller+1):
		if ((x%i == 0) and (y%i==0)):
			hcf = i
	return hcf
	
num1 = input ("Enter a num 1")
num2 = input ("Enter a num 2")
print("The LCF is " , compute_hcf(num1,num2))

#------------------------------------------------------------------------------------------------ 
# Program to find the cube of sum of first n natural numbers

def cube_sum_of_natural(n):
	if n<=0:
		return 0
	else:
		total = sum([i**3 for i in range(1, n+1)])
		return total
		
n = int(input("Enter the value of n: "))

if n <= 0:
	print("Please enter a positive number ")
else:
	result = cube_sum_of_natural(n)
	print("the sum of cube is ", result)
	

#------------------------------------------------------------------------------------------------ 
# Program to find sum of array 

def sum_of_array(arr):
	total = 0
	for element in arr:
		total += element
		
	return total

array = [1,2,3]
result = sum_of_array(array)
print(result)

#------------------------------------------------------------------------------------------------ 
# Program to find largest element of array 

def find_largest_element(arr):
	if not arr:
		return "Array is Empty"
		
	largest_element = arr[0]
	
	for element in arr:
		if element > largest_element:
			largest_element = element
			
	return largest_element

my_array = [10,20,30]
result = find_largest_element(my_array)
print(result)

#------------------------------------------------------------------------------------------------ 
# Program to rotate array by d times 

def rotate_array(arr,d):
	n = len(arr)
	
	if d < 0 or d >= n :
		return "Invalid rotation Value"
		
	# create a new array to save the rotated element
	rotrated_arr = [0] *n
	
	# perform rotation
	for i in range(n):
		rorated_arr[i] = arr[(i+d) % n]
		
	return rotate_array
	
array = [1,2,3,4,5]

result = rotate_array(arr,d)
print(arr)
print("Rotated arr ", result)

#------------------------------------------------------------------------------------------------ 
# Program to check the given array is monotonic or not 
# Array is increasing or decreasing means monotonic

def is_monotonic(arr):
	increasing = decreasing = True 
	
	for i in range (1,len(arr)):
		if arr[i] > arr[i - 1]:
			decreasing = False
		elif arr[i] < arr[i-1]:
			increasing = False
	return increasing and decreasing
	
arr1 = [1,2,2,3]
arr2 = [3,2,1]
print(is_monotonic(arr1))

#------------------------------------------------------------------------------------------------ 
# Program to find smallest and largest number in a list 

numbers = [30,10,-45,5,23]

minimum = number[0]
largest = laregest[0]

for i in numbers:
	if i < minimum:
		minimum = i

print("Then smallest number is " , minimum)

for i in numbers:
	if i > largest:
		largest = i
		
print("Then Largest number is " , largest)	

#------------------------------------------------------------------------------------------------ 
# Program to find words which are greater than given length

def find_words(words , k):
	result = []
	for i in words:
		if len(i) > k:
			result.append(i)
			
	return result 
	
words_list = ['apple' , 'banana' , ' cherry' , 'date' , 'dragon']
k = 5
lonf_word = find_words(words_list ,k)

print(lonf_word)

#------------------------------------------------------------------------------------------------ 
# Program to find all duplicate charactor in a string

def find_duplicate(input_str):
	char_count = {}
	
	#initialize the list to store the duplicate charactor
	duplicate = []
	
	for i in input_str:
		if i in char_count:
			char_count[i] +=1
		else:
			char_count[i] = 1
			
	# Iterate through the dictionary and add charactor with count > 1
	
	for i, count in char_count.items():
		if count > 1:
			duplicate.append(i)
			
	return duplicate
	
input_string = "ABCcfd ehwuoii"
	
duplicatye_chars = find_duplicate(input_str)

print("Duplicate charactor :" , duplicatye_chars)

#------------------------------------------------------------------------------------------------ 
# Program to merging the two dictionary

dict1 = {'a' : 1 , 'b': 2}
dict2 = {'c' : 3 , 'd': 4}

# method 1
dict1.update(dict2)
print("merging dictionary" , dict1)

# method 2
merged_dict = {**dict1 , **dict2}
print("merging dictionary" , merged_dict)

#------------------------------------------------------------------------------------------------ 
# Program to calculate number of words and digits 

sentence = input("Enter a sentence: ")

letter_count = 0
digit_count = 0

for char in sentence:
	if char.isalpha():
		letter_count += 1
	elif char.isdigit():
		digit_count += 1
		
print("LETTERS", letter_count)
print("Digits" , digit_count)

#------------------------------------------------------------------------------------------------ 
# Program to search the binary search 

def binary_search(arr,target):
	left, right = 0,len(arr)-1
	
	while left <= right:
		mid = (left+right)//2
		
		if arr[mid] == target:
			return mid
		elif arr[mid]<target:
			left = mid + 1
		else:
			right = mid - 1
	return -1 
	
sorted_list = [1,3,4,5,6,7,8,9]
target_element = 4

result = binary_search(sorted_list,target_element)

#------------------------------------------------------------------------------------------------ 
# Program to reverse the string and reverse teh opposite case 

def reverse(input_str):
	reversed_str = input_str[::-1].swapcase()
	
	return reversed_str
	
reverse("Hello Word")

#***************2 . sort the list using the woithout using the sort function *******

list1 = [2,4,224,53,25,64,58,223]
n = len(list1)

for i in range(n):
	for j in range(i+1,n):
		if list1[i]>list1[j]:
			list1[i],list1[j] = list1[j],list1[i]
			
print(list1)

#***************3. weather the string the palindrome is not *************************

s = nitin
if s == s[::-1]:
	print("palindrome")
else:
	print('not palindrome')
	
# alternate solution 
s = nitin
n = len(s)
x = 0
for i in range(n):
	if s[i] != s[n-i-1]:
		x = 1
		break
if x == 0:
	print("yes")
else:
	print('No')
	
# *****************4. print the all pairs with given sum ***********

list1 = [8,7,2,5,3,1]
n = len(list1)
k = 10
for i in range(n):
	for j in range(i+1,n):
		if (list1[i]+list1[j]) == k:
			print(list1[i],list1[j])
			


# reverse teh words to given string ****************
s = " the sky is blue"
l = s.split()
l = l[::-1]
l = ' '.joine(l)
print(l)
# output is ---> "blue is sky the"

# removr the punctution from the list (expect space)

str1 = "/*apples are & found% only @red & green"
s = ''
for i in str1:
	if ((i>='A' and i<='Z') | (i>='a' and i<='z') | (i==' ')):
		s = s+i	
print(s)

# find the maximum repeated charactor in a string 

s = "ifnjsdgggggwidnjwuyhfnjhihweh"
ch = {}
for i in s:
	if i in ch:
		ch[i] += 1
	else:
		ch[i] =1
	
max_char = max(ch,key = ch.get)
print(max_char)


#**** Find the maximum and minimum value in a list without using predefinded question

l = [43,25,75,34,687,87,54,221,1]
maximum = l[0]
minimum = l[0]

for i in l:
	if i > maximum:
		maximum = i
	if i < minimum:
		minimum = i
print(maximum,minimum)

#**************** check the number is palindrome or not ************
n = int(input("Entyer a number"))
temp = n
rev = 0
while n > 0:
	dig = n%10
	rev = rev * 10 + dig
	n = n//2
if temp == rev:
	print("palindrome")
else:
	print('not palindrome')


# check the number is armstrong or not 

num = int(input("enter a num"))

sum = 0
temp = num  # finding the cube opf every digit 

while temp > 0:
	digit = temp % 10
	sum += digit ** 3
	temp //= 10

if num == sum :
	print("armstrong num")
else:
	print('not armstrong num')
	
# *****************calculate the factorial of numbner ***************

num = 6
factorial = 1

# Calculate the factorial using a for loop
for i in range(1, num + 1):
    factorial *= i

# Output: The factorial of the number
print(f"The factorial of {num} is {factorial}")

# ******************** Counting Vowels in a Given Word  *************
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)

#****************  Counting the Number of Occurances of a Character in a String
word = "python"
character = "p"
count = 0
for letter in word:
    if letter == character:
        count += 1
print(count)

# reverse a number 
n =  int(input("Enter a number: "))

revNum = 0 
while n > 0:
	ld = n%10
	revNum = (revNum * 10) + 1
	n = n//10
print(revNum)


# palindrome of number 

def palindrome(n):
	revNum = 0 
	dup = n
	while n > 0:
		ld =  n % 10 
		revNum = (revNum * 10) + ld
		n = n//10 
	if dup == revNum:
		return True
	else:
		return False
		
def main():
    number = 4554

    if palindrome(number):
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")


if __name__ == "__main__":
    main()
	
	
# armstrong number 

def isArmsytrong(num):
	k = len(str(num))
	sum = 0
	n = num 
	while n > 0:
		ld = n%10
		sum += ld ** k
		n = n//10
	return sum == num 
	
def main():
    number = 153
    if isArmstrong(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")

if __name__ == "__main__":
    main()
