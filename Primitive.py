print("================================")

count = 100
count_type = type(count)

print(f"the count: {count}, type: {count_type}")

result1 = count.bit_count()
result2 = count.numerator
print(f"bit count: {result1}, numerator: {result2}")

print("===============string=================")
# Methods: upper(), lower(), title(), capitalize(), isupper(), islower(), istitle(), isalpha(), isdigit(), isspace()

course = " Ai Python full stack"
result = type(course)
print(f"the course: {course}, type: {result}")
result = course.title()
print(f"the course: {course}, type: {result}")
result = course.upper()
print(f"the course: {course}, type: {result}")
result = course.lower()
print(f"the course: {course}, type: {result}")
result = course.capitalize()
print(f"the course: {course}, type: {result}")
result = course.replace("Python", "Java")
print(f"the course: {course}, type: {result}")

print("===============boolean=================")
# functions: bool(), and, or, not, is, is not int() input(), len(), type(), range(), sum(), min(), max()
y = input("Enter a number: ")
print("y", y)
result = y.isnumeric()
print(f"the y: {y}, type: {result}")
# Truthy vs Falsy

test_falsy = ""
print("The FALSY:", bool(test_falsy))
