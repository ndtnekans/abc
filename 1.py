from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, u):
        visited = [False] * (len(self.graph) + 1)  # Adjusted for 1-based index
        stack = []
        visited[u] = True
        stack.append(u)

        while stack:
            u = stack.pop(0) #doi neu lam theo chieu sau    
            print(u, end=' ')
            for i in self.graph[u]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True
    def show(self):
        for i in self.graph:
            print(self.graph[i])


if __name__ == '__main__':
        g = Graph()
        g.addEdge(0, 1)
        g.addEdge(1, 0)
        g.addEdge(0, 2)
        g.addEdge(2, 0)
        g.addEdge(2, 4)
        g.addEdge(4, 2)
        g.addEdge(1, 4)
        g.addEdge(4, 1)
        g.addEdge(1, 3)
        g.addEdge(3, 1)
        g.addEdge(3, 4)
        g.addEdge(4, 3)
        g.addEdge(3, 5)
        g.addEdge(5, 3)
        g.addEdge(5, 4)
        g.addEdge(4, 5)

        print("BFS starting from vertex 0:")
        g.BFS(0)
