import argparse
import sys
import hash_functions
import time
import random
import os


def reservoir_sampling(new_val, size, V):
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val


class LinearProbe:
    def __init__(self, N, hash_method):
        self.hash = hash_method
        self.N = N
        self.T = [None for i in range(N)]
        self.M = 0

    def add(self, key, value):
        hash_slot = self.hash(key, self.N)

        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] is None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
        return False

    def search(self, key):
        hash_slot = self.hash(key, self.N)

        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] is None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        return None


class ChainedHash:
    def __init__(self, N, hash_method):
        self.hash = hash_method
        self.N = N
        self.T = [[] for i in range(N)]
        self.M = 0

    def add(self, key, value):
        hash_slot = self.hash(key, self.N)
        self.T[hash_slot].append((key, value))
        self.M += 1
        return True

    def search(self, key):
        hash_slot = self.hash(key, self.N)

        for k, v in self.T[hash_slot]:
            if key == k:
                return v
        return None


class PseudoRandomHash:
    def __init__(self, N, hash_method):
        self.hash = hash_method
        self.N = N
        self.T = [None for i in range(N)]
        self.M = 0
        self.random_list = [i for i in range(1, N)]
        random.shuffle(self.random_list)
        self.random_list = [0] + self.random_list

    def add(self, key, value):
        hash_slot = self.hash(key, self.N)

        for num in self.random_list:
            test_slot = (hash_slot + num) % self.N
            if self.T[test_slot] is None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
        return False

    def search(self, key):
        hash_slot = self.hash(key, self.N)

        for num in self.random_list:
            test_slot = (hash_slot + num) % self.N
            if self.T[test_slot] is None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        return None


if __name__ == '__main__':
    # adding arguments
    parser = argparse.ArgumentParser(
        description='self-defined hash table objects')

    parser.add_argument('--input', type=str, help='Name of the input file')

    parser.add_argument('--size', type=int, help='Size of hash table')

    parser.add_argument('--algorithm', type=str, help='Choice of algorithm'
                        'h_ascii| h_rolling|h_DJB')

    parser.add_argument('--collision_strategy', type=str,
                        help='Choice of collision'
                        'strategy. LinearProbe|ChainedHash|PseudoRandomHash')

    parser.add_argument('--key_to_add', type=int, help='Number of key to add')

    args = parser.parse_args()

    hash_table = None

    if not os.path.exists(args.input):
        raise FileNotFoundError('Input file not found')

    if args.collision_strategy not in [
                        'LinearProbe', 'ChainedHash', 'PseudoRandomHash']:
        raise ValueError('Check collision strategy')

    if args.algorithm not in ['ascii', 'rolling', 'DJB']:
        raise ValueError('Check your hash function algorithm')

    if args.algorithm == 'ascii':
        if args.collision_strategy == 'LinearProbe':
            hash_table = LinearProbe(args.size, hash_functions.h_ascii)
        elif args.collision_strategy == 'ChainedHash':
            hash_table = ChainedHash(args.size, hash_functions.h_ascii)
        else:
            hash_table = PseudoRandomHash(args.size, hash_functions.h_ascii)
    elif args.algorithm == 'rolling':
        if args.collision_strategy == 'LinearProbe':
            hash_table = LinearProbe(args.size, hash_functions.h_ascii)
        elif args.collision_strategy == 'ChainedHash':
            hash_table = ChainedHash(args.size, hash_functions.h_ascii)
        else:
            hash_table = PseudoRandomHash(args.size, hash_functions.h_ascii)
    else:
        if args.collision_strategy == 'LinearProbe':
            hash_table = LinearProbe(args.size, hash_functions.h_DJB)
        elif args.collision_strategy == 'ChainedHash':
            hash_table = ChainedHash(args.size, hash_functions.h_DJB)
        else:
            hash_table = PseudoRandomHash(args.size, hash_functions.h_DJB)

    keys_to_search = 100
    V = []

    for l in open(args.input):
        reservoir_sampling(l, keys_to_search, V)
        t0 = time.time()
        hash_table.add(l, l)
        t1 = time.time()
        print('add', hash_table.M/hash_table.N, t1 - t0)
        if hash_table.M == args.key_to_add:
            break

    for v in V:
        t0 = time.time()
        r = hash_table.search(v)
        t1 = time.time()
        print('search', t1 - t0)
