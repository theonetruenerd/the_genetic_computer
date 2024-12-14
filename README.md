# The Genetic Computer

- Code is made of a string of bases (ACTG)
- Groups of three bases make up an operation
- Programs are formed by long lists of these bases

Perhaps encode other weird behaviour? Two tapes made, one 
of the complementary bases? Indels? Genetic fusion? Start with
the basics I think. Does the code itself become the tape which is 
then being manipulated? Has to be tape-cell based because yanno, CELL

## Rules of work:
1. Reads cell of three letters that its in
2. Performs operation instructed by that cell
3. Moves according to current move pattern
4. Repeats

## Operations:
- Stop program
- Move the head one step to the right (BEFORE step 3, ie skip right one)
- Move the head one step to the left (BEFORE step 3, ie repeat - causes inf loop)
- Stay in place (ie skip step 3, causes infinite loop)
- Overwrite the current cell with the complement
- Copy the current cell to memory
- Overwrite the current cell with what is stored in memory
- Conditional jump?
- Loop start
- Loop end
- Insert a random base
- Insert a random codon
- Delete a random base
- Delete the current codon
- Shuffle the bases of the current codon
- Change head direction to left
- Change head direction to right
- Toggle head direction
- Start program (first occurence of this codon is the initial head)

