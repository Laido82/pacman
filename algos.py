def depthFirstSearch(problem, state=None, visited=None, vertex=None):

    if problem.isGoalState(state):
        path = []
        while vertex["from"] != None:
            path.insert(0, vertex["to"])
            vertex = vertex["from"]
        return path

    if state is None:
        state = problem.getStartState()

    if visited is None:
        visited = set()

    for action in problem.getActions(state):
        child = problem.getNextState(state, action)
        if problem.getNextState(state, action) not in visited:
            new_vertex = {"from": vertex, "to": action,
                          "current_state": child}
            visited.add(child)
    return depthFirstSearch(problem, child, visited, new_vertex)
