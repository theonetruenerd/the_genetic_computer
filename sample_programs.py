import the_genetic_computer

program = """
                AAAATAAAACCCCGAATAAGG
                    """

tape = the_genetic_computer.create_tape(program)

the_genetic_computer.read_tape(tape, debug_mode=False)