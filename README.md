# auto-grade

# Abstract

This is automatically grading tool for UNIST CSE241 Object Oriented Programming.
This tool made by Yunpyo An.
If you have any question regrading this tool please ask by [e-mail](anyunpyo@unist.ac.kr)

# Submission

The collected students submission is under `source` folder.
The file name format need to have `<student id>` + one white space + `<student name>`.
And filename extension is `.zip`
The source code must under directly zip folder.
The source code of each problem is `problem` or `Problem` + `<problem number>` + `.cpp`.

# Compile

This tool supports automatically compile by `g++`.
The compile code is `g++ -o ` + `problem` + `<problem number>` + `.out` + `<source code of each problem>`
The compile results are under `student` folder.
Under the `student` folder, there is folders such that name is `<student id>`.
Also, remain results of each students are under these folder.

# Test condition

In version 1, it supports file input and output testing.
The student must read `input_` + `<problem number>` + `.txt`.
The student must write `output_` + `<problem number>` + `.txt`.
If student fail to write this file, he/she automatically get zero grade.
The output of each task is saved name `output_problem_` + `<problem number>` + `_task_` + `<task number>` + `.txt`.

# Testcase

The test cases are under `test` folder.
This tool support multiple problem grading.
The testcase of each problem is under `problem` + `<number of problem>`.
The number of problem starts 1.
Under the problem, it needs two type of files, input and output.
The file name of input is `input_` + `<Task number>` + `.txt`.
The file name of output is `output_` + `<Task number>` + `.txt`.
The file name of scores of each task is `score.txt`
This program automatically reports the difference between students output and answer by `diff`.
The report of compare is  `report_problem_` + `<problem number>` + `_task_` + `<task number>` + `.txt`.

# Score Report

The total score report is `score_report.txt`.
It stores list of data of `<each student id>` + ` ` + `<each student total score>`.

This tool supports individual report of each student.
The name is `individual_report.txt`.
It shows details of score of student.
It shows score of each problem and task.

# Remain Develop Part

The standard input and output system is more general testing.
I will support this type of grading system.