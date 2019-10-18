import argparse
import os


def h_ascii(key, N):
    """
    Argument:
    key: input key in string format
    N: data structure availability
    Return:
    hash_value: The result after hash function
    """
    res = 0
    for letter in key:
        res += ord(letter)
    return res % N


def h_rolling(key, N, p=53, m=2**64):
    """
    Argument:
    key: input key in string format
    N: data structure availability
    p: constant value as base
    m: module by, in case overflow
    Return:
    hash_value: The result after hash function
    """
    res = 0
    for letter in key:
        res = res * p + ord(letter)
    return (res % m) % N


def h_DJB(key, N):
    """
    Argument:
    key: input key in string format
    N: data structure availability
    Return:
    hash_value: The result after hash function
    """
    res = 5381
    for letter in key:
        res = ((res << 5) + res) + ord(letter)
    return res % N


if __name__ == '__main__':
    # adding arguments
    parser = argparse.ArgumentParser(
        description='self-defined hash functions')

    parser.add_argument('--input', type=str,
                        help='Name of the input file')

    parser.add_argument('--algorithm', type=str,
                        help='Choice of hash function')

    parser.add_argument('--size', type=int,
                        help='Size of hash table')

    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise FileNotFoundError('Input file does not exists!')

    if args.size <= 0:
        raise ValueError('Size must be a positive integer!')

    if args.algorithm not in ['ascii', 'rolling', 'DJB']:
        raise ValueError('Double check your hash algorithm input!')

    for row in open(args.input):
        if args.algorithm == 'ascii':
            print(h_ascii(row, args.size))
        elif args.algorithm == 'rolling':
            print(h_rolling(row, args.size))
        elif args.algorithm == 'DJB':
            print(h_DJB(row, args.size))
