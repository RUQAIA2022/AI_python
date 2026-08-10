students = [
    {
        "name": "Lara",
        "age": 23,
        "track": "AI",
        "hours_studied": 40,
        "scores": [85, 90, 78]
    },
    {
        "name": "Omar",
        "age": 31,
        "track": "Data",
        "hours_studied": 12,
        "scores": [60, 55, 70]
    },
    {
        "name": "Rim",
        "age": 27,
        "track": "AI",
        "hours_studied": 55,
        "scores": [95, 88, 92]
    },
    {
        "name": "Karim",
        "age": 19,
        "track": "Web",
        "hours_studied": 8,
        "scores": [50, 65, 40]
    },
    {
        "name": "Nour",
        "age": 25,
        "track": "AI",
        "hours_studied": 30,
        "scores": [75, 80, 85]
    },
    {
        "name": "Sami",
        "age": 35,
        "track": "Data",
        "hours_studied": 48,
        "scores": [88, 91, 79]
    }
]

# Part 1: Exploring the Data

# 1. Print the name of the first student and the last student
print(students[0]["name"])
print(students[-1]["name"])


# 2. Print Rim's scores
for student in students:
    if student["name"] == "Rim":
        print(student["scores"])


# 3. Print one line for each student
for student in students:
    print(student["name"], "is", student["age"], "years old and studies", student["track"])        


# Part 2: Filtering

# 4. Create a list of students in the AI track
ai_students = []

for student in students:
    if student["track"] == "AI":
        ai_students.append(student)

print(len(ai_students))


# 5.  using list comprehension
ai_students_comprehension = [student for student in students if student["track"] == "AI"]

print(ai_students_comprehension)
print(ai_students == ai_students_comprehension)

# 6. Names of students who studied more than 30 hours
students_over_30 = [student["name"] for student in students if student["hours_studied"] > 30]

print(students_over_30)

# 7. Students older than 24 and in the AI track
older_ai_students = [student for student in students if student["age"] > 24 and student["track"] == "AI"]

print(older_ai_students)




# Part 3: Aggregating

# 8. Calculate the average age of all students
total_age = 0

for student in students:
    total_age += student["age"]

average_age = total_age / len(students)

print(average_age)


# 9. Calculate the total hours studied
total_hours = 0

for student in students:
    total_hours = total_hours + student["hours_studied"]

print(total_hours)


# 10. Find the student who studied the most hours

max_hours = 0
top_student = ""

for student in students:
    if student["hours_studied"] > max_hours:
        max_hours = student["hours_studied"]
        top_student = student["name"]

print(top_student, max_hours)


# 11. Calculate the final grade for each student

for student in students:
    total_score = 0

    for score in student["scores"]:
        total_score = total_score + score

    final_grade = total_score / len(student["scores"])

    print(student["name"], round(final_grade, 1))

    # Part 4: Transforming

# 12. Create a new list with name and average score

student_results = [
    {
        "name": student["name"],
        "average_score": sum(student["scores"]) / len(student["scores"])
    }
    for student in students
]

print(student_results)


# 13. Count the number of students in each track

track_counts = {}

for student in students:
    track = student["track"]

    if track in track_counts:
        track_counts[track] = track_counts[track] + 1
    else:
        track_counts[track] = 1

print(track_counts)


# 14. Create a set of all unique tracks

unique_tracks = set()

for student in students:
    unique_tracks.add(student["track"])

# A set is used because it does not allow duplicate values
print(unique_tracks)


# Part 5: Reusable Functions

# 15. Filter students by track

def filter_by_track(students, track):
    filtered_students = []

    for student in students:
        if student["track"] == track:
            filtered_students.append(student)

    return filtered_students


print(filter_by_track(students, "AI"))
print(filter_by_track(students, "Data"))

# 16. Calculate average score using a function

def average_score(student):
    total = 0

    for score in student["scores"]:
        total = total + score

    average = total / len(student["scores"])

    return average


for student in students:
    print(student["name"], round(average_score(student), 1))


 # 17. Find the student with the highest average score

def top_student(students):
    highest_average = 0
    top_name = ""

    for student in students:
        average = average_score(student)

        if average > highest_average:
            highest_average = average
            top_name = student["name"]

    return top_name


print(top_student(students))   

# 18. Create a summary of the students

def summary(students):
    total_students = len(students)

    total_age = 0
    tracks = set()

    for student in students:
        total_age = total_age + student["age"]
        tracks.add(student["track"])

    average_age = total_age / total_students

    result = {
        "total_students": total_students,
        "average_age": average_age,
        "tracks": tracks
    }

    return result

print(summary(students))

# 19. Mini Data Pipeline

def report(students, min_hours):
    filtered_students = []

    for student in students:
        if student["hours_studied"] >= min_hours:
            filtered_students.append(student)

    results = []

    for student in filtered_students:
        result = {
            "name": student["name"],
            "average_score": average_score(student)
        }
        results.append(result)

    results.sort(key=lambda student: student["average_score"], reverse=True)

    return results


print(report(students, 30))

