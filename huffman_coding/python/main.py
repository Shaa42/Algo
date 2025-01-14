from heapq import heapify, heappop, heappush
from pprint import pprint

class Node:
    def __init__(self, character : str, frequency : int, leftNode, rightNode) -> None:
        self.character = character
        self.frequency = frequency
        
        self.leftNode = leftNode
        self.rightNode = rightNode
    
    def __lt__(self, comparedNode) -> bool:
        return self.frequency <= comparedNode.frequency


def frequency(string : str) -> dict:
    freq_table = {}
    for character in string:
        if freq_table.get(character, 0):
            freq_table[character] += 1
        else :
            freq_table[character] = 1
    return freq_table

def HuffmanTree(string : str) -> Node:
    if len(string) == 0:
        return
    # Put the nodes in a priority queue
    freq_table = frequency(string)
    pq = [Node(ch, f, None, None) for ch, f in freq_table.items()] # N.B : can't work if "Node" doesn't have "__lt__" method
    heapify(pq)
    
    # Create new nodes
    while len(pq) > 1:
        # Get the two smallest value
        leftNode = heappop(pq)
        rightNode = heappop(pq)
        
        # sum the two Nodes and create a Node from it
        newFreq = leftNode.frequency + rightNode.frequency
        newNode = Node(None, newFreq, leftNode, rightNode)
        heappush(pq, newNode)
        
    # return the tree's root
    root = pq[0]
    return root

def treeToDict(Tree: Node) -> dict:
    if Tree is None:
        return None
    
    # Si c'est une feuille, retournez son caractère et sa fréquence
    if Tree.leftNode is None and Tree.rightNode is None:
        return {"character": Tree.character, "frequency": Tree.frequency}
    
    # Sinon, retournez un dictionnaire avec les sous-arbres
    return {
        "value": Tree.frequency,
        "left": treeToDict(Tree.leftNode),
        "right": treeToDict(Tree.rightNode)
    }
    
def HuffmanCodingDic(dic, str='', res_dic = {}):
    if dic.get('character', 0):
        res_dic[dic['character']] = str
    if dic.get('left', 0):
        HuffmanCodingDic(dic['left'], str + '0')
    if dic.get('right', 0):
        HuffmanCodingDic(dic['right'], str + '1')
    return res_dic

def HuffmanCoding(string : str, debug=False):
    root = HuffmanTree(string)
    huffman_dic = treeToDict(root)
    huffmancode_dic = HuffmanCodingDic(huffman_dic)
    
    huffman_string = ''
    for character in string:
        huffman_string += huffmancode_dic[character]

    if debug:
        print(huffmancode_dic)
        
    return huffman_string

if __name__ == "__main__":
    # Tests
    # exemp = "ADBADEDBBDD"
    # exemp = "BCCABBDDAECCBBAEDDCC"
    # exemp = "AABCBAD"
    exemp = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
    
    # Stats
    huffman_exemp = HuffmanCoding(exemp)
    bits_exemp = len(exemp) * 8 # Based on ASCII characters
    bits_huffman_exemp = len(huffman_exemp) * 1 # 1 or 0
    
    # Debug
    print("original : " + exemp)
    print("new : " + huffman_exemp)
    print(f"original size : {bits_exemp} bits")
    print(f"new size : {bits_huffman_exemp} bits")
    pourcentage = bits_exemp / bits_huffman_exemp
    print(f"It's {round(pourcentage, 2)}x smaller !")