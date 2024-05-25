### code will have information about gpa
#about courses and their credit hours
#code will get obtained and total marks of every course
#then calculates the gpa and 
#displays every course name, credit hours, obtained and total marks, gpa and Cgpa


#general info about courses name stored in variable of their short form
#my convention of creating variable name is that only first letter is capaital
Itc = "Introduction to Computing"
Itc_pr = "Introduction to Computing(PR)"
Fun_eng = "Functional English"
App_phy = "Applied Physics"
App_phy_pr = "Applied Physics(PR)"
Workshop = "Workshop(PR)"
Ps = "Pakistan studies"
Isl = "Islamic Studies"
Cad = "Computer Added Design"
Lca = "linear Circuit Analysis"
Lca_pr = "linear Circuit Analysis(PR)"
Caps = "Communication and Presentation Skills"
Pfe = "Programming for Engineers"
Pfe_pr = "Programming for Engineers(PR)"
Ena = "Electrical Network Analysis"
Ena_pr = "Electrical Network Analysis(PR)"
Edc = "Electronic Devices and Circuits"
Edc_pr = "Electronic Devices and Circuits(PR)"
Chi = "Introduction to Chinese Language"
Cal = "Calculus and Analytical Geometry"
Lade = "Linear Algebra and Diffrential Equation"
M_cal = "Multivariable Calculus"

Ccn_thr = input("Enter Specialization (E for Electronics and P for power)") 
if Ccn_thr == "e" or "E" or "electronics" or "Electronics":               #asks specialization and decides courses
    Ccn_thr = "Computer Communication and Networks"
elif Ccn_thr == "p" or "P" or "Power" or 'power':
    Ccn_thr = "Applied Thermodynamics"
else:
    print("Invalid Specialization")
    Ccn_thr = "Second semester distintive course"

if Ccn_thr == "Computer Communication and Networks":         
    Ccn_thr_pr = "Computer Communication and Networks(PR)"
if Ccn_thr ==  "Applied Thermodynamics":
    Ccn_thr_pr = "Applied Thermodynamics(PR)"
else:
    print("Invalid Specialization")

    
#credit hours of courses
Itc_ch :       2.0
Itc_pr_ch :      1.0
Fun_eng_ch :     3.0
App_phy_ch :     3.0
App_phy_pr_ch :  1.0
Workshop_ch :    1.0
Ps_ch :          2.0
Isl_ch :         2.0
Cad_ch :         1.0
Lade_ch :        3.0
Lca_ch :        3.0
Lca_pr_ch :      1.0
Caps_ch :      3.0
Pfe_ch :         3.0
Pfe_pr_ch :      1.0
Ena_ch :         3.0
Ena_pr_ch =      1.0
Edc_ch =         3.0
Edc_pr_ch =      1.0
Chi_ch =         0.0
Cal_ch =         3.0
M_cal_ch =       3.0
Ccn_thr_ch =     3.0
Ccn_thr_pr_ch =  1.0
Total_ch =   Itc_ch +  Itc_pr_ch +  Fun_eng_ch + App_phy_ch + App_phy_pr_ch + Workshop_ch + Ps_ch + Isl_ch + Cad_ch + Lade_ch + Lca_ch + Lca_pr_ch + Caps_ch + Pfe_ch + Pfe_pr_ch + Ena_ch + Ena_pr_ch + Edc_ch + Edc_pr_ch + Chi_ch + Cal_ch + M_cal_ch + Ccn_thr_ch + Ccn_thr_pr_ch 

