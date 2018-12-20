int_list = [0, 1, 2, 3, 4, 5, 6]
print("int_list=", int_list)
print(int_list[0], "type=", type(int_list))

# Note:
# in python 3, map(str, int_list) return map object, we should transform it into list by ourselves
# in python 2, map(str, int_list) return list, nothing need to do
str_transformed_from_int_list = list(map(str, int_list))
print("str_transformed_from_int_list=", int_list)
print(str_transformed_from_int_list[0], "type=", type(str_transformed_from_int_list[0]))

# output
# int_list= [0, 1, 2, 3, 4, 5, 6]
# 0 type= <class 'list'>
# str_transformed_from_int_list= [0, 1, 2, 3, 4, 5, 6]
# 0 type= <class 'str'>
