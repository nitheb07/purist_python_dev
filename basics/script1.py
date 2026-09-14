import sys

a = 100 # int
b = 3.142 # float
c = "Hello" # string
d =["hellow", "world"] # list

comple_list = {
    "key1": "value1",
    "key2": 1,
    "key3": [1, 2, 3],
    "key4": False
} # dictionary containing various types of values

print(comple_list)

print("sum of a and b are as follows: %f" % (float(a)+b))

print(" the a = %d\n b= %f, dict = %s" % (a+1, b, comple_list))

limit_boundary = 50
if a > limit_boundary or a < -limit_boundary:
    print("a is greater than %d or less than -%d" % (limit_boundary, limit_boundary))
elif a == 0:
    print("a is 0")
elif a < 0:
    print("a is less than 0 but not less than -%d" % limit_boundary)
else:
    print("a is between 0 and %d" % limit_boundary)

sys.exit(0)






