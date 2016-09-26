import fileinput
import sys
import os



def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)


##os.path.join(root,file)
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_1.txt', r"{", r"")
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_1.txt', r"}", r"")
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_1.txt', r",", "\t")
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_1.txt', r"*^", "e")
#
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_2.txt', r"{", r"")
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_2.txt', r"}", r"")
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_2.txt', r",", "\t")
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_2.txt', r"*^", "e")
#
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_3.txt', r"{", r"")
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_3.txt', r"}", r"")
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_3.txt', r",", "\t")
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_3.txt', r"*^", "e")
#
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_4.txt', r"{", r"")
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_4.txt', r"}", r"")
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_4.txt', r",", "\t")
#replaceAll('/home/dkahl/Documents/Masterarbeit/arbeiten/Masterarbeit/Python/data/alpha_running/alpha_running_4.txt', r"*^", "e")
#
for root, dirs, files in os.walk("data/alpha_running"):
    for file in files:
        replaceAll(os.path.join(root,file), r"{", r"")
        replaceAll(os.path.join(root,file), r"}", r"")
        replaceAll(os.path.join(root,file), r",", "\t")
        replaceAll(os.path.join(root,file), r"*^", "e")