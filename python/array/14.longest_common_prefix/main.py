# def longestCommonPrefix(strs: list[str]) -> str:
#     char_map = {}
#     shortest_word = float("inf")
#     if len(strs) == 1:
#         return strs[0]
#     # take every word in the list
#     for idx, word in enumerate(strs):
#         if len(word) < shortest_word:
#             shortest_word = len(word)
#         # iterate ove each character in the word
#         for i, c in enumerate(word):
#             if idx == 0:
#                 char_map[i] = c
#                 continue  # After adding first word just move to next word
#             if char_map.get(i) != c:
#                 if (
#                     i == 0
#                 ):  # If I is 0 we are at the start of the word and we cant match
#                     return ""
#                 char_map[i] = ""  # remove the entry from the map
#                 break  # If I is not one then we matched on some chars so we just skip to next word
#
#     prefex: list[str] = [""] * len(char_map)
#     for key, value in char_map.items():
#         if value == "" or key >= shortest_word:
#             break
#         prefex[key] = value
#     return "".join(prefex)


def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""

    # Use the first word as the reference
    first_word = strs[0]

    for i in range(len(first_word)):
        char = first_word[i]

        # Check this character against the same index in all other words
        for other_word in strs[1:]:
            # If the other word is shorter than 'i' OR characters don't match
            if i == len(other_word) or other_word[i] != char:
                return first_word[:i]  # Return everything up to this point

    return first_word
