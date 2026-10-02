from src.calculator import add

# Ganerate random numbers for testing
import random
random.seed(0)  # Set seed for reproducibility
def random_test_add():
    for _ in range(10):
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)
        assert add(a, b) == a + b

