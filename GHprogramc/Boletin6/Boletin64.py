'''
Created on 6 oct 2022

@author: anaat
'''
#4. Design a program that reads a positive number N greater than 0 and show the result
#of the sum of the N numbers between 1 and N. If the number N is not valid, the
#program should ask for it again. The messages are the following:

#-“Enter one number greater than 0:”
#-“The number is not right, try again.”
#-The sum of the N first numbers is XX.

num = int(input ("Enter one number greater than 0: "))

suma=0
while num <=0:
    print ("The number is not right, try again: ")
    num = int(input ("Enter one number greater than 0: "))
    

for i in range (1,num+1):
    suma+=i
print (f"The sum of the {num} first numbers is {suma}")
    