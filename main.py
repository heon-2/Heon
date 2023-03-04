arr = ' 12345678'  # arr[0] 은 비어있는 칸임


def preorder(now):
    if now > len(arr) - 1: return
    print(arr[now], end=' ')
    preorder(now * 2)  # 왼쪽 자식 노드 탐색
    preorder(now * 2 + 1)  # 오른쪽 자식 노드 탐색

def inorder(now):
    if now > len(arr) - 1: return
    inorder(now * 2)
    print(arr[now], end=' ')
    inorder(now * 2 + 1)

def postorder(now):
    if now > len(arr) - 1: return
    postorder(now * 2)
    postorder(now * 2 + 1)
    print(arr[now], end=' ')
preorder(1)  # 전위순회
print()

inorder(1)
print()
postorder(1)