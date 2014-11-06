import random

def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = choose_pivot(a)
        a.remove(pivot)
        left = [i for i in a if i < pivot]
        right = [i for i in a if i >= pivot]
        return (quick_sort(left) + [pivot] + quick_sort(right))

def choose_pivot(a):
    return random.choice(a)
