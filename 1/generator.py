import random
from fractions import Fraction

#整数四则运算（范围0~n）
def newint(num):
    Exercises=''
    Answers=''
    opr = ['＋', '－', '×', '÷']
    fh = random.randint(0, 3)
    n1 = random.randint(1, num)
    n2 = random.randint(1, num)
    rjg = 0
    if fh == 0:
        rjg = n1 + n2
    elif fh == 1:
        n1, n2 = max(n1, n2), min(n1, n2)
        rjg = n1 - n2
    elif fh == 2:
        rjg = n1 * n2
    elif fh == 3:
        n1, n2 = max(n1, n2), min(n1, n2)
        while n1 % n2 != 0:
            n1 = random.randint(1, 10)
            n2 = random.randint(1, 10)
            n1, n2 = max(n1, n2), min(n1, n2)
        rjg = int(n1 / n2)
    Exercises=str(n1) + opr[fh] + str(n2) + '='
    Answers=str(rjg)
    return Exercises,Answers


#真分数四则运算
def newfra(num):
    opr = ['＋', '－', '×', '÷']
    fh = random.randint(0, 3)
    t1 = random.randint(1, num)
    t2 = random.randint(t1, num)
    n1 = Fraction(t1, t2)
    t1 = random.randint(1, num)
    t2 = random.randint(t1, num)
    n2 = Fraction(t1, t2)
    rjg = 0
    if fh == 0:
        rjg = n1 + n2
    elif fh == 1:
        n1, n2 = max(n1, n2), min(n1, n2)
        rjg = n1 - n2
    elif fh == 2:
        rjg = n1 * n2
    elif fh == 3:
        n1, n2 = max(n1, n2), min(n1, n2)
        rjg = n1 / n2
    Exercises=str(n1) + opr[fh] + str(n2) + '='
#对真分数进行规范化表达
    if rjg>1 and (rjg-int(rjg))!=0:
        Answers=str(int(rjg))+"'"+str(rjg-int(rjg))
    else:
        Answers=str(rjg)
    return Exercises,Answers



#生成试卷和答案
def newtest():
    opr = ['＋', '－', '×', '÷']
    Exercises=''
    Answers=''
#输入生成题目的个数和数值的范围
    print('请输入生成题目的个数：')
    n=int(input())
    print('请输入生成题目中数值的范围：')
    num=int(input())
#创建练习和答案文本
    ExercisesFile = open('Exercises.txt' , 'w')
    AnswersFile = open('Answers.txt' , 'w')
#生成题目并写入练习和答案文件
    #随机生成n道四则运算
    m = 0
    while m<=(n-1):
        fh = random.randint(0, 2)
        if fh==0:
            Exercises,Answers=newfra(num)
        else:
            Exercises,Answers=newint(num)
    #写入文本
        ExercisesFile.write('%s、%s\n'  %(m+1,Exercises) )
        AnswersFile.write('%s、%s\n'  %(m+1,Answers) )
        m=m+1
#关闭文件
    ExercisesFile.close()
    AnswersFile.close()


#判定答案中的对错
def check(testanswer):
    Correct=[]
    Wrong=[]
    i=0
    testanswerFile = open(testanswer, 'r')
    AnswersFile = open('Answers.txt', 'r')
    GradeFile = open('Grade.txt', 'w')
    t=testanswerFile.readline()
    a=AnswersFile.readline()
    for i in range(len(t)):
        if t[i]==a[i]:
            Correct.append(str(i+1))
        else:
            Wrong .append(str(i+1))
        i+=1
    print(  'Correct:',len(Correct) ,Correct)
    print(  'Wrong:',len(Wrong) , Wrong,)
    testanswerFile.close()
    AnswersFile.close()
    GradeFile.close()


#运行主函数
newtest()
