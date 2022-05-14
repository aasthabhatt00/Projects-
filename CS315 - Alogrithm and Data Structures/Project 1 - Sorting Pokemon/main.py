# Author - Aastha Bhatt
# CS315  - Programming Assignment 1

import math


def to_arr(filename):
    file = open(filename, "r")
    lines = file.readlines()
    list = []

    lines.pop(0)
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")
        lines[i] = lines[i].split(",")
        lines[i][1] = int(lines[i][1])
        list.append(lines[i][1])
    return list


# Runtime Operation Trackers
insertion_sort_runtime = 0
merge_sort_runtime = 0
quick_sort_runtime = 0


# Helper function to print elements of given array
def print_arr(array):
    print(f"The array elements after sorting are: ")
    print("[", end="")
    for i in range(len(array)):
        print(f"{array[i]} ", end="")
    print("]")


def print_runtime(filename, sorting_algorithm, runtime):
    global insertion_sort_runtime, merge_sort_runtime, quick_sort_runtime
    print(
        f"The number of comparisons made while sorting this array (derived from '{filename}') using {sorting_algorithm} is {runtime}."
    )
    insertion_sort_runtime, merge_sort_runtime, quick_sort_runtime = 0, 0, 0
    print()


# Insertion-Sort
def insertion_sort(array):
    global insertion_sort_runtime

    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and key < array[i]:
            insertion_sort_runtime += (
                1  # as a comparison is made every time the loop is entered
            )
            array[i + 1] = array[i]
            i = i - 1
        insertion_sort_runtime += (
            1  # as the loop makes 1 last check before exiting the loop
        )
        array[i + 1] = key


# Merge-Sort
def merge_sort(array, p, r):
    def merge(array, p, q, r):
        # Variable to keep track of comparisons made in Merge Sort
        global merge_sort_runtime

        m = q - p + 1  # length of the top sub-array
        n = r - q  # length of the bottom sub-array
        top_array = []
        bottom_array = []
        for i in range(m):
            top_array.append(array[p + i])
        for j in range(n):
            bottom_array.append(array[q + j + 1])
        top_array.append(999999999)
        bottom_array.append(99999999)
        i = 0
        j = 0
        for k in range(p, r + 1):
            merge_sort_runtime += (
                1  # A comparison is made only every time this loops is entered
            )
            if top_array[i] <= bottom_array[j]:
                array[k] = top_array[i]
                i = i + 1
            else:
                array[k] = bottom_array[j]
                j = j + 1

    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)


# Quick-Sort
def quick_sort(array, p, r):
    def partition(array, p, r):
        global quick_sort_runtime

        x = array[r]
        i = p - 1
        for j in range(p, r):
            quick_sort_runtime += (
                1  # A comparison is made only every time this loops is entered
            )
            if array[j] <= x:
                i = i + 1
                # swap array[i] and array[j]
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

        # swap array[i+1] and array[r-1]
        temp = array[i + 1]
        array[i + 1] = array[r]
        array[r] = temp
        return i + 1

    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)


# Convert all the csv files to their corresponding arrays
sorted_array_s = to_arr("pokemonSortedSmall.csv")
reverse_array_s = to_arr("pokemonReverseSortedSmall.csv")
random_array_s = to_arr("pokemonRandomSmall.csv")

sorted_array_m = to_arr("pokemonSortedMedium.csv")
reverse_array_m = to_arr("pokemonReverseSortedMedium.csv")
random_array_m = to_arr("pokemonRandomMedium.csv")

sorted_array_l = to_arr("pokemonSortedLarge.csv")
reverse_array_l = to_arr("pokemonReverseSortedLarge.csv")
random_array_l = to_arr("pokemonRandomLarge.csv")

# Insertion Sort Array Initialization
i_sorted_array_s = sorted_array_s.copy()
i_reverse_array_s = reverse_array_s.copy()
i_random_array_s = random_array_s.copy()

i_sorted_array_m = sorted_array_m.copy()
i_reverse_array_m = reverse_array_m.copy()
i_random_array_m = random_array_m.copy()

i_sorted_array_l = sorted_array_l.copy()
i_reverse_array_l = reverse_array_l.copy()
i_random_array_l = random_array_l.copy()

# Perform Insertion Sort
print("Insertion Sort Operations:")
insertion_sort(i_sorted_array_s)
print_arr(i_sorted_array_s)
print_runtime("vt.csv", "Insertion Sort", insertion_sort_runtime)

insertion_sort(i_reverse_array_s)
print_arr(i_reverse_array_s)
print_runtime("pokemonReverseSortedSmall.csv", "Insertion Sort", insertion_sort_runtime)

insertion_sort(i_random_array_s)
print_arr(i_random_array_s)
print_runtime("pokemonRandomSmall.csv", "Insertion Sort", insertion_sort_runtime)

insertion_sort(i_sorted_array_m)
print_arr(i_sorted_array_m)
print_runtime("pokemonSortedMedium.csv", "Insertion Sort", insertion_sort_runtime)

insertion_sort(i_reverse_array_m)
print_arr(i_reverse_array_m)
print_runtime(
    "pokemonReverseSortedMedium.csv", "Insertion Sort", insertion_sort_runtime
)

insertion_sort(i_random_array_m)
print_arr(i_random_array_m)
print_runtime("pokemonRandomMedium.csv", "Insertion Sort", insertion_sort_runtime)

insertion_sort(i_sorted_array_l)
print_arr(i_sorted_array_l)
print_runtime("pokemonSortedLarge.csv", "Insertion Sort", insertion_sort_runtime)

