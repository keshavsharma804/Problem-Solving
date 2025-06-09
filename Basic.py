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

def count_d(d):
    count = 0
    for dig in d:
        if dig.isdigit() and int(dig)%2 == 0:
            count+=1
    return count

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
    
if __name__ == "__main__":
    reverse_string()
        


