# importing json
import json

# Getting user input for the name, id, course
name = input("Enter student name: ")
student_id = input("Enter student ID: ")
course = input("Enter student course: ")

# Creating dictionary
student_info = {
    "Name": name,
    "ID": student_id,
    "course": course
}

# Writing to JSON file
with open('StudentJson.json', 'w') as json_file:  # file created by name of StudentJson.json
    json.dump(student_info, json_file)


# Read from the JSON file
with open('StudentJson.json', 'r') as json_file:
    student_data = json.load(json_file)

# Append additional details as given in the question
student_data["CourseDetails"] = {
    "Group": "A",
    "Year": 2
}

# Update the JSON file
with open('StudentJson.json', 'w') as json_file:
    json.dump(student_data, json_file)


# Read the updated JSON file
with open('StudentJson.json', 'r') as json_file:
    student_data = json.load(json_file)

# Display the output by displaying individual values
print("Details of the Student are")
print("\tName:", student_data["Name"])
print("\tID:", student_data["ID"])
print("\tcourse:", student_data["course"])
print("\tGroup:", student_data["CourseDetails"]["Group"])
print("\tYear:", student_data["CourseDetails"]["Year"])

