def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    start = 0

    for right in range(len(s)):
        # Slide the left pointer if there's a repeating character
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        # Add the current character to the set and update max_length if needed
        char_set.add(s[right])
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start = left

    return s[start:start + max_length]


# Example usage
s = "Plantations"
print(longest_unique_substring(s))  # Output: "abc"
