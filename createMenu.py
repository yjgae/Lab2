#Accepts a list of options
#returns a string of #ed menu options.
def createMenu(optionList):
  tmp = ' '
  ct = 0
  for opt in optionList:
    tmp += str(ct) + '.' + opt + '\n'
    ct += 1
  return tmp
