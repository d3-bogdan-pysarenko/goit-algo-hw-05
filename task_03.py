import timeit

# ------ KMP ------
def kmp_search(text, pattern):
    if not pattern:
        return 0
    lps = [0] * len(pattern)
    j = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1

    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            return i - j
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


# ------ Рабін–Карп ------
def rabin_karp(text, pattern):
    if not pattern:
        return 0

    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    h = pow(d, m-1) % q

    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1


# ------ Боєр–Мур ------
def boyer_moore(text, pattern):
    if not pattern:
        return 0

    skip = {}
    m = len(pattern)
    n = len(text)

    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1

    i = m - 1
    while i < n:
        j = m - 1
        k = i
        while j >= 0 and text[k] == pattern[j]:
            k -= 1
            j -= 1
        if j < 0:
            return k + 1
        i += skip.get(text[i], m)
    return -1


# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

file1 = "article1.txt"
file2 = "article2.txt"

with open(file1, "r", encoding="utf-8") as f:
    text1 = f.read()

with open(file2, "r", encoding="utf-8") as f:
    text2 = f.read()


# Existing case
real_substring = "Література"
# Unreal case
fake_substring = "Літературна"
testing_times = 1000 # how many times to run

def measure(text, pattern):
    print(f"\n--- Searching for: '{pattern}' ---")

    print("KMP:        ", timeit.timeit(lambda: kmp_search(text, pattern), number=testing_times))
    print("Rabin-Karp: ", timeit.timeit(lambda: rabin_karp(text, pattern), number=testing_times))
    print("Boyer-Moore:", timeit.timeit(lambda: boyer_moore(text, pattern), number=testing_times))


# Checking time
# ----------------------------------------------------------------------------------------
print("=== Articles measurement time for EXISTING substring ===")
measure(text1, real_substring)
measure(text2, real_substring)

print("\n=== Articles measurement time for NON-existing substring ===")
measure(text1, fake_substring)
measure(text2, fake_substring)
