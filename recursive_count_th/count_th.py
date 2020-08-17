
def count_th(word):
    '''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
    # if word only has one letter
    if len(word) <= 1:
        return 0
    # else if the word contains "th", count instance of th and recurse through word.
    if word[:2] == 'th':
        return count_th(word[1:]) + 1
    # return the count
    return count_th(word[1:])

#print(count_th("dakdthdkadth"))
