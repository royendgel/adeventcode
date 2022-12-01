if __name__ == '__main__':
    with open('input.txt') as f:
        elfs = []
        c = 0
        for line in f.readlines():
            if line.strip():
                c += int(line)
            else:
                elfs.append(c)
                c = 0
        puzzle1 = max(elfs)
        print(puzzle1)
        sorted_elfs = sorted(elfs)
        puzzle2 = sum(sorted_elfs[-3:])
        print(puzzle2)