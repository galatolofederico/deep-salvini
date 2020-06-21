import argparse
import re
import string


def preporcess(line):
    results = re.search(r'(\d+) (\d+-\d+-\d+ \d+:\d+:\d+) (.+) <(.+)> (.+)', line)
    line = results.group(5)
    symbols = string.ascii_letters+string.digits+"!\"$%&\'()?àèéìùò<>"
    line = re.sub("((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*", "", line)
    line = "".join([i if i in symbols else " " for i in line])
    line = re.sub(" +", " ", line)
    if len(line) > 0:
        if line[0] == " ": line = line[1:]
        return line
    else:
        return None

parser = argparse.ArgumentParser()

parser.add_argument("--input", type=str, required=True)
parser.add_argument("--output", type=str, required=True)

args = parser.parse_args()


output_file = open(args.output, "w")
input_file = open(args.input, "r")

for line in input_file:
    line = preporcess(line)
    if line is not None:
        output_file.write(line+"\n")

input_file.close()
output_file.close()