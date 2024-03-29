# PyGPACalculator
This is a GPA Calculator which is a command-line tool that allows users to calculate their grade point average (GPA) based on their course grades and credit hours. The tool is designed to be user-friendly and easy to use.

At its core, this GPA Calculator is a Python script that takes input from the user (currently through a file) and performs the necessary calculations to determine their GPA. The user inputs their course grades and credit hours, and the script calculates their weighted average and displays their GPA on the terminal.

### To run the script:
- Open terminal
- Make sure you have python installed by runnning:
``` bash
python -V
```
- Access the folder where you have downloaded the script using the following command
  - You can also use your file manager to copy and paste the file location from the address bar
``` bash
cd <path to file>
```
- Run:
``` bash
python main.py
```

# DIRECTIONS:
### Previous GPA and Credits
In courses.py, you will find:
``` python
preGPA = 0
preCredits = 0
```
Set the values of those variables to the value of your previous GPA and credits from your classes from your previous school years.
- If you were not in High School last year then this does not apply to you, leave it as 0

### Class Information
In courses.py, you will also find:
``` python
class0 = {'name': "example-Name0",
          'credits': 0,
          'level': 'A',
          'grades': [0, 0, 0, 0],
          'midterm': 0,
          'final': 0,
          'labSem': "none"  # <-- Can delete from template or leave as "none" if not applicable for your class.
          } 
```
#### PLEASE REFRAIN FROM CHANGING THE DICTIONARY NAMES FOR ANY OF THE CLASS TEMPLATES

Please fill out the following for each class:
- name: name of the course
- credits: credit value of the course
- level: course level
  - "A": Academic
  - "H": Honors
  - "AP": Advanced Placement
- grades: all grades from marking periods 1 to 4:
  - [mp1, mp2, mp3, mp4]
- midterm: midterm grade
- final: final grade
- labSem: lab class (if applicable)
  - "1st" or "first": 1st semester lab class
  - "2nd" or "second": 2nd semester lab class
  - "both": both semesters lab classes
  - Note: Any other string will be considered as no lab class

### Including More Than 8 Classes
- Copy the dictionary template of another class (shown above)
- Go into courses.py
  - Paste the template
  - Change the variable name for your new class
    - Ex: class9, class10, newClass, etc.
- Go into main.py
  - Add "GPA.course(courses.(name of variable))" into the seminaries array on line 6
  - Ex: GPA.course(courses.class9)
``` python
seminaries = [GPA.course(courses.class1), GPA.course(courses.class2), GPA.course(courses.class3), GPA.course(courses.class4), 
           GPA.course(courses.class5), GPA.course(courses.class6), GPA.course(courses.class7), GPA.course(courses.class8), GPA.course(courses.class9)
           # , GPA.course(courses.(name of variable))
           ]
```

# WARNING:
- DO NOT CHANGE ANY DICTIONARY NAMES FOR THE CLASS TEMPLATES
- I do not gaurantee that this will give you your actual GPA. However this method was successfully tested and compared with past GPA scores.
- I am not responsible for any problems that may occur from this program, such as with other people or with the computer that the program was run on.
  - The only purpose of this program is to get your approximate current GPA in a more easier and efficient way.
- This is still a work in progress, so nothing is guaranteed