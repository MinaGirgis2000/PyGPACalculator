from math import ceil
import courses, GPA

preGPA = courses.preGPA
preCredits = courses.preCredits

seminaries = [GPA.course(courses.class1), GPA.course(courses.class2), GPA.course(courses.class3), GPA.course(courses.class4), 
           GPA.course(courses.class5), GPA.course(courses.class6), GPA.course(courses.class7), GPA.course(courses.class8)]

credits = [0, 0, 0] # [totalCredits, Sem1Credits, Sem2Credits]
GPAs = [0, 0, 0, 0, 0] # [gpa, mp1GPA, mp2GPA, mp3GPA, mp4GPA]

for course in seminaries:
    GPAs[0] += course.get_gpa()

    GPAs[1] += course.get_quartgpa(1)
    GPAs[2] += course.get_quartgpa(2)
    GPAs[3] += course.get_quartgpa(3)
    GPAs[4] += course.get_quartgpa(4)

    credits[0] += course.credits
    credits[1] += course.get_quartcredits(1) # Credits for Quarters 1 & 2 are always the same
    credits[2] += course.get_quartcredits(3) # Credits for Quarters 3 & 4 are always the same

print("\nQUARTER GPA:")
for quarter in range(1, len(GPAs)):
    print("Quarter", str(quarter), "GPA:", end=" ")
    if quarter < 3:
        try:
            print(str(round(GPAs[quarter] / credits[1], 4)))

        except ZeroDivisionError:
            print("0.0000")
    else:
        try:
            print(str(round(GPAs[quarter] / credits[2], 4)))

        except ZeroDivisionError:
            print("0.0000")

print("\nPrevious GPA:", str(preGPA))

try:
    tempGPA, tempCredits = 0, 0
    for quarter in range(1, len(GPAs)):
        if GPAs[quarter] != 0:
            tempGPA += GPAs[quarter] * credits[ceil(quarter/2)]
            tempCredits += credits[ceil(quarter/2)]
    tempGPA /= tempCredits

    print("This Year's GPA:", str(round(tempGPA / tempCredits, 4)) +
          "\nCurrent GPA:", str(round((tempGPA + (preGPA * preCredits)) / (tempCredits + preCredits), 4)))

except ZeroDivisionError:
    print("This Year's GPA: 0.0000" +
          "\nCurrent GPA: 0.0000")

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
