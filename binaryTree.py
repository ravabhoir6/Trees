
class Node:
     def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(1)
#       a
#      / \
#     b   c
#    / \   \
#   d   e   f
a.left = b
a.right = c
c.right = f
b.left = d
b.right = e


"""
DEPTH FIRST SEARCH
Depth First SearchIn this we will use stack to 
traverse we will take root node as input
we will use while loop with condition len(stack) > 0
we will pop the top element from the stack and check
if it has left and right, if it does then only we will 
add it to our stack
output = [a, b, d, e, c, f]
"""
def depthFirstSearch(root):
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        
        print(current.value)
        
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

"""
BREADTH FIRST SEARCH
here we have to print all element layer by layer
instead of catching a single node and going deep we have print
all the element of existing layer.
Here we have implemented queue in which the left and right element
are inserted at start and last element is poped(which is current element)
output = [a, b, c, d, e, f]
"""
def breadthFirstSearch(root):
    queue = [root]
    while len(queue) > 0:
        current = queue.pop()
        print(current.value)
        
        if current.left:
            queue.insert(0, current.left)
        if current.right:
            queue.insert(0, current.right)

"""
finding a element in the tree
same we can use breadthFirstSearch or depthFirstSearch
we'll try both
output: true or False
"""    
def findElementDepthFirstTraversal(root, ele):
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        
        if curr.value == ele:
            return [True, f"{ele} is present in the binary tree"]
        
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    
    return [False, f"{ele} is not present in the binary tree"]
    
def findElementBreadthFirstTravesal(root, ele):
    queue = [root]
    while len(queue) > 0:
        curr = queue.pop()
        
        if curr.value == ele:
            return f"{ele} is present in the tree"
        
        if curr.left:
            queue.insert(0, curr.left)
            
        if curr.right:
            queue.insert(0, curr.right)
        
    return f"{ele} is not present in the tree"
    
    
"""
TREE SUM PROBLEM
we have to add all the value in the tree to a sum
we will use same both travesal techniques to calculate count
"""
def sumDepthFirst(root):
    sum = 0
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        sum += curr.value
            
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return f"sum of all nodes is {sum}"

def sumBreadthFirst(root):
    sum = 0
    queue = [root]
    while len(queue) > 0:
        curr = queue.pop()
        sum += curr.value
        
        if curr.right:
            queue.insert(0, curr.right)
        if curr.left:
            queue.insert(0, curr.left)
            
    return f"sum of all nodes is {sum}"
        
"""
TREE MIN, MAX VALUE
keep a single varible check if the current 
elements value is bigger or smaller and atlast after the 
loop is over return biggest and smallest elements we'll use
breadth first search
"""
def breadthFirstMinMax(root):
    minEl = root.value
    maxEl = 0
    queue = [root]
    
    while len(queue) > 0:
        curr = queue.pop()
        
        if curr.value < minEl:minEl = curr.value
        if curr.value > maxEl:maxEl = curr.value
        
        if curr.left:
            queue.insert(0, curr.left)
        if curr.right:
            queue.insert(0, curr.right)
    return f"smallest element in the tree is: {minEl} \n biggest element in the tree is: {maxEl}"
        
"""
MAX PATH SUM
we have the max path from root node to a leaf
we'll use recursion to find the paths from root to leaf nodes
and then we'll store the sum of each path in array and then we'll
return the max element inside the array
"""
pathSum = []
def printPaths(node, path, pathLen):
    if node == None:
        return
    
    path.insert(pathLen, node.value)
    pathLen+=1 
    
    if node.left == None and node.right == None:
        pathSum.append(sum(path[0:pathLen]))
    else:
        printPaths(node.left, path, pathLen)
        printPaths(node.right, path, pathLen)

printPaths(a, [], 0)
print(max(pathSum))


"""
PREORDER TRAVESAL 
        
        