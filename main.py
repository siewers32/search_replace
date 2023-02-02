from os import strerror
from pathlib import Path
import os

def file_list():
    content = []
    p = "import"
    mydir = f"{os.getcwd()}/{p}"
    for f in Path(mydir).iterdir():
        if f.is_file() and f.suffix == '.md':
            # print(f"In filelist..{p}/{f.name}")
            # resultaat = read_xls(f"{p}/{f.name}")
            content.append(f)
    return content

def edit_file(f):
    p = "export"
    myfile = f"{os.getcwd()}/{p}/{f.name}"
    fo = open(myfile, 'at')
    try:
        for line in open(f, 'rt'):
            print(line[:11])
            if line[:14] == "## {{ title }}":
                fo.write('# {{ title }}\n')
            elif line[:11] == "***Uitvoer*":
                fo.write('### Resultaat\n')
            elif line[:11] == "***Taak:***":
                fo.write('### Resultaat\n')
            elif line[:11] == "***Opdracht":
                fo.write('### Resultaat\n')
            elif line[:11] == "***Omschrij":
                fo.write('### Omschrijving\n')
            elif line[:11] == "***Beschrij":
                fo.write('### Omschrijving\n')
            elif line[:11] == "* Programme":
                fo.write('> ### Voorkennis\n')
                fo.write('> Programmeertaal: naar keuze\n')
            else:
                fo.write(line)

    except IOError as e:
        print("Cannot open the source file: ", strerror(e.errno))
        exit(e.errno)

def process_files():
    files = file_list()
    for f in files:
        edit_file(f)



process_files()