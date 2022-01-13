#!/usr/bin/env python3
# copyright (c) 2022 Mitsuhiko Sato. All Rights Reserved.
# Mitsuhiko Sato ( E-mail: mitsuhikoevolution@gmail.com )
#coding:UTF-8

def main():
    from argparse import ArgumentParser
    parser=ArgumentParser(description="",usage="python3 ", epilog="")
    parser.add_argument("-s",required=True, type=str,metavar="str",help="population.structure file")
    parser.add_argument("-o",required=True, type=str,metavar="str",help="output structure file")
    parser.add_argument("-k",required=True, type=int,metavar="str",help="max number of populations K")
    parser.add_argument("-bi", default=10000, type=int,metavar="str",help="burnin (default=10000)")
    parser.add_argument("-nr", default=20000, type=int,metavar="str",help="num reps (default=20000)")
    parser.add_argument("-p", default=2, type=int,metavar="str",help="PLOIDY LEVEL (default=2)")
    parser.add_argument("-l", type=str,metavar="str",help="order list")
    args = parser.parse_args()

    pops={}
    fhr=open(args.s, "r")
    fhr.readline()
    label=fhr.readline()
    pstr={}
    count=0
    out=label
    for line in fhr:
        lines=line.rstrip().rsplit()
        if not lines[1] in pops:
            count+=1
            pops[lines[1]]=count
        lines[1]=str(pops[lines[1]])
        out+="\t".join(lines)+"\n"
        if lines[0] in pstr:
            pstr[lines[0]] += "\t".join(lines)+"\n"
        else:
            pstr[lines[0]] = "\t".join(lines)+"\n"

    fhr.close()

    
    fhw=open(args.o, "w")
    if args.l:
        out=label
        fhr=open(args.l, "r")
        for line in fhr:
            line=line.rstrip()
            if line in pstr:
                out+=pstr[line]
        fhr.close()
        
    fhw.write(out)
    fhw.close()

    labels=label.split()

    mainparams="\
#define MAXPOPS\t"+str(args.k)+"\n\
#define BURNIN\t"+str(args.bi)+"\n\
#define NUMREPS\t"+str(args.nr)+"\n\
#define NUMINDS\t"+str(len(pstr))+"\n\
#define NUMLOCI\t"+str(len(labels))+"\n\
#define PLOIDY\t"+str(args.p)+"\n\
#define MISSING\t0\n\
#define ONEROWPERIND\t0\n\
#define LABEL\t1\n\
#define POPDATA\t1\n\
#define POPFLAG\t0\n\
#define LOCDATA\t0\n\
#define PHENOTYPE\t0\n\
#define EXTRACOLS\t0\n\
#define MARKERNAMES\t1\n\
#define RECESSIVEALLELES\t0\n\
#define MAPDISTANCES\t0\n\
"
    print(mainparams)    
if __name__ == '__main__': main()
