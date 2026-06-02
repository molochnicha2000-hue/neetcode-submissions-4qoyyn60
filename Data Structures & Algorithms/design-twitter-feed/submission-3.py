class Twitter:
    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list) # pairs (count, post)
        self.count = 0 # let it store 0 in default and then decrement (-1)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minH = []
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minH.append([count, tweetId, followeeId, index - 1])
        
        heapq.heapify(minH)
        while minH and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minH)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minH, [count, tweetId, followeeId, index - 1])
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
