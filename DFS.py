def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    ans.append(start)
    while stack:
        print("STACK : ",stack)
        current_node = stack.pop()
        visited.add(current_node)
        if current_node not in ans:
            ans.append(current_node)

        if current_node == goal:
            return True

        for neighbor in graph[current_node]:
            if neighbor not in visited and neighbor not in stack:
                stack.append(neighbor)
    return False

graph = {
  'A' : ['B','D','E'],
  'B' : ['A', 'C','E'],
  'C' : ['B','E','F','G'],
  'D' : ['A','E'],
  'E' : ['A','B','C','D','F'],
  'F' : ['C','E','G'],
  'G' : ['C','F']
}
ans = []


start_node = input("Enter start node:")
goal_node = input("Enter goal node:")

dfs(graph, start_node, goal_node)
print("DFS traversal path : ",ans)
