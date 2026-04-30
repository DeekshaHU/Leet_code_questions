class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        count = 0
        prev = ""

        for i in typed:

            if count < len(name) and i == name[count]:
                prev = i
                count += 1

            elif i == prev:
                continue

            else:
                return False

        if count == len(name):
            return True

        return False  