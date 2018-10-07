
hangman = input ("Type in a word in the subject: food: ")

letters = []
for i in hangman:
  letters.append("-")

y = 7
def hang_man():
  global y
  x = input ("Guess a letter: ")

  count = 0

  while count < len(hangman):
    if x == hangman[count]:
      letters [count] = x
    count = count + 1
  if x not in hangman:
    y = y - 1
    print ("Wrong! You have" + " " + str(y) + " " +"chances left")
    

  print ("".join(letters))


while True:
  hang_man()
  if "-" not in letters:
    print ("You've won!")
    break
  elif y == 0:
    print ("You lost! Loser!")
    break







#if word is in [word]:
#if word is hangman[0]:
  #print  = input ("The word is:" + word + "-"* len(hangman) -1 + " Guess a letter: ")