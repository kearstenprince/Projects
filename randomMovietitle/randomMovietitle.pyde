from random import *

preambles = ["The sad story of", "The rambunctious life of", "A short film on", "The miraculous mystifying movie about"]

character = ["Shleby:", "Andre:", "Milena:", "Rahmi:"]

tagline = ["Coding to save mankind", "Youngest millionaire alive", "Forty year old virgin", "Haunting of Matilda"]

print preambles[randint(0,3)] + " " + character[randint(0,3)]+ " " + tagline[randint(0,3)]

generate = 0
while generate < 10:
 print preambles[randint(0,3)] + " " + character[randint(0,3)]+ " " + tagline[randint(0,3)]
 generate = generate + 1
