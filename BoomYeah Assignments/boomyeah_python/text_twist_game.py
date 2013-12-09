#Create a program wherein the user
#is asked to play a game (Text Twist style).
#Description:
#Player will try to find words from a set of 5-7 jumbled letters.
#When the player finds the longest word, then he can go to the next round.
#Player can swap(shuffle) the letters or surrender from the game.

import random

def main():
    word1= {
            'word': 'ABIDE',
            'match_words':{
            'AID', 'BAD', 'DIE'
            },
            'answer': 3,
    }

    word2 ={
            'word': 'MUSTARD',
            'match_words':{
            'MUST','ART','STAR','DART','DUST','STUD','SUM'
            },
            'answer':4,
    }

    word3={
            'word':'RADIANT',
            'match_words':{
            'ANT','ART','DART','DIRT','AIR','RAIN','TAR'
            },
            'answer':4,
    }

    game_words = [word1, word2, word3]

    for g in game_words:
        user_word = raw_input("Enter your word:")
        len_user_word = len(user_word)

        choice = "y"









main()