import sys

def my_fun(n):
    if n == 2:
        return True

    return my_fun(n/2)


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(my_fun(15))


 """
Q: What is wrong with our logic?
A: It only works if n is a power of 2. If it is not it will run until the stack overflows i.e RuntimeError: maximum recursion depth exceeded
Q: Why doesn't the function stop calling itself?
A: Each number tested  that are not power of two's, they will never dived evenly into 2, reducing until an exception is raised
Q: What's happening to the value of 'n' as the function gets deeper and deeper into recursion?
A: 'n' goes dwindles closer to zero, but will never reach it, but instead raise the following:
RecursionError: maximum recursion depth exceeded in comparison
Uncaught exception. Entering post mortem debugging
Running 'cont' or 'step' will restart the program

*******TERMINAL OUTPUT BELOW***********
(Pdb) n
> /home/lamb0fam/Documents/repos/Sp2018-Online/students/Gabe_Lamberth/lesson05/recursive.py(3)<module>()
-> def my_fun(n):
(Pdb) n
> /home/lamb0fam/Documents/repos/Sp2018-Online/students/Gabe_Lamberth/lesson05/recursive.py(10)<module>()
-> if __name__ == '__main__':
(Pdb) pp n
*** NameError: name 'n' is not defined
(Pdb) n = 15
> /home/lamb0fam/Documents/repos/Sp2018-Online/students/Gabe_Lamberth/lesson05/recursive.py(11)<module>()
-> n = int(sys.argv[1])
(Pdb) ppn
*** NameError: name 'ppn' is not defined
(Pdb) pp n
*** NameError: name 'n' is not defined
(Pdb) ll;
  1  	import sys
  2  	
  3  	def my_fun(n):
  4  	    if n == 2:
  5  	        return True
  6  	
  7  	    return my_fun(n/2)
  8  	
  9  	
 10  	if __name__ == '__main__':
 11  ->	    n = int(sys.argv[1])
 12  	    print(my_fun(n))
 13  	
 14  	
(Pdb) ll
  1  	import sys
  2  	
  3  	def my_fun(n):
  4  	    if n == 2:
  5  	        return True
  6  	
  7  	    return my_fun(n/2)
  8  	
  9  	
 10  	if __name__ == '__main__':
 11  ->	    n = int(sys.argv[1])
 12  	    print(my_fun(n))
 13  	
 14  	
(Pdb) n = 15
> /home/lamb0fam/Documents/repos/Sp2018-Online/students/Gabe_Lamberth/lesson05/recursive.py(12)<module>()
-> print(my_fun(n))
(Pdb) pp n
15
(Pdb) ll
  1  	import sys
  2  	
  3  	def my_fun(n):
  4  	    if n == 2:
  5  	        return True
  6  	
  7  	    return my_fun(n/2)
  8  	
  9  	
 10  	if __name__ == '__main__':
 11  	    n = int(sys.argv[1])
 12  ->	    print(my_fun(n))
 13  	
 14  	
(Pdb) s
--Call--
> /home/lamb0fam/Documents/repos/Sp2018-Online/students/Gabe_Lamberth/lesson05/recursive.py(3)my_fun()
-> def my_fun(n):
(Pdb) n
> /home/lamb0fam/Documents/repos/Sp2018-Online/students/Gabe_Lamberth/lesson05/recursive.py(4)my_fun()
-> if n == 2:
(Pdb) n
> /home/lamb0fam/Documents/repos/Sp2018-Online/students/Gabe_Lamberth/lesson05/recursive.py(7)my_fun()
-> return my_fun(n/2)
(Pdb) s
--Call--
> /home/lamb0fam/Documents/repos/Sp2018-Online/students/Gabe_Lamberth/lesson05/recursive.py(3)my_fun()
-> def my_fun(n):
(Pdb) n
> /home/lamb0fam/Documents/repos/Sp2018-Online/students/Gabe_Lamberth/lesson05/recursive.py(4)my_fun()
-> if n == 2:
(Pdb) pp n
7.5
(Pdb) ll
  3  	def my_fun(n):
  4  ->	    if n == 2:
  5  	        return True
  6  	
  7  	    return my_fun(n/2)
(Pdb) n
> /home/lamb0fam/Documents/repos/Sp2018-Online/students/Gabe_Lamberth/lesson05/recursive.py(7)my_fun()
-> return my_fun(n/2)
(Pdb) s
--Call--
> /home/lamb0fam/Documents/repos/Sp2018-Online/students/Gabe_Lamberth/lesson05/recursive.py(3)my_fun()
-> def my_fun(n):
(Pdb) pp n
3.75
(Pdb) l
  1  	import sys
  2  	
  3  ->	def my_fun(n):
  4  	    if n == 2:
  5  	        return True
  6  	
  7  	    return my_fun(n/2)
  8  	
  9  	
 10  	if __name__ == '__main__':
 11  	    n = int(sys.argv[1])
(Pdb) n
> /home/lamb0fam/Documents/repos/Sp2018-Online/students/Gabe_Lamberth/lesson05/recursive.py(4)my_fun()
-> if n == 2:
(Pdb) l
  1  	import sys
  2  	
  3  	def my_fun(n):
  4  ->	    if n == 2:
  5  	        return True
  6  	
  7  	    return my_fun(n/2)
  8  	
  9  	
 10  	if __name__ == '__main__':
 11  	    n = int(sys.argv[1])
(Pdb) n
> /home/lamb0fam/Documents/repos/Sp2018-Online/students/Gabe_Lamberth/lesson05/recursive.py(7)my_fun()
-> return my_fun(n/2)
(Pdb) s
--Call--
> /home/lamb0fam/Documents/repos/Sp2018-Online/students/Gabe_Lamberth/lesson05/recursive.py(3)my_fun()
-> def my_fun(n):
(Pdb) pp n
1.875
(Pdb)
 
 
 """