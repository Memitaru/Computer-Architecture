"""CPU functionality."""

import sys

HLT = 0b00000001
PRN = 0b01000111
LDI = 0b10000010
ADD = 0b10100000
MUL = 0b10100010

class CPU:
    """Main CPU class."""

    def __init__(self):
        """
        Need memory and 8 registers
        """
        self.reg = [0] * 8
        self.ram = [0] * 256
        self.pc = 0


    def load(self):
        """Load a program into memory."""

        try:
            file = sys.argv[1]
            address = 0
            with open(file) as f:
                # Open and read file
                for line in f:
                    # Remove comments
                    line = line.split("#")[0]
                    # Remove whitespace
                    line = line.strip()
                    # Skip empty lines
                    if line == "":
                        continue

                    value = int(line, 2)

                    # Add instructions to memory
                    self.ram[address] = value
                    address += 1
        except FileNotFoundError:
            print("File not found")
            sys.exit(2)


    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, value, address):
        self.ram[address] = value
        


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
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

    def run(self):
        """Run the CPU."""
        self.load()

        while True:
            # Read ram and set them to IR to get instructions
            IR = self.ram_read(self.pc)
            # Read the bytes after PC to get the next to possible operands in case they are needed
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            # Perform the options based on op codes

            if IR == HLT:
                # exit for halt
                print("Exit")

                break
            elif IR == PRN:
                print(self.reg[operand_a])
                self.pc += 2
            elif IR == LDI:
                # Add the `LDI` instruction
                self.reg[operand_a] = operand_b
                self.pc += 3
            elif IR == ADD:
                self.alu("ADD", operand_a, operand_b)
                self.pc += 3
            elif IR == MUL:
                self.alu("MUL", operand_a, operand_b)
                self.pc += 3
            else:
                print("Error")
        
