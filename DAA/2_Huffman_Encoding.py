import heapq

# Creating Huffman tree node
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # frequency of symbol
        self.symbol = symbol  # symbol name (character)
        self.left = left  # node left of current node
        self.right = right  # node right of current node
        self.huff = ''  # tree direction (0/1)

    def __lt__(self, nxt):  # Check if curr frequency less than next nodes freq
        return self.freq < nxt.freq

def printnodes(node, val=''):
    newval = val + str(node.huff)
    # If node is not an edge node, traverse inside it
    if node.left:
        printnodes(node.left, newval)
    if node.right:
        printnodes(node.right, newval)

    # If node is edge node, display its Huffman code
    if not node.left and not node.right:
        print("{} -> {}".format(node.symbol, newval))

if __name__ == "__main__":
    # User input
    n = int(input("Enter the number of characters: "))
    chars = []
    freq = []

    print("Enter the characters and their frequencies:")
    for _ in range(n):
        char = input("Character: ")
        fr = int(input("Frequency: "))
        chars.append(char)
        freq.append(fr)

    # Huffman coding
    nodes = []
    for i in range(len(chars)):  # Convert characters and frequencies into Huffman tree nodes
        heapq.heappush(nodes, node(freq[i], chars[i]))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1
        # Combine the 2 smallest nodes to create new node as their parent
        newnode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newnode)

    # Display the Huffman codes
    print("\nHuffman Codes:")
    printnodes(nodes[0])  # Passing root of Huffman Tree
