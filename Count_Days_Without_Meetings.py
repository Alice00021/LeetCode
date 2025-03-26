class Solution(object):
    def countDays(self, days, meetings):
        merge_arr = []
        busy_days = 0
        meetings.sort(key=lambda x: x[0])
        for start, end in meetings:
            if not merge_arr or merge_arr[-1][1] < start:
                merge_arr.append([start, end])
            else:
                merge_arr[-1][1] = max(merge_arr[-1][1], end)
        for start, end in merge_arr:
            busy_days += end - start + 1  
        result = days - busy_days
        return result

    
ex = Solution()
days = 5
meetings = [[2,4],[1,3]]
print(ex.countDays(days, meetings))
print(ex.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))
print(ex.countDays(days=8, meetings= [[3,4],[4,8],[2,5],[3,8]]))