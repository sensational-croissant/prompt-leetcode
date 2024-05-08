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

-------------------------------------------------------------------------------
## Code
```python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_dict = {score: str(i + 1) for i, score in enumerate(sorted_score)}
        
        result = []
        for s in score:
            if rank_dict[s] == "1":
                result.append("Gold Medal")
            elif rank_dict[s] == "2":
                result.append("Silver Medal")
            elif rank_dict[s] == "3":
                result.append("Bronze Medal")
            else:
                result.append(rank_dict[s])
        
        return result
```

## Time Complexity:
The time complexity of this solution is O(n log n) due to the sorting of the scores array.

## Space Complexity:
The space complexity of this solution is O(n) as we are creating a dictionary to store the ranks.

-------------------------------------------------------------------------------
# Relative Ranks

## Code
``` python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_dict = {score: rank for rank, score in enumerate(sorted_score, 1)}
        result = []
        
        for s in score:
            rank = rank_dict[s]
            if rank == 1:
                result.append("Gold Medal")
            elif rank == 2:
                result.append("Silver Medal")
            elif rank == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(rank))
        
        return result
```

## Time Complexity: O(n log n) - time taken for sorting the scores

## Space Complexity: O(n) - used for the rank_dict and result lists

-------------------------------------------------------------------------------
# Iterative Approach

## Code
```python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_map = {}
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        for i in range(len(sorted_score)):
            if i < 3:
                rank_map[sorted_score[i]] = medals[i]
            else:
                rank_map[sorted_score[i]] = str(i+1)
        
        return [rank_map[score[i]] for i in range(len(score))]
```

## Time Complexity: O(n log n) - sorting the score array
## Space Complexity: O(n) - used additional space for storing ranks and medals

-------------------------------------------------------------------------------
# Code
```python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(score) + 1)))
        rank_dict = {sorted_score[i]: ranks[i] for i in range(len(score))}
        
        return [rank_dict[score[i]] for i in range(len(score))]
```

# Time Complexity: O(n log n) - Sorting the scores in descending order takes O(n log n) time.
# Space Complexity: O(n) - Used additional space to store the ranks and the rank dictionary.