text = ''
for x in range (1,13): 
    for y in range (1,11):
        z= x*y
        e = str(z)
        if len(e)<2 :
            text += "{} x {} = {}   ".format(y,x,z)
        else :
            text += "{} x {} = {}  ".format(y,x,z)
    text = text + '\n'

print(text)