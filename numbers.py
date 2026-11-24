numbers=[
8,6,8,3,9,7,5,9,7,4

def    sum_numbers(numbers):
       total=0
       for i in numbers:
            total += i
        return total
        
     
def     average_numbers(numbers):
        sum_numbers(numbers)/len(numbers)
     return average 
def     find_median(numbers):
        numbers.sort()
        n=len(numbers)
        if n % 2==1:
        median=numbers[n//2]
        else:
            middle1 =numbers[n//2-1]
            middle2 =numbers[n//2]
            median=(middle1+middle2)/2
            return median
    
        def mode_numbers(numbers):

    frequency = {}

    for i in numbers:

        if i in frequency:

            frequency[i] += 1

        else:

            frequency[i] = 1

    mode = numbers[0]

    highest = 0

    for i in frequency:

        if frequency[i] > highest:

            highest = frequency[i]

            mode = i

    return mode