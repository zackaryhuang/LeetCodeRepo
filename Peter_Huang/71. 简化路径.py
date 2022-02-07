class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = path.split('/')
        simple_path = ''
        for path_component in paths:
            if path_component == '' or path_component == '.':
                continue
            if path_component == '..':
                for i, c in enumerate(simple_path[::-1]):
                    if c == '/':
                        if i != 0:
                            simple_path = simple_path[:len(simple_path) - i - 1]
                        break
            else:
                simple_path += '/'
                simple_path += path_component
        if simple_path == '':
            simple_path = '/'
        return simple_path


if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath('/../'))
