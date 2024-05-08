import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "506. Relative Ranks\nYou are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.\n\nThe athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:\n\nThe 1st place athlete's rank is \"Gold Medal\".\nThe 2nd place athlete's rank is \"Silver Medal\".\nThe 3rd place athlete's rank is \"Bronze Medal\".\nFor the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is \"x\").\nReturn an array answer of size n where answer[i] is the rank of the ith athlete.\n\nExample 1:\n\nInput: score = [5,4,3,2,1]\nOutput: [\"Gold Medal\",\"Silver Medal\",\"Bronze Medal\",\"4\",\"5\"]\nExplanation: The placements are [1st, 2nd, 3rd, 4th, 5th].\nExample 2:\n\nInput: score = [10,3,8,9,4]\nOutput: [\"Gold Medal\",\"5\",\"Bronze Medal\",\"Silver Medal\",\"4\"]\nExplanation: The placements are [1st, 5th, 3rd, 2nd, 4th].\nConstraints:\n\nn == score.length\n1 <= n <= 104\n0 <= score[i] <= 106\nAll the values in score are unique."
    },
    {
      "role": "user",
      "content": "class Solution:\n    def findRelativeRanks(self, score: List[int]) -> List[str]:"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

response_text = response.choices[0].message.content
print(response_text)

with open("relative_ranks.md", "a") as myfile:
  myfile.write("\n\n-------------------------------------------------------------------------------\n")
  myfile.write(response_text)
