import click
import subprocess
import textwrap


@click.command()
@click.option('-t', '--text', help='Text to center in comment.')
@click.option('-w', '--width', type=int, help='Total width of comment.')
def comgen(text, width):
    top = '/' + '-'*(len(text)+2) + '\\'
    top = '#' + top.center(width-1)
    bottom = '\\' + '-'*(len(text)+2) + '/'
    bottom = '#' + bottom.center(width-1)
    middle = '| '+text+' |'  # need to add line wrapping
    middle = '# ' + middle.center(width-2, '-')
    comment = top+'\n'+middle+'\n'+bottom
    subprocess.run("pbcopy", universal_newlines=True, input=comment)
    xprint(comment)
    xprint('Copied to clipboard.', color=colors.OKGREEN)

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def xprint(*args, **kwargs):
    try:
        c = kwargs['color']
        end = colors.ENDC
        del kwargs['color'] # dont pass color to print() kwargs
        print(c+" ".join(map(str,args))+end, **kwargs)
    except: 
        print(" ".join(map(str,args)), **kwargs)

if __name__ == '__main__':
    comgen()
