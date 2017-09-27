# Author :        Alex McCaslin
# Email :         aamccaslin@gmail.com
# Date Modified : 9/27/2017

import sys
import re
from ContactInfo import ContactInfo

def main():
  
    inputfile = getArgs()
    
    #Take business card out of text file and strip off trailing whitespace
    document = open(inputfile).read().strip()


    getContactInfo = ContactInfo(document)
    
    #get the info from the business card
    print("Name:", getContactInfo.getName())
    print("Phone:", getContactInfo.getPhoneNumber())
    print("Email:", getContactInfo.getEmail())





# Gets arguments from user and takes out input file name
def getArgs():

    CORRECTNUMBEROFARGS = 2
    FILENAME = 1

    args = sys.argv

    if len(args) != CORRECTNUMBEROFARGS:
        print("Incorrect number of arguments")
        print("Usage: python parser.py INPUTFILE")
        exit()

    return args[FILENAME]



main()
