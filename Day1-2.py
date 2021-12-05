if __name__ == "__main__":
    # Open the input file
    with open(r"Day1-input.txt", "r", encoding="utf-8") as infile:
        readings = list(map(int, infile.readlines()))

    increased = 0
    prevReading = -1
    for i in range(2,len(readings)):
        newReading = readings[i] + readings[i-1] + readings[i-2]
        if prevReading == -1:
            print("%d (N/A - no previous measurement)" % newReading)
        elif prevReading < newReading:
            print("%d (increased)" % newReading)
            increased += 1
        else:
            print("%d (decreased)" % newReading)
        prevReading = newReading
    print("Increased readings = %d" % increased)
