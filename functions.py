# =========================================================
# 22. LOCAL SCOPE
# =========================================================

def local_example():

    local_message = "I am local"

    print(local_message)


local_example()


# local_message faqat function ichida mavjud


# Agar buni yozsak error beradi:
#
# print(local_message)
#
# NameError


# =========================================================
# 23. GLOBAL VA LOCAL BIRGA
# =========================================================

country = "Uzbekistan"


def person_information():

    name = "Mike"

    age = 24

    print("Name:", name)

    print("Age:", age)

    print("Country:", country)


person_information()


print("Country:", country)


# country -> global
# name -> local
# age -> local


# =========================================================
# 24. GLOBAL VA LOCAL VARIABLE BIR XIL NOMDA
# =========================================================

name = "Mike"


def test():

    name = "Mike"

    print("Inside function:", name)


test()


print("Outside function:", name)


# Natija:
#
# Inside function: Bilol
# Outside function: Mike


# =========================================================
# 25. GLOBAL KEYWORD
# =========================================================

count = 0


def increase():

    global count

    count = count + 1


increase()

increase()

increase()


print("Count:", count)


# Natija:
# Count: 3


# =========================================================
# 26. FUNCTIONDAN BOOLEAN QAYTARISH
# =========================================================

def is_adult(age):

    if age >= 18:
        return True

    else:
        return False


print(is_adult(20))

print(is_adult(15))


# =========================================================
# 27. PASSWORD CHECK FUNCTION
# =========================================================

def check_password(password):

    if len(password) >= 8:
        return "Strong password"

    else:
        return "Weak password"


print(check_password("python123"))

print(check_password("abc"))


# =========================================================
# 28. LOGIN FUNCTION
# =========================================================

def login(username, password):

    correct_username = "admin"

    correct_password = "12345"

    if (
        username == correct_username
        and password == correct_password
    ):

        return "Login successful"

    else:

        return "Login failed"


print(login("admin", "12345"))

print(login("user", "11111"))


# =========================================================
# 29. FUNCTION ICHIDAN BOSHQA FUNCTIONNI CALL QILISH
# =========================================================

def get_name():

    return "Bilolbek"


def welcome_user():

    name = get_name()

    print("Welcome", name)


welcome_user()


# =========================================================
# 30. REAL LIFE EXAMPLE
# PRODUCT CALCULATION
# =========================================================

def calculate_product(
    product,
    price,
    amount,
    discount=0
):

    total = price * amount

    discount_price = (
        total * discount / 100
    )

    final_price = (
        total - discount_price
    )

    print("Product:", product)

    print("Price:", price)

    print("Amount:", amount)

    print("Discount:", discount, "%")

    print("Final price:", final_price)


calculate_product(
    product="iPhone",
    price=1000,
    amount=2,
    discount=10
)


# =========================================================
# 31. FINAL EXAMPLE
# PARAMETER + DEFAULT + KEYWORD + RETURN + SCOPE
# =========================================================

school = "Python Academy"


def student_result(
    name,
    score,
    country="Uzbekistan"
):

    # Local variable
    status = ""

    if score >= 60:

        status = "Passed"

    else:

        status = "Failed"

    print("----------------")

    print("School:", school)

    print("Student:", name)

    print("Country:", country)

    print("Score:", score)

    print("Result:", status)

    print("----------------")


student_result(
    name="Mike",
    score=85
)


student_result(
    name="Mike",
    score=55,
    country="Korea"
)
