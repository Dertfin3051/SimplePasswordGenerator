import os
import random

try:
    import argparse
except ModuleNotFoundError:
    print("Installing required libraries...")
    os.system("pip install argparse")
    print("argparse installed successfully.")
    import argparse


class Aliases:
    char = "abcdefghigklmnopqrstuvw"  # Don't use "xyz", because they are using in another case
    nums = "1234567890"  # Nubmers
    symb = ".!,?"  # Simple Symbols

    # ".." = "."
    # "." = any punctuation symbol
    types = [
        "a123..231b",
        "x12a..231b",
        "A12b.321x",
        "123a213b.",
        "12a3.21bx"
    ]


class Data:
    def __init__(self):
        self.a = random.choice(Aliases.char)
        self.b = random.choice(Aliases.char)
        self.c = random.choice(Aliases.char)
        self.num1 = random.choice(Aliases.nums)
        self.num2 = random.choice(Aliases.nums)
        self.num3 = random.choice(Aliases.nums)
        self.symb1 = random.choice(Aliases.symb)
        self.symb2 = random.choice(Aliases.symb)


parser = argparse.ArgumentParser("Arguments of Simple Password Generator")
parser.add_argument("-t", "--type", type = int, help = f"Choose generator's sample from 0 to {len(Aliases.types)}")
parser.add_argument("-f", "--file", type = str, help = "File name for recording the prepared password")
parser.add_argument("-rw", "--rawfile", type = str, help = "File name for recording the prepared password with deleting another data")
args = parser.parse_args()


def choose_gentype():
    if args.type:
        gen_type = args.type
    else:
        gen_type = random.randint(0, len(Aliases.types) - 1)
    return gen_type


def replace_placeholders(password: str, Data):
    newpass = password
    newpass = newpass.replace("..", ".")
    newpass = newpass.replace("a", data.a)
    newpass = newpass.replace("b", data.b)
    newpass = newpass.replace("c", data.c)
    newpass = newpass.replace("1", data.num1)
    newpass = newpass.replace("2", data.num2)
    newpass = newpass.replace("3", data.num3)
    newpass = newpass.replace(".", data.symb1)
    newpass = newpass.replace(",", data.symb2)

    return newpass


def save_password(password: str):
    if args.file:
        if not os.path.exists(args.file):
            open(args.file, "w")
        with open(args.file, "r") as f:
            file_data = f.readlines()
        file_data.append(password + "\n")
        with open(args.file, "w") as f:
            f.writelines(file_data)
        print("It's written to ", args.file)
    if args.rawfile:
        with open(args.rawfile, "w") as f:
            f.write(password)
        print("It's written(raw) to ", args.rawfile)


gentype = choose_gentype()    # Choose the generator type
data = Data()    # Generating symbols
password = replace_placeholders(
    Aliases.types[gentype],
    data
)
print()    # Empty line
print("Your password is : ", password)    # Reasult
save_password(password)    # Saving password to file if it's required
print()    # Empty line