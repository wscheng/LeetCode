import sys

print(sys.maxsize)
print(sys.maxsize + 1)

max_int = int(sys.maxint)
print(sys.maxint, type(max_int))

print(-(sys.maxint+1))
min_in_overflow = int(-(sys.maxint+2))
print(min_in_overflow, type(min_in_overflow))
