print ('Type in a sentence: ')
sentence = str(input())

sentence = sentence.title().replace(" ", "")
sentence2 = sentence[0].lower() + sentence[1:]

print (sentence2)
