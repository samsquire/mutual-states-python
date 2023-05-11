import random
requests = {
  "1": [],
  "2": [],
  "3": [],
  "4": [],
  "5": []
}
commit_logs = {
  "1": 0,
  "2": 0,
  "3": 0,
  "4": 0,
  "5": 0
}

for message_index in range(0, 10):
  item = random.randrange(1, 6)
  requests[str(item)].append(message_index)
  commit_logs[str(item)] = commit_logs[str(item)] + 1

from pprint import pprint
pprint(commit_logs)
pprint(requests)
  # matrix and position

# use neural networks to learn memory patterns and consequently programs
history = [
  {
    "ref": "0",
    "position": 0,
    "instruction": "a = 0"
  },
  {
    "ref": "0",
    "position": -1,
    "instruction": "a++",
    "new_ref": "1",
    "new_position": 0
    
  }
  
]
