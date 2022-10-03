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
1. heterogenous vehicles: 60% of vehicle's capacity are same as the original ones with traveling cost $c_k$ equals 2, 40% of vehicles has capacity equals original capacity minus 100, and their traveling cost equals 1.
2. multiple periods and due date: For instances with original capacity equals 200, all demands' request date set to 1, their due date are set to 7. For instances with capacity equals 700, all demands' request date are set to 1, their due date are set to 6; For instances with capacity equals 1000, all demands' request date are set to 1, their due date are set to 5.
3. profit $p$ per unit demands are set to 5, outsourcing cost $w$ per demand are set to 1000, overtime wages $f$ per unit time are set to 2, maximum work time $T_{max}$ are set to 80% of original one.