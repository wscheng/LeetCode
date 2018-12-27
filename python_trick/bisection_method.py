import bisect

x = [1, 4, 4, 7, 10, 13, 16]

print(bisect.bisect(x, 3))
print(bisect.bisect_left(x, 3))
print(x)
print(bisect.bisect(x, -1))
print(bisect.bisect_left(x, -1))
# bisect.bisect is the same as bisect_right. You can check the source code.
# [1,4,4,7,10,13,16]
#        ^
print("(matched)=", bisect.bisect(x, 4))
# bisect.bisect_left
# [1,4,4,7,10,13,16]
#    ^
print("left(matched will insert left)=", bisect.bisect_left(x, 4))
# bisect.bisect_right
# [1,4,4,7,10,13,16]
#        ^
print("right(if matched will insert right)=", bisect.bisect_right(x, 4))
print("left(if matched will insert most left matched)=", bisect.bisect_left(x, 4, 3, 5))
print("left(if matched will insert left)=", bisect.bisect_left(x, 4, 1, 5))
