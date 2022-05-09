from hyperparam import *

if function_name == "ackley":
    if dim == 1:
        from benchmark_function import ackley as benchmark_fun
    if dim == 2:
        from benchmark_function import ackley_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import ackley_3d as benchmark_fun

if function_name == "alpine":
    if dim == 1:
        from benchmark_function import alpine as benchmark_fun
    if dim == 2:
        from benchmark_function import alpine_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import alpine_3d as benchmark_fun
    if dim == 5:
        from benchmark_function import alpine_5d as benchmark_fun

if function_name == "deceptive":
    if dim == 2:
        from benchmark_function import deceptive_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import deceptive_3d as benchmark_fun

if function_name == "griewank":
    if dim == 1:
        from benchmark_function import griewank as benchmark_fun
    if dim == 2:
        from benchmark_function import griewank_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import griewank_3d as benchmark_fun

if function_name == "michalewicz":
    if dim == 2:
        from benchmark_function import michalewicz_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import michalewicz_3d as benchmark_fun

if function_name == "rastring":
    if dim == 1:
        from benchmark_function import rastring as benchmark_fun
    if dim == 2:
        from benchmark_function import rastring_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import rastring_3d as benchmark_fun

if function_name == "rosenbrock":
    if dim == 2:
        from benchmark_function import rosenbrock_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import rosenbrock_3d as benchmark_fun

if function_name == "schwefel":
    if dim == 1:
        from benchmark_function import schwefel as benchmark_fun
    if dim == 2:
        from benchmark_function import schwefel_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import schwefel_3d as benchmark_fun

if function_name == "shubert":
    if dim == 1:
        from benchmark_function import shubert as benchmark_fun
    if dim == 2:
        from benchmark_function import shubert_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import shubert_3d as benchmark_fun

if function_name == "vincent":
    if dim == 1:
        from benchmark_function import vincent as benchmark_fun
    if dim == 2:
        from benchmark_function import vincent_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import vincent_3d as benchmark_fun

if function_name == "xinshe":
    if dim == 1:
        from benchmark_function import xinshe as benchmark_fun
    if dim == 2:
        from benchmark_function import xinshe_2d as benchmark_fun
    if dim == 3:
        from benchmark_function import xinshe_3d as benchmark_fun

if function_name == "sum_power":
    if dim == 3:
        from benchmark_function import sum_power_3d as benchmark_fun
