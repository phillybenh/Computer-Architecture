"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.running = True
        # I think this was what Beej was talking about?
        # TODO: figure out how to handle passing in arguments when
        # using a branchtable
        self.branchtable = {}
        self.branchtable[HLT] = self.hlt
        self.branchtable[LDI] = self.ldi
        self.branchtable[PRN] = self.prn
        self.branchtable[MUL] = self.mul

    ## RAM Functions
    # Memory Address Register, holds the memory address we're 
    # reading or writing
    #  Memory Data Register, holds the value to write or the 
    # value just read
    def ram_read(self,MAR):
        return self.ram[MAR]

    def ram_write(self, MDR, MAR):
        self.ram[MAR] = MDR

    def load(self, file):
        """Load a program into memory."""
        # print(test)
        address = 0

        try:
            with open(file) as f:
                for line in f:
                    # print(line)
                    try:
                        line = line.strip()
                        line = line.split('#', 1)[0]
                        line = int(line, 2)
                        self.ram[address] = line
                        address += 1
                    except ValueError:
                        pass
        except FileNotFoundError:
            print(f"Couldn't find file {file}")
            sys.exit(1)


        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()
    
    def hlt(self):
        self.running = False

    def ldi(self, operand_a, operand_b):
        self.reg[operand_a] = operand_b
        self.pc += 3
    
    def prn(self, operand_a):
        print(self.reg[operand_a])
        self.pc += 2

    def mul(self, operand_a, operand_b):
        self.alu("MUL", operand_a, operand_b)
        self.pc += 3

    def run(self):
        """Run the CPU."""
        
        # self.trace()
        while self.running:
            ir = self.pc
            inst = self.ram[ir]
            operand_a = self.ram_read(ir + 1)
            operand_b = self.ram_read(ir + 2)
            # self.branchtable[inst]()
            if inst == HLT:  # 0b00000001
                self.hlt()
            elif inst == LDI:  # 0b10000010
                self.ldi(operand_a, operand_b)
            elif inst == PRN:  # 0b01000111
                self.prn(operand_a)
            elif inst == MUL:  
                self.mul(operand_a, operand_b)
