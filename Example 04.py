# 35 -> 31.671


import time

# fib(35) = fib(34) + fib(33)
# fib(34) = fib(33) + fib(32)
# fib(33) = fib(32) + fib(31)
# fib(32) = fib(31) + fib(30)

memo = {
    0: 0,
    1: 1,
}

def fibonachi(number):
    if number in memo:
        return memo[number]
    else:
        fib_number = fibonachi(number-1) + fibonachi(number-2)
        memo[number] = fib_number
        return fib_number
    # if number == 0:
    #     return 0
    # elif number == 1:
    #     return 1
    # else:
    #     return fibonachi(number-1) + fibonachi(number-2)

start = time.time()
print(fibonachi(35))
end = time.time()
print('execution time:', end-start)