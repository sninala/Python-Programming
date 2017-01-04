S = 'SPAM'
print S.find('pa') # returns -a
print S.find('PA') # returns index of matched character_size
print S.rstrip()
print S.replace('PA', 'XX')
print S ## immutable 
print S.split(',')
print S.isdigit()
print S.lower()
print S.endswith('AM')
print S.endswith('am')
print S.encode('latin-1')

## iterate through string
for char in S:
    print char
    
print [c*2 for c in S] ## list comprehension

### indexing and slicing 
###X[I:J:K] --> extract all the items in X, from offset I through J-1, by K.
S = 'abcdefghijklmnop'
print S[1:10:2]
S = 'hello'
print S[::-1] ## String reversal
print S[5:1:-1] 

print  ord('s') ## convert a single character to its underlying ASCII integer
print  chr(115) ##  an ASCII integer code and converting it to the corresponding character