## Performance of Python Data Structures
### Lists

#### Python List Methods and their execution time 

| *Method*     | *Execution Time*  |
| ----------- | ----------- |
| index()     | O(1)       |
| index assignment   | O(1)        |
| append()   | O(1)        |
| pop()  | O(1)        |
| pop(i)  | O(n)        |
| insert(i,item)  | O(1)        |
| del operator  | O(n)        |
| iteration  | O(n)        |
| contains(in)  | O(n)        |
| get slice[x:y]  | O(k)        |
| del slice  | O(n)        |
| set slice  | O(n+k)        |
| reverse  | O(n)        |
| concatenate  | O(k)        |
| sort | O(n log n )        |
| multiply | O(nk)        |

pop() is faster than pop(i)(_popping from the beginning_) because in python, after the element has been removed, the other elements in the list are shifted forward. 

```
popzero = Timer("x.pop(0)",
                "from __main__ import x")
popend = Timer("x.pop()",
               "from __main__ import x")
print("pop(0)   pop()")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f, %15.5f" %(pz,pt))
```

#### Python Dictionaries and their Big-O Efficiency

| *Method*     | *Execution Time*  |
| ----------- | ----------- |
| copy()     | O(n)       |
| __getitem__()  | O(1)        |
| __setitem__()   | O(1)        |
| deleteitem  | O(1)        |
| contains(in) | O(1)        |
| iteration  | O(n)        |

On average it appears that dictionaries are faster than lists