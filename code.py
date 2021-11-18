from tkinter import *
root=Tk()
root.title("QUIZ")
que=[
  ["What is the maximum possible length of an identifier?",
    "Who developed the Python language?",
    "In which year was the Python language developed?",
    "In which language is Python written?",
    "Which one of the following is the correct extension of the Python file?",
    "In which year was the Python 3.0 version developed?",
    "What do we use to define a block of code in Python language?",
    "Which character is used in Python to make a single line comment?",
    "Which of the following is not a keyword in Python language?",
    "Which one of the following has the highest precedence in the expression?",],
  ["Which of the following statements is correct regarding the object-oriented programming concept in Python?",
    "What is the method inside the class in python language?",
    "Which of the following declarations is incorrect?",
    "Why does the name of local variables start with an underscore discouraged?",
    "Which of the following statements is correct for variable names in Python language?",
    "Which of the following declarations is incorrect in python language?",
    "Which of the following words cannot be a variable in python language?",
    "Which of the following operators is the correct option for power(ab)?",
    "Which of the following option is not a core data type in the python language?",
    "MANGO = APPLE  ",],
  ["Which of the following precedence order is correct in Python?",
    "Which one of the following has the same precedence level?",
    "Which one of the following syntaxes is the correct syntax to read from a simple text file stored in ''d:\java.txt''?",
    "The output to execute string.ascii_letters can also be obtained from:?",
    "What happens when '2' == 2 is executed?",
    "Which of the following is a feature of Python DocString?",
    "What is the maximum possible length of an identifier in Python?",
    "Which of the following statements is used to create an empty set in Python?",
    "Which module in the python standard library parses options received from the command line?",
    "Which one of the following is not a keyword in Python language?",
    ],
]

answ=[
    [
        ['16','32','64','None of these above',],
        ['Zim Den','Guido van Rossum','Niene Stom','Wick van Rossum',],
        ['1995','1972','1981','1989',],
        ['English','PHP','C','All of the above',],
        ['.py','.python','.p','None of these',],
        ['2008','2000','2010','2005',],
        ['Key','Brackets','Indentation','None of these',],
        ['/','//','#','!',],
        ['val','raise','try','with',],
        ['Division','Subtraction','Power','Parentheses',],
    ],
    [
        ['Classes are real-world entities while objects are not real','Objects are real-world entities while classes are not real','Both objects and classes are real-world entities','All of the above',],
        ['Object','Function','Attribute','Argument',],
        ['_x = 2','__x = 3','__xyz__ = 5','None of these',],
        ['To identify the variable','It confuses the interpreter','It indicates a private variable of a class','None of these',],
        ['All variable names must begin with an underscore.','Unlimited length','The variable name length is a maximum of 2.','All of the above',],
        ['xyzp = 5,000,000','x y z p = 5000 6000 7000 8000','x,y,z,p = 5000, 6000, 7000, 8000','x_y_z_p = 5,000,000',],
        ['_val','val','try','_try_',],
        ['a ^ b','a**b','a ^ ^ b','a ^ * b',],
        ['Dictionary','Lists','Class','All of the above',],
        ['NameError','SyntaxError','TypeError','ValueError',],
    ],
    [
        ['Parentheses, Exponential, Multiplication, Division, Addition, Subtraction','Multiplication, Division, Addition, Subtraction, Parentheses, Exponential','Division, Multiplication, Addition, Subtraction, Parentheses, Exponential','Exponential, Parentheses, Multiplication, Division, Addition, Subtraction',],
        ['Division, Power, Multiplication, Addition and Subtraction','Division and Multiplication','Subtraction and Division','Power and Division',],
        ['Infile = open(''d:\\java.txt'', ''r'')','Infile = open(file=''d:\\\java.txt'', ''r'')','Infile = open(''d:\java.txt'',''r'')','Infile = open.file(''d:\\java.txt'',''r'')',],
        ['character','ascii_lowercase_string.digits','lowercase_string.upercase','ascii_lowercase+string.ascii_upercase',],
        ['False','Ture','ValueError occurs','TypeError occurs',],
        ['In Python all functions should have a docstring','Docstrings can be accessed by the __doc__ attribute on objects','It provides a convenient way of associating documentation with Python modules, functions, classes, and methods','All of the mentioned',],
        ['79 characters','31 characters','63 characters','none of the mentioned',],
        ['( )','[ ]','{ }','set()',],
        ['getarg','getopt','main','os',],
        ['pass','eval','assert','nonlocal',],
    ],
]

