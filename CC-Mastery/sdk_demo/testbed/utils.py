def add(a: int, b: int) -> int:
    return a + b

def greet(name):
    return f"Hello, {name}!"

def parse_csv(filepath):
    with open(filepath) as f:
        return [line.strip().split(",") for line in f]

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))