#Gets obtained marks an input
Itc_obt =        float(input("Enter obtained marks of Introduction to Computing"))
Itc_pr_obt =     float(input("Enter obtained marks of Introduction to Computing(PR)"))
Fun_eng_obt =    float(input("Enter obtained marks of Functional English"))
App_phy_obt =    float(input("Enter obtained marks of Applied Physics"))
App_phy_pr_obt = float(input("Enter obtained marks of Applied Physics(PR)"))
Workshop_obt =   float(input("Enter obtained marks of Workshop(PR)"))
Ps_obt =         float(input("Enter obtained marks of Pakistan studies"))
Isl_obt =        float(input("Enter obtained marks of Islamic Studies"))
Cad_obt=         float(input("Enter obtained marks of Computer Added Design"))
Lca_obt =        float(input("Enter obtained marks of linear Circuit Analysis"))
Lca_pr_obt =     float(input("Enter obtained marks of linear Circuit Analysis(PR)"))
Caps_obt =       float(input("Enter obtained marks of Communication and Presentation Skills"))
Lade_obt =       float(input("Enter obtained marks of Linear Algebra and Diffrential Equation"))
Pfe_obt =        float(input("Enter obtained marks of Programming for Engineers"))
Pfe_pr_obt =     float(input("Enter obtained marks of Programming for Engineers(PR)"))
Ena_obt =        float(input("Enter obtained marks of Electrical Network Analysis"))
Ena_pr_obt =     float(input("Enter obtained marks of Electrical Network Analysis(PR)"))
Edc_obt =        float(input("Enter obtained marks of Electronic Devices and Circuits"))
Edc_pr_obt =     float(input("Enter obtained marks of Electronic Devices and Circuits(PR)"))
Chi_obt =        float(input("Enter obtained marks of Introduction to Chinese Language"))
Cal_obt =        float(input("Enter obtained marks of Calculus and Analytical Geometry"))
M_cal_obt =      float(input("Enter obtained marks of Multivariable Calculus"))
Ccn_thr_obt_str =      input("Enter obtained marks of "+ Ccn_thr )
Ccn_thr_obt =    float(Ccn_thr_obt_str)
Ccn_thr_pr_obt_str =      input("Enter obtained marks of "+ Ccn_thr_pr )
Ccn_thr_pr_obt =    float(Ccn_thr_pr_obt_str)

#total marks
Itc_total =        100.0
Itc_pr_total =     50.0
Fun_eng_total =    100.0
App_phy_total =    100.0
App_phy_pr_total = 50.0
Workshop_total =   50.0
Ps_total =         50.0
Isl_total =        50.0
Cad_total =        50.0
Lca_total =        100.0
Lca_pr_total =     50.0
Caps_total =       100.0
Lade_total =       100.0
Pfe_total =        100.0
Pfe_pr_total =     50.0
Ena_total =        100.0
Ena_pr_total =     50.0
Edc_total =        100.0
Edc_pr_total =     50.0
Chi_total =        100.0
Cal_total =        100.0
M_cal_total =      100.0
Ccn_thr_total=     100.0
Ccn_thr_pr_total=  50.0

Total_grades = 0  
#Calculates grade and grade points
Courses = (Itc, Fun_eng, App_phy, Ps, Isl, Lade, Lca, Caps, Pfe, Ena, Edc, Chi, Cal, M_cal, Ccn_thr)
print("Course name             Credit hours     Grade     grade points")  #header or result display
for Course in Courses:
    
    #gets course name from for loop and find obtained and total marks to make calculations
    if Course == Itc:
        Course_obt = Itc_obt
        Course_total = Itc_total 
        Course_ch = Itc_ch
    elif Course == Fun_eng: 
        Course_obt = Fun_eng_obt
        Course_total = Fun_eng_total
        Course_ch = Fun_eng_ch
    elif Course ==App_phy:
        Course_obt = App_phy_obt
        Course_total = App_phy_total
        Course_ch = App_phy_ch
    elif Course == Ps:
        Course_obt = Ps_obt
        Course_total = Ps_total
        Course_ch = Ps_ch
    elif Course == Isl:
        Course_obt = Isl_obt
        Course_total = Isl_total
        Course_ch = Isl_ch
    elif Course == Lca:
        Course_obt = Lca_obt
        Course_total = Lca_total
        Course_ch = Lca_ch
    elif Course == Caps:
        Course_obt = Caps_obt
        Course_total = Caps_total
        Course_ch = Caps_ch
    elif Course == Lade:
        Course_obt = Lade_obt
        Course_total = Lade_total
        Course_ch = Lade_ch
    elif Course ==  Pfe:
        Course_obt =  Pfe_obt
        Course_total =  Pfe_total
        Course_ch = Pfe_ch
    elif Course ==  Ena:
        Course_obt =  Ena_obt
        Course_total =  Ena_total
        Course_ch = Ena_ch
    elif Course ==  Edc:
        Course_obt =  Edc_obt
        Course_total =  Edc_total
        Course_ch = Edc_ch
    elif Course ==  Chi:
        Course_obt =  Chi_obt
        Course_total =  Chi_total
        Course_ch = Chi_ch
    elif Course == Cal:
        Course_obt = Cal_obt
        Course_total = Cal_total
        Course_ch = Cal_ch
    elif Course == M_cal:
        Course_obt = M_cal_obt
        Course_total = M_cal_total
        Course_ch = M_cal_ch
    elif Course == Ccn_thr:
        Course_obt = Ccn_thr_obt
        Course_total = Ccn_thr_total
        Course_ch = Ccn_thr_ch

        
