import pprint

board = {'top-L':'O','top-M':'O','top-R':' ','mid-L':' ','mid-M':'X','mid-R':' ','low-L':' ','low-M':' ','low-R':' '}

def printboard(theboard):
    print("\n",board['top-L'] + "|" + board['top-M'] + "|" + board['top-R'])
    print("-------")
    print("\n",board['mid-L'] + "|" + board['mid-M'] + "|" + board['mid-R'])
    print("-------")
    print("\n",board['low-L'] + "|" + board['low-M'] + "|" + board['low-R'])
    

printboard(board)
