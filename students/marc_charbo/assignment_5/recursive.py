import sys

def my_fun(n):
    if n == 2:
        return True

    return my_fun(n/2)

if __name__ == '__main__':
    n = float(sys.argv[1])
    print(my_fun(n))

"""
questions:
What is wrong with our logic?
    it only works if n is a power of 2. If it is not it will run until
    the stack overflows i.e RuntimeError: maximum recursion depth exceeded
Why doesn't the function stop calling itself?
    because for nummbers that are not power of two's, they will never
    be equal to 2. They will skip two and converge towards 0 until stack overflow
What's happening to the value of 'n' as the function gets deeper and deeper into recursion?
    Gets closer to 0 wihtout ever reaching it, so gets smaller
A copy-and-paste of your terminal debugging activity.
 => python -m pdb recursive.py 7
> /Users/charbo/Documents/WU/Py2/Sp2018-Online/students/marc_charbo/assignment_5/recursive.py(1)<module>()
-> import sys
(Pdb) l
  1  -> import sys
  2     
  3     def my_fun(n):
  4         if n == 2:
  5             return True
  6     
  7         return my_fun(n/2)
  8     
  9     if __name__ == '__main__':
 10         n = float(sys.argv[1])
 11         print(my_fun(n))
(Pdb) b 4
Breakpoint 1 at /Users/charbo/Documents/WU/Py2/Sp2018-Online/students/marc_charbo/assignment_5/recursive.py:4
(Pdb) c
> /Users/charbo/Documents/WU/Py2/Sp2018-Online/students/marc_charbo/assignment_5/recursive.py(4)my_fun()
-> if n == 2:
(Pdb) 
> /Users/charbo/Documents/WU/Py2/Sp2018-Online/students/marc_charbo/assignment_5/recursive.py(4)my_fun()
-> if n == 2:
(Pdb) pp n
3.5
(Pdb) c
> /Users/charbo/Documents/WU/Py2/Sp2018-Online/students/marc_charbo/assignment_5/recursive.py(4)my_fun()
-> if n == 2:
(Pdb) pp n
1.75
(Pdb) c
> /Users/charbo/Documents/WU/Py2/Sp2018-Online/students/marc_charbo/assignment_5/recursive.py(4)my_fun()
-> if n == 2:
(Pdb) c
> /Users/charbo/Documents/WU/Py2/Sp2018-Online/students/marc_charbo/assignment_5/recursive.py(4)my_fun()
-> if n == 2:
(Pdb) c
> /Users/charbo/Documents/WU/Py2/Sp2018-Online/students/marc_charbo/assignment_5/recursive.py(4)my_fun()
-> if n == 2:
(Pdb) pp n
0.21875
(Pdb) condition 1 n < 0.05
(Pdb) c
> /Users/charbo/Documents/WU/Py2/Sp2018-Online/students/marc_charbo/assignment_5/recursive.py(4)my_fun()
-> if n == 2:
(Pdb) pp n
0.02734375
(Pdb) 

"""