# SHA-3 (224-bit) Hash Function in Python

This Python script provides an implementation of the SHA-3 hash function with a 224-bit digest size.

## Functions

The script includes the following functions:

- `rho(A)`: Performs the Rho transformation.
- `pi(A)`: Performs the Pi transformation.
- `chi(A)`: Performs the Chi transformation.
- `iota(A, round_index)`: Performs the Iota transformation.
- `pad_message(N, r)`: Pads the message for SHA-3 with the specified block size `r`.
- `split_into_blocks(N_bin, r)`: Splits the padded binary message into blocks of size `r`.
- `string_to_state_array(S)`: Converts the binary string `S` into a 5x5 array of 64-bit words.
- `state_array_to_string(A)`: Converts a 5x5 array of 64-bit words back into a binary string.
- `sha3_224(input_string)`: Computes the SHA-3 hash of the input string.

## Usage

To use this script, you need to run it from the command line with two arguments: the input file and the output file.

Here is an example of how to use the script:

```bash
python sha3.py input.txt output.txt