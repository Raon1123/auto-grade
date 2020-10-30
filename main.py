import os
import re

from studentclass import Student

homework = "Homework 1" #FIXIT
problem_n = 2 #FIXIT

student_list = []

def readAssignment():
    base_path = '.'
    source_path = base_path + '/source'
    student_path = base_path + '/student'
    parse_str = '[0-9]+\s[a-zA-Z ]+'

    os.system('rm -rf student')

    if not ('student' in os.listdir(base_path)):
        os.mkdir(student_path)

    parser = re.compile(parse_str)

    source_list = os.listdir(source_path)

    for zip in source_list:
        zip_path = source_path + '/' + zip
        p = parser.search(zip)

        if p == None:
            print('fail to parse: ' + zip)
        else:
            p_str = str(p.group())
            s = Student(p_str[0:8], p_str[9:])
            s.set_folderPath(student_path + '/' + s.get_id())
            os.mkdir(s.get_folderPath())
            commend = 'unzip ' + '\'' + zip_path + '\' -d ' + s.get_folderPath()
            os.system(commend)
            student_list.append(s)


def compileAssignment():
    print('=== Start Compile ===')

    for s in student_list:
        print("=== Compile Student Id " + s.get_id() + ' ===')
        folder_path = s.get_folderPath()
        folder_list = os.listdir(folder_path)

        for i in range(1, problem_n+1):
            if (('problem' + str(i) + '.cpp') in folder_list):
                commend = 'g++ -o ' + folder_path + '/problem' + str(i) + '.out ' + folder_path + '/problem' + str(i) +  '.cpp'
                os.system(commend)
        

def testAssignment():
    base_path = '.'
    test_path = base_path + '/test'
    score_list = []

    print('=== Read Score Data ===')

    for i in range(1, problem_n+1):
        score_path = test_path + '/problem' + str(i) + '/score.txt'
        problem_score = []
        p = re.compile('[0-9]+')

        score = open(score_path, 'r')
        
        lines = score.readlines() 
        
        for l in lines:
            parsed = p.match(l)
            problem_score.append(int(parsed.group()))

        score_list.append(problem_score)

    print('=== Start Test ===')

    for s in student_list:
        print("=== Test Student Id " + s.get_id() + ' ===')
        folder_path = s.get_folderPath()
        folder_list = os.listdir(folder_path)

        for i in range(1, problem_n+1):
            problem_path = test_path + '/problem' + str(i)
            student_score = []

            if (('problem' + str(i) + '.out') in folder_list):
                for n, sc in enumerate(score_list[i-1]):
                    problem_input = test_path + '/problem' + str(i) + '/input_' + str(n+1) + '.txt'
                    answer_path = test_path + '/problem' + str(i) + '/output_' + str(n+1) + '.txt'
                    problem_output = folder_path +  '/output_' + str(i) + '.txt'
                    
                    commend = 'cp ' + problem_input + ' ' + folder_path + '/input_' + str(i) + '.txt'
                    os.system(commend)

                    commend = 'touch ' + folder_path + '/output_' + str(i) + '.txt'
                    os.system(commend)

                    commend = 'cd ' + folder_path + ' && ./problem' + str(i) + '.out'
                    os.system(commend)

                    commend = 'diff ' + problem_output + ' ' + answer_path + ' > ' + folder_path + '/report_problem_' + str(i) + '_test_' + str(n+1) + '.txt' 
                    os.system(commend)

                    report = open(folder_path + '/report_problem_' + str(i) + '_test_' + str(n+1) + '.txt' ,'r')
                    if report.read() == '':
                        student_score.append(score_list[i-1][n])
                    else:
                        student_score.append(0)

                    commend = 'rm ' + folder_path + '/input_' + str(i) + '.txt'
                    os.system(commend)

                    commend = 'mv ' + folder_path + '/output_' + str(i) + '.txt ' + folder_path + '/output_problem_' + str(i) + '_test_' + str(n+1) + '.txt' 
                    os.system(commend)
            else:
                for n in enumerate(score_list[i-1]):
                    student_score.append(0)

            s.append_scoreList(student_score)

def individualReport():
    print('=== Make Individual Report ===')

    for s in student_list:
        s.individualReport()


def printReport():
    print('=== Print Report ===')

    report_path = './score_report.txt'
    report = open(report_path, 'w')

    for s in student_list:
        l = s.get_id() + ' ' + str(s.get_score()) + '\n'
        report.write(l)


def main():
    readAssignment()
    compileAssignment()
    testAssignment()
    individualReport()
    printReport()

if __name__ == "__main__":
    main()