class course:
    
    def __init__(self, course):
        self.course = course
        self.name = course['name']
        self.grades = course['grades']
        self.midterm = course.get('midterm', 0)
        self.final = course.get('final', 0)
        self.credits = course['credits']
        self.level = course['level']
        self.letter = self.get_letter(self.get_finalgrade())
        if self.credits < 5:
            self.full_year = False
        else:
            self.full_year = True

    def get_value(self, grade):

        letters = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
        academic = [4.3, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0.7, 0]
        honors = [4.945, 4.6, 4.255, 3.795, 3.45, 3.105, 2.645, 2.3, 1.955, 1.338, 1.15, 0.805, 0]
        advanced = [5.375, 5, 4.625, 4.125, 3.75, 3.375, 2.875, 2.5, 2.125, 1.625, 1.25, 0.875, 0]

        value_index = letters.index(self.get_letter(grade))

        if self.level == 'H':
            return honors[value_index]
        elif self.level == 'AP':
            return advanced[value_index]
        else:
            return academic[value_index]
    
    def get_letter(self, grade):
        letters = ["A", "B", "C", "D", "F"]
        
        if grade >= 100:
            return "A+"
            
        first_digit = int(grade / 10)
        try:
            letter = letters[abs(first_digit - 9)]
        except IndexError:
            return "F"

        while grade > 10:
            grade -= 10

        if grade >= 7.5 and first_digit == 9:
            return letter + "+"
        elif grade >= 9.5:
            letter = letters[letters.index(letter) - 1]
            return letter + "-"
        else:
            if grade < 1.5:
                return letter + "-"
            elif grade >= 5.5 and first_digit != 9:
                return letter + "+"
            return letter
        
    def get_finalgrade(self):
        non_zeros = 0
        total = 0
        
        for grade in self.grades:
            if grade != 0:
                non_zeros += 1
            total += grade
        
        if non_zeros != 0:
            if self.midterm != 0 and self.final != 0:
                if 'labSem' in self.course:
                    if (self.course['labSem'] == "first" or self.course['labSem'] == '1st'):
                        return ((total / non_zeros) * 0.8) + (self.midterm * 0.12) + (self.final * 0.08)
                    
                    elif self.course['labSem'] == "second" or self.course['labSem'] == "2nd":
                        return ((total / non_zeros) * 0.8) + (self.midterm * 0.08) + (self.final * 0.12)
                    
                    return ((total / non_zeros) * 0.8) + (self.midterm * 0.1) + (self.final * 0.1)
                    
                return ((total / non_zeros) * 0.8) + (self.midterm * 0.1) + (self.final * 0.1)
            
            elif self.midterm != 0 and non_zeros == 4:
                return ((total / non_zeros) * (8/9)) + (self.midterm * (1/9))
            
            elif self.midterm != 0 and non_zeros == 3:
                return ((total / non_zeros) * (6/7)) + (self.midterm * (1/7))
            
            elif self.midterm != 0:
                return ((total / non_zeros) * 0.8) + (self.midterm * 0.2)
            
            elif self.final != 0:
                return ((total / non_zeros) * 0.8) + (self.final * 0.2)
            
            return total / non_zeros
        return 0

    def get_gpa(self):
        return self.get_value(self.get_finalgrade()) * self.credits

    def get_quartgpa(self, quarter):
        return self.get_value(self.grades[quarter - 1]) * self.get_quartcredits(quarter)
    
    def get_quartcredits(self, semester):
        if self.full_year == True:
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