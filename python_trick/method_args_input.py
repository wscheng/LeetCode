# http://book.pythontips.com/en/latest/args_and_kwargs.html
def method_input(input1, input2, *the_rest):
    print(input1)
    print(input2)
    print("the_rest type is", type(the_rest))
    print(the_rest)
    method2_input(*the_rest)


def method2_input(input1, input2, input3):
    print(input1, input2, input3)


def multi_element_input(input1, input2, *the_rests):
    print(input1)
    print(input2)
    for the_rest in the_rests:
        print(the_rest)
        method2_input(*the_rest)


method_input("A", "B", "C", "D", "E")

print('++++++++')
multi_element_input("INPUT1", "INPUT2", ("AA", "AA_INPUT2", "ANS_AA"), ("BB", "BB_INPUT2", "ANS_BB"))
print('++++++++')
print("not tuple inside:", (("input1"), "input2"))
print("is tuple inside:", (("input1",), "input2"))
