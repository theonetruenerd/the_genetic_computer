import re
import random
import logging

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
PRINT_STORED_CODON_AS_ASCII = "ATG"
PRINT_NEXT_CODON = "CGA"
PRINT_NEXT_CODON_AS_ASCII = "CGG"
APPEND_STORED_CODON = "TGA"
MOVE_TO_STORED_CODON = "TCA"
STORE_USER_ASCII_INPUT_CODON = "TCT"
STORE_USER_CODON_INPUT_CODON = "TCC"
ADD_NEXT_CODON_AND_STORE_CODON = "TAT"
COMBINE_CODONS = "TAA"
MOVE_EQUAL_TO_LAST_STORED_CODON_ASCII = "TAC"
LOAD_TAPE_CODON = "TAG"
RETURN_CODON = "TCG"
START_NEW_TAPE_CODON = "TGC"
STORE_POSITION_IN_NEXT_TAPE_CODON = "TGG"
RETURN_TO_START_CODON = "GGG"
REMOVE_LAST_STORED_CODON = "GAG"

def create_tape(program):
    valid_tape = r'^[ACTG]+$'
    program = re.sub(r"[\n\t\s]*", "",program)
    program = program.upper()
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

def add_next_codon(current_codon,codon_to_add):
    value = int(codon_to_ascii(current_codon))
    value_being_added_to = int(codon_to_ascii(codon_to_add))
    value -= 48
    value_being_added_to -= 48
    new_value = value + value_being_added_to
    new_value += 96
    print(new_value)
    return ascii_to_codon(str(new_value))

def combine_codons(codon_one, codon_two):
    value_one = int(codon_to_ascii(codon_one))
    value_two = int(codon_to_ascii(codon_two))
    combined_value = value_one + value_two
    return ascii_to_codon(str(combined_value))

def initialise_tape_list(tapes):
    tape_list = []
    for tape in tapes:
        tape_list.append((tape, find_start_position_of_tape(tape)))
    return tape_list

