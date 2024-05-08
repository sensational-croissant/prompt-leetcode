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

-------------------------------------------------------------------------------
# Code
```python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort_rank = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        
        sorted_score = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        
        result = [0] * len(score)
        
        for i, (index,_) in enumerate(sorted_score):
            result[index] = sort_rank.get(i, str(i + 1))
        
        return result
``` 

# Time Complexity
The time complexity of this solution is O(n log n), where n is the number of athletes.

# Space Complexity
The space complexity is O(n) to store the sorted indices.

-------------------------------------------------------------------------------
# Code
```python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_map = {score: str(i+1) for i, score in enumerate(sorted_score)}
        
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = []
        
        for s in score:
            if rank_map[s] in medals:
                result.append(rank_map[s])
            else:
                result.append(rank_map[s])
        
        return result
```

-------------------------------------------------------------------------------
# Code
```python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_map = {score: str(i+1) for i, score in enumerate(sorted_score)}
        
        result = []
        for s in score:
            rank = rank_map[s]
            if rank == '1':
                result.append("Gold Medal")
            elif rank == '2':
                result.append("Silver Medal")
            elif rank == '3':
                result.append("Bronze Medal")
            else:
                result.append(rank)
                
        return result
```

-------------------------------------------------------------------------------
# Code
```python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_dict = {sorted_score[i]: str(i+1) for i in range(len(sorted_score))}
        
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
        
        return [rank_map[score[i]] for i in range(len(score))]
```

# Time Complexity
The time complexity of this solution is O(n log n) due to the sorting of scores.

# Space Complexity
The space complexity is O(n) to store the sorted scores and rank mapping.

-------------------------------------------------------------------------------
# Code
``` python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        rank_map = {sorted_scores[i]: str(i+1) for i in range(len(sorted_scores))}
        
        result = []
        for s in score:
            rank = rank_map[s]
            if rank == "1":
                result.append("Gold Medal")
            elif rank == "2":
                result.append("Silver Medal")
            elif rank == "3":
                result.append("Bronze Medal")
            else:
                result.append(rank)
        
        return result
```

# Time Complexity
The time complexity of this solution is O(n log n) due to sorting the scores array.

# Space Complexity
The space complexity is O(n) where n is the number of athletes.

-------------------------------------------------------------------------------
# Code
```python
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        rank_map = {sorted_scores[i]: str(i+1) for i in range(len(sorted_scores))}
        
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = []
        
        for s in score:
            if rank_map[s] in medals:
                result.append(rank_map[s])
            else:
                result.append(rank_map[s])
        
        return result
```

# Time Complexity
The time complexity of sorting the scores is O(nlogn) where n is the number of athletes. Retrieving the ranks from the map takes O(n). Overall, the time complexity is O(nlogn).

# Space Complexity
The space complexity is O(n) due to the extra space used to store the sorted scores and the rank map.

-------------------------------------------------------------------------------
# Code
```python
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        ranks = ['' for _ in range(len(score))]
        
        for rank, (s, i) in enumerate(sorted_scores):
            if rank == 0:
                ranks[i] = "Gold Medal"
            elif rank == 1:
                ranks[i] = "Silver Medal"
            elif rank == 2:
                ranks[i] = "Bronze Medal"
            else:
                ranks[i] = str(rank+1)
        return ranks
```

# Time Complexity
The time complexity is O(n log n) because we sort the scores.

# Space Complexity
The space complexity is O(n) because we keep the sorted scores and ranks in additional data structures.

-------------------------------------------------------------------------------
# Code
``` python
class Solution:
    def findRelativeRanks(self, score):
        sort = sorted(score)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(score) + 1)))
        return list(map(dict(zip(sort, rank)).get, score))
```

# Time Complexity
The time complexity is O(n log n) because we are sorting the scores.

# Space Complexity
The space complexity is O(n) because we are creating a new sorted list and a rank list.