key=[
  ["d","d","d","c","a","a","c","c","a","d",],
  ["b","b","d","c","b","b","c","b","c","a",],
  ["a","b","a","d","a","d","d","d","b","b",],
]
global g,lblque,r1,r2,r3,r4
g=IntVar()
g.set("0")
def onclick(value):
    root.withdraw()
    screen=Tk()
    screen.title("QUIZ")
    screen.geometry("500x250")
    userans=[None]*10
    s=[0,1,2,3,4,5,6,7,8,9,]
    def select(r):
        global g
        userans[g.get()]=r
    g=0
    def change(c):
        global g,lblque,r1,r2,r3,r4
        if c=="pre":
            g.set(g.get()-1)
            lblque.config(text=que[value][s[g.get()]])
            r1['text']=answ[value][s[g.get()]][0]
            r2['text']=answ[value][s[g.get()]][1]
            r3['text']=answ[value][s[g.get()]][2]
            r4['text']=answ[value][s[g.get()]][3]
        elif c=="next":
            g.set(g.get()+1)
            if g.get()==10:
                change('end')
            else:
                lblque.config(text=que[value][s[g.get()]])
                r1['text']=answ[value][s[g.get()]][0]
                r2['text']=answ[value][s[g.get()]][1]
                r3['text']=answ[value][s[g.get()]][2]
                r4['text']=answ[value][s[g.get()]][3]
        elif c=="end":
            screen.withdraw()
            tree=Tk()
            tree.title("QUIZ")
            tree.geometry("200x50")
            sum=0
            for i in range(10):
                if userans[i]==key[value][i]:
                    sum+=1
            
            Label(tree,text="your score is "+str(sum)+"/10").pack()
            Label(tree,text="You got "+str(sum)+"0"+"%"+" answer correctly").pack()
        elif c=="save":
            print(userans)
    global lblque,r1,r2,r3,r4
    intr=Label(screen,text="Hello, "+name.get())
    intr.pack()
    lblque=Label(screen,text=que[value][s[0]],justify="center",wraplength=400)
    lblque.pack()
    r=IntVar()
    r.set('-1')
    r1=Radiobutton(screen,text=answ[value][s[g]][0],variable=r,value=0,command=lambda:select("a"))
    r1.pack()
    r2=Radiobutton(screen,text=answ[value][s[g]][1],variable=r,value=1,command=lambda:select("b"))
    r2.pack()
    r3=Radiobutton(screen,text=answ[value][s[g]][2],variable=r,value=2,command=lambda:select("c"))
    r3.pack()
    r4=Radiobutton(screen,text=answ[value][s[g]][3],variable=r,value=3,command=lambda:select("d"))
    r4.pack()
    screeno=LabelFrame(screen)
    screeno.pack()
    screeno.config(width=10)
    save=Button(screeno,text="save", command=lambda:change("save"),height=1,width=8)
    save.pack(side= TOP)
    pre=Button(screeno,text="previous",command=lambda:change("pre"),height=1,width=8)
    pre.pack(side=LEFT)
    next=Button(screeno,text="next",command=lambda:change("next"),height=1,width=8)
    next.pack(side=RIGHT)
    end=Button(screeno,text="end",command=lambda:change("end"),height=1,width=8)
    end.pack(side=BOTTOM)
Label(root, text="NAME").grid(row=0,column=0)
Label(root, text="REGISTRATION NUMBER").grid(row=1,column=0)
Label(root, text="SECTION").grid(row=2,column=0)
Label(root, text="LEVEL",).grid(row=3,column=0)
name=Entry(root, width=50, border=5)
name.grid(row=0,column=1)
Entry(root, width=50, border=5).grid(row=1,column=1)
Entry(root, width=50, border=5).grid(row=2,column=1)
v=IntVar()
v.set("-1")
v1=Radiobutton(root, text="EASY",value=0,variable=v,).grid(row=3,column=1)
v2=Radiobutton(root, text="NORMAL",value=1,variable=v,).grid(row=4,column=1)
v3=Radiobutton(root, text="HARD",value=2,variable=v,).grid(row=5,column=1)
Button(root, text="SUBMIT",command=lambda: onclick(v.get())).grid(row=6,column=1)
root.mainloop()
