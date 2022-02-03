import sys

input_text="""#************************************************************
#*                     MadGraph5_aMC@NLO                    *
#*                                                          *
#*                *                       *                 *
#*                  *        * *        *                   *
#*                    * * * * 5 * * * *                     *
#*                  *        * *        *                   *
#*                *                       *                 *
#*                                                          *
#*                                                          *
#*         VERSION 2.7.3                 2020-06-21         *
#*                                                          *
#*    The MadGraph5_aMC@NLO Development Team - Find us at   *
#*    https://server06.fynu.ucl.ac.be/projects/madgraph     *
#*                                                          *
#************************************************************
#*                                                          *
#*               Command File for MadGraph5_aMC@NLO         *
#*                                                          *
#*     run as ./bin/mg5_aMC  filename                       *
#*                                                          *
#************************************************************
import model DMsimp_s_spin2
define p = 21 2 4 1 3 -2 -4 -1 -3 5 -5 # pass to 5 flavors
define j = p
generate p p > t t~ xr xr [QCD]
output """+sys.argv[1]+"""_"""+sys.argv[2]+""" -nojpeg"""
inputfile = open("./DMsignal/{0}_{1}/{0}_{1}_proc_card.dat".format(sys.argv[1],sys.argv[2]),"w")
#spinfile = open("./process/madspingrid/decay_me/Cards/param_card.dat","w")
inputfile.write(input_text)
inputfile.close()

