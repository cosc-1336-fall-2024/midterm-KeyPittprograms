#get_sum_of_evens

def get_sum_of_evens(num):
    sum = 0
    for i in range(1, num+1):
        if (i%2 ==0 ):
            sum += i

    return sum
