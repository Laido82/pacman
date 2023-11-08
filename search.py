# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from util import Stack
from util import PriorityQueue
from util import Queue


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    return [w, w, w, w, s, s, e, s, s, w]


def depthFirstSearch(problem):
    stack = Stack()
    visited = set()
    start_state = problem.getStartState()

    vertex = {"from": None, "to": None, "current_pos": start_state}
    stack.push(vertex)

    while not stack.isEmpty():
        vertex = stack.pop()
        current_state = vertex["current_pos"]
        if current_state in visited:
            continue

        visited.add(current_state)
        if problem.isGoalState(current_state):
            break

        for action in problem.getActions(current_state):
            next_state = problem.getNextState(current_state, action)
            if next_state not in visited:
                next_vertex = {"from": vertex, "to": action, "current_pos": next_state}
                stack.push(next_vertex)
    return getPath(vertex)


def getPath(vertex):
    actions = []
    while vertex["from"] != None:
        actions.insert(0, vertex["to"])
        vertex = vertex["from"]
    return actions


def breadthFirstSearch(problem):
    queue = Queue()

    visited = set()

    start_state = problem.getStartState()

    vertex = {"from": None, "to": None, "current_pos": start_state}

    print(problem.getActions(start_state))

    queue.push(vertex)

    while not queue.isEmpty():
        vertex = queue.pop()
        current_pos = vertex["current_pos"]
        if current_pos in visited:
            continue

        visited.add(current_pos)
        if problem.isGoalState(current_pos):
            break

        for action in problem.getActions(current_pos):
            next_state = problem.getNextState(current_pos, action)
            if next_state not in visited:
                next_vertex = {"from": vertex, "to": action, "current_pos": next_state}
                queue.push(next_vertex)

    return getPath(vertex)


def uniformCostSearch(problem):
    "Search the node of least total cost first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    start = problem.getStartState()
    queue = PriorityQueue()
    visited = set()

    vertex = {"from": None, "to": None, "current_pos": start}
    cost = {}
    queue.push(vertex, 0)
    cost[start] = 0

    while not queue.isEmpty():
        vertex = queue.pop()
        state = vertex["current_pos"]
        if problem.isGoalState(state):
            break

        visited.add(vertex["current_pos"])

        for next_state, action, stepCost in problem.expand(state):
            new_cost = cost[state] + stepCost
            if next_state not in visited:
                cost[next_state] = new_cost
                total_cost = new_cost + heuristic(next_state, problem)
                next_vertex = {"from": vertex, "to": action, "current_pos": next_state}
                queue.update(next_vertex, total_cost)

    return getPath(vertex)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
