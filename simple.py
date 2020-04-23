import sys

PRINT_NAME = 1
HALT = 2
PRINT_NUM = 3
SAVE = 4
PRINT_REGISTER = 5

memory = [
    PRINT_NAME,
    PRINT_NAME,
    PRINT_NAME,
    PRINT_NUM,
    14,
    SAVE,
    99,
    2,
    PRINT_REGISTER,
    2,
    HALT
]

running = True
pc = 0

registers = [0] * 8

while running is True:
    command = memory[pc]

    if command == PRINT_NAME:
        print("Ami")
        pc += 1

    elif command == PRINT_NUM:
        print(memory[pc+1])
        pc += 2

    elif command == SAVE:
        reg_index = memory[pc+2]
        number_to_save = memory[pc+1]
        registers[reg_index] = number_to_save
        pc += 3

    elif command == PRINT_REGISTER:
        saved = registers[memory[pc+1]]
        print(saved)
        pc += 2

    elif command == HALT:
        running = False

    else:
        print("Error")
        sys.exit(1)
