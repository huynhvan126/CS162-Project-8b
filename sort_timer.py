# Author: Van Huynh
# GitHub username: huynhvan126
# Date: 11/20/2024
# Description: Write a function called compare_sorts that takes the two decorated sort functions as parameters.
import time
import random
from matplotlib import pyplot as plt
from functools import wraps

def sort_timer(func):
    """Decorate a function to be used as a timer decorator."""
    @wraps(func)
    def wrapper(lst):
        start_time = time.perf_counter()
        func(lst)
        end_time = time.perf_counter()
        return end_time - start_time
    return wrapper

@sort_timer
def bubble_sort(lst):
    """Bubble sort implementation."""
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

@sort_timer
def insertion_sort(lst):
    """Insertion sort implementation."""
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

def make_lists_of_sort_times(sort_func1, sort_func2, lengths):
    """Makes lists of sort times for two sorting algorithms over varying lengths."""
    times1, times2 = [], []
    for length in lengths:
        lst = [random.randint(1, 10000) for _ in range(length)]
        lst_copy = list(lst)
        times1.append(sort_func1(lst))
        times2.append(sort_func2(lst_copy))
    return times1, times2

def compare_sorts(sort_func1, sort_func2):
    """Compares two sorting algorithms over varying lengths."""
    lengths = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    times1, times2 = make_lists_of_sort_times(sort_func1, sort_func2, lengths)

    plt.plot(lengths, times1, 'ro--', linewidth=2, label='Bubble Sort')
    plt.plot(lengths, times2, 'go--', linewidth=2, label='Insertion Sort')
    plt.xlabel('Number of Elements Being Sorted')
    plt.ylabel('Time (Seconds)')
    plt.legend(loc='upper left')
    plt.title('Sorting Algorithm Performance')
    plt.show()

def main():
    """Main function to compare the performance of the bubble sort and insertion sort."""
    compare_sorts(bubble_sort, insertion_sort)

if __name__ == '__main__':
    main()
