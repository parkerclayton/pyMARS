#!/usr/bin/env python
from pyMARS import readin
import argparse


def main(args=None):
    """
    Parameters
    ----------
        file : str
            Input mechanism file (ex. --file=gri30.cti)
        conditions_file : str
            File of initial conditions for autoignition
        species : str
            Species to eliminate (ex. --species='H, OH')
        thermo : str
            Thermo data file if Chemkin format (ex. --thermo= thermo.dat)
        transport : str
            Transport data file if Chemkin format
        conditions :
            Text file of initial conditions for autoignition
        thresholds :
            csv file containing threshold values to test (usr prompted otherwise)
        run_drg :
            Run Direct Relation Graphing model reduction based on
            a given threshold value

        plot :
            Plot a temperature profile of autoignition
        points :
            Return sampling and ignition points
        writecsv :
            Write autoignition data to a csv file
        writehdf5 :
            Write autoignition to a hdf5 file

    """
    #gets arguments from terminal
    parser=argparse.ArgumentParser(description='pyMARS main: \
                converts and trims mechanism files \n')
    parser.add_argument('--file', \
                        help='input mechanism file name', \
                        type=str)
    parser.add_argument('--conditions', \
                        help='initial conditions file name', \
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
    parser.add_argument('--run_drg', \
                        help='run Direct Relation Graph method to reduce', \
                        action="store_true")
    parser.add_argument('--thresholds', \
                        help='csv file containing threshold values to test (usr prompted otherwise)', \
                        type=str)
    parser.add_argument('--convert', \
                        help='Only conver selected file from .cti <====> .inp', \
                        action="store_true")


    args=parser.parse_args()
    if args.file is not None:
        readin(args)
    if args.file is None:
        #readin(args)
        print """
        Python Model Automated Reduction Software (pyMARS)

        Arguments
            --file:
                Input mechanism file (ex. --file=gri30.cti)
            --run_drg:
                Run Direct Relation Graphing model reduction based on
                a given threshold value
            --conditions:
                Text file of initial conditions for autoignition
            --thresholds:
                csv file containing threshold values to test (usr prompted otherwise)
            --convert:
                Convert .cti <==> .inp
            --thermo:
                Thermo data file if Chemkin format (ex. --thermo= thermo.dat)
            --transport:
                Transport data file if Chemkin format
            --species:
                Specific species to eliminate (ex. --species='H, OH')
            --plot:
                Plot a temperature profile of autoignition
            --points:
                Return sampling and ignition points
            --writecsv:
                Write autoignition data to a csv file
            --writehdf5:
                Write autoignition to a hdf5 file


        """
