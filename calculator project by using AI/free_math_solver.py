import re

def solve_query(query):
    query = query.lower()

    # Percentage: "What is 25% of 640?"
    percent_match = re.search(r"(\d+(\.\d+)?)\s*%\s*of\s*(\d+(\.\d+)?)", query)
    if percent_match:
        percent = float(percent_match.group(1))
        value = float(percent_match.group(3))
        result = (percent / 100) * value
        return f"{percent}% of {value} is {result}"

    # Add: "Add 45 and 67"
    add_match = re.search(r"add\s+(\d+(\.\d+)?)\s+and\s+(\d+(\.\d+)?)", query)
    if add_match:
        a = float(add_match.group(1))
        b = float(add_match.group(3))
        return f"The sum of {a} and {b} is {a + b}"

    # Subtract: "Subtract 30 from 100"
    sub_match = re.search(r"subtract\s+(\d+(\.\d+)?)\s+from\s+(\d+(\.\d+)?)", query)
    if sub_match:
        a = float(sub_match.group(3))
        b = float(sub_match.group(1))
        return f"{a} minus {b} is {a - b}"

    # Multiply: "Multiply 8 and 5"
    mul_match = re.search(r"multiply\s+(\d+(\.\d+)?)\s+(and|by)\s+(\d+(\.\d+)?)", query)
    if mul_match:
        a = float(mul_match.group(1))
        b = float(mul_match.group(4))
        return f"The product of {a} and {b} is {a * b}"

    # Divide: "Divide 100 by 4"
    div_match = re.search(r"divide\s+(\d+(\.\d+)?)\s+by\s+(\d+(\.\d+)?)", query)
    if div_match:
        a = float(div_match.group(1))
        b = float(div_match.group(3))
        if b == 0:
            return "Cannot divide by zero"
        return f"{a} divided by {b} is {a / b}"

    return "Sorry, I couldn't understand the question. Try using basic math terms."
