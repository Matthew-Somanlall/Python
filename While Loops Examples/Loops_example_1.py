name = input("Please entre your name here:")

while name == "":
    name = input("Please entre your name here:")

a = 0
b = 0
count = 0

while b != -1:

    b = int(input("Please enter in you marks and if you want to stop enter -1:"))
    if b > 100 or b < 0:
        print("you cannot entre a mark higher then 100 lower lower then 0")
    else:
        a = a + b
        count += 1

d = a / count

print(f"your average is:{d}")