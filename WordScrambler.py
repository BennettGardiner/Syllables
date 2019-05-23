#Takes a paragraph and rearranges each word randomly, but keeping the first and last letters the same.

# import pdb
# pdb.set_trace()
print ('This script will scramble the inside of all the words in a sentence.\n\n'
'Please enter the text you would like scrambled below.\n')

text2 = raw_input()

words = text2.split()

scrambled_words = []

for word in words:

    letters = list(word)

    if len(letters)>3:
        start_letter = letters.pop(0)
        # if start_letter.isupper() == True:
        #     capLetter = True
        # else:
        #     capLetter = False

        if letters[-1]=='.':
            fullStop = True
            end_letter = letters.pop(len(letters)-2)
            letters.pop()
        elif letters[-1]==',':
            comma = True
            end_letter = letters.pop(len(letters)-2)
            letters.pop()
        else:
            end_letter = letters.pop()
            fullStop=False
            comma=False

            import random

        random.shuffle(letters,random.random)

        letters.insert(0,start_letter)
        letters.append(end_letter)

        if fullStop==True:
            letters.append('.')

        if comma==True:
            letters.append(',')

        word = ''.join(letters)

    # if capLetter==True:
    #     scrambled_words.append('{sep}')
    #     scrambled_words.append(word)
    # else:
    scrambled_words.append(word)

scrambled_text = ' '.join(scrambled_words)
#format(sep=2*'\n')
print(scrambled_text)
