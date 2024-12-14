import re
import random

START_CODON = "AAA"
STOP_CODON = "TTT"
MOVE_LEFT_CODON = "AAT"
MOVE_RIGHT_CODON = "AAC"
STAY_IN_PLACE_CODON = "AAG"
COMPLEMENT_CODON = "ATT"
STORE_NEXT_CODON = "ATA"
OVERWRITE_CODON = "ATC"
INSERT_BASE_CODON = "ACA"
INSERT_CODON_CODON = "ACC"
DELETE_BASE_CODON = "ACT"
DELETE_CODON_CODON = "ACG"
SHUFFLE_BASES_CODON = "AGA"
CHANGE_DIRECTION_TO_LEFT_CODON = "AGC"
CHANGE_DIRECTION_TO_RIGHT_CODON = "AGT"
TOGGLE_DIRECTION_CODON = "AGG"
REVERSE_CODON = "CTA"
PRINT_STORED_CODON = "CCC"
PRINT_STORED_CODON_AS_ASCII = "CAT"
PRINT_NEXT_CODON = "CGA"
PRINT_NEXT_CODON_AS_ASCII = "CGG"
APPEND_STORED_CODON = "TGA"
MOVE_TO_STORED_CODON = "TCA"

def create_tape(program):
    valid_tape = r'^[ACTG]+$'
    program = re.sub(r"[\n\t\s]*", "",program)
    program = program.upper()
    print(program)
    if re.fullmatch(valid_tape, program):
        tape = [program[i:i+3] for i in range(0, len(program), 3)]
        if len(tape[-1]) != 3:
            tape.pop()
        return tape
    else:
        raise ValueError("Invalid tape format")

def find_start_position_of_tape(tape):
    for index, value in enumerate(tape):
        if value == START_CODON:
            return index

def move_head(current_cell, direction):
    if direction == -1:
        current_cell -= 1
    elif direction == 1:
        current_cell += 1
    return current_cell

def shuffle_codon(codon):
    codon_list = list(codon)
    random.shuffle(codon_list)
    return ''.join(codon_list)

def invert_codon(codon):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    return ''.join(complement[base] for base in codon)


def codon_to_ascii(codon):
    base_to_index = {'A': 0, 'C': 1, 'T': 2, 'G': 3}

    index = base_to_index[codon[0]] * 16 + base_to_index[codon[1]] * 4 + base_to_index[codon[2]]
    index += 32

    return chr(index)

def ascii_to_codon(ascii_to_convert):
    index_to_base = ['A','C','T','G']
    index = ord(ascii_to_convert) - 32
    codon = ""
    for _ in range(3):
        codon = index_to_base[index%4] + codon
        index //= 4
    return codon

def read_tape(tape, debug_mode=False):
    current_cell = find_start_position_of_tape(tape)  # Locates first start codon in tape
    direction = 1  # Initially moving right
    stored_codon = ""  # Initially empty memory
    keep_going = True
    while keep_going:
        codon = tape[current_cell]
        if debug_mode:
            print(codon)
        if codon == STOP_CODON:
            keep_going = False
        elif codon == MOVE_LEFT_CODON:
            current_cell -= 1
        elif codon == MOVE_RIGHT_CODON:
            current_cell += 1
        elif codon == STAY_IN_PLACE_CODON:
            continue
        elif codon == COMPLEMENT_CODON:
            current_cell = move_head(current_cell, direction)
            new_codon = invert_codon(tape[current_cell])
            tape[current_cell] = new_codon
            continue
        elif codon == STORE_NEXT_CODON:
            current_cell = move_head(current_cell, direction)
            stored_codon = tape[current_cell]
            continue
        elif codon == OVERWRITE_CODON:
            current_cell = move_head(current_cell, direction)
            tape[current_cell] = stored_codon
            continue
        elif codon == DELETE_CODON_CODON:
            current_cell = move_head(current_cell, direction)
            del tape[current_cell]
        elif codon == SHUFFLE_BASES_CODON:
            current_cell = move_head(current_cell, direction)
            tape[current_cell] = shuffle_codon(tape[current_cell])
            continue
        elif codon == CHANGE_DIRECTION_TO_LEFT_CODON:
            direction = -1
        elif codon == CHANGE_DIRECTION_TO_RIGHT_CODON:
            direction = 1
        elif codon == TOGGLE_DIRECTION_CODON:
            direction *= -1
        elif codon == REVERSE_CODON:
            current_cell = move_head(current_cell, direction)
            tape[current_cell] = tape[current_cell][::-1]
        elif codon == PRINT_STORED_CODON:
            print(stored_codon)
        elif codon == PRINT_STORED_CODON_AS_ASCII:
            print(codon_to_ascii(stored_codon))
        elif codon == APPEND_STORED_CODON:
            tape.append(stored_codon)
        elif codon == MOVE_TO_STORED_CODON:
            while tape[current_cell] != stored_codon:
                current_cell = move_head(current_cell, direction)
        elif codon == INSERT_CODON_CODON:
            tape.insert(stored_codon, current_cell+direction)
        elif codon == PRINT_NEXT_CODON:
            current_cell = move_head(current_cell, direction)
            print(tape[current_cell])
        elif codon == PRINT_NEXT_CODON_AS_ASCII:
            current_cell = move_head(current_cell, direction)
            print(codon_to_ascii(tape[current_cell]))
        current_cell = move_head(current_cell, direction)
        if current_cell < 0 or current_cell >= len(tape):
            current_cell = move_head(current_cell, -direction)