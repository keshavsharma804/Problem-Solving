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

