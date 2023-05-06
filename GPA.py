class course:
    def __init__(self, course):
        self.course = course
        self.name = course['name']
        self.grades = course['grades']
        self.midterm = course.get('midterm', 0)
        self.final = course.get('final', 0)
        self.credits = course['credits']
        self.level = course['level']
        self.letter = self.getLetter()
        if self.credits < 5:
            self.fullYear = False
        else:
            self.fullYear = True

    def getValue(self, grade):
        value = 0 # F
        if grade >= 97.5: # A+
            if self.level == 'A':
                value = 4.3
            elif self.level == 'H':
                value = 4.945
            elif self.level == 'AP':
                value = 5.375
        elif grade >= 91.5: # A
            if self.level == 'A':
                value = 4
            elif self.level == 'H':
                value = 4.6
            elif self.level == 'AP':
                value = 5
        elif grade >= 89.5: # A-
            if self.level == 'A':
                value = 3.7
            elif self.level == 'H':
                value = 4.255
            elif self.level == 'AP':
                value = 4.625
        elif grade >= 85.5: # B+
            if self.level == 'A':
                value = 3.3
            elif self.level == 'H':
                value = 3.795
            elif self.level == 'AP':
                value = 4.125
        elif grade >= 81.5: # B
            if self.level == 'A':
                value = 3
            elif self.level == 'H':
                value = 3.45
            elif self.level == 'AP':
                value = 3.75
        elif grade >= 79.5: # B-
            if self.level == 'A':
                value = 2.7
            elif self.level == 'H':
                value = 3.105
            elif self.level == 'AP':
                value = 3.375
        elif grade >= 75.5: # C+
            if self.level == 'A':
                value = 2.3
            elif self.level == 'H':
                value = 2.645
            elif self.level == 'AP':
                value = 2.875
        elif grade >= 71.5: # C
            if self.level == 'A':
                value = 2
            elif self.level == 'H':
                value = 2.3
            elif self.level == 'AP':
                value = 2.5
        elif grade >= 69.5: # C-
            if self.level == 'A':
                value = 1.7
            elif self.level == 'H':
                value = 1.955
            elif self.level == 'AP':
                value = 2.125
        elif grade >= 65.5: # D+
            if self.level == 'A':
                value = 1.3
            elif self.level == 'H':
                value = 1.338
            elif self.level == 'AP':
                value = 1.625
        elif grade >= 61.5: # D
            if self.level == 'A':
                value = 1
            elif self.level == 'H':
                value = 1.15
            elif self.level == 'AP':
                value = 1.25
        elif grade >= 59.5:  # D-
            if self.level == 'A':
                value = 0.7
            elif self.level == 'H':
                value = 0.805
            elif self.level == 'AP':
                value = 0.875
        return value
    
    def getLetter(self):
        grade = self.getFinalGrade()
        letters = ["A", "B", "C", "D"]
        
        firstDigit = int(grade / 10)
        if (grade >= 60):
            letter = letters[abs(firstDigit - 9)]
        else:
            return "F";

        while grade >= 10:
            grade -= 10

        if grade >= 7.5 and firstDigit == 9:
            return letter + "+"
        elif grade >= 9.5:
            letter = letters[letters.index(letter) - 1]
            return letter + "-"
        elif letter != "F":
            if grade <= 1.5:
                return letter + "-"
            elif grade >= 5.5:
                return letter + "+"
        
        return letter

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