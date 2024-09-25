# age_list = [25,36,12,15,16,19, "hoda", 3.14, [2,5, 6 , [5,6 , [ 8, 5]]]]

# # Get the index of the element you want to exclude
# exclude_index = int(input("Enter the index of the element to exclude (starting from 0): ")) % len(age_list)

# for i, age in enumerate(age_list):
#     if i != exclude_index:
#         print(age)

# print(type({1,2,3}))

# ehsan = {"ehsan", "ehsan", "ehsan" , 1 , 1 ,1}

# print(ehsan)

# list_order = [6,3,5]
# list_order.sort()

# #breakpoint()

# tuple_topole = (6,3,5)

# print(type(tuple_topole))


# another_t = 1, 2, 3, "cherry"
# print(type(another_t))

# single_element_tuple = (42,)
# print(type(single_element_tuple))


# my_tuple = ("apple", "banana", "cherry")
# print(my_tuple[2])  # Output: banana



# my_dictionary = {
#     'apple': 'A red fruit', 
#     'bear': 'A scary animal',
#      1 : "test",
#      256 : 2236
# }
# a = 'asghar' not in " asghar dar khanh ast"
# print(a)

# jamee_yek_ba_yek = input("salam,1+1 = ??? ")

# try:
#     jamee_yek_ba_yek = int(jamee_yek_ba_yek)

#     if jamee_yek_ba_yek == 2:
#         print('ok doroste')
#     else:
#         print('na eshtebahe')
# except:
#     print("lotfan ba adad javab bede")




# if jamee_yek_ba_yek == 2:
#     print('ok doroste')
# else:
#     print('na eshtebahe')


# a = True
# b = False
# c = True
# if a:
#     print('It is true!')
#     print('Also print this')
#     if b:
#         print('Both are true')
#         if c:
#             print('All three are true')
# else:
#     print('It is false!')
# print('Always print this')
no = 2568486 # global
a = range(1,1001)
def aa():
    for no in a:
        print(no)   # local 
aa()
print(no)
