# analysis.py
# -----------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

######################
# ANALYSIS QUESTIONS #
######################

# Change these default values to obtain the specified policies through
# value iteration.

def question2():
  answerDiscount = 0.9
  answerNoise = 0.005
  """Description:
  I changed values that would best fit the discount value and the noise 
  value and returned those values. I kept tweaking the values until the
  results I was looking for appeared
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise

def question3a():
  answerDiscount = 0.5
  answerNoise = 0.001
  answerLivingReward = -1
  """Description:
  Kept adjusting the values till I got the result that was expected. I put a huge
  living reward to get the expected output 
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3b():
  answerDiscount = 0.5
  answerNoise = 0.4
  answerLivingReward = -0.3
  """Description:
  Kept adjusting the values until I got the result. I mostly changed the living 
  reward and it seemed that made the most effect for me.
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3c():
  answerDiscount = 1
  answerNoise = 0.001
  answerLivingReward = -0.3
  """Description:
  I kept changing the values, mainly the answerDiscount until I got the result I was looking for
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3d():
  answerDiscount = 0.9
  answerNoise = 0.2
  answerLivingReward = 0.0
  """Description:
  I did not change the code for this question 
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3e():
  answerDiscount = 0.9
  answerNoise = 0.2
  answerLivingReward = 0.0
  """Description:
  I did not change the code for this question 
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question6():
  answerEpsilon = None
  answerLearningRate = None
  """Description:
  Returned not possible in this question with the epsilon and
  the answerLearningRate. Forgot to change this earlier as a heads up
  but changed it in last or some of most recent solutions.
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return 'NOT POSSIBLE' 
  # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
  print 'Answers to analysis questions:'
  import analysis
  for q in [q for q in dir(analysis) if q.startswith('question')]:
    response = getattr(analysis, q)()
    print '  Question %s:\t%s' % (q, str(response))
