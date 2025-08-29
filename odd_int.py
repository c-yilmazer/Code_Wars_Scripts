def find_it(seq):
    for i in seq: # i = seq[x]
        if seq.count(i) %2 != 0: #this pretty much holds seq[0], counts how many seq[0] are inside 
            #seq array and then checks the remainder from divind into 2
            return i #this means seq[x], the seq array item that occurred odd number of times


print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))



# counter % 2 == 1 --> to get odd number of times