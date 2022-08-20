binary=input("Enter the binary numbers:-")
binary2=binary.split(",")
for i in binary2:
    if int(i)%5==0:
        print(i)

'''list=[x for x in input("Enter binary numbers..").split(",")]
#print(list)
'''
