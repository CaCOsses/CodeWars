from re import search
Test.describe("Basic tests")
Test.assert_equals(bool(search(regex, 'fjd3IR9')), True)
Test.assert_equals(bool(search(regex, 'ghdfj32')), False)
Test.assert_equals(bool(search(regex, 'DSJKHD23')), False)
Test.assert_equals(bool(search(regex, 'dsF43')), False)
Test.assert_equals(bool(search(regex, '4fdg5Fj3')), True)
Test.assert_equals(bool(search(regex, 'DHSJdhjsU')), False)
Test.assert_equals(bool(search(regex, 'fjd3IR9.;')), False)
Test.assert_equals(bool(search(regex, 'fjd3  IR9')), False)
Test.assert_equals(bool(search(regex, 'djI38D55')), True)
Test.assert_equals(bool(search(regex, 'a2.d412')), False)
Test.assert_equals(bool(search(regex, 'JHD5FJ53')), False)
Test.assert_equals(bool(search(regex, '!fdjn345')), False)
Test.assert_equals(bool(search(regex, 'jfkdfj3j')), False)
Test.assert_equals(bool(search(regex, '123')), False)
Test.assert_equals(bool(search(regex, 'abc')), False)
Test.assert_equals(bool(search(regex, '123abcABC')), True)
Test.assert_equals(bool(search(regex, 'ABC123abc')), True)
Test.assert_equals(bool(search(regex, 'Password123')), True)

Test.describe("Random tests")
from random import random, randint
sol=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="0123456789"
all="".join([lower,upper,digits])
wrong=" !_+-?/\\"

for _ in range(100):
  s="".join(sorted([upper[randint(0,len(upper)-1)], lower[randint(0,len(lower)-1)], digits[randint(0,len(digits)-1)]]+[all[randint(0,len(all)-1)] if randint(0,10) else wrong[randint(0,len(wrong)-1)] for q in range(randint(0,15))], key=lambda a: random()))
  Test.it("Testing for "+repr(s))
  Test.assert_equals(search(regex,s)!=None, search(sol,s)!=None, "It should work for random inputs too")