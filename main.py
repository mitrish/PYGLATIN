pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print original
  #word = original.lower()
  first = original[0] 
  new_word = original + first + pyg
  #new_word = new_word[1:len(new_word)]
  print new_word[1:len(new_word)]
else:
  print 'empty'
