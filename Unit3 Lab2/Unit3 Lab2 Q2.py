#  Function: main
#
#  This function opens the weddingGifts text file and asks the user
#  if they want to add a gift. If the user inputs Y, then the user is
#  asked to enter who the gift is from and what type of gift it is.
#  Depending on the type of gift they choose will be asked to enter
#  the cash amount and/or a description of the gift. The users inputs
#  will be appended to the end of weddingGifts text file. This will
#  continue to loop until the user inputs N.
#  
#  line. It counts the number of gifts and the total amount of 
#  cash in the weddingGifts text file and then displays this.
#
#  Parameters:  None
#  Returns   : None
def main():
    print("Gift Registry\n")
    weddingGiftsFile = open(r'C:\temp\weddingGifts.txt', 'a')
    choice = input("Another gift? (Y/N): ").capitalize()
    while choice == 'Y':
        giftFrom = input("Who is this gift from: ")
        giftType = input("Enter gift type (Cash, Gift, Both): ").capitalize()
        if giftType == "Cash":
            cash = float(input("Enter amount of cash gift: "))
            weddingGiftsFile.write("\n" + giftFrom + "\t" + giftType + "\t" + str(cash))
        elif giftType == "Gift":
            cash = 0
            gift = input("Enter description of gift: ")
            weddingGiftsFile.write("\n" + giftFrom + "\t" + giftType + "\t" + str(cash) + "\t" + gift)
        elif giftType == "Both":
            cash = float(input("Enter amount of cash gift: "))
            gift = gift = input("Enter description of gift: ")
            weddingGiftsFile.write("\n" + giftFrom + "\t" + giftType + "\t" + str(cash) + "\t" + gift)
        choice = input("Another gift? (Y/N): ").capitalize()
    print("File successfully written")
    weddingGiftsFile.close()
    

if __name__ == "__main__":
    main()
