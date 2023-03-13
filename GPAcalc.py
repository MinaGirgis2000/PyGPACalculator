class course:
    def __init__(self, course):
        self.course = course
        self.name = course['name']
        self.grades = course['grades']
        self.midterm = course.get('midterm', 0)
        self.final = course.get('final', 0)
        self.credits = course['credits']
        self.level = course['level']
        if self.credits < 5:
            self.fullYear = False
        else:
            self.fullYear = True

    def getValue(self, grade):
        value = 0 # F
        if grade >= 97.5 or grade == 'A+': # A+
            if self.level == 'A':
                value = 4.3
            elif self.level == 'H':
                value = 4.945
            elif self.level == 'AP':
                value = 5.375
        elif grade >= 91.5 or grade == 'A': # A
            if self.level == 'A':
                value = 4
            elif self.level == 'H':
                value = 4.6
            elif self.level == 'AP':
                value = 5
        elif grade >= 89.5 or grade == 'A-': # A-
            if self.level == 'A':
                value = 3.7
            elif self.level == 'H':
                value = 4.255
            elif self.level == 'AP':
                value = 4.625
        elif grade >= 85.5 or grade == 'B+': # B+
            if self.level == 'A':
                value = 3.3
            elif self.level == 'H':
                value = 3.795
            elif self.level == 'AP':
                value = 4.125
        elif grade >= 81.5 or grade == 'B': # B
            if self.level == 'A':
                value = 3
            elif self.level == 'H':
                value = 3.45
            elif self.level == 'AP':
                value = 3.75
        elif grade >= 79.5 or grade == 'B-': # B-
            if self.level == 'A':
                value = 2.7
            elif self.level == 'H':
                value = 3.105
            elif self.level == 'AP':
                value = 3.375
        elif grade >= 75.5 or grade == 'C+': # C+
            if self.level == 'A':
                value = 2.3
            elif self.level == 'H':
                value = 2.645
            elif self.level == 'AP':
                value = 2.875
        elif grade >= 71.5 or grade == 'C': # C
            if self.level == 'A':
                value = 2
            elif self.level == 'H':
                value = 2.3
            elif self.level == 'AP':
                value = 2.5
        elif grade >= 69.5 or grade == 'C-': # C-
            if self.level == 'A':
                value = 1.7
            elif self.level == 'H':
                value = 1.955
            elif self.level == 'AP':
                value = 2.125
        elif grade >= 65.5 or grade == 'D+': # D+
            if self.level == 'A':
                value = 1.3
            elif self.level == 'H':
                value = 1.338
            elif self.level == 'AP':
                value = 1.625
        elif grade >= 61.5 or grade == 'D': # D
            if self.level == 'A':
                value = 1
            elif self.level == 'H':
                value = 1.15
            elif self.level == 'AP':
                value = 1.25
        elif grade >= 59.5 or grade == 'D-':  # D-
            if self.level == 'A':
                value = 0.7
            elif self.level == 'H':
                value = 0.805
            elif self.level == 'AP':
                value = 0.875
        else:
            value == 0
        return value

    def getFinalGrade(self):
        nonZeros = 0
        total = 0
        for grade in self.grades:
            if grade != 0:
                nonZeros += 1
            total += grade
        if nonZeros != 0:
            if self.midterm != 0 and self.final != 0:
                if 'labSem' in self.course:
                    if (self.course['labSem'] == "first" or self.course['labSem'] == '1st'):
                        return ((total / nonZeros) * 0.8) + (self.midterm * 0.12) + (self.final * 0.08)
                    elif self.course['labSem'] == "second" or self.course['labSem'] == "2nd":
                        return ((total / nonZeros) * 0.8) + (self.midterm * 0.08) + (self.final * 0.12)
                    else:
                        return ((total / nonZeros) * 0.8) + (self.midterm * 0.1) + (self.final * 0.1)
                return ((total / nonZeros) * 0.8) + (self.midterm * 0.1) + (self.final * 0.1)
            elif self.midterm != 0:
                return ((total / nonZeros) * 0.8) + (self.midterm * 0.2)
            elif self.final != 0:
                return ((total / nonZeros) * 0.8) + (self.final * 0.2)
            else:
                return total / nonZeros
        else:
            return 0

    def getGPA(self):
        return self.getValue(self.getFinalGrade()) * self.credits

    def getQuartGPA(self, quarter):
        if self.fullYear == True:
            if 'labSem' in self.course:
                if ((self.course['labSem'] == "first" or self.course['labSem'] == '1st') and quarter <= 2) or ((self.course['labSem'] == "second" or self.course['labSem'] == '2nd') and quarter >= 3):
                    return self.getValue(self.grades[quarter - 1]) * 2.5
                elif ((self.course['labSem'] == "second" or self.course['labSem'] == '2nd') and quarter >= 3) or ((self.course['labSem'] == "first" or self.course['labSem'] == '1st') and quarter <= 2):
                    return self.getValue(self.grades[quarter - 1]) * 1.25
                else:
                    return self.getValue(self.grades[quarter - 1]) * (self.credits / 4)
            else:
                return self.getValue(self.grades[quarter - 1]) * (self.credits / 4)
        else:
            return self.getValue(self.grades[quarter - 1]) * (self.credits / 2)
    def getQuartCredits(self, semester):
        if self.fullYear == True:
            if 'labSem' in self.course:
                if ((self.course['labSem'] == "first" or self.course['labSem'] == '1st') and semester == 1) or ((self.course['labSem'] == "second" or self.course['labSem'] == '2nd') and semester == 2):
                    return 2.5
                elif ((self.course['labSem'] == "second" or self.course['labSem'] == '2nd') and semester == 1) or ((self.course['labSem'] == "first" or self.course['labSem'] == '1st') and semester == 2):
                    return 1.25
                else:
                    return self.credits / 4
            else:
                return self.credits / 4
        else:
            return self.credits / 2


import classes

preGPA = classes.preGPA
preCredits = classes.preCredits

classes = [course(classes.class1), course(classes.class2), course(classes.class3), course(classes.class4), 
           course(classes.class5), course(classes.class6), course(classes.class7), course(classes.class8)]

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
    
    print(str(round(course.getFinalGrade(), 2)), "\t", end="")
    
    for quarter in range(0, len(course.grades)):
        if (quarter != len(course.grades) - 1):
            print("\t", str(round(course.grades[quarter], 2)), end="")
    
    print("\t", str(round(course.grades[len(course.grades) - 1], 2)), "\t", str(course.midterm), "\t", str(course.final))
print()