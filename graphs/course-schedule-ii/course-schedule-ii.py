from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for dest,src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] +=1 # dest needs +1 prerequisite

        # starting queue with only courses without prequisites
        q = deque([])

        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        order = []
        while q:
            c = q.popleft()
            order.append(c)

            for dep in graph[c]:
                in_degree[dep] -= 1
                if in_degree[dep] == 0:
                        q.append(dep)

        
        return order if len(order) == numCourses else []


    



        
                

        