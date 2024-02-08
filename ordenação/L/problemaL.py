class TreeNode:
    def __init__(self, val, right, left):
        self.val = val
        self.right = right
        self.left = left


def inserirNaArvore(root, node):
    current = root
    if current == None:
        node.left = None
        node.right = None
        return node
    if node.val >= current.val:
        current.right = inserirNaArvore(current.right, node)
    else:
        current.left = inserirNaArvore(current.left, node)
    
    return root


lista = list(map(int, input().split()))
arvore = TreeNode(lista[0], None, None)
for i in range(1, len(lista)):
    newnode = TreeNode(lista[i], None, None)
    inserirNaArvore(arvore, newnode)


def PreOrdem(root):
    if root != None:
        print(root.val, end = " ")
        PreOrdem(root.left)
        PreOrdem(root.right)

def InOrdem(root):
    if root != None:
        InOrdem(root.left)
        print(root.val, end = " ")
        InOrdem(root.right)

def PosOrdem(root):
    if root != None:
        PosOrdem(root.left)
        PosOrdem(root.right)
        print(root.val, end = " ")



PreOrdem(arvore)
print()
InOrdem(arvore)
print()
PosOrdem(arvore)