import sys

class Union:
    def __init__(self, size):
        self.parent = [''] * (size+1)
        for i in range(1, size+1):
            self.parent[0] = 0
            self.parent[i] = i

    def find(self, key):
        if key == self.parent[key]:
            return key
        else:
            p = self.find(self.parent[key])
            self.parent[key] = p
            return p

    def union(self, key1, key2):
        x, y = self.find(key1), self.find(key2)

        if x != y:
            self.parent[y] = x

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break
    u = Union(N)
    vector = [[0] * (N+1) for i in range(N + 1)]
    d = dict()
    for _ in range(M):
        line = sys.stdin.readline().split()
        c = line[0]
        key1 = int(line[1])
        key2 = int(line[2])
        if c == "!":
            weight = int(line[3])
            vector[key1][key2] = weight
            vector[key2][key1] = -weight
            u.union(key1, key2)
            print(vector)
        elif c == "?":
            if u.find(key1) == u.find(key2):
                print("same root")
                print(u.parent)
                result = 0
                while True:
                    p = key2
                    if u.parent[p] == u.find(key1) or u.parent[key1] == u.find(p):
                        result += vector[key1][p]
                        print(result)
                        break
                    else:
                        result += vector[u.parent[p]][p]
                        p = u.parent[p]
            else:
                print("UNKNOWN")