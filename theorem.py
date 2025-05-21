import sys

func_lookup = {
    "print": 1,
    "print_endline": 1,
    "|>": 1,
}


class Program:
    def __init__(self):
        self.stack = []
        self.var_lookup = {}

    def exec(self, code):
        words = code.split(" ")
        args = []
        for word, i in words:
            if word in func_lookup:
                for j in range(0, func_lookup[word]):
                    args.append(words[i+j])
            match word:
                case "print":
                    print(args[0], end='')
                case "print_endline":
                    print(args[0])
                case "|>":
                    self.var_lookup[args[0]] = self.stack.pop()



def parse(path):
    lines = []
    fp = open(path, "r")
    for ln in fp:
        lines.append(ln)
    return lines


file_path = sys.argv[1]
if file_path.endswith(".theorem"):
    1/1
else:
    print("theorem: error: file is not a theorem file")
    sys.exit(1)


if len(sys.argv) < 2:
    print("Usage: python theorem.py <file.theorem>")
    sys.exit(1)


runner = Program()
