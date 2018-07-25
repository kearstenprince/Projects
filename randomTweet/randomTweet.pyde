import json
import random
tweetWords = {}

from random import *


json_file = open('2017.json')
json_str = json_file.read()
json_data = json.loads(json_str)


def getText(tweet):
  return tweet["text"]

# REPLACE THIS CODE
for tweet in json_data:
 sentence = getText(tweet)
 #print sentence
 sentence = sentence.split(" ")
 #print sentence

 for word_Index in range (len(sentence) - 1 ):
   word = sentence[word_Index]
   nextWord = sentence[word_Index + 1]
   #print sentence[word_Index]
   # test if it's in dictionary
   # value "was"
   # If not in dictionary add another list
   if not word in tweetWords:
     tweetWords[word] = []
   tweetWords[word].append(nextWord)

randomNum = randint (0, (len(tweetWords.keys())))
newTweet = tweetWords.keys()[randomNum]
print newTweet
willContinue = True
wordFound = newTweet
while len(newTweet) < 140 and willContinue:
 if wordFound in tweetWords.keys():
   possibleWords = tweetWords[wordFound]
   randomNum = randint (0, (len(possibleWords) - 1))
   wordFound = possibleWords[randomNum]
   newTweet = newTweet + " " + wordFound
 else:
   willContinue = False


print newTweet
