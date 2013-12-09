#Create a word game where we take the first letter of a word
# (if the word starts with a consonant letter)
# and put it on the end while also adding a vowel sound 'ay'.
# So bazinga becomes "azingabay":
#If the word starts with a vowel, ahoy becomes "ahoyay"

#Note: when user types some random characters and numbers,
#have the program display "error":

from collections import deque

def main():
    word = raw_input("Enter your word: ")
    word_list = list(word)
    vowels =['a','e','i','o''u']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n',
                 'p','q','r','s','t','u','v','x','z']

    if word_list[0] in consonants:
       word_list = deque(word_list)
       word_list.rotate(-1)
       word_list.append('a')
       word_list.append('y')
       new_word = ''.join(word_list)
       print "Since Your word starts with consonant letter",new_word

    elif word_list[0] in vowels:
       word_list.append('a')
       word_list.append('y')
       new_word = ''.join(word_list)
       print new_word

    elif word.isalnum():
       print "Error!"

main()