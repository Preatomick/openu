import sys
import os


def check_input():
    try:
        assert len(sys.argv) > 2
    except AssertionError:
        print("Bad usage, try again")
        exit(0)


def main():
    check_input()
    os.system(f"tar -xvf {str(sys.argv[1])}.tar.gz")
    os.system(f"rm {str(sys.argv[1])}.tar.gz")
    for g in range(len(sys.argv)-2):
        os.system(f"mv {str(sys.argv[g+2])} {str(sys.argv[1])}")
    os.system(f"cd {str(sys.argv[1])}")
    os.system(f"./{str(sys.argv[1])}.SlackBuild")
    os.system(f"cd ./tmp/")
    os.system(f"upgradepkg install-new ")
    exit(0)


main()
