if __name__ == "__main__":
    # Open the input file
    with open(r"Day2-input.txt", "r", encoding="utf-8") as infile:
        instructions = infile.readlines()
    distance = 0
    depth = 0
    aim = 0
    for instruction in instructions:
        dir,amt = instruction.strip().split()
        if (dir == "up"):
            aim -= int(amt)
        elif (dir == "down"):
            aim += int(amt)
        elif (dir == "forward"):
            distance += int(amt)
            depth += int(amt)*aim
        elif (dir == "back"):
            distance -= int(amt)*aim
            depth += int(amt)*aim

    print("Total distance travelled: %d, Final depth: %d, Final aim: %d" % (distance,depth,aim))
    print("Final product: %d" % int(distance*depth))
