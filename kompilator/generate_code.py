class generator():
        
    def __init__(self):
        self.variables = dict()
        self.free_space = [0]
        self.cmd = []
        self.r = [0 for _ in range(8)]
        self.main_start = 2
        
    def program_start(self, line):
        # self.cmd.append(f"JUMP {line}")
        self.cmd = [f"JUMP {line}"] + self.cmd
        
    def add_variable(self, id):
        self.variables[id] = self.free_space[-1]
        if len(self.free_space) < 2: self.free_space[0] += 1
        else: del self.free_space[-1]
        
    def get_variable(self, id):
        if id in self.variables:
            return self.variables[id]
        return -1
    
    def read_value(self, id):
        if not id in self.variables:
            return -1
        self.cmd.append("READ")
        self.r[0] = -1               # value
        x = self.r.index(0)          # first empty register {r_x}
        self.cmd.append(f"PUT {x}")  # putting value to register {r_x}
        
        
    def assign_num(self, value):
        if value <= 0: 
            self.cmd.append("RST 0")
            return
        self.cmd.append("RST 0")
        self.cmd.append("RST 4")
        self.cmd.append("INC 4")
        for c in reversed(bin(value)[2:]):
            if c == '1': self.cmd.append("ADD 4")
            self.cmd.append("SHL 4")
        self.cmd.append("RST 4")
                
    
    def assign(self, id, value):
        if not id in self.variables:
            return -1
        mem_location = self.variables[id]
        self.assign_num(mem_location)
        self.cmd.append("PUT 1")
        self.assign_num(value)
        self.cmd.append("STORE 1")
        self.cmd.append("RST 1")
        
        
            