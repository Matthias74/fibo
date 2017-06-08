
from subprocess import call
# Fibonacci numbers module


def fib(n):    # write Fibonacci series up to n

        print "Bonjour", n
        pwd = call(["pwd"])
        print pwd


fib(3)
