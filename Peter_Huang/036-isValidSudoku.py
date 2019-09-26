import copy
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0,9):
            if ((self.isRowValid(i, board)) and (self.isColumValid(i, board)) and (self.isSquareValid(i, board))) == False:
                return False
        return True

    def isSquareValid(self, indexOfSquare, board):
        suqareList = []
        rowIndex = 0
        columIndex = 0
        if indexOfSquare in [0,1,2]:
            rowIndex = 0
            columIndex = indexOfSquare * 3
        elif indexOfSquare in [3,4,5]:
            rowIndex = 3
            columIndex = (indexOfSquare % 3) * 3
        else:
            rowIndex = 6
            columIndex = (indexOfSquare % 6) * 3

        for i in range(rowIndex, rowIndex + 3):
            suqareList.append(board[i][columIndex])
            suqareList.append(board[i][columIndex + 1])
            suqareList.append(board[i][columIndex + 2])
        print('square',indexOfSquare,':',suqareList)
        if self.isListValid(suqareList):
            return True
        else:
            print("square" ,indexOfSquare ,"is not valid")
            return False

    def isColumValid(self, colum, board):
        columList = []
        for list in board:
            columList.append(list[colum])
        print('colum',colum,":",columList)
        if self.isListValid(columList):
            return True
        else:
            print("colum" ,colum, "is not valid")
            return False

    def isRowValid(self, row, board):
        rowList = board[row]
        print('row',row,':',rowList)
        if self.isListValid(rowList):
            return True
        else:
            print("row" ,row ,"is not valid")
            return False

    def isListValid(self, list):
        for num in list:
            tempList = copy.deepcopy(list)
            tempList.remove(num)
            if num in tempList:
                if num != '.':
                    return False
        return True
if __name__ == "__main__":
    s = Solution()
    res = s.isValidSudoku([
        [".",".",".",".",".",".","5",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","3"],
        [".","2",".","7",".",".",".",".","."],
        ["8","3","6","5",".",".",".",".","1"],
        [".",".",".",".",".","1",".",".","."],
        ["2",".",".",".",".",".",".",".","5"],
        [".",".",".",".",".",".",".",".","7"],
        [".",".",".","4",".",".",".","7","."]])
    print(res)
