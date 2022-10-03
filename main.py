import numpy as np
import os
import subprocess
import uuid
import argparse


def homberger_parser(file_name, rouneded=True):
    demands = []
    mode = ''
    capacity = None
    no_vehicles = 0
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip(' \t\n')
            if line == "VEHICLE":
                f.readline()
                line = f.readline()
                line = line.strip(' \t\n')
                line = " ".join(line.split()).split(" ")
                no_vehicles = int(line[0])
                capacity = int(line[1])
            if line == "CUSTOMER":
                f.readline()
                f.readline()
                mode = "customer"
            if mode == "customer":
                line = f.readline()
                line = line.strip(' \t\n')
                line = " ".join(line.split()).split(" ")
                demands.append([line[1], line[2], line[4], line[5], 1, 1, line[3], line[6]])
    temp_file_name = file_name.split("/")[-1] + "__" + str(uuid.uuid4())
    temp_file = open(temp_file_name, "w")
    temp_file.write("VEHICLES\n")
    for _ in range(no_vehicles):
        temp_file.write(str(capacity) + "," + str(1) + "\n")
    temp_file.write("DEMANDS\n")
    for row in demands:
        temp_file.write(str(row).replace("[", "").replace("]", "").replace("'", "").replace(" ", "") + "\n")
    temp_file.close()


def solomon_parser(file_name):
    demands = []
    mode = ''
    capacity = None
    no_vehicles = 0
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip(' \t\n')
            if line == "VEHICLE":
                f.readline()
                line = f.readline()
                line = line.strip(' \t\n')
                line = " ".join(line.split()).split(" ")
                no_vehicles = int(line[0])
                capacity = int(line[1])
            elif line == "CUSTOMER":
                f.readline()
                f.readline()
                mode = "customer"
            elif mode == "customer":
                line = line.strip(' \t\n')
                line = " ".join(line.split()).split(" ")
                demands.append([line[1], line[2], line[4], line[5], 1, 1, line[3], line[6]])
    temp_file_name = file_name.split("/")[-1] + "__" + str(uuid.uuid4())
    temp_file = open(temp_file_name, "w")
    temp_file.write("VEHICLES\n")
    for _ in range(no_vehicles):
        temp_file.write(str(capacity) + "," + str(1) + "\n")
    temp_file.write("DEMANDS\n")
    for row in demands:
        temp_file.write(str(row).replace("[", "").replace("]", "").replace("'", "").replace(" ", "") + "\n")
    temp_file.close()
    return temp_file_name


def new_instances_generator(file_name):
    demands = []
    mode = ''
    capacity = None
    no_vehicles = 0
    T_max = 0
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip(' \t\n')
            if line == "VEHICLE":
                f.readline()
                line = f.readline()
                line = line.strip(' \t\n')
                line = " ".join(line.split()).split(" ")
                no_vehicles = int(line[0])
                capacity = int(line[1])
            elif line == "CUSTOMER":
                f.readline()
                f.readline()
                mode = "customer"
                if capacity >= 1000:
                    due_date = 5
                elif capacity <= 200:
                    due_date = 7
                else:
                    due_date = 6
            elif mode == "customer":
                line = line.strip(' \t\n')
                line = " ".join(line.split()).split(" ")
                if line[0] == "0":
                    T_max = int(int(line[5]) * 0.8)
                demands.append([line[1], line[2], line[4], line[5], 1, due_date, line[3], line[6]])
    temp_file_name = file_name.split("/")[-1] + "_new"
    temp_file = open(temp_file_name, "w")
    temp_file.write("PARAM\n")
    temp_file.write(str(5) + "," + str(1000) + "," + str(2) + "," + str(T_max) + "\n")
    temp_file.write("VEHICLES\n")
    for _ in range(int(no_vehicles * 3 / 5)):
        temp_file.write(str(capacity) + "," + str(2) + "\n")
    for _ in range(int(no_vehicles * 2 / 5)):
        temp_file.write(str(capacity - 100) + "," + str(1) + "\n")
    temp_file.write("DEMANDS\n")
    idx = 0
    for row in demands:
        temp_file.write(
            str(idx) + "," + str(row).replace("[", "").replace("]", "").replace("'", "").replace(" ", "") + "\n")
        idx += 1
    temp_file.close()
    return temp_file_name


# parser = argparse.ArgumentParser()
# parser.add_argument("--instance", type=str, default="")
# args = parser.parse_args()
# file_name = solomon_parser(args.instance)
# with subprocess.Popen(["./milp", file_name], stdout=subprocess.PIPE, universal_newlines=True) as p:
#     for _ in p.stdout:
#         continue
#     os.remove(file_name)
new_instances_generator("./CVRPTW_instances/Solomon/C101.txt")
