#!/bin/bash

for ((number=1;number<=$1;number++))
do
    name="Problema_"$(printf %02d $number)".tex"
    touch $name
done

