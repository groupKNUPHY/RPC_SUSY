import sys

input_text="""#************************************************************
#*                        MadSpin                           *
#*                                                          *
#*    P. Artoisenet, R. Frederix, R. Rietkerk, O. Mattelaer * 
#*                                                          *
#*    Part of the MadGraph5_aMC@NLO Framework:              *
#*    The MadGraph5_aMC@NLO Development Team - Find us at   *
#*    https://server06.fynu.ucl.ac.be/projects/madgraph     *
#*                                                          *
#*    Manual:                                               *
#*    cp3.irmp.ucl.ac.be/projects/madgraph/wiki/MadSpin     *
#*                                                          *
#************************************************************
#Some options (uncomment to apply)
#
# set seed 1
# set Nevents_for_max_weight 75 # number of events for the estimate of the max. weight
# set BW_cut 15                 # cut on how far the particle can be off-shell
# set spinmode onshell          # Use one of the madspin special mode
set ms_dir ./madspingrid

set max_weight_ps_point 400  # number of PS to estimate the maximum for each event

# specify the decay for the final state particles
decay t > w+ b, w+ > l+ vl
decay t~ > w- b~, w- > l- vl~
decay w+ > all all
decay w- > all all
decay z > all all
# running the actual code
launch"""

inputfile = open("./DMsignal/{0}_{1}/{0}_{1}_madspin_card.dat".format(sys.argv[1],sys.argv[2]),"w")
#spinfile = open("./process/madspingrid/decay_me/Cards/param_card.dat","w")
inputfile.write(input_text)
inputfile.close()

