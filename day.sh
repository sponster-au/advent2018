#!/bin/bash -x

day=$1

cat template/advent01.py | sed 's/01/'$day'/g' > advent$day.py
cat template/_test_01.py | sed 's/01/'$day'/g' > test_$day.py
