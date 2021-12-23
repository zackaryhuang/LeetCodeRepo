class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        board_str = board[0] + board[1] + board[2]
        x_count = board_str.count('X')
        o_count = board_str.count('O')
        if 0 <= x_count - o_count <= 1:
            match_list = self.win_mark(board_str)
            if len(match_list) == 2:
                return False
            if len(match_list) == 1:
                if match_list[0] == 'X':
                    return x_count > o_count
                return x_count == o_count
            return True
        return False

    def win_mark(self, board_str):
        wind_list = []
        if board_str[0] == board_str[1] == board_str[2] and board_str[0] != ' ':
            if board_str[0] not in wind_list:
                wind_list.append(board_str[0])
        if board_str[3] == board_str[4] == board_str[5] and board_str[3] != ' ':
            if board_str[3] not in wind_list:
                wind_list.append(board_str[3])
        if board_str[6] == board_str[7] == board_str[8] and board_str[6] != ' ':
            if board_str[6] not in wind_list:
                wind_list.append(board_str[6])
        if board_str[0] == board_str[3] == board_str[6] and board_str[0] != ' ':
            if board_str[0] not in wind_list:
                wind_list.append(board_str[0])
        if board_str[1] == board_str[4] == board_str[7] and board_str[1] != ' ':
            if board_str[1] not in wind_list:
                wind_list.append(board_str[1])
        if board_str[2] == board_str[5] == board_str[8] and board_str[2] != ' ':
            if board_str[2] not in wind_list:
                wind_list.append(board_str[2])
        if board_str[0] == board_str[4] == board_str[8] and board_str[0] != ' ':
            if board_str[0] not in wind_list:
                wind_list.append(board_str[0])
        if board_str[2] == board_str[4] == board_str[6] and board_str[2] != ' ':
            if board_str[2] not in wind_list:
                wind_list.append(board_str[2])
        return wind_list


if __name__ == '__main__':
    s = Solution()
    print(s.validTicTacToe(["OXX","XOX","OXO"]))