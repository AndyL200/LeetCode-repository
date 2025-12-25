def maxTwoEvents(events) -> int:
    events.sort()
    dp = [[-1] * 3 for _ in range(len(events))]
    
    def rec(idx, cnt):
        nonlocal dp
        if idx >= len(events) or cnt == 2:
            return 0
        if dp[idx][cnt] == -1:
            end = events[idx][1]
            low, high = idx + 1, len(events) - 1
            while low < high:
                mid = low + ((high-low) >> 1)
                if events[mid][0] > end:
                    high = mid
                else:
                    low = mid+1
            include = None
            exclude = None
            if low < len(events) and events[low][0] > end:
                include = events[idx][2] + rec(low, cnt+1)
            else:
                include = events[idx][2]
            exclude = rec(idx+1, cnt)
            dp[idx][cnt] = max(include, exclude)
        #include
        return dp[idx][cnt]
    return rec(0,0)

print(maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]))
