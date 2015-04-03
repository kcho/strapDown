#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import os
import sys
import re

def main(textfiles,theme):

    toWriteBeg='<!DOCTYPE html>\n
                <html>\n
                <xmp theme="{superhero}" style="display:non;">\n'.format(superhero=theme)

    toWriteEnd='\n</xmp>
                \n<script src="http://strapdownjs.com/v/0.2/strapdown.js">
                \n</script>
                \n</html>'

    preEditText=open(textfiles,'r').read()
    newText=open(textfile.split('.')[0]+'.html','w')
    newText.write(toWriteBeg+preEditText+toWriteEnd)
    newText.close()

def change(html,theme):
    text=open(html,'r').read()
    themePattern=re.compile('theme\W*"(\S*)"')
    current=re.findall(themePattern,text)
    open(html,'w').write(text.replace(current[0],theme))


if __name__=='__main__':
    argparser = argparse.ArgumentParser(prog='strapDown.py',
                                        formatter_class=argparse.RawDescriptionHelpFormatter,
                                        description='''\
                    Creates html strapdwon java file
                    from markdown text files

                    theme =
                        one of
                        'shamrock','amelia','cerulean','cosmo',
                        'cyborg','journal','readable','simplex',
                        'slate','spacelab','spruce','superheror',united',
                    ''',epilog="Kevin Cho 2012_03_05")

    argparser.add_argument("--input",
                           "-i",
                           metavar='Mard down or text files', 
                           help='''
                            Markdown text file
                           ''')

    argparser.add_argument("--theme",
                           "-t",
                           metavar='theme',
                           default='journal')

    argparser.add_argument("--html",
                           "-h",
                           metavar='html file that you want to change style')

    args = argparser.parse_args()

    if args.input:
        print 'a copy of {0} will be produced in html'.format(args.input)
        main(args.input,args.theme)

    if args.html:
        if raw_input('Change existing markdown to "Journal" theme ? [ Y or N ] : ') == 'Y':
            change(args.html,args.theme)
        else:
            sys.exit('Then, please specify theme with --theme')
