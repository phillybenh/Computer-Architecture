# Computer Architecture

## Day 1: Basics & Number Bases

### Computer Components
 - *CPU*: Central Processing Unit
     - executes instructions from computer programs
     - *Registers*: a fixed nubmer of storage locations in the cpu, they are the same size as a CPU word
         - can be thought of as variables the CPU has at it's disposal
         - registers are similar to RAM, but faster
         - the number of registers is limited and depends on CPU architecture
     - *CPU Clock*: controls number of times per second the CPU does something
         - teh faster the clock speed, the mroe often it can execute an instruction
     - *Program Counter (PC)*: keeps track of the address of CPU instructions
     - *Arithmetic Logic Unit (ALU)*: performs arithmetic and bitwise operations on integer binary numbers
     - *Interrupt Handler*:
     - *Cache*: memory on CPU between registers and RAM in size and speed
 - *Memory (RAM)*: Ramdon Access Memory
     - fast compaired to hard-drive
     - can be though of as a big array of bytes that can be accessed by index
     - each element of the RAM stores one byte, an 8-bit number
         - larget nubmers stored sequentially in RAM
     - CPU communicated with RAM thru the memory bus
 - *System Bus*: collection of wires on the motherboard between the CPU, memory, and peripherals

### Concepts
 - *CPU Words*: the natural size of data with which the CPU interacts
     - larger 64-bit (8-byte) numbers are stored sequentially in RAM, these sequences are called words
     - number of bytes per word depends on architecture
         - 8 bytes for a 64-bit CPU
         - 4 bytes for a 32-bit CPU
         - 1 byte for an 8-bit CPU
 - *CPU Instructions*:
     - stored on RAM wiht other data
     - they are jsut numbers
     - CPU keeps track of the currently-executing instruction in RAM and performs actions based ont eh instructions there
     - address of the currently-executing instruction is held in teh  *program counter*
 - Concurrency and Parallelism: CPU can do multiple things at once through a variety of mechanisms, including having multiple cores, or other features such as pipelining or hyperthreading 
 - *Caching*: memory that is part of the CPU that speeds up access to RAM 
     - between RAM and registers in terms of speed
     - `cache miss`: trying to access memory that's not in the cahe yet
     - `cache hit`: memory you want is already in teh cache

### Number Bases and Conversion
 - *Numbers adn Values*: values exist no matter how we write them down
 - *Number Bases*:
     - Decimal: has 10 digits, base 10
     - Bunary: has 2 digits, base 2 - binary-digit is called bit for short
         - "each subsequent digit's value is the base raised to the power of how many places it's displaced from the first"
     - Hexadecimal (hex): 16 digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)
     - Octal: 8 didigts (0, 1, 2, 3, 4, 5, 6, 7)
         - used by accident in some languages
          - Decimal `int x = 12; // x is 12`
          - Octal `int y = 012; // Octal, decimal value is 10`
 - Conversions:
     ```
    +------ 8's place
    |+----- 4's place
    ||+---- 2's place
    |||+--- 1's place
    ||||
    1010 = 10 decimal

    ----

    67 decimal...

    64 + 2 + 1 == 67
    +------- 64's x 1
    |+------ 32's x 0
    ||+----- 16's x 0
    |||+----  8's x 0
    ||||+---  4's x 0
    |||||+--  2's x 1
    ||||||+-  1's x 1
    |||||||
    1000011

    ----

    33 decimal...

    32 + 1 == 33
    +------ 32's x 1
    |+----- 16's x 0
    ||+----  8's x 0
    |||+---  4's x 0
    ||||+--  2's x 0
    |||||+-  1's x 1
    ||||||
    100001

    ----
    *Binary to Hex*
    10100011
         - split into "nibbles" (half a byte)
            1010 0011
         - convert 
            1010 == 8 + 2 == (10 indecimal) == A
            0011 == 2 + 1 == 3
         - add the nibbles together
            A3 hex == 10100011

    ----

    * Hex to Binary*
    C7 hex
         - C hex === 12 decimal
            12 decimal == 8+4 decimal = 1100 binary
         - 7 hex == 4 + 2 + 1 == 0111
          - Add back together
            C7 hex == 11000111 binary
    ```

### Bitwise Operations
Bitwise Operations
------------------

Truth Table

Boolean:

A   B       A and B
-------------------
F   F         F
F   T         F
T   F         F
T   T         T

if a > 10 and a < 20:
    do something

Bitwise:

A   not A (the bitwise NOT operator is ~)
---------
0     1
1     0

A   B       A xor B  (the bitwise Exclusive-OR operator is ^)
-------------------
0   0         0
0   1         1
1   0         1
1   1         0

A   B       A or B  (the bitwise OR operator is |)
-------------------
0   0         0
0   1         1
1   0         1
1   1         1

A   B       A and B  (the bitwise AND operator is &)
-------------------
0   0         0
0   1         0
1   0         0
1   1         1

NAND == NOT AND
a NAND b == ~(a & b)

NOR == NOT OR
a NOR b == ~(a | b)

Bonus puzzle: if you have only NAND, how can you build NOT?

       vvvv
  0b11101010
& 0b00011110  AND mask
------------
  0b00001010
       ^^^^
    

If an instruction has 2 arguments, the total length is 3 bytes

If an instruction has 1 argument, the total length is 2 bytes

If an instruction has 0 arguments, the total length is 1 byte


To extract bits

1) Mask

    vv
  0b10000010
& 0b11000000
------------
  0b10000000
    ^^

2) Shift   shift operator is >> for right shift, and << for left shift

vv
10000000
01000000
00100000
00010000
00001000
00000100
00000010
      ^^

number of operands = (instruction value & 0b11000000) >> 6
Instruction length = number of operands + 1


Analogy in decimal: extract the number 34 from this number:

  vv
123456

1) Mask

123456
009900
------
003400

2) Shift

003400
000340
000034


Clearing bits

      v
  0b11100011
& 0b11011111   And with 0
------------
  0b11000011


Setting bits

        v
  0b11100011
| 0b00001000   Or with 1
------------
  0b11101011


