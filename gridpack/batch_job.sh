#!/bin/bash

for ((i=80; i<1030; i+=50)); do
for ((j=10; 2*j<i; j+=20)); do
./Condom_run.sh "${i}_${j}_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz" $i $j
echo $i $j
done
done
