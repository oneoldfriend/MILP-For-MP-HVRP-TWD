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


parser = argparse.ArgumentParser()
parser.add_argument("--instance", type=str, default="")
args = parser.parse_args()
file_name = solomon_parser(args.instance)
with subprocess.Popen(["./milp", file_name], stdout=subprocess.PIPE, universal_newlines=True) as p:
    for _ in p.stdout:
        continue
    os.remove(file_name)
