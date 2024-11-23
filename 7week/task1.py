"""
https://leetcode.com/problems/repeated-dna-sequences/description/?envType=problem-list-v2&envId=sliding-window
"""

from collections import Counter
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, dna_sequence: str) -> List[str]:
        sequence_count = Counter()
        repeated_sequences = []
        num_substrings = len(dna_sequence) - 10
        for i in range(num_substrings + 1):
            subsequence = dna_sequence[i : i + 10]
            sequence_count[subsequence] += 1
            if sequence_count[subsequence] == 2:
                repeated_sequences.append(subsequence)
        return repeated_sequences
