# Author :        Alex McCaslin
# Email :         aamccaslin@gmail.com
# Date Modified : 9/27/2017 

import re
from nltk.corpus import words

#CONSTANTS
NAMEREGEX = "[A-Z][a-z]+ [A-Z][a-z]+"
PHONEREGEX = "[\d\\(\\)\\- ]{10,}"
EMAILREGEX = ".*@.*\\.com"
ASCII0 = 48
ASCII9 = 57

class ContactInfo:
    
    #Constructor
    def __init__(self, document):
        
        self.doc = document
        self.name = ""
        self.email = ""
        self.phoneNum = ""

        self.updateName()
        self.updatePhone()
        self.updateEmail()


    #Getters
    def getName(self):
        return self.name

    def getPhoneNumber(self):
        return self.phoneNum

    def getEmail(self):
        return self.email



    # Performs regex on document for two word names with capital letters at start
    # Checks if words are names or words
    # If they are names then continue, if they are words throw them out
    # Updates name
    def updateName(self):
        
        theName = re.findall(r'' + NAMEREGEX, self.doc)
        chances = [0 for x in range(len(theName))]

        #go through all possibilities for names separating each "name" into a list
        for i in range(len(theName)):

            bigram = theName[i].split()

            #check if the word is in the nltk library list of words
            for word in bigram:
                if word in words.words():
                    chances[i] += 1



        #get the result with the highest chance of being a name
        top = 0
        for j in range(len(chances)):
            if chances[j] > top:
                self.name = theName[j]
                top = chances[j]
            



    # Performs regex on document for phone number
    # Takes out characters that aren't numbers
    # Updates phone number
    def updatePhone(self):

        tempPhone = ""
        thePhoneNum = re.search(r'' + PHONEREGEX, self.doc).group()

        #cleans up phone number
        #checks if character is " ", "-", "(", ")", "0-9" in ascii values
        for ch in thePhoneNum:
            if ord(ch) >= ASCII0 and ord(ch) <= ASCII9 :
                tempPhone += ch

        self.phoneNum = tempPhone
        


    # Performs regex on document for email
    # Updates Email
    def updateEmail(self):
        theEmail = re.search(r'' + EMAILREGEX, self.doc).group()
        self.email = theEmail
