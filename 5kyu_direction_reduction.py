#Once upon a time, on a way through the old wild mountainous west,…
#… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

#Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

#How I crossed a mountainous desert the smart way.
#The directions given to the man are, for example, the following (depending on the language):

#["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
#or
#{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
#or
#[North, South, South, East, West, North, West]
#You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

#["WEST"]
#or
#{ "WEST" }
#or
#[West]



def dir_reduc(arr):
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "WEST": "EAST", "EAST": "WEST"}
    new_arr= []
    for direction in arr:
        if new_arr and new_arr[-1] == opposites[direction]:
            new_arr.pop()
        else:
            new_arr.append(direction)
    return new_arr

print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))