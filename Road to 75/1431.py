def kidsWithCandies(candies, extraCandies):
        results = [False]*len(candies)
        max = 0
        for i in range(0,len(candies)):
            if max < candies[i]:
                max = candies[i]
            i += 1
        for i in range(0,len(candies)):
            if candies[i]+extraCandies >= max:
                results[i] = True
            else:
                results[i] = False
            i += 1
        return results

candy = [4,2,1,1,2]
print(kidsWithCandies(candy, 1))