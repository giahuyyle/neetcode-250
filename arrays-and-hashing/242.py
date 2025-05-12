"""
PROBLEM 242 - Valid Anagram
Given two strings s and t, return true if t is an anagram of s and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Input: s = "anagram", t = "nagaram"
Output: true
"""

from typing import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
"""
Time Complexity: O(n) - as we are iterating through both strings to count the frequency of each character.
Space Complexity: O(n)
Where n is the length of the input strings.
"""