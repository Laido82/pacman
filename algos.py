def dfs(problem, state, visited, path):

    if problem.isGoalState(state):
        return path
    if path is None:
        path = []
    if visited is None:
        visited = set()

    print("state : ", state, "actions : ", problem.getActions(state))

    for child in problem.getActions(state):
        if problem.getNextState(state, child) not in visited:
            visited.add(problem.getNextState(state, child))
            path.append(child)
            return dfs(problem, problem.getNextState(state, child), visited, path)
