class Solution:
    # Not Python naming convention but this is the way LeetCode wants the function named
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        sub_start = 0
        substrings = []
        seen_letters = set()

        # Iterates through the string
        i = 0
        while i < len(s):
            # If we see a repeated character, we slice out the relevant
            # substring and start the next possible substring one element
            # to the right of the previous starting point.
            #
            # The index is moved to wherever the next substring will start
            # to be checked, and we forget any letters we've seen for the
            # previous substring.
            if s[i] in seen_letters:
                substrings.append(s[sub_start:i])
                sub_start += 1
                i = sub_start
                seen_letters.clear()
            else:
                seen_letters.add(s[i])
                i += 1

        # If we exit the loop and still have a substring left over,
        # we simply add it to the list.
        if seen_letters:
            substrings.append(s[sub_start:i])

        if substrings:
            return len(max(substrings, key=len))
        else:
            return 0


string = 'dvdf'
print(Solution.lengthOfLongestSubstring(Solution(), string))
