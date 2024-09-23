# 전위 순회 VLR / 후위 순회 LRV
import sys

sys.setrecursionlimit(10**6)

class NODE:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def set_tree(val):
    global header
    node = NODE(val)
    p = header
    if header is None:
        header = node
    else:
        while True:
            if val < p.data:
                if p.left is None:
                    p.left = node
                    break
                else:
                    p = p.left
            else:
                if p.right is None:
                    p.right = node
                    break
                else:
                    p = p.right

def postorder(h):
    if h.left:
        postorder(h.left)
    if h.right:
        postorder(h.right)
    print(h.data)


header = None

while True:
    try:
        value = int(input())
        set_tree(value)

    except EOFError:
        break


postorder(header)
