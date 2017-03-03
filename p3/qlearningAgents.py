# qlearningAgents.py
# ------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
  """
    Q-Learning Agent

    Functions you should fill in:
      - getQValue
      - getAction
      - getValue
      - getPolicy
      - update

    Instance variables you have access to
      - self.epsilon (exploration prob)
      - self.alpha (learning rate)
      - self.discountRate (discount rate)

    Functions you should use
      - self.getLegalActions(state)
        which returns legal actions
        for a state
  """
  def __init__(self, **args):
    "You can initialize Q-values here..."
    ReinforcementAgent.__init__(self, **args)
    self.valuesList = util.Counter()


  def getQValue(self, state, action):
    """
      Returns Q(state,action)
      Should return 0.0 if we never seen
      a state or (state,action) tuple
    """
    """Description:
    I intially did some complex code but then changed it to returning just the value
    of the list at the certain index of (state,action)
    """
    """ YOUR CODE HERE """
   
    temp = 0
    zero = 0 
    """
    for state2,action2 in self.valuesList:
        if state2 == state and action2 == action:
            temp2 = self.valuesList[(state,action)]
            temp = temp2
            break
        elif state2 != state or action2 != action:
            temp = zero
        else:
            temp = zero
    return temp
    """
    return self.valuesList[(state,action)]

    """ END CODE """



  def getValue(self, state):
    """
      Returns max_action Q(state,action)
      where the max is over legal actions.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return a value of 0.0.
    """
    """Description:
    Go through all the actions in the legal actions set and append
    to a list which contains the qvalue from that state to doing that action
    I return 0 if the length of the list is zero. Otherwise, return the maximum
    value of that list.  
    """
    """ YOUR CODE HERE """
    self.list2 = []
    self.zero = 0
    counter = 0

    def maxList(myList):
        temp = myList[0]
        for value in myList:
            if value > temp:
                temp = value
        return temp

    for myAction in self.getLegalActions(state):
        self.list2.append(self.getQValue(state,myAction))
        counter = counter + 1

    if counter == 0:
        return self.zero
    else:
        return max(self.list2) 
 
    """ END CODE """

  def getPolicy(self, state):
    """
      Compute the best action to take in a state.  Note that if there
      are no legal actions, which is the case at the terminal state,
      you should return None.
    """
    """Description:
    Finally found my stupid mistake! I did not say self.List3 and instead wrote List3. Basically in this
    method, I loop through all the legal actions meanwhile increasing a counter. I calculate the q value
    inside this method and set it to equal the value at the action inside a list. The list is defined as
    ac Counter from the util class. I then do the argMax() and return the value at the very end depending
    on the value of the counter. If the counter is 0, 0 is returned. Otherwise, the argMax() is returned
    """
    """ YOUR CODE HERE """
    myVal = self.getValue(state)
    self.myList3 = util.Counter()
    counter = 0
    emptyOrArgMax = None
    for myAction in self.getLegalActions(state):
        counter = counter + 1
        temp = self.getQValue(state,myAction)
        self.myList3[myAction] = temp
        emptyOrArgMax = self.myList3.argMax() 
    if counter == 0:
        return None
    else:
        return emptyOrArgMax  
    #util.raiseNotDefined()
    """ END CODE """

  def getAction(self, state):
    """
      Compute the action to take in the current state.  With
      probability self.epsilon, we should take a random action and
      take the best policy action otherwise.  Note that if there are
      no legal actions, which is the case at the terminal state, you
      should choose None as the action.

      HINT: You might want to use util.flipCoin(prob)
      HINT: To pick randomly from a list, use random.choice(list)
    """
    # Pick Action
    legalActions = self.getLegalActions(state)
    action = None

    """Description:
    In this method I used the hints provided and call teh flipCoin method.
    Depending on the returned value of flipCoin, either random.choice will
    be returned or the getPolicy method will be returned
    """
    """ YOUR CODE HERE """
    trueOrFalse = util.flipCoin(self.epsilon)
    possActions1 = random.choice(legalActions)
    possActions2 = self.getPolicy(state)
    if trueOrFalse:
        return possActions1
    else:
        return possActions2

    """ END CODE """

  def update(self, state, action, nextState, reward):
    """
      The parent class calls this to observe a
      state = action => nextState and reward transition.
      You should do your Q-Value update here

      NOTE: You should never call this function,
      it will be called on your behalf
    """
    """Description:
    This code finally works! Made some mistake up above which is fixed now. In this method,
    I loop through all the legal actions and append the qvalue of the nextState and the current
    action to the list created in this method. I then also increase a counter. Depending on the 
    counter's value, I then return either a value dependent on the max of the list or not.
    """
    """ YOUR CODE HERE """
    self.list4 = []
    counter = 0
    myRew = reward
    for myAction in self.getLegalActions(nextState):
        self.list4.append(self.getQValue(nextState,myAction))
        counter = counter + 1

    if counter != 0:
        self.valuesList[(state,action)] = (((1 - self.alpha) * (self.getQValue(state,action))) + (self.alpha * (self.discountRate * max(self.list4) + reward)))
    else:
        self.valuesList[(state,action)] = (((1 - self.alpha) * (self.getQValue(state,action))) + (self.alpha * reward)) 

    #util.raiseNotDefined()
    """ END CODE """

