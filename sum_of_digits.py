#Digital root is the recursive sum of all the digits in a number.

#Given n, take the sum of the digits of n. 
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
# The input will be a non-negative integer.

#Examples
#    16  -->  1 + 6 = 7
#   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
#132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
#493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

#x = 16
#y = str(x)
#z = list(y)

#print(z) outputs ['1', '6']

def digital_root(n):
    str_n = str(n)
    list_n = list(str_n) #now it is an array with individual numbers as string
    
    sum_n = 0
    
    for num in list_n:
        sum_n += int(num)
    
    if len(list(str(sum_n))) > 1: #if it becomes 1, it is a single digit and for loop can stop
        return digital_root(sum_n)
    return sum_n      
    
#might be the only one that has done this with recursive in codewars...   

print(digital_root(942))
     




