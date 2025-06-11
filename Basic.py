# Find if a number is odd or even

def odd_or_even():
    a = int(input("Add number:"))
    if a%2 == 0:
       print("even")
    else:
        print("odd")



# Find the largest out of 3 numbers
def Largest_number():
    a = int(input("Add number:"))
    b = int(input("Add number:"))
    c = int(input("Add number:"))
    if a > b:
        print(a)
    elif b > c:
        print(b)
    elif c > a:
        print(c)



# Check if a string is a palindrome
def palindrome():
    a = "jack"
    if a == a[::-1]:
        print("Its palindrome")
    else:
        print("Its not a palindrome")
        
        
        
# Check if a list is a palindrome
def num_palindrome():
    a = [2,4,6,8]
    if a == a[::-1]:
        print("Num is palindrome")
    else:
        print("Its not")

if __name__ == "__main__":
    num_palindrome()



# Count vowels in a string
def count_vowel(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
s = "Hello World"



# Count only even digits in a string
def count_digits(d):
    count = 0
    for dig in d:
        if dig.isdigit() and int(dig)%2 == 0:
            count += 1
    return count
d = "ihaveMango456"


# Reverse a list without .reverse()
def reverse_list():
    a = [2, 4, 6, 8, 10]
    print("Reversed list:", a[::-1])

    
# Print all prime numbers between 1 and 100.
def prime():
    for num in range(2,101):
        is_prime = True
        for i in range(2, int(num ** 0)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end='')
            
            
# Revere a String
def reverse_string():
    a = "jack_sparrow"
    print("Reversed String:", a[::-1])
    
   

# Sum of digits of a number.
def sum_of_digits():
    num = input("Enter a number: ")
    sum = 0
    for i in num:
        sum += int(i)
    print("Sum of digits:", sum)


# sum of number
def sum_of_list(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum

numbers_list = [1,2,3,4,5,6]
print(sum_of_list(numbers_list))


#multiplication of number
def mul_of_num(num):
    mul = 1
    for i in num:
        mul *= i
    return mul

num_list = [4,5]
print(mul_of_num(num_list))




# find a fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# # Input & Output
num = int(input("Enter the position (starting from 0): "))
fib_num = fibonacci(num)
print(f"The Fibonacci number at position {num} is: {fib_num}")



# find a factorial
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

# # Test
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")




# Find the second largest number in a list.
def second(n):
    first  = second = float("-inf")
    for num in n:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float("inf") else "No second  largest number"

ns = [10, 20, 4, 45, 99, 99]
print("Second largest:", second(ns))



# Sort a list without using built-in sort function.
def sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
    
    arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

print(sort([4, 2, 7, 1, 3]))



# Remove duplicates from a list.
def dup(n):
    list = []
    for i in n:
        if i not in n:
            n.append(i)
    return n

print(dup([1,4,5,4,6,1]))



# Merge two lists and sort them.

def merge_and_sort(list1, list2):

    merged = list1 + list2

    n = len(merged)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if merged[j] < merged[min_index]:
                min_index = j

        merged[i], merged[min_index] = merged[min_index], merged[i]
        return merged


list1 = [4, 1, 3]
list2 = [2, 5, 6]
print(merge_and_sort(list1, list2))


# Check if two strings are anagrams.
def anagrams(str1, str2):
  
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

print(anagrams("listen", "silent"))  
print(anagrams("hello", "world")) 

