from queue import SimpleQueue, LifoQueue

class Node:
    def __init__(self, idx, parent):
        self.idx = idx
        self.parent = parent
        self.visited = False
        self.left = None
        self.right = None

def insertTreesBreadthFirst(root, indexes):
    if root is None:
        return

    queue = SimpleQueue()

    queue.put(root)

    for index in indexes:
        node = queue.get()

        if index[0] != -1:
            new_node = Node(index[0], node)
            node.left = new_node
        if index[1] != -1:
            new_node = Node(index[1], node)
            node.right = new_node

        if node.left is not None:
            queue.put(node.left)

        if node.right is not None:
            queue.put(node.right)

def swapLevels(root, query):
    if root is None:
        return

    queue = SimpleQueue()

    height = 1
    queue.put([root, height])

    while not queue.empty():
        node_with_height = queue.get()

        node = node_with_height[0]
        height = node_with_height[1]

        if height % query == 0:
            temp = node.left
            node.left = node.right
            node.right = temp
        if node.left != None:
            queue.put([node.left, height + 1])
        if node.right != None:
            queue.put([node.right, height + 1])

def printTraversal(root, traversal):
    stack = LifoQueue()

    node = root

    while True:
        if node is not None:
            stack.put(node)
            node = node.left
        elif not stack.empty():
            node = stack.get()
            traversal += [node.idx]
            node = node.right
        else:
            break





def swapNodes(indexes, queries):
    root = Node(1, None)

    insertTreesBreadthFirst(root, indexes)

    traversals = []
    for query in queries:
        swapLevels(root, query)
        traversal = []
        printTraversal(root, traversal)
        traversals.append(traversal)

    return traversals

if __name__ == '__main__':
    infile = "Input//Test.txt"
    with open(infile, 'r') as f:

        n = int(f.readline().rstrip())

        indexes = []

        for _ in range(n):
            indexes.append(list(map(int, f.readline().rstrip().split())))

        queries_count = int(f.readline().rstrip())

        queries = []

        for _ in range(queries_count):
            queries_item = int(f.readline().rstrip())
            queries.append(queries_item)

        result = swapNodes(indexes, queries)

        print('\n'.join([' '.join(map(str, x)) for x in result]))
        print('\n')
