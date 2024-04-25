num = ""
addition = 1

while addition != 0:

    addition = int(input('Please entre a number:'))   

    if addition != 0:
        num += f"{addition}"
        num += ","
    
print (num)