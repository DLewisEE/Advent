if __name__ == "__main__":
    # Open the input file
    with open(r"Day1-input.txt", "r", encoding="utf-8") as infile:
        readings = list(map(int, infile.readlines()))
    prevReading = -1
    increased = 0
    for reading in readings:
        if prevReading == -1:
            print("%d (N/A - no previous measurement)" % reading)
        elif prevReading < reading:
            print("%d (increased)" % reading)
            increased += 1
        else:
            print("%d (decreased)" % reading)
        prevReading = reading
    print("Increased readings = %d" % increased)