insertion_sort(i_reverse_array_l)
print_arr(i_reverse_array_l)
print_runtime("pokemonReverseSortedLarge.csv", "Insertion Sort", insertion_sort_runtime)

insertion_sort(i_random_array_l)
print_arr(i_random_array_l)
print_runtime("pokemonRandomLarge.csv", "Insertion Sort", insertion_sort_runtime)


# Merge Sort Array Initializations
m_sorted_array_s = sorted_array_s.copy()
m_reverse_array_s = reverse_array_s.copy()
m_random_array_s = random_array_s.copy()
m_sorted_array_m = sorted_array_m.copy()
m_reverse_array_m = reverse_array_m.copy()
m_random_array_m = random_array_m.copy()
m_sorted_array_l = sorted_array_l.copy()
m_reverse_array_l = reverse_array_l.copy()
m_random_array_l = random_array_l.copy()

# Perform Merge Sort
print("Merge Sort Operations:")
merge_sort(m_sorted_array_s, 0, len(m_sorted_array_s) - 1)
print_arr(m_sorted_array_s)
print_runtime("pokemonSortedSmall.csv", "Merge Sort", merge_sort_runtime)

merge_sort(m_reverse_array_s, 0, len(m_reverse_array_s) - 1)
print_arr(m_reverse_array_s)
print_runtime("pokemonReverseSortedSmall.csv", "Merge Sort", merge_sort_runtime)

merge_sort(m_random_array_s, 0, len(m_random_array_s) - 1)
print_arr(m_random_array_s)
print_runtime("pokemonRandomSmall.csv", "Merge Sort", merge_sort_runtime)

merge_sort(m_sorted_array_m, 0, len(m_sorted_array_m) - 1)
print_arr(m_sorted_array_m)
print_runtime("pokemonSortedMedium.csv", "Merge Sort", merge_sort_runtime)

merge_sort(m_reverse_array_m, 0, len(m_reverse_array_m) - 1)
print_arr(m_reverse_array_m)
print_runtime("pokemonReverseSortedMedium.csv", "Merge Sort", merge_sort_runtime)

merge_sort(m_random_array_m, 0, len(m_random_array_m) - 1)
print_arr(m_random_array_m)
print_runtime("pokemonRandomMedium.csv", "Merge Sort", merge_sort_runtime)

merge_sort(m_sorted_array_l, 0, len(m_sorted_array_l) - 1)
print_arr(m_sorted_array_l)
print_runtime("pokemonSortedLarge.csv", "Merge Sort", merge_sort_runtime)

merge_sort(m_reverse_array_l, 0, len(m_reverse_array_l) - 1)
print_arr(m_reverse_array_l)
print_runtime("pokemonReverseSortedLarge.csv", "Merge Sort", merge_sort_runtime)

merge_sort(m_random_array_l, 0, len(m_random_array_l) - 1)
print_arr(m_random_array_l)
print_runtime("pokemonRandomLarge.csv", "Merge Sort", merge_sort_runtime)


# Quick Sort Array Initializations
q_sorted_array_s = sorted_array_s.copy()
q_reverse_array_s = reverse_array_s.copy()
q_random_array_s = random_array_s.copy()
q_sorted_array_m = sorted_array_m.copy()
q_reverse_array_m = reverse_array_m.copy()
q_random_array_m = random_array_m.copy()
q_sorted_array_l = sorted_array_l.copy()
q_reverse_array_l = reverse_array_l.copy()
q_random_array_l = random_array_l.copy()

# Perform Quick Sort
print("Quick Sort Operations:")
quick_sort(q_sorted_array_s, 0, len(q_sorted_array_s) - 1)
print_arr(q_sorted_array_s)
print_runtime("pokemonSortedSmall.csv", "QUICK SORT", quick_sort_runtime)

quick_sort(q_reverse_array_s, 0, len(q_reverse_array_s) - 1)
print_arr(q_reverse_array_s)
print_runtime("pokemonReverseSortedSmall.csv", "QUICK SORT", quick_sort_runtime)

quick_sort(q_random_array_s, 0, len(q_random_array_s) - 1)
print_arr(q_random_array_s)
print_runtime("pokemonRandomSmall.csv", "QUICK SORT", quick_sort_runtime)

quick_sort(q_sorted_array_m, 0, len(q_sorted_array_m) - 1)
print_arr(q_sorted_array_m)
print_runtime("pokemonSortedMedium.csv", "QUICK SORT", quick_sort_runtime)

quick_sort(q_reverse_array_m, 0, len(q_reverse_array_m) - 1)
print_arr(q_reverse_array_m)
print_runtime("pokemonReverseSortedMedium.csv", "QUICK SORT", quick_sort_runtime)

quick_sort(q_random_array_m, 0, len(q_random_array_m) - 1)
print_arr(q_random_array_m)
print_runtime("pokemonRandomMedium.csv", "QUICK SORT", quick_sort_runtime)

quick_sort(q_sorted_array_l, 0, len(q_sorted_array_l) - 1)
print_arr(q_sorted_array_l)
print_runtime("pokemonSortedLarge.csv", "QUICK SORT", quick_sort_runtime)

quick_sort(q_reverse_array_l, 0, len(q_reverse_array_l) - 1)
print_arr(q_reverse_array_l)
print_runtime("pokemonReverseSortedLarge.csv", "QUICK SORT", quick_sort_runtime)

quick_sort(q_random_array_l, 0, len(q_random_array_l) - 1)
print_arr(q_random_array_l)
print_runtime("pokemonRandomLarge.csv", "QUICK SORT", quick_sort_runtime)
print("##################################################################")
