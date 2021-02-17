'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # keep track of a count variable
    count = 0

    # base case:
    # there is 1 or less letters left in our word
    if len(word) <= 1:
        return count

    # check if the first letter is 't'
    if word[0] == 't':
        # check if the second letter is 'h'
        if word[1]=='h':
            # we've encountered our first 'th', bump the counter
            count +=1
            # chop off the first 2 letters and repeat process with recursion
            return count + count_th(word[2:])
        # if our second letter is 't', get rid of just the first letter and recurse
        elif word[1] =='t':
            return count_th(word[1:])
        # otherwise, just get rid of both letters and recurse
        else:
            return count_th(word[2:])
    # otherwise, first letter is not 't' --> get rid of it and recurse
    else:
        return count_th(word[1:])