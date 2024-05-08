-------------------------------------------------------------------------------
```python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        rank_dict = {sorted_scores[i]: str(i+1) for i in range(len(sorted_scores))}
        
        for i in range(len(score)):
            if rank_dict[score[i]] == "1":
                score[i] = "Gold Medal"
            elif rank_dict[score[i]] == "2":
                score[i] = "Silver Medal"
            elif rank_dict[score[i]] == "3":
                score[i] = "Bronze Medal"
            else:
                score[i] = rank_dict[score[i]]
        
        return score
```

-------------------------------------------------------------------------------
## Time Complexity:
The time complexity of this solution is O(n log n) due to the sorting of the scores array.

## Space Complexity:
The space complexity of this solution is O(n) to store the rank dictionary.