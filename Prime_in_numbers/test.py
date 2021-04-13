import re
from random import randint
from functools import reduce
import solution
try:
    prime_factors = solution.prime_factors
except:
    prime_factors = solution.primeFactors

test.assert_equals(prime_factors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
test.assert_equals(prime_factors(7919), "(7919)")
test.assert_equals(prime_factors(17*17*93*677), "(3)(17**2)(31)(677)")
test.assert_equals(prime_factors(933555431), "(7537)(123863)")
test.assert_equals(prime_factors(342217392), "(2**4)(3)(11)(43)(15073)")
test.assert_equals(prime_factors(35791357), "(7)(5113051)", )
test.assert_equals(prime_factors(782611830), "(2)(3**2)(5)(7**2)(11)(13)(17)(73)")
test.assert_equals(prime_factors(775878912), "(2**8)(3**4)(17)(31)(71)")



def check(string, expected):
    G = re.findall(r'\((\d+)\*?\*?(\d*)', string)
    primes, power = [], []
    for i, j in G:
        if j == '1':
            test.fail('n(i) should be empty when n(i) = 1')
            return
        primes.append(int(i))
        power.append(int(j) if j else 1)
    if sorted(primes) != primes:
        test.fail('p(i) should be in increasing order')
        return
    actual = reduce(lambda x, y: x*y, [i ** j for i, j in zip(primes, power)])
    if actual != expected:
        test.fail(f'{string} != {expected}')
        return
    return True


@test.describe("Small Tests")
def small_tests():
    for i in range(100):
        number = randint(2, 1000)
        test.assert_equals(check(prime_factors(number), number), True)


@test.describe("Big Tests")
def big_tests():
    for i in range(30):
        number = randint(100, 1000000)
        test.assert_equals(check(prime_factors(number), number), True)



@test.describe("Extremely Big Tests")
def bigg_tests():
    for i in range(10):
        number = randint(1000000, 10000000)
        test.assert_equals(check(prime_factors(number), number), True)