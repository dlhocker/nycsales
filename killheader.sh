#!/bin/bash
cp $1 $1.tmp
cat $1.tmp |sed 's/","/,/g'|sed 's/"BOR/BOR/g' |sed '/,,,,*/d' > $1
rm $1.tmp