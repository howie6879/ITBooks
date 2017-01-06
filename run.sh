#!/bin/bash

array=(search title author)
if [[ "${array[@]}" =~ $1 ]]
then
    python ITBooks/abook.py $1 $2 $3
fi