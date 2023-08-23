import json
import matplotlib.pyplot as plt
data = []
# Load data from JSON file with multiple objects
with open('students.json', 'r') as file:
    for line in file:
        obj = json.loads(line)
        data.append(obj)
# Extracting student names and their exam scores
student_names = [student['name'] for student in data]
exam_scores = [student['scores'][0]['score'] for student in data]
# Plotting the bar graph
plt.figure(figsize=(16,7))
plt.bar(student_names, exam_scores, label='Exam')
plt.title('Student Exam Scores')
plt.xlabel('Students')
plt.ylabel('Exam Scores')
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



# Extracting quiz scores
quiz_scores = [student['scores'][1]['score'] for student in data]
# Plotting the bar graph for quiz scores
plt.figure(figsize=(16, 6))
plt.bar(student_names, quiz_scores, label='Quiz')
plt.title('Student Quiz Scores')
plt.xlabel('Students')
plt.ylabel('Quiz Scores')
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



# Extracting homework scores
homework_scores = [student['scores'][2]['score'] for student in data]
# Plotting the bar graph for homework scores
plt.figure(figsize=(16, 6))
plt.bar(student_names, homework_scores,label='Homework')
plt.title('Student Homework Scores')
plt.xlabel('Students')
plt.ylabel('Homework Scores')
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()