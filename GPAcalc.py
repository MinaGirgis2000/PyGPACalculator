import classes, GPA

preGPA = classes.preGPA
preCredits = classes.preCredits

classes = [GPA.course(classes.class1), GPA.course(classes.class2), GPA.course(classes.class3), GPA.course(classes.class4), 
           GPA.course(classes.class5), GPA.course(classes.class6), GPA.course(classes.class7), GPA.course(classes.class8)]

credits = [0, 0, 0] # [totalCredits, Sem1Credits, Sem2Credits]
GPAs = [0, 0, 0, 0, 0] # [gpa, mp1GPA, mp2GPA, mp3GPA, mp4GPA]

for course in classes:
    GPAs[0] += course.getGPA()

    GPAs[1] += course.getQuartGPA(1)
    GPAs[2] += course.getQuartGPA(2)
    GPAs[3] += course.getQuartGPA(3)
    GPAs[4] += course.getQuartGPA(4)

    credits[0] += course.credits
    credits[1] += course.getQuartCredits(1) # Credits for Quarters 1 & 2 are always the same
    credits[2] += course.getQuartCredits(3) # Credits for Quarters 3 & 4 are always the same

print("\nQUARTER GPA:")
for quarter in range(len(GPAs)):
    if quarter > 0 and quarter < 5:
        print("Quarter", str(quarter), "GPA:", end=" ")
        if quarter < 3:
            print(str(round(GPAs[quarter] / credits[1], 4)))
        else:
            print(str(round(GPAs[quarter] / credits[2], 4)))

print("\nPrevious GPA:", str(preGPA) + 
    "\nThis Year's GPA:", str(round(GPAs[0] / credits[0], 4)) +
    "\nCurrent GPA:", str(round((GPAs[0] + (preGPA * preCredits)) / (credits[0] + preCredits), 4)) +
    "\nTotal Credits:", str(credits[0] + preCredits))

print("\nCLASS\t\t\tGRADES\t\t MP1\t MP2\t MP3\t MP4\t Mid\t Final")
for course in classes:
    print(course.name + ":\t", end="");

    if len(course.name) < 15:
        print("\t", end="");
    
    print(str(format(round(course.getFinalGrade(), 2), '.2f')) + "  " + course.letter, end="")
    
    for quarter in range(0, len(course.grades)):
        if (quarter != len(course.grades) - 1):
            print("\t", str(round(course.grades[quarter], 2)), end="")
    
    print("\t", str(round(course.grades[len(course.grades) - 1], 2)), "\t", str(course.midterm), "\t", str(course.final))
print()
