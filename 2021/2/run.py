def read(inputfile):
    with open(inputfile, 'r') as f:
        return f.read().splitlines()


def part1(inputList):
    X = 0
    Z = 0 # Depth
    for inp in inputList:
        command = str(inp.split()[0])
        x = int(inp.split()[1])
        #print(f"{command} {x}")
        if command == "forward":
            X += x
        elif command == "down":
            Z += x
        elif command == "up":
            Z -= x
    return X*Z 
        
def part2(inputList):
    aim = 0
    hoz = 0
    dep = 0

    for inp in inputList:
        command = str(inp.split()[0])
        x = int(inp.split()[1])
        #print(f"{command} {x}")
        if command == "down":
            aim += x
        elif command == "up":
            aim -= x
        elif command == "forward":
            hoz += x
            dep += aim*x
    return hoz*dep


def main():
    print(f"Part1 Sanity Check:  {part1(read('sample.txt'))}")
    print(f"Part1 Answer:        {part1(read('input.txt'))}\n")
    print(f"Part2 Sanity Check:  {part2(read('sample.txt'))}")
    print(f"Part2 Answer:        {part2(read('input.txt'))}\n")


if __name__ == "__main__":
    main()