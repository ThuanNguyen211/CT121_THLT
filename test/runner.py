import cnf 
import sys

filename = 'input_1.txt'
grammar, start, terminal = cnf.read_grammar(filename)
print(grammar,"\n",start,"\n",terminal)

r = cnf.convert_to_cnf(grammar, terminal)

# {'S': [['A'], ['A', 'b', 'A']], 'A': [['a', 'A'], ['a'], ['B']], 'B': [['b', 'B'], ['b']]} 
# S 
# ['a', 'b']