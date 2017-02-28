# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """


  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    "Add more of your code here if you want to"

    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (oldFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPosition = successorGameState.getPacmanPosition()

    # All food variables created here
    oldFood = currentGameState.getFood()
    foodLeft = successorGameState.getFood()
    foodLeftList = foodLeft.asList()

    # All ghost variables created here 
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    ghostOne = currentGameState.getGhostPosition(1)

    # The rest of the varibles are created here
    totScore = 0
    normalize = 50 
    ghostOnetoPacman = util.manhattanDistance(ghostOne,newPosition)

    # Return 0 or the normalized value depending on what the food value is
    def numFoodFunc(currentGameState,successorGameState):
        curNum = currentGameState.getNumFood()
        sucNum = successorGameState.getNumFood()
        if sucNum >= curNum:
            return 0
        else:
            return normalize

    # Find the minimum of the food list passed in as a parameter
    def findMinimum(foodLeftList):
        bigFoodDist = normalize
        for foodItem in foodLeftList:
            newDistance = util.manhattanDistance(foodItem,newPosition)
            if bigFoodDist < newDistance:
                continue
            else:
                bigFoodDist = newDistance
        return bigFoodDist

    # Add up all the scores that make up the total score 
    totScore += ghostOnetoPacman 
    totScore += successorGameState.getScore() 
    totScore -= findMinimum(foodLeftList)
    totScore += numFoodFunc(currentGameState,successorGameState)
        
    return totScore

def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.treeDepth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 2)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.treeDepth
      and self.evaluationFunction.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game
    """

    # All the variables are created right here
    treeDepth = self.treeDepth #the tree depth as global variable
    numAgentsWithPac = gameState.getNumAgents()
    actionChosen = Directions.STOP #initial action set -> will be used later
    worstUtility = -9999999999
    nextWorstUtil = -9999999999
    turnSet = 1 #variable set for choosing which min's turn it is    

    """
     This method will find the minimum value between the two utilities
     it recieves as input
    """
    def findMin(value1, value2):
        if value1 < value2:
            return value1
        else:
            return value2

    """
     This method will find the maximum value between the two utilities
     it recieves as input
    """
    def findMax(value1, value2):
        if value1 > value2:
            return value1
        else:
            return value2
 
    """
     This will do the normal max part of the minimax algorithm pseudocode that can
     be found in the slides and in the book
    """ 
    def doMax(gameState, treeDepth, turnSet):
        if gameState.isWin() or gameState.isLose() or treeDepth == 0:
            return self.evaluationFunction(gameState)
        utility = -999999999 #basically negative infinity

        """
         Pacman scans through all possible actions it could take and finds
         the maximum value it can get out of the ones returned.
        """
        for moveLeft in gameState.getLegalActions(0):
            utility = findMax(utility, doMin(gameState.generateSuccessor(0, moveLeft), treeDepth - 1, turnSet))
        return utility
   
    """
     This will do the normal min part of the minimax algorithm pseudocode that can
     be found in the slides and in the book
    """  
    def doMin(gameState, treeDepth, turnSet):
        "numghosts = len(gameState.getGhostStates())"
        if gameState.isWin() or gameState.isLose() or treeDepth == 0:
            return self.evaluationFunction(gameState)
        utility = 9999999999 #basically positive infinity

        """
         Depending on the value of turnSet either the first ghost will move
         or the second ghost will move. In this case the second ghost moves first.

         The bottom if statement allows the second ghost to go next instead of
         pacman. Pacman will move after both these ghosts move.
        """
        if turnSet == 0:
            for moveLeft in gameState.getLegalActions(2):
                turnSet = 1;
                utility = findMin(utility, doMax(gameState.generateSuccessor(2, moveLeft), treeDepth - 1, turnSet))
        elif turnSet == 1:
            for moveLeft in gameState.getLegalActions(1):
                turnSet = 0;
                utility = findMin(utility, doMin(gameState.generateSuccessor(1, moveLeft), treeDepth, turnSet))

        return utility

    """
     This method calls the doMin method which respectively calls the doMax and
     doMin interchangeably. It calls them interchangeably to allow the turn based
     based moves between the pacman and the ghosts.
    """
    def doMinimax(gameState, worstUtility, turnSet, treeDepth, actionChosen):
        """
         This for loop is for all the possible movements that could be made.
         They need to be looped through so that all positions are considered.
        """
        for moveLeft in gameState.getLegalActions():
            nextWorstUtil = worstUtility
            worstUtility = findMax(worstUtility, doMin(gameState.generateSuccessor(0, moveLeft), treeDepth, turnSet))
            if worstUtility <= nextWorstUtil:
                continue
            else:
                actionChosen = moveLeft
        return actionChosen

    finalAction = doMinimax(gameState, worstUtility, turnSet, treeDepth, actionChosen)
    return finalAction

    #util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action using self.treeDepth and self.evaluationFunction
    """
    treeDepth = self.treeDepth #the tree depth as global variable
    numAgentsWithPac = gameState.getNumAgents()
    actionChosen = Directions.STOP #initial action set -> will be used later
    worstUtility = -9999999999
    nextWorstUtil = -9999999999
    alphaVal = -9999999999 
    betaVal = 9999999999
    turnSet = 1 #variable set for choosing which min's turn it is    

    """
     This method will find the minimum value between the two utilities
     it recieves as input
    """
    def findMin(value1, value2):
        if value1 < value2:
            return value1
        else:
            return value2

    """
     This method will find the maximum value between the two utilities
     it recieves as input
    """
    def findMax(value1, value2):
        if value1 > value2:
            return value1
        else:
            return value2

    """
     This will do the normal max part of the minimax algorithm pseudocode that can
     be found in the slides and in the book
    """ 
    def doMax(gameState, treeDepth, turnSet, alphaVal, betaVal):
        if gameState.isWin() or gameState.isLose() or treeDepth == 0:
            return self.evaluationFunction(gameState)
        utility = -9999999999 #basically negative infinity

        """
         Pacman scans through all possible actions it could take and finds
         the maximum value it can get out of the ones returned.
        """
        for moveLeft in gameState.getLegalActions(0):
            utility = findMax(utility, doMin(gameState.generateSuccessor(0, moveLeft), treeDepth - 1, turnSet, alphaVal, betaVal))
            """
             This basically checks to make sure the betaVal is greater than the utility value. If not
             the utility value will get returned. It then finds the maximum between the current alpha value and
             the utility value recieved and set that as the new utility value.
            """
            if utility >= betaVal:
                return utility
            else: 
                alphaVal = findMax(alphaVal, utility)
        return utility
    """
     This will do the normal min part of the minimax algorithm pseudocode that can
     be found in the slides and in the book
    """  
    def doMin(gameState, treeDepth, turnSet, alphaVal, betaVal):
        "numghosts = len(gameState.getGhostStates())"
        if gameState.isWin() or gameState.isLose() or treeDepth == 0:
            return self.evaluationFunction(gameState)
        utility = 9999999999 #basically positive infinity

        """
         Depending on the value of turnSet either the first ghost will move
         or the second ghost will move. In this case the second ghost moves first.

         The bottom if statement allows the second ghost to go next instead of
         pacman. Pacman will move after both these ghosts move.
        """
        if turnSet == 0:
            for moveLeft in gameState.getLegalActions(2):
                turnSet = 1;
                utility = findMin(utility, doMax(gameState.generateSuccessor(2, moveLeft), treeDepth - 1, turnSet, alphaVal, betaVal))
                if utility <= alphaVal:
                    return utility
                else:
                    betaVal = findMin(betaVal, utility)
        elif turnSet == 1:
            for moveLeft in gameState.getLegalActions(1):
                turnSet = 0;
                utility = findMin(utility, doMin(gameState.generateSuccessor(1, moveLeft), treeDepth, turnSet, alphaVal, betaVal))
                """
                 This basically checks to make sure the alphaVal is greater than the utility value. If not
                 the utility value will get returned. It then finds the minimum between the current beta value
                 and the utility value recieved and set that as the new utility value.
                """
                if utility <= alphaVal:
                    return utility
                else:
                    betaVal = findMin(betaVal, utility)
        return utility

    """
     This is the minimax main that will call the max portion first because it's first pacman's turn
    """
    def doMinimax(gameState, worstUtility, turnSet, treeDepth, actionChosen, alphaVal, betaVal):
        """
         This for loop is for all the possible movements that could be made.
         They need to be looped through so that all positions are considered.
        """
        for moveLeft in gameState.getLegalActions():
            nextWorstUtil = worstUtility
            worstUtility = findMax(worstUtility, doMin(gameState.generateSuccessor(0, moveLeft), treeDepth, turnSet, alphaVal, betaVal))
            if worstUtility <= nextWorstUtil:
                continue
            else:
                actionChosen = moveLeft
        return actionChosen

    finalAction = doMinimax(gameState, worstUtility, turnSet, treeDepth, actionChosen, alphaVal, betaVal)
    return finalAction



