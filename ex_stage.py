import numpy

class Shift_reg:
    def __init__(self, *args, **kwargs):
        # Size of shift registers (nxn bytes)
        self.shift_size = kwargs['ss'] if 'ss' in kwargs else 16
        # Shift register name
        self.name = kwargs['name'] if 'name' in kwargs else 'Default register'
        # Constructing shift register
        self.reg = [[0 for row in range(self.shift_size)] for col in range(self.shift_size)]

    def shift(self, data_in):
        # Check sizes, throw error if mismatch
        if len(data_in) != shift_size:
            print "ERROR: Data width " + len(data_in) + ", " \
                + "expected width " + self.shift_size
            exit(1)
        # Pop first row, push input into last row
        output = self.reg.pop(0)
        self.reg.append(data_in)
        # Return 'popped' output
        return output

    def reset(self):
        self.reg = [[0 for row in range(self.shift_size)] for col in range(self.shift_size)]

class ALU:
    def add(op1, op2):
        return op1 + op2

    def sub(op1, op2):
        return op1 - op2

    def mult(op1, op2):
        return op1 * op2

    def comp(op1, op2):
        if op1 > op2:
            return 1
        elif op1 < op2:
            return -1
        else:
            return 0

class Reduce:
    def add(op1, op2):
        return op1 + op2

    def max(op1, op2):
        return numpy.max(op1, op2)

class Interface:
    def __init__(self, *args, **kwargs):
        # Size of convolution window (nxn bytes)
        self.window_size = kwargs['ws'] if 'ws' in kwargs else 1
        # Number of ALU functional units
        self.alu_num = kwargs['alu'] if 'alu' in kwargs else 64

    # Flatten 2d input array into 1d output array
    def generate(self, data_in):
        if len(data_in) != self.window_size or \
            len(data_in[0]) != self.window_size:
            print "ERROR: Data width " + len(data_in) + ", " \
                + "expected width " + self.window_size
            exit(1)

        output = []
        for row in len(data_in):
            output.append(data_in(row))
        return output

class ex_stage:
    def __init__(self, *args, **kwargs):
        # Size of convolution window (nxn bytes)
        self.window_size = kwargs['ws'] if 'ws' in kwargs else 1
        # Size of input image (nxn bytes)
        self.image_size = kwargs['is'] if 'is' in kwargs else 256
        # Size of shift registers (nxn bytes)
        self.shift_size = kwargs['ss'] if 'ss' in kwargs else 16
        # Number of ALU functional units
        self.alu_num = kwargs['alu'] if 'alu' in kwargs else 64

        # Reduction tree depth
        self.re_depth = int(numpy.ceil( numpy.log2(self.alu_num) ))

        self.input_data = Shift_reg(ss=self.shift_size)
        self.coeff_data = Shift_reg(ss=self.window_size)
        self.input_if   = Interface(ws = self.window_size)
        self.coeff_if   = Interface(ws = self.window_size)
        self.alu_array  = [ALU() for _ in range(self.alu_num)]
        self.reduce_tree = [[Reduce() for _ in range(2^(depth-1))] for depth in reversed(range(self.re_depth))]


    # Load coefficients
    def load_coefficients():
        pass

    # Load next input pixels
    def shift_next_input():
        pass

    # Perform 2d convolution:
    def convolve_2d():
        pass

