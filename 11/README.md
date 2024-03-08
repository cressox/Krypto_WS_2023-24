# SHA-3 (224-bit) Hash Function in Python

This Python script provides an implementation of the SHA-3 hash function with a 224-bit digest size.

## Functions

The script includes the following functions:

- `pad_message(N, r)`: Pads the message for SHA-3 with the specified block size `r`.
- `split_into_blocks(N, r)`: Splits the padded message into blocks of size `r`.
- `theta(A)`: Performs the Theta step of the Keccak permutation.
- `permutation_function(S)`: Performs the Keccak permutation on the state `S`.
- `sha3_224(input_file, output_file, r=1152, d=224)`: Computes the SHA-3 hash of the contents of `input_file` and writes the result to `output_file`.

## Usage

To use this script, you need to run it from the command line with two arguments: the input file and the output file.

Here is an example of how to use the script:

```bash
python sha3.py input.txt output.txt