def read_tape(tape_list, debug_mode=False):
    if debug_mode:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.ERROR)
    direction = 1  # Initially moving right
    stored_codon = []  # Initially empty memory
    tape, current_cell = tape_list[0]
    keep_going = True
    while keep_going:
        codon = tape[current_cell]
        if codon == STOP_CODON:
            logging.debug("Stop Codon encountered")
            keep_going = False
        elif codon == LOAD_TAPE_CODON:
            logging.debug("Load Tape Encountered")
            new_tape = ''.join(stored_codon)
            new_tape = create_tape(new_tape)
            tape_list.append((new_tape, find_start_position_of_tape(new_tape)))
            logging.debug(tape_list)
        elif codon == RETURN_CODON:
            logging.debug("Return Codon encountered")
            tape, current_cell = tape_list[0]
            current_cell = move_head(current_cell, direction)
        elif codon == START_NEW_TAPE_CODON:
            logging.debug("Start New Tape Encountered")
            tape, current_cell = tape_list[int(codon_to_ascii(stored_codon.pop()))]
        elif codon == MOVE_LEFT_CODON:
            logging.debug("Move Left Codon encountered")
            current_cell -= 1
        elif codon == MOVE_RIGHT_CODON:
            logging.debug("Move Right Codon encountered")
            current_cell += 1
        elif codon == STAY_IN_PLACE_CODON:
            logging.debug("Stay In Place Codon encountered")
            continue
        elif codon == COMPLEMENT_CODON:
            logging.debug("Complement Codon encountered")
            current_cell = move_head(current_cell, direction)
            new_codon = invert_codon(tape[current_cell])
            tape[current_cell] = new_codon
            continue
        elif codon == STORE_NEXT_CODON:
            logging.debug("Store next Codon encountered")
            current_cell = move_head(current_cell, direction)
            stored_codon.append(tape[current_cell])
            continue
        elif codon == OVERWRITE_CODON:
            logging.debug("Overwrite Codon encountered")
            current_cell = move_head(current_cell, direction)
            tape[current_cell] = stored_codon.pop()
            continue
        elif codon == DELETE_CODON_CODON:
            logging.debug("Delete Codon Codon Encountered")
            current_cell = move_head(current_cell, direction)
            del tape[current_cell]
        elif codon == SHUFFLE_BASES_CODON:
            logging.debug("Shuffle bases Codon encountered")
            current_cell = move_head(current_cell, direction)
            tape[current_cell] = shuffle_codon(tape[current_cell])
            continue
        elif codon == CHANGE_DIRECTION_TO_LEFT_CODON:
            logging.DEBUG("Change direction to left codon encountered")
            direction = -1
        elif codon == CHANGE_DIRECTION_TO_RIGHT_CODON:
            logging.debug("Change direction to right Codon encountered")
            direction = 1
        elif codon == TOGGLE_DIRECTION_CODON:
            logging.debug("Toggle direction Codon encountered")
            direction *= -1
        elif codon == REVERSE_CODON:
            logging.debug("Reverse Codon encountered")
            current_cell = move_head(current_cell, direction)
            tape[current_cell] = tape[current_cell][::-1]
        elif codon == PRINT_STORED_CODON:
            logging.debug("Print stored Codon encountered")
            print(stored_codon[-1])
        elif codon == PRINT_STORED_CODON_AS_ASCII:
            logging.debug("Print stored Codon as ASCII encountered")
            print(codon_to_ascii(stored_codon[-1]))
        elif codon == APPEND_STORED_CODON:
            logging.debug("Append stored Codon encountered")
            tape.append(stored_codon.pop())
        elif codon == MOVE_TO_STORED_CODON:
            logging.debug("Move to stored Codon encountered")
            while tape[current_cell] != stored_codon[-1]:
                current_cell = move_head(current_cell, direction)
                logging.debug(f"{tape[current_cell]}, {stored_codon[-1]}")
        elif codon == INSERT_CODON_CODON:
            logging.debug("Insert Codon Codon encountered")
            tape.insert(stored_codon[-1], current_cell+direction)
        elif codon == PRINT_NEXT_CODON:
            logging.debug("Print Next Codon encountered")
            current_cell = move_head(current_cell, direction)
            print(tape[current_cell])
        elif codon == PRINT_NEXT_CODON_AS_ASCII:
            logging.debug("Print Next Codon as ASCII encountered")
            current_cell = move_head(current_cell, direction)
            print(codon_to_ascii(tape[current_cell]))
        elif codon == STORE_USER_CODON_INPUT_CODON:
            logging.debug("Store user codon input Codon encountered")
            stored_codon.append(input(""))
        elif codon == STORE_USER_ASCII_INPUT_CODON:
            logging.debug("Store user ASCII input Codon encountered")
            stored_codon.append(ascii_to_codon(input("")))
        elif codon == ADD_NEXT_CODON_AND_STORE_CODON:
            logging.debug("Add Next Codon and Store Codon encountered")
            current_cell = move_head(current_cell, direction)
            stored_codon.append(add_next_codon(stored_codon.pop(), tape[current_cell]))
            continue
        elif codon == COMBINE_CODONS:
            logging.debug("Combine Codon encountered")
            current_cell = move_head(current_cell, direction)
            stored_codon.append(combine_codons(stored_codon.pop(), tape[current_cell]))
            continue
        elif codon == MOVE_EQUAL_TO_LAST_STORED_CODON_ASCII:
            logging.debug("Move Equal to last stored Codon encountered")
            i = 0
            while i < ord(codon_to_ascii(stored_codon.pop())):
                current_cell = move_head(current_cell, direction)
                i+=1
            continue
        elif codon == STORE_POSITION_IN_NEXT_TAPE_CODON:
            logging.debug("Store position in Next Tape Codon encountered")
            tape_list[0] = (tape, current_cell)
            tape, current_cell = tape_list[1]
            current_cell = move_head(current_cell, direction)
            tape_list[1] = (tape, current_cell)
            logging.debug(f"{tape[current_cell]}, {current_cell}")
            stored_codon.append(tape[current_cell])
            logging.debug(stored_codon)
            tape, current_cell = tape_list[0]
            logging.debug(f"{tape}, {current_cell}")
        elif codon == RETURN_TO_START_CODON:
            logging.debug("Return to start Codon encountered")
            current_cell = find_start_position_of_tape(tape)
        elif codon == REMOVE_LAST_STORED_CODON:
            logging.debug("Remove last stored Codon encountered")
            stored_codon.pop()
        current_cell = move_head(current_cell, direction)
        if current_cell < 0 or current_cell >= len(tape):
            logging.ERROR("Tape head moved out of bounds.")
            current_cell = move_head(current_cell, -direction)