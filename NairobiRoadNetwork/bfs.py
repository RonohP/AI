from collections import deque


class BfsTransverse:

    # Constructor
    def __init__(self):
        self.visited = []
        self.end_search = False

    def bfs(self, graph, start_node, goal_node):
        queue = [start_node]
        # print(queue)
        # set of visited nodes
        self.visited.append(start_node)
        while queue and not self.end_search:
            # Deque a vertex from
            s = queue.pop(0)
            print("Drive to", s, end="\n")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in list(graph[s]):
                if i not in self.visited:
                    print("Is this goal node", goal_node, "? Current Node ", i)
                    if i is goal_node:
                        self.end_search = True
                        print(self.end_search)
                        self.visited.append(i)
                        break
                    else:
                        print(self.end_search)
                        queue.append(i)
                        # visited[i] = True
                        self.visited.append(i)
        # return visited
