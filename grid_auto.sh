#!/bin/bash

for ((med=680; med<1180; med+=50)); do ## 1st parameter. in my case, mediator mass
for ((dm=10; 2*dm<med; dm+=20)); do ## 2nd parameter. dark matter mass

echo "${med}_${dm}" ## check parameter
cd DMsignal ## global card directory
mkdir "${med}_${dm}" ## sub directory
cd ..
python make_param_card.py ${med} ${dm}  ### in my case, 2 parameters required for making gridpack
python make_proc_card.py ${med} ${dm}
python make_spin_card.py ${med} ${dm}
python make_run_card.py ${med} ${dm}
./gridpack_generation.sh "${med}_${dm}" DMsignal/"${med}_${dm}" ### launcher
cd /x6/spool/twkim/genproductions/bin/MadGraph5_aMCatNLO ### back to the main
done
done
