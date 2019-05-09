#This is a project to investigate the dependence of number of syllables to
#word length in the English language. A pronounciation dictionary was found,
#containing words and their phonetic pronounciation, and the number of
#syllables in each word counted by vowel sound, along with its length.

#We then plot the dependence of no. of syllables vs no. of letters.

import csv
#Open the dictionary file
file_object = open('CMUdict_test.txt')

#Name of results file
results_file_name = 'CMUdict_test_results.txt'
#Clears the results file
results_file = open(results_file_name, "w")
results_file.truncate()

#Create an empty dictionary to keep syllable word length pairs
Freq_pairs = {}
Freq_pairs.clear()

#Reads through the dictionary
for line in file_object:
    #Strip apostrophes off start and end of line
    line = line.strip()

    #Split word from the phonetic representation
    word, phones = line.split("  ")

    #Some words have alternative pronounciation, specified by EXAMPLE(1),
    #this will remove the bracketed numeral
    if word[-1] == ')':
        word=word[:-3]

    #Vowel sounds are represented by 0,1 or 2, so simply count these to retrieve
    #the number of syllables
    syllable_count = phones.count('0')+phones.count('1')+phones.count('2')

    #Length of the word, ie number of letters
    word_length = len(word)

    #Add one to the value of a syllable, length pair
    if word_length == 1 or word_length > syllable_count:
        try:
            Freq_pairs[(word_length,syllable_count)] += 1
        except:
            Freq_pairs[(word_length,syllable_count)] = 1

    #Write all information to results file
    writer = csv.writer(open(results_file_name, "a"), delimiter = ",")
    writer.writerow([word, phones, word_length, syllable_count])

#Read the results into the code
results = csv.reader(open(results_file_name, "r"), delimiter=',')

#There are some small abreviations in the dictionary, lets filter by a high
#number of syllables
min_syll_size = 4

#We are looking to find maximum ratio of syllables:letters, so start with a ratio
#of zero and only keep current winners
max_ratio = 0
max_ratio_words = []
max_ratio_words[:] = []

counter=0
for row in results:
    if int(row[-1]) >= min_syll_size:
        #Save the old maximum ratio
        old_max_ratio = max_ratio

        #Find the current ratio
        ratio = int(row[-1])/float(row[-2])

        #Check if it is equal to or larger than the current winner
        #Note that some annoying abbreviations have ratio = 1, so filter them
        if ratio == old_max_ratio and ratio < 1:
            max_ratio = max(ratio, old_max_ratio)
            max_ratio_words.append(row[0]) #If same as current winner, add to winners
        elif ratio > old_max_ratio and ratio < 1:
            max_ratio = max(ratio, old_max_ratio)
            max_ratio_words[:] = [] #If larger than current winner, delete list of winners
            max_ratio_words.append(row[0]) #and start a new list

        counter += 1

#Print the results
print('\nThere are '+ str(counter) +' words with more than '+ str(min_syll_size) +' or more syllables.')

print('\nThe maximum syllable to letter ratio was given by the words '+str(max_ratio_words) +', with a ratio of '+ str(max_ratio) + '\n' )

#The following frequency pairs were found by running this code on the full dictionary, CMUdict.txt
#This takes a long time.

Freq_pairs = {(7, 3): 6727, (16, 6): 78, (14, 4): 243, (13, 4): 753, (19, 4): 1, (18, 4): 2, (20, 7): 2, (8, 5): 36, (11, 5): 746, (16, 3): 3, (17, 7): 29, (12, 6): 112, (13, 7): 14, (15, 4): 90, (1, 1): 26, (3, 2): 206, (8, 2): 10202, (9, 3): 8250, (7, 5): 3, (14, 2): 3, (3, 1): 1380, (34, 14): 1, (14, 8): 2, (17, 8): 2, (2, 1): 215, (22, 9): 1, (9, 4): 2610, (5, 1): 5854, (28, 12): 1, (10, 3): 5526, (7, 2): 16473, (12, 2): 74, (17, 6): 41, (14, 5): 417, (13, 3): 285, (19, 7): 2, (18, 5): 8, (7, 1): 1141, (4, 1): 4606, (6, 4): 86, (5, 4): 5, (11, 4): 2593, (10, 4): 3096, (16, 4): 25, (12, 7): 2, (14, 6): 179, (13, 6): 177, (18, 6): 11, (15, 7): 24, (20, 5): 1, (8, 3): 8559, (9, 2): 4660, (6, 1): 3471, (11, 3): 2542, (7, 4): 563, (12, 4): 1599, (14, 3): 58, (6, 2): 16560, (12, 3): 906, (17, 5): 19, (13, 2): 17, (19, 6): 7, (15, 3): 11, (4, 2): 2232, (9, 6): 1, (5, 3): 729, (10, 5): 480, (16, 5): 83, (16, 8): 2, (14, 7): 10, (13, 5): 789, (19, 5): 2, (18, 7): 16, (15, 6): 155, (20, 6): 1, (8, 4): 1749, (9, 1): 21, (11, 2): 425, (10, 6): 3, (12, 5): 930, (15, 8): 3, (20, 8): 5, (18, 8): 2, (15, 5): 208, (8, 1): 198, (6, 3): 3303, (16, 7): 30, (17, 4): 6, (19, 9): 1, (4, 3): 57, (9, 5): 139, (5, 2): 8920, (11, 6): 46, (10, 2): 1635}

print Freq_pairs
#Plotting the scatterplot of frequencies
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['figure.figsize'] = [12,8]
x=[]
y=[]
f=[]
s=[]

for i in range(0,len(Freq_pairs.values())): #
    x.append(Freq_pairs.keys()[i][0])
    y.append(Freq_pairs.keys()[i][1])
    f.append(Freq_pairs.values()[i])

    #The following makes the area of the markers proportional to the frequency.
    s.append(400*(3.1415/4)*(Freq_pairs.values()[i]+100)/float(max(Freq_pairs.values())))

plt.scatter(np.log(x),np.log(y),s=s)

#Calculating a weighted least squares using the log-log plot and matrix methods.
from numpy.linalg import inv

A = np.zeros((len(Freq_pairs), 2))
for i in range(0,len(Freq_pairs)):
    A[i] = [np.log(x[i])*f[i]**0.5, 1*f[i]**0.5]
A=np.asmatrix(A)

b = np.zeros((len(Freq_pairs), 1))
for i in range(0,len(Freq_pairs)):
    b[i] = [np.log(y[i])*f[i]**0.5]
b=np.asmatrix(b)

print '\nWe are now solving the linear system Astar x = bstar, where the unknowns are the gradient and y-intercept of a straight line \n'

Astar=np.transpose(A)*A
print 'Astar = ' + str(Astar)

bstar = np.transpose(A)*b
print 'bstar = ' + str(bstar)

xstar = inv(Astar)*bstar
m = xstar[0].item(0)
c = xstar[1].item(0)
print '\nTo obtain the straight line with gradient m = ' + str(m) +', and intercept c = ' + str(c)

#Plotting the line of best fit
X = np.arange(0.0, 3.6, 0.001)
Y = m*X+c
plt.plot(X, Y,'r')
plt.xlabel('log(Word Length)', fontsize=18)
plt.ylabel('log(Number of Syllables)', fontsize=16)

#Calculating the average number of syllables per word
print '\nThe average number of syallables per word is ' + str(1/(np.exp(1)**(c/m)))

plt.show(block=False)
input("Hit Enter To Close")
plt.close()
