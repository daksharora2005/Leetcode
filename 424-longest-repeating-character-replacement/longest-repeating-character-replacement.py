class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = 0
        max_freq = 0
        best = 0

        for right, char in enumerate(s):
            counts[char] += 1
            max_freq = max(max_freq, counts[char])

            window_len = right - left + 1
            if window_len - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
        