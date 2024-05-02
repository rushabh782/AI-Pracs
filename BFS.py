graph = {
  'A' : ['B','D','E'],
  'B' : ['A', 'C','E'],
  'C' : ['B','E','F','G'],
  'D' : ['A','E'],
  'E' : ['A','B','C','D','F'],
  'F' : ['C','E','G'],
  'G' : ['C','F']
}

visited = []
queue = []
ans = []

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    print(f"QUEUE :  ['{node}']")
    while queue:
        m = queue.pop(0)
        ans.append(m)
        if m == goal:
            print("\nQUEUE : ",queue)
            break

        for neighbor in graph[m]:
            if neighbor not in visited and neighbor:
                visited.append(neighbor)
                queue.append(neighbor)
        print("\nQUEUE : ",queue)

node = input("Enter the start node : ")
goal = input("Enter the goal node : ")
bfs(visited,graph,node)
print("BFS TRAVERSAL PATH : ",ans)