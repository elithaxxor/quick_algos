''' fibonacci sequence- sequence of numbers where a # is the sum of 2 preceeding #'s'''

## iterative (o)n
def fib(n):
    a = 0
    b = 1
    print(a, b)
    print('n', n)
    for i in range(2, n):
        c = a+b
        a=b
        b=c
        print(c)
fib(6)
print('x'*50)


## recursive  o(n)^2
def fib_ii(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        calc_fib = fib_ii(i-1) + fib_ii(i-2)
        if calc_fib == 6:
            print('found val', calc_fib)
        return calc_fib

for i in range(6):
    print(fib_ii(i))


## fib memoization:

fib_cache={1:0, 2:1} ## store the basecase
def fib_iii(i):
    if i in fib_cache:
        return fib_cache[i]
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        calc_fib = fib_iii(i-1) + fib_iii(i-2)
        if calc_fib == 6:
            print('found val', calc_fib)
        return calc_fib

print('x'*50, '\nfib_cached')
for i in range(6):
    print(fib_iii(i))
