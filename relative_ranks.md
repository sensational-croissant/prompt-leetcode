-------------------------------------------------------------------------------
# Code
```python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank_map = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        
        sorted_score = sorted(score, reverse=True)
        rank = {}
        for i, s in enumerate(sorted_score):
            if i in rank_map:
                rank[s] = rank_map[i]
            else:
                rank[s] = str(i+1)
        
        return [rank[s] for s in score]
```

# Time Complexity
The time complexity of this solution is O(n log n) due to sorting the scores.

# Space Complexity
The space complexity is O(n) to store the ranks.

-------------------------------------------------------------------------------
# Code
```python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_map = {}
        for i in range(len(sorted_score)):
            if i == 0:
                rank_map[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                rank_map[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                rank_map[sorted_score[i]] = "Bronze Medal"
            else:
                rank_map[sorted_score[i]] = str(i + 1)
        
        return [rank_map[s] for s in score]
``` 

# Time Complexity
The time complexity of this solution is O(n log n) due to sorting the scores array.

# Space Complexity
The space complexity is O(n) to store the rank information for each score.

-------------------------------------------------------------------------------
# Code
```python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_map = {}
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        for i, s in enumerate(sorted_score):
            if i < 3:
                rank_map[s] = medals[i]
            else:
                rank_map[s] = str(i + 1)
        
        return [rank_map[s] for s in score]
```

# Time Complexity
The time complexity of this solution is O(nlogn) due to sorting the scores array. Here, n is the number of athletes.

# Space Complexity
The space complexity of this solution is O(n) to store the sorted scores and the ranks map.

-------------------------------------------------------------------------------
# Code
``` python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(score)+1)))
        rank_map = {score: rank for score, rank in zip(sorted_score, ranks)}
        return [rank_map[s] for s in score]
``` 

# Time Complexity
The time complexity of this solution is O(n log n) due to sorting the original scores.

# Space Complexity
The space complexity of this solution is O(n) to store the rank_map dictionary.

-------------------------------------------------------------------------------
# Code
```python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_dict = {sorted_score[i]: str(i+1) for i in range(len(sorted_score))}
        
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        result = []
        for s in score:
            rank = rank_dict[s]
            if rank in ["1", "2", "3"]:
                result.append(medals[int(rank)-1])
            else:
                result.append(rank)
        
        return result
``` 

# Time Complexity
The time complexity is O(n log n) due to sorting the scores.

# Space Complexity
The space complexity is O(n) to store the sorted scores and the rank dictionary.