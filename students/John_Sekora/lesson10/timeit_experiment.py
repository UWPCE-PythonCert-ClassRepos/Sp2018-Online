
from timeit import timeit as timer

my_repititions = 10000
my_range = 10000
my_lower_limit = my_range / 2
my_list = list(range(my_range))


def multiply_by_two(x):
    return x * 2


def greater_than_lower_limit(x):
    return x > my_lower_limit


def map_filter_with_functions_func(mult, greater, my_list):
    map_filter_with_functions = map(mult, filter(greater, my_list))
    return list(map_filter_with_functions)


def map_filter_with_lambdas_func(my_lower, my_list):
    map_filter_with_lambdas = map(lambda x: x * 2, filter(lambda x: x > my_lower, my_list))
    return list(map_filter_with_lambdas)


def comprehension_func(my_lower,_my_list):
    comprehension = [x * 2 for x in my_list if x > my_lower]
    return list(comprehension)


def comprehension_with_lambdas_func(my_lower, _my_list):
    comprehension_with_lambdas = [(lambda x: x * 2)(x) for x in my_list if (lambda x: x)(x) > my_lower]
    return list(comprehension_with_lambdas)


if __name__ == '__main__':

    print("\n\nmap_filter_with_functions")
    print(timer(
        'map_filter_with_functions = map(multiply_by_two, filter(greater_than_lower_limit, my_list))',
        globals=globals(),
        number=my_repititions))

    print("\n\nmap_filter_with_lambdas")
    print(timer(
        'map_filter_with_lambdas = map(lambda x: x * 2, filter(lambda x: x > my_lower_limit, my_list))',
        globals=globals(),
        number=my_repititions))

    print("\n\ncomprehension")
    print(timer(
        'comprehension = [x * 2 for x in my_list if x > my_lower_limit]',
        globals=globals(),
        number=my_repititions))

    print("\n\ncomprehension_with_lambdas")
    print(timer(
        'comprehension_with_lambdas = [(lambda x: x * 2)(x) for x in my_list if (lambda x: x)(x) > my_lower_limit]',
        globals=globals(),
        number=my_repititions))

