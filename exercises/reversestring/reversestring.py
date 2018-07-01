'''
--- Directions
Given a string, return a new string with reversed
order of characters

--- Examples
reversestring('apple') == 'leppa'
reversestring('hello') == 'hello'
reversestring('Greetings!') == '!sgniteerG'
'''

# Solution #1
# def reversestring(string):
#    return string[::-1]

# Solution #2
def reversestring(string):
    reverse = ''
    for character in string:
        reverse = character + reverse
    return reverse
