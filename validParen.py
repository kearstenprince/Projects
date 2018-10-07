


def validateParens(paren):
  if num == num2:
    for p in paren:
      op = 0
      cl = 0
      if p == "(":
        op = op + 1
      elif p == ")":
        cl = cl + 1
      if cl < op:
        return True
      elif cl > op:
        return False
  else:
    return False

paren = input ("Type in a parenthesis sequence: ")

while "(" not in paren and ")" not in paren:
  paren = input ("Type in a parenthesis sequence: ")
num = paren.count("(")
num2 = paren.count(")")

print (validateParens(paren))