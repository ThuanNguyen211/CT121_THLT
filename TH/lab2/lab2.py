# Họ và tên: Nguyen Minh Thuan
# MSSV: B2207568
# STT: 37

class DFA(object):
    def __init__(self, states, alphabet, transition_function, start_state, accept_state, current_state):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_state = accept_state
        self.current_state = current_state
        return

    def transition_to_state_with_input(self, input_value):
        if(self.current_state, input_value) not in self.transition_function.keys():
            self.current_state = None
            return
        self.current_state = self.transition_function[(self.current_state, input_value)]
        return
    
    def in_accept_state(self):
        return self.current_state in self.accept_state
    
    def go_to_initial_state(self):
        self.current_state = self.start_state
        return
    
    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            print(inp, self.current_state)
            continue
        return self.in_accept_state()

state = {0, 1, 2}
alphabet = {'0', '1'}
start_state = 0
accept_state = {0}
tf = dict()
tf[(0, '0')] = 0
tf[(0, '1')] = 1
tf[(1, '0')] = 2
tf[(1, '1')] = 0
tf[(2, '0')] = 1
tf[(2, '1')] = 2
L1 = list('1011101')
L2 = list('10111011')
current_state = None
dfa1 = DFA(state, alphabet, tf, start_state, accept_state, current_state)
# print('Input: ' + str(L1))
# print(dfa1.run_with_input_list(L1))
# print('Input: ' + str(L2))
# print(dfa1.run_with_input_list(L2))

