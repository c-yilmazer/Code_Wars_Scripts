#If we list all the natural numbers BELOW 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Finish the solution so that it returns the sum of all the multiples of 3 or 5 BELOW the number passed in.

#Additionally, if the number is negative, return 0.

#Note: If a number is a multiple of both 3 and 5, only count it once.

def multiples(div): #dividend
    sum_5 = 0
    sum_3=0
    i_5=1 #iterator for 5
    i_3=1 #iterator for 3
    if div < 0:
        return 0
    else:
        while div > i_5*5: #1*5. 2*5, 3*5... 
            sum_5 += i_5*5
            i_5 += 1
    
        while div > i_3*3:
            if i_3 % 5 == 0: #to prevent overlaps 
                sum_3 += 0
            else:
                sum_3 += i_3*3
            i_3 +=1

        return(sum_3+sum_5)

print(multiples(6))
