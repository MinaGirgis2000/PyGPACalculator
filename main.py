import my_courses as courses, GPA
from math import ceil

preGPA = courses.preGPA
preCredits = courses.preCredits

seminaries = [GPA.course(courses.class1), GPA.course(courses.class2), GPA.course(courses.class3), GPA.course(courses.class4), 
           GPA.course(courses.class5), GPA.course(courses.class6), GPA.course(courses.class7), GPA.course(courses.class8)]

credits = [0, 0, 0, 0, 0] # [totalCredits, mp1Credits, mp2Credits, mp3Credits, mp4Credits]
GPAs = [0, 0, 0, 0, 0] # [gpa, mp1GPA, mp2GPA, mp3GPA, mp4GPA]

for course in seminaries:
    GPAs[0] += course.get_value(course.get_finalgrade())
    credits[0] += course.credits
    
    for quarter in range(1, len(GPAs)):
        GPAs[quarter] += course.get_value(course.grades[quarter-1])
        if course.grades[quarter-1] != 0:
            if quarter < 3:
                credits[quarter] += course.get_quartcredits(1)
            else:
                credits[quarter] += course.get_quartcredits(2)

print("\nQUARTER GPA:")
for quarter in range(1, len(GPAs)):
    print("Quarter", str(quarter), "GPA:", end=" ")
    try:
        print(str(round(GPAs[quarter] / credits[quarter], 4)))

    except ZeroDivisionError:
        print("0.0000")

print("\nPrevious GPA:", str(preGPA))

try:
    tempGPA, tempCredits = 0, 0
    for quarter in range(1, len(GPAs)):
        if GPAs[quarter] != 0:
            tempGPA += GPAs[quarter]
            tempCredits += credits[quarter]

    print("This Year's GPA:", str(round(tempGPA / tempCredits, 4)) +
          "\nCummulative GPA (Weighted):", str(round((tempGPA + (preGPA * preCredits)) / (tempCredits + preCredits), 4)))

except ZeroDivisionError:
    print("This Year's GPA: 0.0000" +
          "\nCummulative GPA (Weighted): 0.0000")

print("Total Credits:", str(credits[0] + preCredits))

print("\nCLASS\t\t\t|    GRADES\t|  GPA\t|  MP1\t|  MP2\t|  MP3\t|  MP4\t|  Mid\t| Final\t|")
print("------------------------------------------------------------------------------------------------|")

for course in seminaries:
    print(course.name + ":\t", end="");

    if len(course.name) < 15:
        print("\t", end="");
    print("|", end="")
    
    print(str(format(round(course.get_finalgrade(), 2), '.2f')) + "\t   " + course.letter + "\t| " + str(format(round(course.get_value(course.get_finalgrade()), 2), '.2f')), end="")
    
    for quarter in range(0, len(course.grades)):
        if (quarter != len(course.grades) - 1):
            print("\t| ", str(round(course.grades[quarter], 2)), end="")
    
    print("\t| ", str(round(course.grades[len(course.grades) - 1], 2)), "\t| ", str(course.midterm), "\t| ", str(course.final), "\t|")
print("-------------------------------------------------------------------------------------------------\n")
