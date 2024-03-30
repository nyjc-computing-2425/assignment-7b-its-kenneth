# Built-in imports
import math

# Your code below
GRADE = {}
letter_grade = "ABCDESU"
score_range = [70,60,55,50,45,40,0]


for i in range(1,101):
    for x in range(len(score_range)):
        if i >= score_range[x]:
            GRADE[i] = letter_grade[x]
            break
#print(GRADE)


def read_testscores(filename):
    '''
    Parameter
    ---------
    filename: str
        name of file to be read
    Returns
    -------
    dict
        list of dictionaries, each dictionary representing 'class', 'name', 'overall', 'grade' data for a single student
    '''
    # Class1,Student1,14,15,45,19
    studentdata = []
    with open(filename,'r') as f:
        f.readline()
        for line in f:
            #print(f.readline()[:-1].split(","))
            s_class,s_no,p1,p2,p3,p4 = line[:-1].split(",")
            p1,p2,p3,p4 = int(p1),int(p2),int(p3),int(p4)
            overall = math.ceil((p1/30 * 15) + (p2/40 * 30) + (p3/80 * 35) + (p4/30 * 20))
            grade = GRADE[overall]
            dict = {"class":s_class,"name":s_no,"overall":overall,"grade":grade}
            studentdata.append(dict)
        # f.close() is called automatically
    return studentdata


def analyze_grades(studentdata):
    '''
    Parameter
    ---------
    studentdata: list
        list of dictionaries, each dictionary representing 'class', 'name', 'overall', 'grade' data for a single student
        
    Returns
    -------
    analysis: dict 
        dictionary of dictionaries representing the number of each grade scored for each class
    '''
    analysis = {}
    #class_list = []
    for i in studentdata:
        if not(i['class'] in analysis.keys()):
            #class_list.append(i['class'])
            analysis[i['class']] = {}
    #return analysis
    #return analysis.keys()
    
    #for classes in class_list:
    for class_ in analysis.keys():
        for student in studentdata:
            for grade in letter_grade:
                if student['class'] == class_ and student['grade'] == grade:
                    if analysis[class_].get(grade) is None:
                        analysis[class_][grade] = 1
                    else:
                        analysis[class_][grade] = analysis[class_][grade] + 1
                    break
                else:
                    if analysis[class_].get(grade) is None:
                        analysis[class_][grade] = 0
                
                    
    return analysis                
                
    
        
    #{"Class 1":{"A":1,"B":2},}