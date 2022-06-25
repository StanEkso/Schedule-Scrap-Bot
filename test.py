from stack import Stack

message_stack = Stack()

for i in range(1,100):
    result = message_stack.add(i)
    if (result["state"]):
         print('ok')