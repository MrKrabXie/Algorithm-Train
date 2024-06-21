def generate_bad_char_table(pattern):
    """
    Generate the bad character table for Boyer-Moore algorithm.

    Args:
    - pattern: The pattern string for which bad character table is to be generated.

    Returns:
    - bad_char: Dictionary mapping each character to the furthest position in the pattern.
               If the character does not appear in the pattern, it maps to -1.
    """
    length = len(pattern)
    bad_char = {}

    # Initialize all occurrences as -1
    for i in range(256):
        bad_char[chr(i)] = -1

    # Fill the actual value of last occurrence of a character
    for i in range(length):
        bad_char[pattern[i]] = i

    return bad_char

def generate_good_suffix_table(pattern):
    """
    Generate the good suffix table for Boyer-Moore algorithm.

    Args:
    - pattern: The pattern string for which good suffix table is to be generated.

    Returns:
    - good_suffix: List where good_suffix[i] is the length of the longest suffix which is also a prefix
                   of pattern[:i+1].
    """
    length = len(pattern)
    good_suffix = [0] * (length + 1)
    suffix = [0] * (length + 1)
    j = length

    for i in range(length - 1, -1, -1):
        while j <= length and pattern[i] != pattern[j - 1]:
            if suffix[j] == 0:
                suffix[j] = j - i - 1
            j = good_suffix[j]
        j -= 1
        good_suffix[i] = j

    j = good_suffix[0]
    for i in range(length):
        if suffix[i + 1] == 0:
            suffix[i + 1] = j
        if i == j:
            j = good_suffix[j]

    return suffix

def boyer_moore_search(text, pattern):
    """
    Search for occurrences of a pattern in a text using Boyer-Moore algorithm.

    Args:
    - text: The text string in which to search.
    - pattern: The pattern string to search for.

    Returns:
    - List of indices where the pattern starts in the text (empty list if not found).
    """
    n = len(text)
    m = len(pattern)
    indices = []

    if m > n:
        return indices

    bad_char = generate_bad_char_table(pattern)
    good_suffix = generate_good_suffix_table(pattern)
    j = 0

    while j <= n - m:
        i = m - 1
        while i >= 0 and pattern[i] == text[j + i]:
            i -= 1
        if i < 0:
            indices.append(j)
            j += good_suffix[0]
        else:
            j += max(good_suffix[i + 1], i - bad_char.get(text[j + i], -1))

    return indices

# Example usage:
text = "ABAAABCDBBABCDDEBCABC"
pattern = "ABC"
indices = boyer_moore_search(text, pattern)
print(f"Pattern found at indices: {indices}")
