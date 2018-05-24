"""The methods below are used for calculating different types of factorial using recursion"""

"""The method below calculates simple factorial"""
def factorial_number(num):
    fact_num = abs(num)
    if fact_num == 0 or fact_num == 1:
        return 1
    else:
        return fact_num * factorial_number(fact_num - 1)


""" The product of all the odd integers up to some odd positive integer n is called the double factorial. 
     The method below computes double factorial"""
def double_factorial(num):
    double_fact_num = abs(num)
    if double_fact_num == 0 or double_fact_num == 1:
        return 1
    else:
        if num % 2 != 0:
            return double_fact_num * double_factorial(double_fact_num -1)
        else:
            return double_factorial(double_fact_num -1)


"""Super factorial is the product of factorials of all the numbers starting from 1 until the super factorial number.
   The method below computes super factorial"""
def super_factorial(num):
    super_fact = abs(num)
    if super_fact == 0 or super_fact == 1:
        return 1
    else:
        return factorial_number(super_fact) * super_factorial(super_fact - 1)





if __name__ == '__main__':
    assert(factorial_number(3)) == 6
    assert(factorial_number(-1)) == 1
    assert(factorial_number(5))  == 120
    assert(double_factorial(9))  == 945
    assert(double_factorial(11)) == 10395
    assert(super_factorial(4)) == 288
    assert(super_factorial(5)) == 34560



