from __future__ import annotations # Really?
from typing import Dict, List, Optional, Tuple
from interface import Action, Assignment1Domain, State

from policy import Policy

class ValueFunction: 
    '''
    This class implements a value function, 
    i.e., a mapping from states to floats.
    Given a value function V, the value of state s can be accessed and modified via:
      V[s]
    '''
    _domain: Assignment1Domain
    _values: Dict[State,float]
    _default_value: float

    def __init__(self, domain: Assignment1Domain, default_value: Optional[float] = 0): 
        self._domain = domain
        self._values = {  }
        self._default_value = default_value

    def __getitem__(self, state: State) -> float: 
        '''
        Defines accessor V[s]
        '''
        if state in self._values:
            return self._values[state]
        return self._default_value

    def __setitem__(self, state: State, value: float) -> None:
        '''
        Defines getter V[s]
        '''
        self._values[state] = value

    def q_value(self, state: State, action: Action, gamma: float) -> float:
        '''
        Returns the Q value of the specified action in the specified state, 
        using the current value function, with the specified discount factor gamma.
        '''
        # TODO
        return -1
    
    def compute_single_policy_backup(self, policy: Policy, gamma: float) -> Tuple[ValueFunction, float]:
        '''
        Performs a policy backup on the current value function 
        and using the specified policy.  
        This method does not modify the current value function; 
        instead it returns a new value function, 
        together with the error associated with the backup operation.
        '''
        # TODO
        return self, -1

    def compute_bellmann_backup(self, gamma: float) -> Tuple[ValueFunction, float]:
        '''
        Performs a Bellmann Backup of the current value function 
        with the specified discount factor.
        This method does not modify the current value function; 
        instead it returns a new value function, 
        together with the Bellmann error.
        '''
        # TODO
        return self, 0

    def greedy_action(self, state: State, gamma: float) -> Tuple[Action,float]:
        '''
        Computes the greedy action that should be performed in the specified state 
        according to the current value function.
        This method also returns the Q value of the greedy action.
        '''
        # TODO
        return Action(), 0

    def greedy_policy(self, gamma: float) -> Policy:
        '''
        Computes the greedy policy of this value function.
        '''
        pol = Policy(self._domain)
        for state in self._domain.get_observation_space().get_elements():
            pol[state] = self.greedy_action(state, gamma)[0]
        return pol


    def print(self) -> None: 
        '''
        Prints out this value.
        '''
        print("+++++++")
        print("Values:")
        for state, value in self._values.items():
            print("State {} -> {}".format(state, value))


def compute_value_function_of_policy(pol: Policy, gamma: float, epsilon: Optional[float] = 0.01) -> ValueFunction:
    '''
    Computes an approximated value function of the specified policy (V_{pi})
    by running the iterative algorithm described in the lecture.
    '''
    # TODO
    return ValueFunction(pol.get_domain())
