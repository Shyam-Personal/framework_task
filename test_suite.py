import sys
import os

from Libs.setup import setup
from Libs.read_test_case import read_test_case
from Libs.update_log import update_log
from Libs.execute_command import exe_cmd
import importlib

""" Set up """
fh = open("summary.txt", "w")
fh.write("Testcase ID \t Testcase Name \t Test Result\n\n")
path = os.getcwd()

#obj = setup(raw_input("Enter the mount point : "), raw_input("Enter the test data folder path : "))
obj = setup("/mnt", "/mytestdata")
obj_log = update_log(path, "test_log.log")
logger = obj_log.setup_log("INFO")

if(not obj.validate()):
    print("Given mount point or test data folder doesn't exist")
    sys.exit()
 
""" Test Case Execution"""
tc_list = os.listdir(os.path.join(path, "testcases"))
for testcase in tc_list:
    obj = read_test_case(path, testcase)
    d1 = obj.tc_dict()
    obj_log.write_log(logger, "info", d1["id"])
    fail = 0
    for step in obj.key_value(d1, "steps"):
        if(obj.key_value(step, "cmd")):
            out,err = exe_cmd(step["cmd"])
            if(err):
                fail += 1
                obj_log.write_log(logger, "error", err)
            else:
                obj_log.write_log(logger, "info", out)
                out,err = exe_cmd(step["expected"])
                if (err):
                    obj_log.write_log(logger, "error", err)
                else:
                    obj_log.write_log(logger, "info", out)
                
        elif(obj.key_value(step, "file")):
            sys.path.append(os.path.join(os.getcwd(), "scripts"))
            a=importlib.import_module("scripts.{}".format(step["file"]))
            bool1, err = getattr(a,step["file"])(obj.key_value(step, "expected"), "b.txt", 22, 10)
            if (not bool1):
                fail += 1
                obj_log.write_log(logger, "error", err)
    
    """ Summary Report Update"""        
    if(fail):
        fh.write("{}\t\t{}\t\t{}".format(d1["id"], d1["name"], "Fail\n"))
    else:
        fh.write("{}\t\t{}\t\t{}".format(d1["id"], d1["name"], "Pass\n"))
