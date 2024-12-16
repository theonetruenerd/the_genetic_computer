import the_genetic_computer

hello_world = """AAACGGTTACGGTCCCGGTGACGGTGACGGTGGCGGAGACGGAAACGGGCGCGGTGGCGGGATCGGTGACGGTCATTT"""   # Prints hello world
adjacent_tape_printer = """AAAATACACGTCCTTTTT"""   # Prints the tape of whatever program is next in the tape stack
truth_machine = """AAATCTTCACAATTTCACATGAATTTT"""   # Takes user input of 1 or 0, if 0 program halts, if 1 program prints 1s until user stops it
cat_program = """AAATCTCTCTTT"""  # Takes user input and prints it
program_selector = """AAAATACCCTGCTCTTGCTTT"""  # Takes numerical user input and runs whichever tape corresponds to that number in the tape list
instructions_program = """AAAATAGCAATATGGATAAAAATAGATATAGCCATATGTATAAAAATATACATAAAAATAGAA
                       ATAGATATATGGATATCGATAGATATATACATATGCATAAGAATAAAAATATCCATATGTATA
                       GCAATATCCATAGATATAAAAATATTCATAGCAATAACGATAGAGATAAAAATATGTATAGCC
                       ATATGCATATATATATCCATAGATATAAGTATAAAAATACACATACTTATAAAAATATTAATA
                       TCCATATGAATATGAATATGGATAAGAATAAAAATAGCGATATGGATAGATATATGAATATCA
                       ATAAGTATAAAAATACATATACTTATAAAAATAGAAATAGATATATTCATATGTATAGCAATA
                       TCCATAGATATAAGTATAAAAATACAGATACTTATAGCAATAGATATAGCCATAGCAATATTA
                       ATAAAAATATGCATATACATATAGATATTAATATTCATATGTATATCCATAAGTATAAAAATA
                       CCAATACTTATAAAAATATAGATATACATAGCAATAAAAATAGAAATAGATATATGGATATCG
                       ATAGATATATACATATGCATAAGTCTCTTATCG"""


instructions_tape = the_genetic_computer.create_tape(instructions_program)
hello_world_tape = the_genetic_computer.create_tape(hello_world)
adjacent_tape_printer_tape = the_genetic_computer.create_tape(adjacent_tape_printer)
truth_machine_tape = the_genetic_computer.create_tape(truth_machine)
cat_program_tape = the_genetic_computer.create_tape(cat_program)
program_selector_tape = the_genetic_computer.create_tape(program_selector)

tapes = [program_selector_tape,
         hello_world_tape,
         adjacent_tape_printer_tape,
         truth_machine_tape,
         cat_program_tape,
         instructions_tape]

tape_list = the_genetic_computer.initialise_tape_list(tapes)

the_genetic_computer.read_tape(tape_list, debug_mode=True)
