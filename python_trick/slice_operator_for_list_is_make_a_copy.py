def move_element_in_list(li):
    li[0], li[1] = li[1], li[0]


a_list = [1, 2, 3, 4]
print(a_list)
move_element_in_list(a_list)
print(a_list)


class TmpClass:
    def move_element_in_list(self, li):
        li[0], li[1] = li[1], li[0]


tmp = TmpClass()
b_list = [1, 2, 3, 4]
print(b_list)
tmp.move_element_in_list(b_list)
print(b_list)

tmp.move_element_in_list(b_list[0:3])
print(b_list)

tmp.move_element_in_list(b_list[0:4])
print(b_list)

tmp.move_element_in_list(b_list)
print(b_list)

tmp.move_element_in_list(b_list[:])
print(b_list)