class PacmanQAgent(QLearningAgent):
  "Exactly the same as QLearningAgent, but with different default parameters"

  def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
    """
    These default parameters can be changed from the pacman.py command line.
    For example, to change the exploration rate, try:
        python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

    alpha    - learning rate
    epsilon  - exploration rate
    gamma    - discount factor
    numTraining - number of training episodes, i.e. no learning after these many episodes
    """
    args['epsilon'] = epsilon
    args['gamma'] = gamma
    args['alpha'] = alpha
    args['numTraining'] = numTraining
    self.index = 0  # This is always Pacman
    QLearningAgent.__init__(self, **args)

  def getAction(self, state):
    """
    Simply calls the getAction method of QLearningAgent and then
    informs parent of action for Pacman.  Do not change or remove this
    method.
    """
    action = QLearningAgent.getAction(self,state)
    self.doAction(state,action)
    return action


class ApproximateQAgent(PacmanQAgent):
  """
     ApproximateQLearningAgent

     You should only have to overwrite getQValue
     and update.  All other QLearningAgent functions
     should work as is.
  """
  def __init__(self, extractor='IdentityExtractor', **args):
    self.featExtractor = util.lookup(extractor, globals())()
    PacmanQAgent.__init__(self, **args)

    # You might want to initialize weights here.
    self.myWeights = util.Counter()


  def getQValue(self, state, action):
    """
      Should return Q(state,action) = w * featureVector
      where * is the dotProduct operator
    """
    """Description:
    Implemented this method but for some reason does not work
    """
    """ YOUR CODE HERE """
    self.tot = 0
    self.counter = 0
    for feat in self.featExtractor.getFeatures(state,action):
        self.counter = self.counter +1 
        self.tot += self.featExtractor.getFeatures(state,action)[feat] * self.myWeights[feat]
    if self.counter == 0:
        return self.tot 
    else:
        return 0
    """ END CODE """

  def update(self, state, action, nextState, reward):
    """
       Should update your weights based on transition
    """
    """Description:
    Implemented this method but for some reason does not work
    """
    """ YOUR CODE HERE """
    for feat in self.featExtractor.getFeatures(state,action):
        self.myWeights[feat] = self.alpha * ((reward + self.discountRate*self.getValue(nextState)) - self.getQValue(state,action)) * self.featExtractor.getFeatures(state,action)[feat]
    """ END CODE """

  def final(self, state):
    "Called at the end of each game."
    # call the super-class final method
    PacmanQAgent.final(self, state)

    # did we finish training?
    if self.episodesSoFar == self.numTraining:
      # you might want to print your weights here for debugging
      pass 
