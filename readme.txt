1) Libs : Libs folder contains all the libraries that are required to exeucute the test cases.
Those libraries will be imported to another file to use.

2) Log : Log folder contains log files generated.

3) Scripts : The scripts folder contains the individual scripts for any test cases.

4) Testcases: The testcases folder contains the all the testcases in the json format. Each testcase has its own .tc file.
The json format contains the id, name, description & array of steps.
The array of steps again contains the dictionary with cmd/file & expected output.
If there is cmd in the file then we execute the command & get the output.
If the test case contains the file then we execute that python file & gets the output.
The python file name & the method name in that file has too be same.

5) Summary.txt : Summary file contains the results of the tests. It is the report for the tets suite.

6) Test suite: The test_suite.py file contains the logic to read all the testcases from the testcases folder & 
execute them one by one.
Collect the logs & maintain the results in the summary file.