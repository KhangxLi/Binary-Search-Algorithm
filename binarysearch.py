
num_tries = 0
def binarysearch(numlist, target):
    global num_tries
    if len(numlist) == 0:
        print("The target was not in the list.")
    else:
        midpoint_index = len(numlist) // 2
        if numlist[midpoint_index] == target:
            num_tries += 1
            print("The target", target, "was found in", num_tries, "guesses.")
        elif numlist[midpoint_index] < target:
            num_tries += 1
            print("Guess: ", numlist[midpoint_index], "is too low")
            return binarysearch(numlist[midpoint_index + 1:], target)
        elif numlist[midpoint_index] > target:
            num_tries += 1
            print("Guess: ", numlist[midpoint_index], "is too high")
            return binarysearch(numlist[:midpoint_index], target)

def listmaker(min, max):
    '''Simple ordered numbers list maker'''
    alist = []
    for x in range(min, max):
        alist.append(x)
    return alist

# Example with list of numbers from 1 to 999 with target = 744
binarysearch(listmaker(1, 1000), 744)