class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1 = {value: key for key, value in enumerate(list1)}
        list2 = {value: key for key, value in enumerate(list2)}
        
        if len(list1)>len(list2):
            list1, list2 = list2, list1
            
        ans = [float("inf"), [""]]
        
        for i in list1:
            if i in list2:
                if list1[i]+list2[i] < ans[0]:
                    ans[0] = list1[i]+list2[i]
                    ans[1] = [i]
                elif list1[i]+list2[i] == ans[0]:
                    ans[1].append(i)
                    
        return ans[1]