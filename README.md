# MILP-For-MP-HVRP-TWD
## install cplex
refer to https://www.ibm.com/support/pages/installation-ibm-ilog-cplex-optimization-studio-linux-platforms
## make the c++ project
modify the following fields so that the value is aligned with your environment.
1. SYSTEM: x86-64_osx, x86-64_linux, x86-64_windows
2. CPLEXDIR: the directories where CPLEX and CONCERT are installed.
3. CONCERTDIR: the directories where CPLEX and CONCERT are installed.
type "make milp" in the CMD to make the project.
## run the python file
type "python main.py --instance ${instances_path}" in the CMD to run the cplex solver.
## instances modification
25 vehicles: 10 x 2, 15 x-200 1
200 capacity 1-7 days
700 capacity 1-6 days
1000 capacity 1-5 days
p: 5
w: 1000
f: 2
20% off from T_max