#After geeting course detail, code calculates grade
    Percentage = (Course_obt / Course_total) * 100
    if Percentage>= 92.5:
                Course_grade=4.0 

    elif Percentage>=86.5:
        Course_grade=3.67

    elif Percentage>=81.5 :
        Course_grade=3.33

    elif Percentage>=76.5 :
        Course_grade=3.0

    elif Percentage>=71.5 :
        Course_grade=2.67

    elif Percentage>=67.5 :
        Course_grade=2.33

    elif Percentage>=63.5 :
        Course_grade=2.0

    elif Percentage>=59.5 :
        Course_grade=1.67

    else:
        Course_grade = "0"
    
    Course_grade_point = Course_grade * Course_ch
    Total_grades = Total_grades + float(Course_grade_point)
    print( Course ,"       " , Course_ch ,Course_grade, Course_grade_point)

#grading of practical courses
Courses = (Itc_pr, App_phy_pr, Workshop, Cad, Lca_pr, Pfe_pr, Ena_pr, Edc_pr, Ccn_thr_pr)
print("Course name             Credit hours     Grade     grade points")  #header or result display
for Course in Courses:
    
    #gets course name from for loop and find obtained and total marks to make calculations
    if Course == Itc_pr:
        Course_obt = Itc_pr_obt
        Course_total = Itc_pr_total 
        Course_ch = Itc_pr_ch

    elif Course == App_phy_pr:
        Course_obt = App_phy_pr_obt
        Course_total = App_phy_pr_total
        Course_ch = App_phy_pr_ch
    elif Course == Workshop:
        Course_obt = Workshop_obt
        Course_total = Workshop_total
        Course_ch = Workshop_ch
    elif Course == Cad:
        Course_obt = Cad_obt
        Course_total = Cad_total
        Course_ch = Cad_ch
    elif Course == Lca_pr:
        Course_obt = Lca_pr_obt
        Course_total = Lca_pr_total
        Course_ch = Lca_pr_ch
    elif Course == Pfe_pr:
        Course_obt = Pfe_pr_obt
        Course_total = Pfe_pr_total
        Course_ch = Pfe_pr_ch
    elif Course == Ena_pr:
        Course_obt = Ena_pr_obt
        Course_total = Ena_pr_total
        Course_ch = Ena_pr_ch
    elif Course == Edc_pr:
        Course_obt = Edc_pr_obt
        Course_total = Edc_pr_total
        Course_ch = Edc_pr_ch
    elif Course == Ccn_thr_pr:
        Course_obt = Ccn_thr_pr_obt
        Course_total = Ccn_thr_pr_total
        Course_ch = Ccn_thr_pr_ch

        
#After geeting course detail, code calculates grade
    Percentage = (Course_obt / Course_total) * 100
    if Percentage>= 91:
                Course_grade=4.0 

    elif Percentage>=87:
        Course_grade=3.67

    elif Percentage>=83 :
        Course_grade=3.33

    elif Percentage>=77 :
        Course_grade=3.0

    elif Percentage>=73 :
        Course_grade=2.67

    elif Percentage>=69 :
        Course_grade=2.33

    elif Percentage>=63 :
        Course_grade=2.0

    elif Percentage>=57 :
        Course_grade=1.67

    else:
        Course_grade = "0"
    
    Course_grade_point = Course_grade * Course_ch
    Total_grades = Total_grades + float(Course_grade)
    print( Course ,"       " , Course_ch ,Course_grade, Course_grade_point)           
Cgpa = Total_grades / Total_ch 
print("Your Cgpa is", Cgpa)
