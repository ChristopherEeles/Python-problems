"""
Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.

Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String = BANANA

Kevin's vowel beginning word = ANA

Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


Solution:
Solving this requires we notice the pattern that the number
of occurences of substrings of a word is equal to the length of the
word minus the index of the character.

For example, for BANANA:
B
BA
BAN
BANA
BANAN
BANANA
6 words therefore score of 6, len(BANANA) - index of B = 6 - 0 = 6
A
AN
ANA
ANAN
ANANA
5 words therefore score of 5, len(BANANA) - index of A = 6 - 1 = 5

This continues pattern continues for the whole string, therefore we can
solve this in O(N)
"""

VOWELS = tuple("AEIOU")
P1 = "Kevin"
P2 = "Stuart"

def minion_game(s):
    p1 = 0
    p2 = 0
    l = len(s)
    for i in range(l):
        if s[i] in VOWELS:
            p1 += (l - i)
        else:
            p2 += (l - i)
    if (p1 == p2):
        print("Draw")
    else:
        print((f"{P1} {p1}", f"{P2} {p2}")[p2 > p1])


if __name__ == "__main__":
    main()
