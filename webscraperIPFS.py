from bs4 import BeautifulSoup
import requests
import os 
import os.path
import csv 
import time
import pprint


def parseHTMLForIpfs(filename):

    with open(filename, 'r') as htmlFile:
        contents = htmlFile.read()
        soup = BeautifulSoup(contents, 'lxml')
        table = soup.find_all("a", {"class": "ipfs-hash"})
        print(table)

        ipfs = []
        for ipfsLink in table:
            print(ipfsLink)
            if ipfsLink!=None:
                #ipfs.append("ipfs://" + ipfsLink['href'].split('/')[4].split('?')[0])
                ipfs.append(ipfsLink['href'])
                
    return ipfs

def printIpfsLinksToFile(ipfsCIDArray):
    with open('CID_gif_31_to_50.txt', 'w') as f:
        for cid in ipfsCIDArray:
            f.write(cid + "\n")
        

printIpfsLinksToFile(parseHTMLForIpfs("ipfs31to50.html"))
