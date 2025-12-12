from src.helpers.turing_machine import TuringMachineSimulator


# ==========================================
# PROGRAM 1: Nondeterministic TM [cite: 137]
# ==========================================
class NTM_Tracer(TuringMachineSimulator):
    class Config:
        def __init__(self, config, parent=None, transition=None, depth=0):
            self.config = config   # left, state, right
            self.parent = parent   # config or none
            self.transition = transition # trans_dict
            self.depth = depth
    
    def get_head_symbol(self, config):      
        # symbol is under head Γ 
        left,q,right = config
        return "_" if right == "" else right[0] 
    
    def apply_transition(self, config, trans_dict):  
        # δ(Q×Γ) → (Q×Γ×{L,R}
        left,q,right = config   
        next_q = trans_dict['next'] 
        write_symbol = trans_dict['write'][0]
        move_dir = trans_dict['move'][0]
        
        # write symbol at head
        if right == "":
            new_right = write_symbol
        else:
            new_right = write_symbol + right[1:]
        new_left = left
    
        if move_dir == "R":
            if new_right == "":
                new_left = new_left + "_"
                new_right = ""
            else: 
                new_left = new_left + new_right[0]
                new_right = new_right[1:]
        
        elif move_dir == "L":
            if new_left == "":
                new_left = ""
                new_right = "_" + new_right
            else:
                new_right = new_left[-1] + new_right
                new_left = new_left[:-1]
        
        return [new_left,next_q,new_right]  

    def run(self, input_string, max_depth):
        """
        Performs a Breadth-First Search (BFS) trace of the NTM.
        Ref: Section 4.1 "Trees as List of Lists" [cite: 146]
        """
        print(f"Tracing NTM: {self.machine_name} on input '{input_string}'")

        # Initial Configuration: ["", start_state, input_string]
        # Note: Represent configuration as triples (left, state, right) [cite: 156]
        initial_config = ["", self.start_state, input_string]
        root = NTM_Tracer.Config(initial_config, parent=None, transition=None, depth=0)  

        # the tree is a list of lists of configurations
        tree = [[root]]

        depth = 0
        accepted = False
        accepting_n = None
        total_transitions = 0
        max_reject_depth = 0

        while depth < max_depth and not accepted:
            current_level = tree[-1]
            next_level = []
            all_rejected = True
            
            for n in current_level:
                left,q,right = n.config
                
                if q == self.accept_state:  
                    accepted = True
                    accepting_n = n
                    break
                if q == self.reject_state:
                    
                    if n.depth > max_reject_depth:
                        max_reject_depth = n.depth
                    continue
                #non-halting
                read_sym = self.get_head_symbol(n.config)
                read_symbols = (read_sym,)
                valid_trans = self.get_transitions(q,read_symbols)
            
                if valid_trans:
                    all_rejected = False
                for t in valid_trans:
                    child_config = self.apply_transition(n.config,t)  
                    child_n = NTM_Tracer.Config(
                        config = child_config,      
                        parent=n,
                        transition=t,
                        depth=depth + 1,
                    )
                    next_level.append(child_n)
                    total_transitions += 1
            
            if accepted:
                break
            if not next_level:
                # all paths rejected [cite: 217]
                print(f"String rejected in {max_reject_depth} steps.")
                print(f"\nDepth of tree: {depth}")
                print(f"\nTotal transitions simulated: {total_transitions}")
                self.print_nondeterminism_degree(tree)
                return
            
            tree.append(next_level)
            depth += 1

        if accepted:
            print(f"String accepted in {accepting_n.depth} steps.")
            self.print_trace_path(accepting_n)
        elif depth >= max_depth:
            print(f"Execution stopped after {max_depth} steps.")

        print(f"\nDepth of tree: {depth}")
        print(f"\nTotal transitions simulated: {total_transitions}")
        self.print_nondeterminism_degree(tree)

    def print_nondeterminism_degree(self, tree):
        """
        Calculate and print degree of nondeterminism.
        Ref: Section 4.3 [cite: 231]
        Average number of new configurations from each non-halting configuration.
        """
        total_configs = 0
        total_successors = 0
        
        for level_idx in range(len(tree) - 1):
            level = tree[level_idx]
            next_level = tree[level_idx + 1]
            
            non_halting = 0
            for n in level:
                left, q, right = n.config
                if q != self.accept_state and q != self.reject_state:
                    non_halting += 1
            
            if non_halting > 0:
                total_configs += non_halting
                total_successors += len(next_level)
        
        if total_configs > 0:
            degree = total_successors / total_configs
            print(f"Degree of nondeterminism: {degree:.2f}")
        else:
            print("Degree of nondeterminism: 1.00 (deterministic)")

    def print_trace_path(self, final_node):
        """
        Backtrack and print the path from root to the accepting node.
        Ref: Section 4.2 [cite: 165]
        """
        path = []
        node = final_node
        while node is not None:
            path.append(node)
            node = node.parent
        path.reverse()

        print("=== Accepting path ===")
        for step, n in enumerate(path):
            left, state, right = n.config
            print(f"Step {step}: ({left!r}, {state}, {right!r})")
            if n.transition is not None:
                t = n.transition
                # The previous state is in the parent node
                prev_state = n.parent.config[1] if n.parent else state
                read_sym = t['read'][0]
                print(f"   via: δ({prev_state!r}, {read_sym!r}) -> ({t['next']!r}, {t['write'][0]!r}, {t['move'][0]})")
