from pyMARS import readin
import argparse



"""-------------------------------------------------------------------------
Get details from command line
-------------------------------------------------------------------------"""

#gets arguments from terminal
parser=argparse.ArgumentParser(description='pyMARS main: \
            converts and trims mechanism files \n')
parser.add_argument('--file', \
                    help='input mechanism file name', \
                    type=str)

parser.add_argument('--species',  \
                    help='comma separated list input of species to exclude',\
                    type=str)

parser.add_argument('--thermo', \
                    help='thermodynamic data file', \
                    type=str)

parser.add_argument('--transport', \
                    help='transport data file', \
                    type=str)

parser.add_argument('--plot', \
                    help='plots ignition curve', \
                    action="store_true")

parser.add_argument('--points', \
                    help='print sim sample points', \
                    action="store_true")

parser.add_argument('--writecsv', \
                    help='write species data to csv', \
                    action="store_true")

parser.add_argument('--writehdf5', \
                    help='write species data to hdf5', \
                    action="store_true")




args=parser.parse_args()

readin(args)


"""
Arguments
    --file: Input mechanism file (ex. --file=gri30.cti)
    --species: Species to eliminate (ex. --species='H, OH')
    --thermo: Thermo data file if Chemkin format (ex. --thermo= thermo.dat)
    --transport: Transport data file if Chemkin format
    --plot
    --points
    --writecsv
    --writehdf5

"""