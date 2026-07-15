class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = defaultdict(list)

        for n in nums:
            dictionary[n].append(n)

        sorted_dict = sorted(dictionary.items(), key=lambda item: len(item[1]), reverse=True)
        k_most_frequent = islice(sorted_dict, k)

        return [item[0] for item in k_most_frequent]