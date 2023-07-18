#!/usr/bin/env python3
#string reversal function
def reverse_string(string:str):
    word = string[::-1]
    return word

# my approach was crazzy!

# def reverse_string(word: str):
#     for i in range(0, len(word)):
#         print(word[len(word)-(i+1)], end='')
# reverse_string(word)