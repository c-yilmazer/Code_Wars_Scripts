#You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
# Write a method that takes the array as an argument and returns this "outlier" N.

#Examples
#[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

#[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

def find_outlier(integers):
    a = []
    b = []
    for i in integers:
        if i % 2 == 0: #even numbers
            a.append(i) #list with even numbers
        else:
            b.append(i) #list with odd numbers
    if len(a) > len(b): #if there are more even numbers, then N has to be an odd number
        return int(b[0])
    else:
        return int(a[0]) #if there are more odd numbers, then N has to be an even number and since there is only 
    #one number inside one list, that number is the N number. 

print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))