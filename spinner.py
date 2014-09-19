import random

# Convert an array of probabilities that sum to 1.0 to one that spin() can use.
def convert_array(arr):
    if len(arr) <= 1:
        return [1]
    else:
        result = [arr[0]]
        for i in xrange(1, len(arr)):
            result.append(result[i-1]+arr[i])
        result[len(arr)-1] = 1.0
        return result

# p_prime - the final entry is 1.0 and is sorted in ascending order
# Return the index the spinner lands on.
def spin(p_prime):
    if len(p_prime) <= 1:
        return 0
    
    r = random.random()
    
    if p_prime[0] > r:
        return 0
    
    high = len(p_prime) - 1
    low = 1
    while low <= high:
        i = (high-low)/2 + low
        
        assert i <= high
        
        if p_prime[i] > r:
            if p_prime[i-1] <= r:
                return i
            else:
                high = i
        else:
            low = i + 1
    assert False

if __name__ == "__main__":
    categories = ["red", "green", "yellow", "blue"]
    p = [0.15, 0.25, 0.05, 0.55] # probabilities
    p_prime = convert_array(p) # conversion for spin()
    counts = [0 for i in xrange(len(p_prime))] # initialize counts
    num_iterations = 100 # number of trials
    print p_prime
    for i in xrange(num_iterations): # run the experiment
        index = spin(p_prime)
        counts[index] += 1
    print counts
    print [counts[i]/float(num_iterations) for i in xrange(len(counts))] # print estimated probabilities
    
    # Try with 10000 sized vector of weights.
    # May run slow as it spams the console.
    arr = [] # same as p above, only with more entries
    len_arr = 10000 # number of probabilities to create
    sum_arr = 0
    for i in xrange(len_arr):
        arr.append(random.randint(0, 10000))
        sum_arr += arr[-1]
    for i in xrange(len_arr):
        arr[i] = arr[i]/float(sum_arr)
    arr_prime = convert_array(arr)
    arr_counts = [0 for i in xrange(len_arr)]
    arr_total = 0
    num_iterations2 = 100000
    for i in xrange(num_iterations2):
        index = spin(arr_prime)
        arr_counts[index] += 1
        arr_total += 1
    print arr
    print [arr_counts[i]/float(arr_total) for i in xrange(len(arr_counts))]
