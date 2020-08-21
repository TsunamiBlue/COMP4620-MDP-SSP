from vi import ValueIteration
from statemachine import StateMachine, SMTransition

def hard_instance() -> StateMachine: 
    '''
  Creates an MDP that is as hard as possible for VI to find a good approximation. 
  The MDP should be built on top of the StateMachine framework available in the file statemachine.py
  The restrictions are as follows: 
  1. The state machine contains six states, named s1 to s6.  
     The initial state is s1.  
     Only one action, a1, is available in s6; 
     this action costs 0 and loops on state s6.
  2. The cost of any action is always in the interval [0,1].
  3. The probability of a transition from one state to another 
     is either 0 or at least 0.1.
    '''
    # TODO
    return StateMachine(
        [
        ], "s1"
    )

if __name__ == '__main__':
    domain = hard_instance()
    vi = ValueIteration(domain, gamma=1)
    vi.backup(epsilon = 0.5) # Notice that the value of 0.5 is very large!
    print("Number of iterations: {}".format(vi.nb_iterations()))
