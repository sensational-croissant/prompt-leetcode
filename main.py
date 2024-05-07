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
      "content": "2816. Double a Number Represented as a Linked List\nYou are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.\n\nReturn the head of the linked list after doubling it.\n\nExample 1:\n\n\n\nInput: head = [1,8,9]\nOutput: [3,7,8]\nExplanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.\nExample 2:\n\n\n\nInput: head = [9,9,9]\nOutput: [1,9,9,8]\nExplanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998. \nConstraints:\n\nThe number of nodes in the list is in the range [1, 104]\n0 <= Node.val <= 9\nThe input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself."
    },
    {
      "role": "user",
      "content": "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\nclass Solution:\n    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:\n        "
    },
    {
      "role": "assistant",
      "content": "To double a number represented as a linked list, we can follow these steps:\n1. Reverse the linked list to facilitate the multiplication by 2 operation.\n2. Initialize a variable carry as 0.\n3. Traverse the reversed linked list and for each node, multiply its value by 2, add the carry, and update the carry accordingly.\n4. After the traversal is complete, if there is a non-zero carry left, create a new node with the carry as its value and add it to the beginning of the list.\n5. Reverse the list again to return it to its original order.\n\nHere is the implementation of the above approach:\n\n```python\n# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self, val=0, next=None):\n#         self.val = val\n#         self.next = next\n\nclass Solution:\n    def reverseLinkedList(self, head):\n        prev = None\n        curr = head\n        while curr"
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

with open("double-a-number-represented-as-a-linked-list.md", "a") as myfile:
  myfile.write(response_text)
