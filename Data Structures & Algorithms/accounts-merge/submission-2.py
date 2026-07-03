class UnionFind:
    def __init__(self, N):
        self.rank = [1] * N
        self.par = [i for i in range(N)]

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1 = self.find(x1)
        p2 = self.find(x2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True
    
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        UF = UnionFind(len(accounts))
        emailToAcc = {}
        for index, emails in enumerate(accounts):

            for m in emails[1:]:
                if m in emailToAcc:
                    # union
                    UF.union(index, emailToAcc[m])
                else:
                    emailToAcc[m] = index
        
        f = collections.defaultdict(list)
        for mail, index in emailToAcc.items():
            leader = UF.find(index)
            f[leader].append(mail)
        
        res = []
        for index, mails in f.items():
            name = accounts[index][0]
            res.append([name] + sorted(f[index]))


        return res