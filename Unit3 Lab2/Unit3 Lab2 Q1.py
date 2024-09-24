#  Function: main
#
#  This function opens the weddingGifts text file and reads each
#  line. It counts the number of gifts and the total amount of 
#  cash in the weddingGifts text file and then displays this.
#
#  Parameters:  None
#  Returns   : None
def main():
    weddingGiftsFile = open(r'C:\temp\weddingGifts.txt', 'r')
    line = weddingGiftsFile.readline()
    cashGiftsList = []
    while line != '':
        items = line.split('\t')
        cashGiftsList.append(items[2])
        line = weddingGiftsFile.readline()
    weddingGiftsFile.close()
    totalCash = 0
    for cash in cashGiftsList:
        totalCash += float(cash)
    print("Recived ", len(cashGiftsList), " gifts including cash of $", format(totalCash, ",.2f"), sep='')

if __name__ == "__main__":
    main()
