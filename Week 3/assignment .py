# Assignment Solution:

'''
English_int - the number of students who have subscribed to the English newspaper.

English_str - space separated roll numbers of those students.

French_int - the number of students who have subscribed to the French newspaper.

French_str - space separated roll numbers of those students.

Eng_subscribers - English newspaper subscribers.

Fre_subscribers - French newspaper subscribers.
'''

English_int = int(input())
English_str = input()
French_int = int(input())
French_str = input()

Eng_subscribers = set(English_str.split())
Fre_subscribers = set(French_str.split())

# & is the same as intersection()
Total_subscribers = len(Eng_subscribers & Fre_subscribers) 
print(Total_subscribers)


