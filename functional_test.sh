#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_pystyle pycodestyle test_hash_tables.py
assert_no_stdout

run test_pystyle pycodestyle test_hash_functions.py
assert_no_stdout

run test_pystyle pycodestyle hash_functions.py
assert_no_stdout

run test_pystyle pycodestyle hash_tables.py
assert_no_stdout

run bad_input python hash_functions.py --input=bad.txt --algorithm=ascii --size=1000
assert_in_stderr 'Input file does not exists!'

run bad_algorithm python hash_functions.py --input=rand_words.txt --algorithm=bad --size=1000
assert_in_stderr 'Double check your hash algorithm input!'

run bad_size python hash_functions.py --input=rand_words.txt --algorithm=ascii --size=-1000
assert_in_stderr 'Size must be a positive integer!'

echo 'Generating all figures'

echo '---- Hash function figures ----'

python hash_functions.py --input=rand_words.txt --algorithm=ascii --size=1000 | python scatter.py hash_function_images/ascii_hash_function.png "Hashed word" "Hashed value"

python hash_functions.py --input=rand_words.txt --algorithm=rolling --size=1000 | python scatter.py hash_function_images/rolling_hash_function.png "Hashed word" "Hashed value"

python hash_functions.py --input=rand_words.txt --algorithm=DJB --size=1000 | python scatter.py hash_function_images/DJB_hash_function.png "Hashed word" "Hashed value"

python hash_functions.py --input=non_rand_words.txt --algorithm=ascii --size=1000 | python scatter.py hash_function_images/non_rand_ascii_hash_function.png "Hashed word" "Hashed value"

python hash_functions.py --input=non_rand_words.txt --algorithm=rolling --size=1000 | python scatter.py hash_function_images/non_rand_rolling_hash_function.png "Hashed word" "Hashed value"

python hash_functions.py --input=non_rand_words.txt --algorithm=DJB --size=1000 | python scatter.py hash_function_images/non_rand_DJB_hash_function.png "Hashed word" "Hashed value"

echo '---- Hash function images generated! ----'

echo '---- Hash table figures ----'

echo '----- ascii v.s. all collision strategy -----'
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --size=10000 --algorithm=ascii --collision_strategy=LinearProbe --input=rand_words.txt --key_to_add=$M >  ascii_LinearProbe_rand.$M.txt
done;

grep add ascii_LinearProbe_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/ascii_LinearProbe_add_time.png "Load factor" "Add time"
grep search ascii_LinearProbe_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/ascii_LinearProbe_search_time.png "Load factor" "Search time"
rm *.*.txt

for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --size=10000 --algorithm=ascii --collision_strategy=ChainedHash --input=rand_words.txt --key_to_add=$M >  ascii_ChainedHash_rand.$M.txt
done;

grep add ascii_ChainedHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/ascii_ChainedHash_add_time.png "Load factor" "Add time"
grep search ascii_ChainedHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/ascii_ChainedHash_search_time.png "Load factor" "Search time"
rm *.*.txt

for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --size=10000 --algorithm=ascii --collision_strategy=PseudoRandomHash --input=rand_words.txt --key_to_add=$M >  ascii_PseudoRandomHash_rand.$M.txt
done;

grep add ascii_PseudoRandomHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/ascii_PseudoRandomHash_add_time.png "Load factor" "Add time"
grep search ascii_PseudoRandomHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/ascii_PseudoRandomHash_search_time.png "Load factor" "Search time"
rm *.*.txt
echo '----- ascii v.s. all collision strategy finished! -----'

echo '----- rolling v.s. all collision strategy -----'
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --size=10000 --algorithm=rolling --collision_strategy=LinearProbe --input=rand_words.txt --key_to_add=$M >  rolling_LinearProbe_rand.$M.txt
done;

grep add rolling_LinearProbe_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/rolling_LinearProbe_add_time.png "Load factor" "Add time"
grep search rolling_LinearProbe_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/rolling_LinearProbe_search_time.png "Load factor" "Search time"
rm *.*.txt

for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --size=10000 --algorithm=rolling --collision_strategy=ChainedHash --input=rand_words.txt --key_to_add=$M >  rolling_ChainedHash_rand.$M.txt
done;

grep add rolling_ChainedHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/rolling_ChainedHash_add_time.png "Load factor" "Add time"
grep search rolling_ChainedHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/rolling_ChainedHash_search_time.png "Load factor" "Search time"
rm *.*.txt

for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --size=10000 --algorithm=rolling --collision_strategy=PseudoRandomHash --input=rand_words.txt --key_to_add=$M >  rolling_PseudoRandomHash_rand.$M.txt
done;

grep add rolling_PseudoRandomHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/rolling_PseudoRandomHash_add_time.png "Load factor" "Add time"
grep search rolling_PseudoRandomHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/rolling_PseudoRandomHash_search_time.png "Load factor" "Search time"
rm *.*.txt
echo '----- rolling v.s. all collision strategy finished! -----'

echo '----- DJB v.s. all collision strategy -----'
for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --size=10000 --algorithm=DJB --collision_strategy=LinearProbe --input=rand_words.txt --key_to_add=$M >  DJB_LinearProbe_rand.$M.txt
done;

grep add DJB_LinearProbe_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/DJB_LinearProbe_add_time.png "Load factor" "Add time"
grep search DJB_LinearProbe_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/DJB_LinearProbe_search_time.png "Load factor" "Search time"
rm *.*.txt

for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --size=10000 --algorithm=DJB --collision_strategy=ChainedHash --input=rand_words.txt --key_to_add=$M >  DJB_ChainedHash_rand.$M.txt
done;

grep add DJB_ChainedHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/DJB_ChainedHash_add_time.png "Load factor" "Add time"
grep search DJB_ChainedHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/DJB_ChainedHash_search_time.png "Load factor" "Search time"
rm *.*.txt

for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --size=10000 --algorithm=DJB --collision_strategy=PseudoRandomHash --input=rand_words.txt --key_to_add=$M >  DJB_PseudoRandomHash_rand.$M.txt
done;

grep add DJB_PseudoRandomHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/DJB_PseudoRandomHash_add_time.png "Load factor" "Add time"
grep search DJB_PseudoRandomHash_rand.*.txt | cut -d " " -f2,3 | python scatter.py hash_table_images/DJB_PseudoRandomHash_search_time.png "Load factor" "Search time"
rm *.*.txt
echo '----- DJB v.s. all collision strategy finished! -----'

echo 'All figures are generated' 

