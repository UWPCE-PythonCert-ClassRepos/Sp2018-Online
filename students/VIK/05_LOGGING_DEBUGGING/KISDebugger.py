#!/usr/bin/env python3

"""********************************************************************************************************************
         TITLE: UW PYTHON 220 - Lesson 05 - Activity
     SUB TITLE: Python Debugger
       CREATOR: PydPiper
  DATE CREATED: 5/6/18
 LAST MODIFIED: 5/6/18
   DESCRIPTION: Run python debugger on the given recursive code below.
                1) Address the problem with the code in a few sentances
                2) Copy and paste the Terminal Debugging activity to catch the error.
********************************************************************************************************************"""

""" ACTIVITY CODE """
import sys


def my_fun(n):
    if n == 2:
        return True
 
    return my_fun(n/2)


if __name__ == '__main__':
    n = int(sys.argv[1])
    print(my_fun(n))


""" SOLUTION - 1 """
"""
The recursive code is intendent to return Bool - True for powers of 2, however the code
does not have a condition to stop recursion if an input value is not a power of 2 and
thereby maxes out allowed python stacks. A quick fix:

def my_fun(n):
    if n == 2:
        return True
    elif n < 2:
        return False
 
    return my_fun(n/2)
"""

""" SOLUTION - 2 """

# >>>05_LOGGING_DEBUGGING [IN]:  python -m pdb .\KISDebugger.py 8
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(12)<module>()
# -> ********************************************************************************************************************"""
# (Pdb) ll
  # 1     #!/usr/bin/env python3
  # 2
  # 3     """********************************************************************************************************************
  # 4              TITLE: UW PYTHON 220 - Lesson 05 - Activity
  # 5          SUB TITLE: Python Debugger
  # 6            CREATOR: PydPiper
  # 7       DATE CREATED: 5/6/18
  # 8      LAST MODIFIED: 5/6/18
  # 9        DESCRIPTION: Run python debugger on the given recursive code below.
 # 10                     1) Address the problem with the code in a few sentances
 # 11                     2) Copy and paste the Terminal Debugging activity to catch the error.
 # 12  -> ********************************************************************************************************************"""
 # 13
 # 14     """ ACTIVITY CODE """
 # 15     import sys
 # 16
 # 17
 # 18     def my_fun(n):
 # 19         if n == 2:
 # 20             return True
 # 21
 # 22         return my_fun(n/2)
 # 23
 # 24
 # 25     if __name__ == '__main__':
 # 26         n = int(sys.argv[1])
 # 27         print(my_fun(n))
 # 28
 # 29
 # 30     """ SOLUTION - 1 """
 # 31     """
 # 32     The recursive code is intendent to return Bool - True for powers of 2, however the code
 # 33     does not have a condition to stop recursion if an input value is not a power of 2 and
 # 34     thereby maxes out allowed python stacks. A quick fix:
 # 35
 # 36     def my_fun(n):
 # 37         if n == 2:
 # 38             return True
 # 39         elif n < 2:
 # 40             return False
 # 41
 # 42         return my_fun(n/2)
 # 43     """
 # 44
# (Pdb) b 22
# Breakpoint 1 at c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py:22
# (Pdb) c
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(22)my_fun()
# -> return my_fun(n/2)
# (Pdb) pp n
# 8
# (Pdb) c
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(22)my_fun()
# -> return my_fun(n/2)
# (Pdb) pp n
# 4.0
# (Pdb) s
# --Call--
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(18)my_fun()
# -> def my_fun(n):
# (Pdb) pp n
# 2.0
# (Pdb) s
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(19)my_fun()
# -> if n == 2:
# (Pdb) s
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(20)my_fun()
# -> return True
# (Pdb) s
# --Return--
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(20)my_fun()->True
# -> return True
# (Pdb) pp n
# 2.0
# (Pdb) s
# --Return--
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(22)my_fun()->True
# -> return my_fun(n/2)
# (Pdb) pp n
# 4.0
# (Pdb) s
# --Return--
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(22)my_fun()->True
# -> return my_fun(n/2)
# (Pdb) pp n
# 8
# (Pdb) s
# True
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(43)<module>()
# -> """
# (Pdb) c
# The program finished and will be restarted
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(12)<module>()
# -> ********************************************************************************************************************"""
# (Pdb) exit



# >>>05_LOGGING_DEBUGGING [IN]:  python -m pdb .\KISDebugger.py 5
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(12)<module>()
# -> ********************************************************************************************************************"""
# (Pdb) ll
  # 1     #!/usr/bin/env python3
  # 2
  # 3     """********************************************************************************************************************
  # 4              TITLE: UW PYTHON 220 - Lesson 05 - Activity
  # 5          SUB TITLE: Python Debugger
  # 6            CREATOR: PydPiper
  # 7       DATE CREATED: 5/6/18
  # 8      LAST MODIFIED: 5/6/18
  # 9        DESCRIPTION: Run python debugger on the given recursive code below.
 # 10                     1) Address the problem with the code in a few sentances
 # 11                     2) Copy and paste the Terminal Debugging activity to catch the error.
 # 12  -> ********************************************************************************************************************"""
 # 13
 # 14     """ ACTIVITY CODE """
 # 15     import sys
 # 16
 # 17
 # 18     def my_fun(n):
 # 19         if n == 2:
 # 20             return True
 # 21
 # 22         return my_fun(n/2)
 # 23
 # 24
 # 25     if __name__ == '__main__':
 # 26         n = int(sys.argv[1])
 # 27         print(my_fun(n))
 # 28
 # 29
 # 30     """ SOLUTION - 1 """
 # 31     """
 # 32     The recursive code is intendent to return Bool - True for powers of 2, however the code
 # 33     does not have a condition to stop recursion if an input value is not a power of 2 and
 # 34     thereby maxes out allowed python stacks. A quick fix:
 # 35
 # 36     def my_fun(n):
 # 37         if n == 2:
 # 38             return True
 # 39         elif n < 2:
 # 40             return False
 # 41
 # 42         return my_fun(n/2)
 # 43     """
 # 44
# (Pdb) b 22
# Breakpoint 1 at c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py:22
# (Pdb) c
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(22)my_fun()
# -> return my_fun(n/2)
# (Pdb) pp n
# 5
# (Pdb) c
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(22)my_fun()
# -> return my_fun(n/2)
# (Pdb) pp n
# 2.5
# (Pdb) c
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(22)my_fun()
# -> return my_fun(n/2)
# (Pdb) pp n
# 1.25
# (Pdb) c
# > c:\users\vkisf\desktop\python101\sp2018-online\students\vik\05_logging_debugging\kisdebugger.py(22)my_fun()
# -> return my_fun(n/2)
# (Pdb) pp n
# 0.625
# (Pdb) exit