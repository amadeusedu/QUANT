from __future__ import annotations
import random

def gen_mental_math() -> dict[str, object]:
    a,b = random.randint(12,99), random.randint(11,89)
    return {"prompt": f"Compute {a} * {b}", "answer": str(a*b), "difficulty": 1.0, "tags": ["arithmetic"]}

def gen_probability() -> dict[str, object]:
    p = random.choice([0.2,0.3,0.4])
    return {"prompt": f"If P(A)={p} and P(B|A)=0.5, find P(A and B).", "answer": f"{p*0.5:.2f}", "difficulty": 1.2, "tags": ["conditional"]}

def gen_stats() -> dict[str, object]:
    n = random.choice([25,36,49,64])
    return {"prompt": f"What is sqrt({n})?", "answer": str(int(n**0.5)), "difficulty": 0.8, "tags": ["inference"]}

def gen_coding() -> dict[str, object]:
    return {"prompt": "Write a function that returns unique sorted values from a list.", "answer": "sorted(set(xs))", "difficulty": 1.1, "tags": ["python"]}
