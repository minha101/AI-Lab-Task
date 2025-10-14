

def apply_operator(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

def evaluate(expression):
    numbers = []   
    operators = []
    i = 0

    while i < len(expression):
        ch = expression[i]

        # for space
        if ch == ' ':
            i += 1
            continue

        # for digit
        if ch.isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = val * 10 + int(expression[i])
                i += 1
            numbers.append(val)
            continue

        # for operator
        if ch in "+-*/":
            operators.append(ch)

        i += 1
    result = numbers[0]
    for j in range(len(operators)):
        result = apply_operator(result, numbers[j+1], operators[j])

    return result


print("=== Simple Dynamic Calculator ===")
expr = input("Enter expression (e.g., 10+5-3*2/2): ")

try:
    ans = evaluate(expr)
    print("Result =", ans)
except Exception as e:
    print("Error:", e)