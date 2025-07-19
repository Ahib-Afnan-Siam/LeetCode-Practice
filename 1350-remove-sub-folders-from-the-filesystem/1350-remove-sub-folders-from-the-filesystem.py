class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = []
        for f in folder:
            if ans and f.startswith(ans[-1] + '/'):
                continue
            ans.append(f)
        return ans