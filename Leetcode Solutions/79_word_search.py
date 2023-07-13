'''
Question Link - https://leetcode.com/problems/word-search/description/
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = set()
        
        def helperFunc(row,col,board,word):
            
            if len(word)==0:
                return True
            
            if row<0 or col<0 or row>=len(board) or col>=len(board[0]) or (row,col) in path:
                return False
            
            path.add((row,col))
            smallRes = False
            if board[row][col]==word[0]:
                steps=[[0,1],[0,-1],[1,0],[-1,0]]
                for step in steps:
                    smallRes = smallRes or helperFunc(row+step[0],col+step[1],board,word[1:])            
            path.remove((row,col))
            
            return smallRes

        count = Counter(sum(board, []))
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False  
        if count[word[0]] > count[word[-1]]:
             word = word[::-1] 
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                smallRes = helperFunc(i,j,board, word)
                if smallRes:
                    return True
        
        return False
