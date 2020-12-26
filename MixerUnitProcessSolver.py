#Solve a single Unit mixing process
import matplotlib as pyplot  #Graph results over time?
import numpy as np   #Solve balances
import torch        #solve balances another way?
#x = torch.rand(3, 5)
#y = np.array([[10,3],[10,4],[10,5],[10,6], [10,7], [10, 8], [10, 9], [10, 10]])

#Gather inputs
totalBalances = int(input("How many differnent material balances are input into the mixer?"))
totalInputs = int(input("How many different input streams are there?"))
totalOutputs = input("How many output streams are there?")
totalRelationships = ("How many relationships are there?")

balanceNames = []
balanceInputNames = []
n = 0
balanceArray = totalBalances


for n in range (n, totalInputs):
    X_input = int(input("How many balances are in the " + f'{n+1}' + " input stream?"))
    for y in range (y, X_input):
        balanceInputNames.append(input("what is the name of the " + f'{y+1}' + " value in the input stream?" ))
    y=0

print(balanceInputNames)

#create dictionary.
#Your heart is free, have the courage to follow it.
my_variables = {}
i = 0
for j in range(5):
    i += 1
    my_variables["w" + str(i)] = i
print(my_variables)

areRatios = ("Are there ratio's in any of the input streams: Yes or No")
ratioStream = []

if (areRatios == "Yes" or "yes"):
    totalRatios = int(input("How many input stream ratios are there total"))
    for n in range (0, totalRatios):
        whichStream = input("Which stream has a ration: enter one at a time.")

    #which balance
    #what ratio with what other balance
    #mass or molar ratio.
    #Known inputs and outputs


    #Determine the Degrees of Freedom Analysis.
#is the problem solvable?
#how many equations, how many balances, how many extra parameters?
#include a basis calculator
#set up array.
#Solve unknows..
#print resuts...
