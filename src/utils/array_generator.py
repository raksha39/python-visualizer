def generate_random_array(size, min_value=1, max_value=100):
    import random
    return [random.randint(min_value, max_value) for _ in range(size)]

def generate_sorted_array(size):
    return list(range(1, size + 1))

def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))