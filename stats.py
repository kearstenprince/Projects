num = 1
numlist = []
while num != 0:
 num = int(input ("Type in a number: "))
 numlist.append(num)
numlist.sort()

if len(numlist) >= 2:
  print ("The 2nd smallest number is: " + str(numlist[1]))
  print ("The 2nd largest number is: " + str(numlist[-2]))
else: 
  print ("Error: There are not enough numbers in the list.")

k = 0
for i in numlist:
  k = k + i
m = k / len(numlist)
print ("The average of the numers is: " + str(m) )

dict = {}
for track in numlist:
  if track not in dict:
    dict[track] = 1
  else:
    dict[track] = dict[track]+1
values = 0
for key in dict:
  if dict[key] > values:
    values = dict[key]
    maxValue = key
print ("The most frequent number is: " + str(maxValue))


