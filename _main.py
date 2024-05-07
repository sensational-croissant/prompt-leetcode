import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set your API key
client = OpenAI()


def get_response(system_prompt, user_prompt):
    # Assign the role and content for each message
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    response = client.chat.completions.create(
        model="gpt-4", messages=messages, temperature=1
    )

    return response.choices[0].message.content
    
# Craft a prompt that asks the model for the function
user_prompt = f"""
2487. Remove Nodes From Linked List
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

Example 1:



Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
"""


methods = ["Arrays & Hashing", "Two Pointers", "Sliding Window", "Binary Search", "Backtracking", "Graphs", "Advanced Graphs", "1-D Dynamic Programming", "2-D Dynamic Programming", "Greedy", "Intervals", "Math & Geometry", "Bit Manipulation"]

for method in methods:


    # Define the system prompt
    system_prompt = f"""You are provided with input-output examples for a Python function to solve a LeetCode problem and return in this format: 

    # {method}

    ## Code

    ``` python
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        
    ```

    ## Time complexity:

    ## Space complexity:
    """



    # Get the response to the user prompt
    response = get_response(system_prompt, user_prompt)

    print(response)

    with open("remove-nodes-from-linked-list.md", "a") as myfile:
        myfile.write(f"--------------{method}--------------")
        myfile.write(response)
        myfile.write("\n\n")