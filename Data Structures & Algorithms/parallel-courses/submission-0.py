from collections import defaultdict,deque

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        prereq_count = defaultdict(int)
        frontier = deque()
        related = defaultdict(list)
        for p in relations:
            prereq_count[p[1]]+=1
            related[p[0]].append(p[1])

        for num in range(1,n+1):
            count = prereq_count[num]
            if count == 0:
                frontier.append((num,1))

        return self.bfs(frontier,prereq_count,related,n)

    def bfs(self,frontier,prereq_count,related,n):
        taken_courses = 0
        sem = 0
        while frontier:
            crs,num = frontier.popleft()
            taken_courses+=1
            sem = max(sem,num)

            for nextcrs in related[crs]:
                prereq_count[nextcrs]-=1
                if prereq_count[nextcrs] == 0:
                    frontier.append((nextcrs,num+1))
        
        if taken_courses == n:
            return sem
        return -1