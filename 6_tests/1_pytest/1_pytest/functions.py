def mnozenie(a, b):
    if not isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return None
    return round(a * b, 8)

