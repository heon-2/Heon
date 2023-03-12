arr=' ABCDEFG'


def preorder(now):
    if now>=len(arr): return
    print(arr[now],end=' ')
    preorder(now*2)
    preorder(now*2+1)

def postorder(now):
    if now >= len(arr) : return
    postorder(now * 2)
    postorder(now * 2 + 1)
    print(arr[now], end=' ')

def inorder(now):
    if now >= len(arr) : return
    inorder(now * 2)
    print(arr[now], end=' ')
    inorder(now * 2 + 1)

preorder(1)   # 전위순회
print()
postorder(1)  # 후위순회
print()
inorder(1) # 중위순회 2