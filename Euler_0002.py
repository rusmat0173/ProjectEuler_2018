"""
Project Euler: https://projecteuler.net/problem=2

Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.

Found out from internet research and some trial and error:
> Cannot use a classic generator.
> Cannot use Binet's formula due to decmal point accuracy.
> Don't be afraid to "bulk out" sequence by brute force method.  Series goes up very quickly.
> Don't use recursive approach, you will max laptop out at >30 recursions.
> "yield" command is like return for a generator.
> Try using the elegant while True: ...
> Use numpy array?

My approach:
> Every 3rd number in sequence is even, that means you can rearrange the formula, as this person has below,
and just sum every result. (Rather than every 3rd result.)
>> https://medium.com/@TheZaki/project-euler-2-even-fibonacci-numbers-2219e9438970

Result:
> It is 2 orders of magnitude faster, hurray!

"""
import time

# first, sum of all elements to the limit
def fibsum(limit):
    a = 0
    b = 1
    sum = 0
    while (a+b) <= limit:
        c = a + b
        a = b
        b = c
        print(c)
        sum += c

    return "sum", sum

# print(fibsum(10))


# next, same with a while True
def while_fibsum(limit):
    a = 0
    b = 1
    sum = 0
    while True:
        if limit == 0: return a
        elif limit == 1: return b
        else:
            if (a + b) <= limit:
                c = a + b
                a = b
                b = c
                print(c)
                sum += c
            else: break

    return "sum", sum

# print(while_fibsum(10))


# next, better while True condition
def while_fibsum2(limit):
    a = 0
    b = 1
    sum = 0
    while True:
        if limit == 0:
            return a
        elif limit == 1:
            return b
        elif (b + a) >= limit:
            return "sum", sum
        else:
            c = a + b
            a = b
            b = c
            print(c)
            sum += c

# print(while_fibsum2(10))


# next, brute force even sum
def bruteEvenfibsum(limit):
    a = 0
    b = 1
    sum = 0
    while True:
        if limit == 0:
            return 0
        elif limit == 1:
            return 0
        elif (a + b) <= limit:
            c = a + b
            a = b
            b = c
            if c % 2 == 0:
                print(c)
                sum += c
        else:
            break

    return "sum", sum

start = time.time()
print(bruteEvenfibsum(400000))
end = time.time()
print(end - start)

# next, efficient even sum
def Evenfibsum(limit):
    a = 2
    b = 8
    if limit < 2: return 0
    if 2 <= limit < 8: return 10
    sum = 10
    while True:
        c = 4 * b + a
        if c > limit: return sum
        else:
            sum += c
            a = b
            b = c

start = time.time()
print(Evenfibsum(400000))
end = time.time()
print(end - start)