import the_genetic_computer

program = """AAACGGTTACGGTCCCGGTGACGGTGACGGTGGCGGAGACGGAAACGGGCGCGGTGGCGGGATCGGTGACGGTCATTT"""
program_two = "AAATCCTGCTTT"

tape = the_genetic_computer.create_tape(program)
tape_2 = the_genetic_computer.create_tape(program_two)

tape_list = the_genetic_computer.initialise_tape_list([tape_2,tape])

the_genetic_computer.read_tape(tape_list, debug_mode=False)