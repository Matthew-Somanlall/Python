num = ""
addition = 1

while addition != 0:

    addition = int(input('Please entre a number:'))
    
    num += f"{addition}"

    if addition != 0:
        num += ","
    
print (num)