def compute_lps(pattern):
    """
    Compute the longest prefix which is also suffix (lps) array for KMP algorithm.

    Args:
    - pattern: The pattern string for which lps array is to be computed.

    Returns:
    - lps: The lps array.
    """
    length = len(pattern)
    lps = [0] * length
    j = 0  # length of previous longest prefix suffix

    i = 1
    while i < length:
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

    return lps

def kmp_search(text, pattern):
    """
    Search for occurrences of a pattern in a text using KMP algorithm.

    Args:
    - text: The text string in which to search.
    - pattern: The pattern string to search for.

    Returns:
    - List of indices where the pattern starts in the text (empty list if not found).
    """
    if not pattern:
        return []

    lps = compute_lps(pattern)
    n = len(text)
    m = len(pattern)
    indices = []

    i = 0  # index for text[]
    j = 0  # index for pattern[]
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            indices.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices

# Example usage:
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
indices = kmp_search(text, pattern)
print(f"Pattern found at indices: {indices}")
