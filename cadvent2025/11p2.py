txt = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

from treelib import tree

# wee i LOVE parsing
data = txt.split("\n")
data = [x.split() for x in data]
values = [x[1:] for x in data]
keys = [x[0].strip(":") for x in data]

lookup = dict(zip(keys,values))

paths = Tree()

paths.create_node("svr",data="svr") # start node

def go(node):
    print(node)
    global paths
    for x in paths.get_node(node):
        paths.create_node(x,data=x)
        go(x)
        
go('svr')
paths.show