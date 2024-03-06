stacks = int(input("How many stacks should there be? "))
if stacks >= 1 and stacks <= 8:
     for stacks in range (1, stacks + 1, 1):
        for j in range (1):
            print(' ' * (8 - stacks) +'#' * stacks, end='')
        print()
else:
    print("There can only be 1-8 stacks.")
