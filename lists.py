# Write a Python program to get a single string from two given strings, 
# separated by a space, and swap the first two characters of each string
#take input string from user
n = "cynthia"
m = "mumbua"
print(n, m)
new_string1 = m[:2] + n[2:]
new_string2 = n[:2] + m[2:]
swap_string = new_string1 + " " + new_string2
print(swap_string)




# Write a Python function that takes a list of words and returns
#  the longest word and the length of the longest one
def find_longest_word(words_list):
    longest_word = []
    for n in words_list:
        longest_word.append((len(n), n))
    longest_word.sort()
    return longest_word[-1][0], longest_word[-1][1]
result = find_longest_word(["Cynthia","jeff","judie"])
print("Longest word: ",result[1])
print("Length of the longest word: ",result[0])


# Write a Python program that accepts a comma-separated sequence of words as
#  input and prints the distinct words in sorted form (alphanumerically).
def distinct_words(words):
  sorted_words=[]
words=["blue","green","yellow"]

print(distinct_words(words))


#  Write a Python function that takes two lists and returns True if they have at least one common member.
def one_common_member(list1, list2):
     result = True
     for num in list1:
         for num in list2:
             if num == num:
                 result = True
                 return result
print(one_common_member([1,2,3,4,5], [5,6,7,8,9]))
print(one_common_member([1,2,3,4,5], [6,7,8,9]))


# 5. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
def convert_dictionaries(y_list):
    y_list = ["Pink", "Joyce", "Tesla"], ["color", "Name", "Make"]
keys = ["Pink", "Joyce", "Tesla"]
values = ["color", "Name", "Make"]
list_of_dictionaries = [{keys[i]: values[i]} for i in range(len(keys))]
print(list_of_dictionaries)
# Write a Python program to check whether all dictionaries in a list are empty or not

def check_dictionaries(lists):
        dict= [{},{},{}]
        print(all(not d for d in list))
        print(all(not d for d in list))
        check_dictionaries(list)
        print(check_dictionaries)


# Given a list of numbers, use list comprehension to remove all odd numbers from the list:
numbers = [3,5,45,97,32,22,10,19,39,43]

def remove_odd(x):
    for i in x[:]:
        if (i % 2) != 0:
            x.remove(i)
    return x 
numbers = [3,5,45,97,32,22,10,19,39,43]
print(remove_odd(numbers))


# Find the common numbers in two lists (without using a tuple or set)
def find_common(a,b): 
 result = [a for i in a if  i in b]
 return result
lista = 1, 2, 3, 4, 
listb= 2, 3, 4, 5
print(find_common(lista,listb))

# Use a nested list comprehension to find all of the numbers from 1-1000
#  that are divisible by any single digit besides 1 (2-9)
def divisible_by_single_digits(numbers):
    for x in range(1, 100):
     for i in range(2,10):
       if x% i == 0:
          i=numbers.add(x)
print(numbers)
result = [number for number in range(1,1000) if True in [True for x in range(2,10) if number % x == 0]]
print(result)

# Write a Python function to remove all vowels in a string
def removeVowels(string):
    vowel = 'aeiou'
    string="synthia"
    for ch in string.lower():
        if ch in vowel:
            string = string.replace(ch, '')
    print(removeVowels(string))




    







  
