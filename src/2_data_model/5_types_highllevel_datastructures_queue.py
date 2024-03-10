from collections import deque

queue = deque(["cust1", "cust2", "cust3"])
print(f"current queue: {queue}")

print("customer arrives")
queue.append("cust4")
print("customer queued")

print("customer arrives")
queue.append("cust5")
print("customer queued")

print("servicing customer")
queue.popleft()
print(f"current queue: {queue}")

print("servicing customer")
queue.popleft()
print(f"current queue: {queue}")
