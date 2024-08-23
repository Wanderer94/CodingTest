def solution(operations):
    queue = []
    for operation in operations:
        queue = cal(operation, queue)
    if len(queue) == 0:
        return [0,0]
    else:
        return [max(queue),min(queue)]

def cal(operation, queue):
    op = operation.split(" ")
    if op[0] == "I":
        queue.append(int(op[1]))
    elif op[0] == "D" and len(queue) == 0:
        return queue
    elif op[0] == "D" and op[1] == "1":
        queue.remove(max(queue))
    elif op[0] == "D" and op[1] == "-1":
        queue.remove(min(queue))
    return queue