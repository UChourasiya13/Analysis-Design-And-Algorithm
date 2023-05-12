from queue import PriorityQueue

# Node class for creating Huffman tree nodes
class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
    
    # comparator for nodes
    def __lt__(self, other):
        return self.freq < other.freq

# function to build Huffman tree
def build_huffman_tree(freq_dict):
    # create a priority queue of nodes
    pq = PriorityQueue()
    for char, freq in freq_dict.items():
        pq.put(Node(freq, char))
    
    # repeatedly remove two nodes with lowest frequency and combine them into one node
    while pq.qsize() > 1:
        left_node = pq.get()
        right_node = pq.get()
        combined_freq = left_node.freq + right_node.freq
        combined_node = Node(combined_freq, left=left_node, right=right_node)
        pq.put(combined_node)
    
    # the remaining node is the root of the Huffman tree
    return pq.get()

# function to generate Huffman codes for each character in the tree
def generate_huffman_codes(root, code_dict, code=""):
    if root.char:
        code_dict[root.char] = code
    else:
        generate_huffman_codes(root.left, code_dict, code + "0")
        generate_huffman_codes(root.right, code_dict, code + "1")

# function to compress a given string using Huffman coding
def compress_string(input_str):
    # create a dictionary of character frequencies
    freq_dict = {}
    for char in input_str:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    
    # build Huffman tree
    root = build_huffman_tree(freq_dict)
    
    # generate Huffman codes
    code_dict = {}
    generate_huffman_codes(root, code_dict)
    
    # compress input string using Huffman codes
    compressed_bits = ""
    for char in input_str:
        compressed_bits += code_dict[char]
    
    # pad compressed bits to make length a multiple of 8
    num_padding_bits = (8 - len(compressed_bits) % 8) % 8
    compressed_bits += "0" * num_padding_bits
    
    # convert compressed bits to bytes
    compressed_bytes = bytearray()
    for i in range(0, len(compressed_bits), 8):
        byte_str = compressed_bits[i:i+8]
        compressed_bytes.append(int(byte_str, 2))
    
    # return compressed bytes and padding information
    return compressed_bytes, num_padding_bits
