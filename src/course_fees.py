courses = {
    "Python": 5000,
    "Git": 3000,
    "SQL": 4000
}


def get_course_price(course_name):
    normalized_name = course_name.strip().lower()
    for name, price in courses.items():
        if name.lower() == normalized_name:
            return price
    return None


def calculate_discount(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        return "Invalid discount."
    discount_amount = price * discount_percent / 100
    return price - discount_amount


def calculate_course_fee(course_name, discount_percent=0):
    price = get_course_price(course_name)

    if price is None:
        return "Course not found."

    return calculate_discount(price, discount_percent)