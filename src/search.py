# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions


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

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def dfsHelper(problem, state, pact = None, visited = set()):
    """
    helper function for dfs
    used to carry over recursive stack trace args
    and return final path
    """
    path = []
    if problem.isGoalState(state):
        return [pact]
    for succ, act, _cost in problem.getSuccessors(state):
        if succ in visited: continue
        visited.add(succ)
        res = dfsHelper(problem, succ, act, visited)
        if len(res) > 0:
            path = [act] + res + path
    return path


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    return dfsHelper(problem, problem.getStartState())

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    Q = [[problem.getStartState(), []]]
    visited = set([problem.getStartState()])

    while len(Q) > 0:
        top = Q.pop()
        if problem.isGoalState(top[0]):
            return top[1]
        for succ, act, _cost in problem.getSuccessors(top[0]):
            if succ in visited: continue
            visited.add(succ)
            Q.insert(0, [succ, top[1]+[act]])
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    Q = util.PriorityQueue()
    paths = dict()
    Q.push(problem.getStartState(), 0)
    vis = set([problem.getStartState()])
    while not Q.isEmpty():
        best = Q.pop()
        if problem.isGoalState(best):
            return paths[best]
        for succ, act, cost in problem.getSuccessors(best):
            if succ in vis: continue
            vis.add(succ)
            Q.push(succ, cost)
            if paths.get(succ, 0) == 0:
                paths[succ] = paths.get(best, []) + [act]
            else:
                paths[succ].append(act)
    return max(paths.items(), key = lambda x: len(x[1]))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
