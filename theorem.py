import sys

stack=[]
memory=[]
var_lookup={}

class Page:
    def __init__(self, initilizer):
        self.value = initilizer
        self.addr = len(memory)
    def read(self):
        return self.value
    def write(self, value):
        memory[self.addr] = value

if len(sys.argv) < 2:
    print("Usage: python theorem.py <file.theorem>")
    sys.exit(1)

file_path = sys.argv[1]
if file_path.endswith(".theorem"):
    1/1
else:
    print("theorem: error: file is not a theorem file")
    sys.exit(1)

lines=[]
def parse(path):
    fp = open(path, "r")
    for ln in fp:
        lines.append(ln)
    return lines

def exec(ln):
    words = ln.split(" ")
    print(words)
    i=0
    for word in words:
        i += 1
        match word:
            case "read_line":
                stack.append(input())
            case "|>":
                print(i)
                if words[i+1].startswith("$"):
                    var_lookup[words[i+1]] = stack.pop()
                else: 1/0
            case "printfn":
                if words[i+1].startswith("$"):
                    print(var_lookup[words[i+1]])
                else: 1/0
    
parse(file_path)
print(lines)
for ln in lines:
    exec(ln)