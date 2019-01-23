# Ref: https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result

squares = []
for x in range(5):
    squares.append(lambda: x ** 2)

print(squares[2]())
print(squares[4]())
