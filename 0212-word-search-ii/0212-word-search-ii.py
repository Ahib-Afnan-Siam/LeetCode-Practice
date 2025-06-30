class TrieNode:
    __slots__ = ['children', 'word']
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word
        
        m, n = len(board), len(board[0])
        result = set()
        
        def dfs(i, j, parent_node):
            c = board[i][j]
            if c not in parent_node.children:
                return
            
            node = parent_node.children[c]
            if node.word is not None:
                result.add(node.word)
                node.word = None
            
            board[i][j] = '#'
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#' and board[ni][nj] in node.children:
                    dfs(ni, nj, node)
            board[i][j] = c
            
            if not node.children and node.word is None:
                del parent_node.children[c]
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        
        return list(result)