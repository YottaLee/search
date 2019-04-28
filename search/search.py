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


class Node(object):
    def __init__(self, state, state_list, path, cost):
        self.state = state
        self.state_list = state_list
        self.path = path
        self.cost = cost



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
    "*** YOUR CODE HERE ***"
    from util import Stack
    visitedPath = Stack()
    visitPath = []
    visitedNode = []
    stack = Stack()
    stack.push(problem.getStartState())
    current = stack.pop()
    while not problem.isGoalState(current):
        if current not in visitedNode:
            visitedNode.append(current)
            nextNodes = problem.getSuccessors(current)
            for neighbour in nextNodes:
                currentPath = visitPath + [neighbour[1]]
                stack.push(neighbour[0])
                visitedPath.push(currentPath)
        current = stack.pop()
        visitPath = visitedPath.pop()
    return visitPath





def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    visitedPath = Queue()
    visitPath = []
    visitedNode = []
    queue = Queue()
    queue.push(problem.getStartState())
    current = queue.pop()
    while not problem.isGoalState(current):
        if current not in visitedNode:
            visitedNode.append(current)
            nextNodes = problem.getSuccessors(current)
            for neighbour in nextNodes:
                currentPath = visitPath + [neighbour[1]]
                queue.push(neighbour[0])
                visitedPath.push(currentPath)
        current = queue.pop()
        visitPath = visitedPath.pop()
    return visitPath

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue

    priorityqueue = PriorityQueue()
    priorityqueue.push((problem.getStartState(), [], 0),0)
    visitedNode = []
    while priorityqueue:
        current = priorityqueue.pop()
        if current[0] not in visitedNode:
            visitedNode.append(current[0])
            if problem.isGoalState(current[0]):
                return current[1]
            nextNodes = problem.getSuccessors(current[0])
            for neighbours in nextNodes:
                currentPath = current[1] + [neighbours[1]]
                currentCost = current[2] + neighbours[2]
                priorityqueue.push((neighbours[0],currentPath, currentCost),currentCost)



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"




    from util import PriorityQueue
    priorityqueue = PriorityQueue()
    initCost = 0
    priorityqueue.push((problem.getStartState(), [], initCost),initCost+heuristic(problem.getStartState(), problem))
    visitedNode = []
    while priorityqueue:
        current = priorityqueue.pop()
        if current[0] not in visitedNode:
            visitedNode.append(current[0])
            if problem.isGoalState(current[0]):
                return current[1]
            nextNode = problem.getSuccessors(current[0])
            for neighbour in nextNode:
                currentPath = current[1] + [neighbour[1]]
                currentCost = current[2] + neighbour[2]
                priorityqueue.push((neighbour[0], currentPath, currentCost), currentCost+heuristic(neighbour[0], problem))




    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
