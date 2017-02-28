# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """
  def __init__(self, mdp, discountRate = 0.9, iters = 100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.

      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
    """
    self.mdp = mdp
    self.discountRate = discountRate
    self.iters = iters
    self.values = util.Counter() # A Counter is a dict with default 0
    """Description:
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    #self.values2 = util.Counter()
    self.counter = 0 
    self.low = -9999999999999999999 #negative infinity
    self.values2 = util.Counter()   
 
    def findMinimum(val1,val2):
        if val1 >= val2:
            return val2
        else:
            return val1
   
    def findMaximum(val1,val2):
        if val1 > val2:
            return val1
        else:
            return val2
 
    for myState in self.mdp.getStates(): 
        if self.mdp.isTerminal(myState):
            self.values2[myState] = 0;
    
    while(self.counter <= (self.iters - 1)):
        values2 = util.Counter()
        for myState in self.mdp.getStates(): 
            if not self.mdp.isTerminal(myState):
                self.low = -999999999999999999
                for myAction in self.mdp.getPossibleActions(myState):
                    myTot = self.getQValue(myState,myAction)
                    if self.low == findMinimum(self.low,myTot):
                        self.low = findMaximum(myTot,self.low)
                values2[myState] = self.low
            else:
                values2[myState] = 0
        self.counter = self.counter + 1
        self.values = values2    

    """ END CODE """

  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """
    """Description:
    I just returned the value for a state using the list I have defined
    """
    """ YOUR CODE HERE """
    return self.values[state]
    #util.raiseNotDefined()
    """ END CODE """

  def getQValue(self, state, action):
    """
      The q-value of the state action pair
      (after the indicated number of value iteration
      passes).  Note that value iteration does not
      necessarily create this quantity and you may have
      to derive it on the fly.
    """
    """Description:
    """
    """ YOUR CODE HERE """
    qvalTot = 0
    for myState, myProbab in self.mdp.getTransitionStatesAndProbs(state,action):
        qvalTot = qvalTot + (myProbab * (self.mdp.getReward(state,action,myState) + (self.discountRate * self.values[myState])))
    return qvalTot     
    """ END CODE """

  def getPolicy(self, state):
    """
      The policy is the best action in the given state
      according to the values computed by value iteration.
      You may break ties any way you see fit.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """

    """Description:
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    #util.raiseNotDefined()
    values3 = util.Counter()
    possActions = self.mdp.getPossibleActions(state)
    result = 0

    if len(possActions) <= 0:
        return None

    if len(possActions) > 0:
      for myAction in possActions:
        qvalTot = 0
        for myState, myProbab in self.mdp.getTransitionStatesAndProbs(state,myAction):
            qvalTot = qvalTot + (myProbab * (self.mdp.getReward(state,myAction,myState) + (self.discountRate * self.values[myState])))
        values3[myAction] = qvalTot
      result = values3.argMax()

    return result
    """ END CODE """

  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.getPolicy(state)
