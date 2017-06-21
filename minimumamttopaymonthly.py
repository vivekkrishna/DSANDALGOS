# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.






#word=input("enter a word")
#school = 'Massachusetts Institute of Technology'
#numVowels = 0
#numCons = 0
#
#for char in school:
#    if char == 'a' or char == 'e' or char == 'i' \
#       or char == 'o' or char == 'u':
#        numVowels += 1
#    elif char == 'o' or char == 'M':
#        print(char)
#    else:
#        numCons -= 1
#
#print('numVowels is: '+str(numVowels))
#print('numCons is: '+str(numCons)) 

num=input()
#==============================================================================
# s = 'ujicfayvcij'
# order='abcdefghijklmnopqrstuvwxyz'
# biggestsubstr=''
# newsubstr=''
# previndex=0
# currentindex=0
# for i in range(len(s)):
#     for j in range(len(order)):
#         if s[i]==order[j]:
#             currentindex=j
#             break
#     if previndex<=currentindex:
#         newsubstr+=s[i]
#     else:
#         if len(biggestsubstr)<len(newsubstr):
#             biggestsubstr=newsubstr
#         newsubstr=s[i]
#     previndex=currentindex
# if len(biggestsubstr)<len(newsubstr):
#     biggestsubstr=newsubstr
# print('Longest substring in alphabetical order is: '+biggestsubstr)
# 
#==============================================================================







#
#"""
#l=0
#h=100
#guess=50
#while 1:
#    res=input("Is your secret number "+str(guess)+"?")
#    if res=='h':
#        h=guess
#        guess=(l+guess)/2;
#    elif res=='l':
#        l=guess
#        guess=(guess+h)/2;
#    elif res=='c':
#        print('Game over. Your secret number was: '+guess)
#        break;
#    else:
#        print('Sorry, I did not understand your input.')
#        

def remainingbal(balance,annualInterestRate,payamt):
    Previousbalance=balance
    for i in range(12):
        Monthlyinterestrate= (annualInterestRate) / 12.0
        #Minimummonthlypayment = (monthlyPaymentRate)*(Previousbalance)
        Monthlyunpaidbalance = (Previousbalance)-(payamt)
        Updatedbalanceeachmonth = (Monthlyunpaidbalance)+(Monthlyinterestrate*Monthlyunpaidbalance)
        Previousbalance=Updatedbalanceeachmonth
    return round(Previousbalance,2)
a=True
payamt=10
balance = 999999
annualInterestRate = 0.18
Monthlyinterestrate = (annualInterestRate) / 12.0
Monthlypaymentlowerbound = balance / 12
Monthlypaymentupperbound = (balance * (1 + Monthlyinterestrate)**12) / 12.0
while(a):
    payamt=(Monthlypaymentlowerbound+Monthlypaymentupperbound)/2
    rebal=remainingbal(balance,annualInterestRate,payamt) 
    print(str(rebal))
    if rebal<-0.001:
        Monthlypaymentupperbound=payamt
    elif rebal>0.001:
        Monthlypaymentlowerbound=payamt
    else:
        break
print('Lowest Payment: '+str(round(payamt,2)))  
#summ=0
#n=1
#while n<=end:
#    summ+=n
#    n+=1
#print(summ)
#
#
#total=end
#for i in range(end):
#    total+=i
#print(total)
#
#"""