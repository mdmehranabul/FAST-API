"""
For & While loops
"""

my_list=[1,2,3,4,5]

# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
#
# for iterator in my_list:
#     print(iterator)
#
# for x in range(3,6):
#     print(x)


# sum_for_loop = 0
#
# for x in my_list:
#     sum_for_loop += x
# print(sum_for_loop)
#
# my_list = ["Monday", "Tuesday", "Wednesday", "Thursday"]
#
# for x in my_list:
#     print(f"Happy {x}!")


i = 0
#
# while i <5:
#     i+=1
#     print(i)

# while i <5:
#     i+=1
#     if i==3:
#         continue
#     print(i)

# while i <5:
#     i+=1
#     if i==3:
#         continue
#     print(i)
# else:
#     print("i is now larger or equal to 5")


while i <5:
    i+=1
    if i==3:
        continue
    print(i)
    if i==4:
        break
else:
    print("i is now larger or equal to 5")


# Assignment
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

x = 0
while x<3:
    x+=1
    for i in my_list:
        if i =="Monday":
            print("------")
            continue
        print(i)
