"""
Running timeit and cProfile
"""

#
#
# map_filter_with_functions
# 0.002967999999782478
#
#
# map_filter_with_lambdas
# 0.003861000000142667
#
#
# comprehension
# 8.679376000000047
#
#
# comprehension_with_lambdas
# 111.44657400000051
#          100010399 function calls (100010389 primitive calls) in 95.977 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
#       3/1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
#        18    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:232(_requires_builtin_wrapper)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
#         8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:433(spec_from_loader)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:564(module_from_spec)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
#       2/1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:651(_load_unlocked)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:707(find_spec)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:728(create_module)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:736(exec_module)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:753(is_package)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:780(find_spec)
#         4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:843(__enter__)
#         4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:847(__exit__)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:870(_find_spec)
#       2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:936(_find_and_load_unlocked)
#       2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:966(_find_and_load)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:997(_handle_fromlist)
#         4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1080(_path_importer_cache)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1117(_get_spec)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1149(find_spec)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1228(_get_spec)
#         3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1233(find_spec)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:263(cache_from_source)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:361(_get_cached)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:393(_check_name_wrapper)
#         3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:41(_relax_case)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:430(_validate_bytecode_header)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:485(_compile_bytecode)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:52(_r_long)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:524(spec_from_file_location)
#        16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:57(_path_join)
#        16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:59(<listcomp>)
#         2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:63(_path_split)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:669(create_module)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:672(exec_module)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:743(get_code)
#         5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:75(_path_stat)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:800(__init__)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:825(get_filename)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:830(get_data)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:840(path_stats)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:85(_path_is_mode_type)
#         1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:94(_path_isfile)
#         1    0.000    0.000    0.000    0.000 <timeit-src>:2(<module>)
#         1    0.338    0.338  111.447  111.447 <timeit-src>:2(inner)
# 100000000   27.268    0.000   27.268    0.000 <timeit-src>:6(<lambda>)
#     10000   68.366    0.007  111.109    0.011 <timeit-src>:6(<listcomp>)
#         4    0.000    0.000    0.001    0.000 timeit.py:102(__init__)
#         4    0.000    0.000  120.133   30.033 timeit.py:164(timeit)
#         4    0.000    0.000  120.134   30.033 timeit.py:230(timeit)
#         1    0.000    0.000    0.000    0.000 timeit.py:51(<module>)
#         8    0.000    0.000    0.000    0.000 timeit.py:80(reindent)
#         1    0.000    0.000    0.000    0.000 timeit.py:84(Timer)
#         1    0.000    0.000  120.138  120.138 timeit_experiment.py:2(<module>)
#         1    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
#         8    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
#         1    0.000    0.000    0.000    0.000 {built-in method _imp.create_builtin}
#         1    0.000    0.000    0.000    0.000 {built-in method _imp.exec_builtin}
#         2    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
#         1    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
#         8    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
#         4    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
#         4    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.any}
#        12    0.001    0.000    0.001    0.000 {built-in method builtins.compile}
#       6/1    0.000    0.000  120.138  120.138 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.globals}
#        10    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
#        13    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         8    0.003    0.000    0.003    0.000 {built-in method builtins.print}
#         2    0.000    0.000    0.000    0.000 {built-in method from_bytes}
#         4    0.000    0.000    0.000    0.000 {built-in method gc.disable}
#         4    0.000    0.000    0.000    0.000 {built-in method gc.enable}
#         4    0.000    0.000    0.000    0.000 {built-in method gc.isenabled}
#         1    0.000    0.000    0.000    0.000 {built-in method marshal.loads}
#         3    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
#         2    0.000    0.000    0.000    0.000 {built-in method posix.getcwd}
#         5    0.000    0.000    0.000    0.000 {built-in method posix.stat}
#         8    0.000    0.000    0.000    0.000 {built-in method time.perf_counter}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
#         4    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
#         4    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
#        18    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#         1    0.000    0.000    0.000    0.000 {method 'read' of '_io.FileIO' objects}
#         8    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
#        11    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
#        34    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}

