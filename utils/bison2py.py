#@+leo-ver=4
#@+node:@file utils/bison2py.py
#@@language python

"""
Utility which creates a boilerplate pybison-compatible
python file from a yacc file and lex file

Run it with 2 arguments - filename.y and filename.l
Output is filename.py
"""
#@+others
#@+node:imports
import sys, os, re, getopt

from bison import bisonToPython
#@-node:imports
#@+node:globals
argv = sys.argv
argc = len(argv)
progname = argv[0]

reSpaces = re.compile("\\s+")
#@-node:globals
#@+node:usage
def usage(s=None):
    """
    Display usage info and exit
    """
    if s:
        print progname+": "+s
    
    print "\n".join([
        "Usage: %s [-c] basefilename" % progname,
        "   or: %s [-c] grammarfile.y lexfile.l pyfile.py" % progname,
        "(generates a boilerplate python file from a grammar and lex file)",
        "The first form uses 'basefilename' as base for all files, so:",
        "  %s fred" % progname,
        "is equivalent to:",
        "  %s fred.y fred.l fred.py" % progname,
        '',
        'The "-c" argument causes the creation of a unique node class',
        'for each parse target - highly recommended for complex grammars',
        ])
    
    sys.exit(1)

#@-node:usage
#@+node:main
def main():
    """
    Command-line interface for bison2py
    """
    global argc, argv

    if '-c' in argv:
        generateClasses = 1
        argv.remove('-c')
        argc = argc - 1
    else:
        generateClasses = 0

    if argc == 2:
        basename = argv[1]
        bisonfile = basename+".y"
        lexfile = basename+".l"
        pyfile = basename+".py"
    elif argc == 4:
        bisonfile, lexfile, pyfile = argv[1:4]
    else:
        usage("Bad argument count")
    
    bisonToPython(bisonfile, lexfile, pyfile, generateClasses)

#@-node:main
#@+node:MAINLINE
if __name__ == '__main__':
    main()
#@-node:MAINLINE
#@-others
#@-node:@file utils/bison2py.py
#@-leo
