# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        results = []

        for i in range(len(pairs)):
            key = pairs[i]
            j = i - 1

            while j >= 0 and pairs[j].key > key.key:
                pairs[j + 1] = pairs[j]
                j -= 1

            pairs[j + 1] = key

            results.append(pairs[:])
        return results
