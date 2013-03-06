#!/usr/bin/python

import argparse
import os
import re

def main(textfiles,option):

    toWriteBeg='<!DOCTYPE html><html><xmp theme="{superhero}" style="display:non;">\n'.format(superhero=option)
    toWriteEnd='</xmp><script src="http://strapdownjs.com/v/0.2/strapdown.js"></script></html>'
    preEditText=open(textfiles,'r').read()
    newText=open('.new','w')
    newText.write(toWriteBeg+preEditText+toWriteEnd)
    newText.close()

    os.system('mv {0} {1}'.format('.new',textfiles.split('.')[0]+'.html'))
    os.system('rm {0}'.format(textfiles))

def change(html,option):
    text=open(html,'r').read()
    optionPattern=re.compile('theme\W*"(\S*)"')
    current=re.findall(optionPattern,text)
    open(html,'w').write(text.replace(current[0],option))


if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='strapDown.py',formatter_class=argparse.RawDescriptionHelpFormatter,description='''\
Creates html strapdwon java file
from markdown text files

option =
    one of
    'shamrock','amelia','cerulean','cosmo',
    'cyborg','journal','readable','simplex',
    'slate','spacelab','spruce','superheror',united',
''',epilog="Kevin Cho 2012_03_05")
    argparser.add_argument("--md","-md",metavar='Mard down files', help='''
    Markdown text file
    ''')
    argparser.add_argument("--option","-option",metavar='option')
    argparser.add_argument("--html","-html",metavar='html file that you want to change style')

    args = argparser.parse_args()
    if args.md:
        print args.md
        main(args.md,args.option)
    if args.html and not args.option:
            print '''
    If you want to change existing html file,
    you have to specify the option
    '''
            exit(0)



