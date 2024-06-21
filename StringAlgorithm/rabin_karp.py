def rabin_karp_search(text, pattern):
    """
    Search for occurrences of a pattern in a text using Rabin-Karp algorithm.

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

    # Define prime number for the hash function and a large constant
    prime = 101  # A prime number
    d = 256  # Number of characters in the input alphabet (ASCII characters)

    # Calculate hash value for pattern and the first window of text
    pattern_hash = 0
    text_hash = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % prime
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime

    # Slide the pattern over the text one by one
    for i in range(n - m + 1):
        # Check if the hash values match
        if pattern_hash == text_hash:
            # Check if all characters match
            match = True
            for j in range(m):
                if pattern[j] != text[i + j]:
                    match = False
                    break
            if match:
                indices.append(i)

        # Calculate hash value for next window of text: remove leading digit,
        # add trailing digit
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime

    return indices

# Example usage:
text = "AABAACAADAABAABA"
pattern = "AABA"
indices = rabin_karp_search(text, pattern)
print(f"Pattern found at indices: {indices}")
