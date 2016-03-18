#!/bin/bash

user_dict=$(cat ./dict/dict.txt.big.ibbd)
for u in $user_dict; 
do
    if grep -E "^$u(\s|$)" ./dict/dict.txt.big;
    then
        echo "$u is in!"
    else
        echo "$u 20000" | tee -a ./dict/dict.txt.big
    fi
done

echo "=====> Finish!"
