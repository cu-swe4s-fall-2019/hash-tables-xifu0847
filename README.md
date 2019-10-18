# Hash tables

## Usage

### Hash Function

```sh
python hash_functions.py --input=${FILE_NAME} --algorithm=${ALGORITHM} --size=${HASH_TABLE_SIZE}
| python scatter.py ${OUTPUT_FILE} ${X_LABEL} ${Y_LABEL}
```

The hash_functions.py and scatter.py should be used in pipe since hash_functions.py will print\
information on the console and scatter.py will fetch it and plot the figures.

- FILE_NAME: name of input file. usually in .txt format
- ALGORITHM: ascii | rolling | DJB
- HASH_TABLE_SIZE: capacity of hash table
- OUTPUT_FILE: the output figure directory. usually in .png format.
- X_LABEL: name of x label
- Y_LABEL: name of y label

Example:
```sh
python hash_functions.py --input=rand_words.txt --algorithm=ascii --size=1000 | python scatter.py hash_function_images/ascii_hash_function.png "Hashed word" "Hashed value"
```

### Hash Table

- Step 1: Generate data
```sh
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --size=10000 --algorithm=ascii --collision_strategy=LinearProbe --input=rand_words.txt
    --key_to_add=$M >  ascii_LinearProbe_rand.$M.txt
done;
```

- Step 2: Grep information and draw figures
```sh
grep add ascii_LinearProbe_rand.*.txt | cut -d " " -f2,3\
| python scatter.py hash_table_images/ascii_LinearProbe_add_time.png "Load factor" "Add time"
```

```sh
grep search ascii_LinearProbe_rand.*.txt | cut -d " " -f2,3\
| python scatter.py hash_table_images/ascii_LinearProbe_search_time.png "Load factor" "Search time"
```

## Figures and results

### Hash functions

#### ascii in rand_words.txt
```sh
python hash_functions.py --input=rand_words.txt --algorithm=ascii --size=1000 | python scatter.py hash_function_images/ascii_hash_function.png "Hashed word" "Hashed value"
```

![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/hash-tables-xifu0847/master/hash_function_images/ascii_hash_function.png)

#### rolling in rand_words.txt
```sh
python hash_functions.py --input=rand_words.txt --algorithm=rolling --size=1000 | python scatter.py hash_function_images/rolling_hash_function.png "Hashed word" "Hashed value"
```

![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/hash-tables-xifu0847/master/hash_function_images/rolling_hash_function.png)

#### DJB in rand_words.txt
```sh
python hash_functions.py --input=rand_words.txt --algorithm=DJB --size=1000 | python scatter.py hash_function_images/DJB_hash_function.png "Hashed word" "Hashed value"
```

![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/hash-tables-xifu0847/master/hash_function_images/DJB_hash_function.png)

#### ascii in non_rand_words.txt
```sh
python hash_functions.py --input=non_rand_words.txt --algorithm=ascii --size=1000 | python scatter.py hash_function_images/non_rand_ascii_hash_function.png "Hashed word" "Hashed value"
```

![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/hash-tables-xifu0847/master/hash_function_images/non_rand_ascii_hash_function.png)

#### rolling in non_rand_words.txt
```sh
python hash_functions.py --input=non_rand_words.txt --algorithm=rolling --size=1000 | python scatter.py hash_function_images/non_rand_rolling_hash_function.png "Hashed word" "Hashed value"
```

![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/hash-tables-xifu0847/master/hash_function_images/non_rand_rolling_hash_function.png)

#### DJB in non_rand_words.txt
```sh
python hash_functions.py --input=non_rand_words.txt --algorithm=DJB --size=1000 | python scatter.py hash_function_images/non_rand_DJB_hash_function.png "Hashed word" "Hashed value"
```
![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/hash-tables-xifu0847/master/hash_function_images/non_rand_DJB_hash_function.png)

### Summary

Apparently, the performance of hash function is DJB = rolling > ascii

### Hash tables

With the limitation of this README.md, we will only show the result of DJB v.s. all collision strategy in rand_words.txt.\
More figures can be found at hash_table_images/

#### DJB hash function with LinearProbe

```sh
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --size=10000 --algorithm=DJB --collision_strategy=LinearProbe --input=rand_words.txt --key_to_add=$M >  DJB_LinearProbe_rand.$M.txt
done;

grep add DJB_LinearProbe_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/DJB_LinearProbe_add_time.png "Load factor" "Add time"
grep search DJB_LinearProbe_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/DJB_LinearProbe_search_time.png "Load factor" "Search time"
```
![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/hash-tables-xifu0847/master/hash_table_images/DJB_LinearProbe_add_time.png)
![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/hash-tables-xifu0847/master/hash_table_images/DJB_LinearProbe_search_time.png)

#### DJB hash function with ChainedHash

```sh
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --size=10000 --algorithm=DJB --collision_strategy=ChainedHash --input=rand_words.txt --key_to_add=$M >  DJB_ChainedHash_rand.$M.txt
done;

grep add DJB_ChainedHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/DJB_ChainedHash_add_time.png "Load factor" "Add time"
grep search DJB_ChainedHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/DJB_ChainedHash_search_time.png "Load factor" "Search time"
```

![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/hash-tables-xifu0847/master/hash_table_images/DJB_ChainedHash_add_time.png)
![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/hash-tables-xifu0847/master/hash_table_images/DJB_ChainedHash_search_time.png)

#### DJB hash function with PseudoRandomHash

```sh
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --size=10000 --algorithm=DJB --collision_strategy=PseudoRandomHash --input=rand_words.txt --key_to_add=$M >  DJB_PseudoRandomHash_rand.$M.txt
done;

grep add DJB_PseudoRandomHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/DJB_PseudoRandomHash_add_time.png "Load factor" "Add time"
grep search DJB_PseudoRandomHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/DJB_PseudoRandomHash_search_time.png "Load factor" "Search time"
```
![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/hash-tables-xifu0847/master/hash_table_images/DJB_PseudoRandomHash_add_time.png)
![avatar](https://raw.githubusercontent.com/cu-swe4s-fall-2019/hash-tables-xifu0847/master/hash_table_images/DJB_PseudoRandomHash_search_time.png)

### Summary

In this experiment,
Performance: PseudoRandomHash > ChainedHash > LinearProbe

## Overall Summary

The performance in this experiment is not a final indicator of either a hash function or a collision strategy.\
Because all hash functions and collision strategies have their own use case. And there is always tradeoffs\
between different method and strategy.




