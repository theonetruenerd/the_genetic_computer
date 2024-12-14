# The Genetic Computer

- Code is made of a string of bases (ACTG)
- Groups of three bases make up an operation
- Programs are formed by long lists of these bases

## Rules of work:
1. Reads cell of three letters that its in
2. Performs operation instructed by that cell
3. Moves according to current move pattern
4. Repeats

## Ascii codon codes:

| Ascii Character | Codon | Ascii Character | Codon | Ascii Character | Codon |
|:---------------:|:-----:|:---------------:|:-----:|:---------------:|:-----:|
|      space      |  AAA  |        8        |  CTA  |        P        |  GAA  |
|        !        |  AAC  |        9        |  CTC  |        Q        |  GAC  |
|        "        |  AAT  |        :        |  CTT  |        R        |  GAT  |
|        #        |  AAG  |        ;        |  CTG  |        S        |  GAG  |
|        $        |  ACA  |        <        |  CGA  |        T        |  GCA  |
|        %        |  ACC  |        =        |  CGC  |        U        |  GCC  |
|        &        |  ACT  |        >        |  CGT  |        V        |  GCT  |
|        '        |  ACG  |        ?        |  CGG  |        W        |  GCG  |
|        (        |  ATA  |        @        |  TAA  |        X        |  GTA  |
|        )        |  ATC  |        A        |  TAC  |        Y        |  GTC  |
|        *        |  ATT  |        B        |  TAT  |        Z        |  GTG  |
|        +        |  ATG  |        C        |  TAG  |        [        |  GGA  |
|        ,        |  AGA  |        D        |  TCA  |        \        |  GGC  |
|        -        |  AGC  |        E        |  TCC  |        ]        |  GGT  |
|        .        |  AGT  |        F        |  TCT  |        ^        |  GGG  |
|        /        |  AGG  |        G        |  TCG  |
|        0        |  CAA  |        H        |  TTA  |
|        1        |  CAC  |        I        |  TTC  |
|        2        |  CAT  |        J        |  TTT  |
|        3        |  CAG  |        K        |  TTG  |
|        4        |  CCA  |        L        |  TGA  |
|        5        |  CCC  |        M        |  TGC  |
|        6        |  CCT  |        N        |  TGT  |
|        7        |  CCG  |        O        |  TGG  |
