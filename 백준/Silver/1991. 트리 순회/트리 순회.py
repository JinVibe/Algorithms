class NODE:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find(node, ele):
    global p
    ptr = node
    if ptr.data == ele:
        p = ptr
        return
    if ptr.left is not None:
        find(ptr.left, ele)
    if ptr.right is not None:
        find(ptr.right, ele)

    return


def preorder(node):
    print(node.data, end='')
    if node.left is not None:
        preorder(node.left)
    if node.right is not None:
        preorder(node.right)


def inorder(node):
    if node.left is not None:
        inorder(node.left)
    print(node.data, end='')
    if node.right is not None:
        inorder(node.right)


def postorder(node):
    if node.left is not None:
        postorder(node.left)
    if node.right is not None:
        postorder(node.right)
    print(node.data, end='')


head = None
p = None

n = int(input())

for i in range(n):
    data, l, r = input().split()
    new_node = NODE(data)
    if head is None:
        head = new_node
        if l != '.':
            head.left = NODE(l)
        if r != '.':
            head.right = NODE(r)
    else:
        find(head, data)

        if l != '.':
            p.left = NODE(l)
        if r != '.':
            p.right = NODE(r)

preorder(head)
print()
inorder(head)
print()
postorder(head)
