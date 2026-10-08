# Task 7: Strings & Collections

# ---------- Strings ----------
print("===== STRING OPERATIONS =====")
text = "Python for Data Analytics"
print("Original :", text)
print("upper()  :", text.upper())
print("lower()  :", text.lower())
print("replace():", text.replace("Python", "SQL"))
print("find()   :", text.find("Data"), "(index of 'Data')")

# ---------- Lists ----------
print("\n===== LIST OPERATIONS =====")
subjects = ["Python", "SQL", "Excel"]
print("Original :", subjects)
subjects.append("Power BI")
print("append() :", subjects)
subjects.remove("Excel")
print("remove() :", subjects)
subjects.sort()
print("sort()   :", subjects)

# ---------- Tuples ----------
print("\n===== TUPLE =====")
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
print("Tuple      :", days)
print("days[0]    :", days[0])
print("days[-1]   :", days[-1])
print("days[1:3]  :", days[1:3])

# ---------- Dictionary ----------
print("\n===== DICTIONARY =====")
student = {
    "name": "Deepanshu",
    "college": "University of Delhi",
    "course": "B.A. Economics",
    "year": 2024,
}
print("Student  :", student)
print("Name     :", student["name"])
student["city"] = "Delhi"
print("Updated  :", student)

# ---------- Sets ----------
print("\n===== SET OPERATIONS =====")
skills = {"Python", "SQL", "Excel"}
print("Original :", skills)
skills.add("Tableau")
print("add()    :", skills)
skills.remove("Excel")
print("remove() :", skills)
