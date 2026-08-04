from collections import defaultdict,deque

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        preq_count = defaultdict(int)
        related_crs = defaultdict(list)

        for prev,nxt in relations:
            related_crs[prev].append(nxt)
            preq_count[nxt]+=1
        
        frontier = deque()

        for i in range(1,n+1):
            if preq_count[i] == 0:
                frontier.append((i,1))
        
        # bfs
        sem = 0
        taken_courses = 0

        while frontier:
            crs,cur_sem = frontier.popleft()
            taken_courses+=1

            sem = max(sem,cur_sem)

            for nxt_crs in related_crs[crs]:
                preq_count[nxt_crs]-=1
                if preq_count[nxt_crs] == 0:
                    frontier.append((nxt_crs,cur_sem+1))
        
        if taken_courses == n:
            return sem
        return -1

        
   
   
   
   
   
   
   
   
   
   
   
   
   
    #     prereq_count = defaultdict(int)
    #     frontier = deque()
    #     related = defaultdict(list)
    #     for p in relations:
    #         prereq_count[p[1]]+=1
    #         related[p[0]].append(p[1])

    #     for num in range(1,n+1):
    #         count = prereq_count[num]
    #         if count == 0:
    #             frontier.append((num,1))

    #     return self.bfs(frontier,prereq_count,related,n)

    # def bfs(self,frontier,prereq_count,related,n):
    #     taken_courses = 0
    #     sem = 0
    #     while frontier:
    #         crs,num = frontier.popleft()
    #         taken_courses+=1
    #         sem = max(sem,num)

    #         for nextcrs in related[crs]:
    #             prereq_count[nextcrs]-=1
    #             if prereq_count[nextcrs] == 0:
    #                 frontier.append((nextcrs,num+1))
        
    #     if taken_courses == n:
    #         return sem
    #     return -1