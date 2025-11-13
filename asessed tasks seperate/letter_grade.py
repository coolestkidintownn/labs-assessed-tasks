def letter_grade(dataInput):
    creditTotal = 0
    total = 0
    average = 0 
    grade = 0

    for i in dataInput:
        total = total + (i["score"] * i["credits"])
        creditTotal = creditTotal + i["credits"]

    average = total / creditTotal    
    
    if average < 50:
        grade = "F"
    elif average <= 60:
        grade = "D"
    elif average <= 70:
        grade = "C"
    elif average <= 90:
        grade = "B"
    else:
        grade = "A"

    return average, grade


data_input = [
    {"subject": "Math", "score": 90, "credits": 40},
    {"subject": "History", "score": 75, "credits": 20},
    {"subject": "English", "score": 60, "credits": 20},
    {"subject": "Science", "score": 85, "credits": 40},
    {"subject": "Art", "score": 50, "credits": 40}
]


#print(data_input[1]["subject"])
#print(len(data_input))

average, grade = letter_grade(data_input)

print("average:", average)
print("grade:", grade)