class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.treeDepth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """

    """
     Calculating the average of the list and returing that value
    """
    def calcAvg(myList):
        myList = list(myList)
        return sum(myList)/len(myList)

    """
     This method does all the calculations for expectimax. This
     method gets called below
    """
    def lookDepth(state, depth, agent):
        """
         Calls this same method again when agent == state.getNumAgents() or 
         the evaluationFunction instead
        """
        if agent == state.getNumAgents():
            if depth != self.treeDepth:
                return lookDepth(state, depth + 1, 0)
            else:
                return self.evaluationFunction(state)
        else:
            actions = state.getLegalActions(agent)

            # If the length is equal to 0, call the evaluationFunction
            if len(actions) == 0:
                return self.evaluationFunction(state)

            """
             Creates a tuple called nextVals with a for loop and calling lookDepth
             inside the tuple.
            """
            nextVals = (
                lookDepth(state.generateSuccessor(agent, action), depth, agent + 1)
                for action in actions
            )

            # Returns the max of the values choses. The tuple is passed in to a method
            # of either max or calcAvg
            if (agent == 0):
                return max(nextVals)
            else:
                return calcAvg(nextVals)

    """
     This method returns the max between the legalstates and the 
     lookdepth method. The lookDepth is passed in with the lambda function
    """
    def doExpecti():
        return max(
            gameState.getLegalActions(0),
            key = lambda x: lookDepth(gameState.generateSuccessor(0, x), 1, 1)
        )

    return doExpecti()

def betterEvaluationFunction(currentGameState):
  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    Not enough time to attempt this question
  """
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
  """
    Your agent for the mini-contest
  """

  def getAction(self, gameState):
    """
      Returns an action.  You can use any method you want and search to any depth you want.
      Just remember that the mini-contest is timed, so you have to trade off speed and computation.

      Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
      just make a beeline straight towards Pacman (or away from him if they're scared!)
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

