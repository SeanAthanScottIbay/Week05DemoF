# for demo

num = int(input("Enter a number: "))

#for i in range(num):       # default; starts with 0
#for i in range(1, num+1):  # start with 1
for i in range(0, num, 2):  # skips every 2
    print(i)

print("Thank you for using this program.")