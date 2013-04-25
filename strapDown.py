#!/usr/bin/python

import argparse
import os
import re

def main(textfiles,option):

    toWriteBeg='<!DOCTYPE html>\n<html>\n<xmp theme="{superhero}" style="display:non;">\n'.format(superhero=option)
    toWriteEnd='\n</xmp>\n<script src="http://strapdownjs.com/v/0.2/strapdown.js">\n</script>\n</html>'
    preEditText=open(textfiles,'r').read()
    newText=open('.new','w')
    newText.write(toWriteBeg+preEditText+toWriteEnd)
    newText.close()

    os.system('mv {0} {1}'.format('.new',textfiles.split('.')[0]+'.html'))
    #os.system('rm {0}'.format(textfiles))

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
    argparser.add_argument("--input","-input",metavar='Mard down or text files', help='''
    Markdown text file
    ''')
    argparser.add_argument("--option","-option",metavar='option',default='journal')
    argparser.add_argument("--html","-html",metavar='html file that you want to change style')

    args = argparser.parse_args()
    if args.input:
        print 'a copy of {0} will be produced in html'.format(args.input)
        main(args.input,args.option)
    if args.html and not args.option:
            print '''
    If you want to change existing html file, you have to specify the option ''' exit(0) if args.html and args.option: change(args.html,args.option)





