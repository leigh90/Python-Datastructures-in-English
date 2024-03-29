import timeit

# For loop
def test1():
    l = []
    for i in range(1000):
        l = l + [i]
        



# Append
def test2():
    l = []
    for i in range(10000):
        l.append(i)

# List comprehension
def test3():
    l = [i for i in range(10000)]

# Range function with list constructor
def test4():
    l = list(range(10000))



t1 = timeit.Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")
# >>>concat  0.6146520290003537 millisecond


t2 = timeit.Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
# >>>append  0.30748103499990975 milliseconds

t3 = timeit.Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
# >>>append  0.30748103499990975 milliseconds

t4 = timeit.Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")
# >>>append  0.30748103499990975 milliseconds

# l = []
# for i in range(10):
#     l = l + [i]
#     print(l)

# l = []
# for i in range(10):
#     l.append(i)
#     print(l)

# l = [i for i in range(10)]
# print(l)
# l = list(range(10))
# print(l)