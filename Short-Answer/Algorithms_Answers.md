#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  Linear O(n)
rewriting the while loop to look a little cleaner , we have:
```python
    while(a < n**3):
        a += n**2
```
n^3 contains exactly n number of n^2's --> 
```python
3**3 = 27 
3**2 = 9 
9 + 9 + 9 = 27 # -> n is 3 -> n * n**2 = n**3  or n**3/n**2 = n
```
n^3 / n ^2 == n therefore there will be n operations performend no matter how big n is; therefore , we have a linear time complexity O(n)

b) O(n log n)
```python
sum = 0  #O(1)
    for i in range(n): #O(n)
      j = 1 # O(1)
      while j < n: # O(log n) because j increases by power of 2, therefore approaches n twice as quickly
        j *= 2
        sum += 1 # O(1)
```
Looking at it from an example perspective:
n = 2
number of iterations should be 1, because 2^1 <= 2 or log 2 = 1
n= 3
number of iterations should be between 1 and 2, because 2^1 < 3 < 2^2
n= 5
number of iterations should be between 2 and 3, because 2^2 < 5 < 2^3 
n=100
number of iterations should be between 6 and 7, because 2^6 < 100 <7

Combining all of that together(we multiply everything inside the foorloop)
O(1 + n(1 + (logn *1))) -> drop constants -> O(n log n)

c) Linear O(n)
```python
def bunnyEars(bunnies): 
      if bunnies == 0: # O(1)
        return 0 

      return 2 + bunnyEars(bunnies-1) # O(n)
```
we're dealing with a simple recursion call, which in most cases will have a linear time complexity O(n).
For each n we put in, our output is 2 times it since each bunny has 2 ears, so we can say that the run time would be O(2n) --> drop constants --> O(n)

## Exercise II

This problem is very similar to guessing a number that the computer picked that was described during one of our lectures. 
Similarly, we could use binary search:

```python
# think of the number of floors as a sorted array of ascending numbers
# our `first failure floor` f is somewhere in that array

# firt of all, check if the egg breaks on the very first floor, because if it does, we're done: just return that first floor

# define a start point 
# define an end point
# find the middle of given array  => (start + end)/ 2

# if we want to use recursion, we could think of the stopping point (base case):
    # probably when our start point becomes smaller or equal to our end point, meaning we cant halve/split the array anymore

# check if the egg breaks on the middle floor, if so:
    # we could potentially check one floor below the middle, if the egg doesnt break there: we're done! the middle is our f(the first floor to start breaking eggs), otherwise: 
    # we must look lower
    # our start point stays the same
    # our endpoint is now middle - 1(since middle was already checked)
    # we can use recursion to start over the process with the left half of our array and overwrite old middle with a new one

# otherwise, the egg doesnt break
    # for sanity check we check just a floor above it and see if the egg breaks, if so: we're done! the middle is our f(the first floor to start breaking eggs), otherwise: 
    # we must look higher
    # our start point becomes middle +1 (since we already checked the middle)
    # our endpoint stays the same
    # we can use recursion to start over the process with the right half of our array and overwrite old middle with a new one

# the process would continue until we'd find the first floor to break eggs

# in case none of the floors are breaking eggs, we could just return None at the end 

# the runtime of this process would be logarythmic O(log n) since we're halving the array/number of things we're considering each time 


```
