import fileinput
import sys
import os



def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)


#os.path.join(root,file)
replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running1.txt', r"{", r"")
replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running1.txt', r"}", r"")
replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running1.txt', r",", "\t")

replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running2.txt', r"{", r"")
replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running2.txt', r"}", r"")
replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running2.txt', r",", "\t")

replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running3.txt', r"{", r"")
replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running3.txt', r"}", r"")
replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running3.txt', r",", "\t")

replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running4.txt', r"{", r"")
replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running4.txt', r"}", r"")
replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running4.txt', r",", "\t")