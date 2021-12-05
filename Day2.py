if __name__ == "__main__":
    # Open the input file
    with open(r"Day2-input.txt", "r", encoding="utf-8") as infile:
        instructions = infile.readlines()
    distance = 0
    depth = 0
    for instruction in instructions:
        dir,amt = instruction.strip().split()
        if (dir == "up"):
            depth -= int(amt)
        elif (dir == "down"):
            depth += int(amt)
        elif (dir == "forward"):
            distance += int(amt)
        elif (dir == "back"):
            distance -= int(amt)

    print("Total distance travelled: %d, Final depth: %d" % (distance,depth))
    print("Final product: %d" % int(distance*depth))
