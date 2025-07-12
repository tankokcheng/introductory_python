def countCharacters(sentence):    
    return len(sentence)
   
def countVowels(sentence):
    count = 0
    for i in sentence:
      if i.upper() in ["A", "E", "I", "O", "U"]:
        count = count + 1
    return count

