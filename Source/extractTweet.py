'''
Created by Balachandar Kulala

This code does the following actions:
1. Reads the JSON file which has the tweets line by line.
2. Extracts the Hash tags and URLs from the tweet
3. Finally writes into  the Text File.
'''

import sys
import re
class jsonFileParser:
    def __init__(self):
        print("Init started..")
    
    def parseJsonData(self, srcFile):
        hashTagURLFile = open("extractedHashTagURLs.txt",'w')
        try:
            jsonFile= open(srcFile,'r');row_count = 1
            if jsonFile is None:
                print ("source JSON file not found")
                sys.exit()
            else:
                for line in jsonFile:
                    line_split = line.split(',"')
                    for _char in (line_split):
                        if _char == "":
                            continue
                        tweetdata = _char.split(':')
                        if '{' in  tweetdata[0] :
                            print ("Start of the JSON data..")
                        elif "#" in tweetdata[1]:
                            hashTagsList = self.parseHashTags(tweetdata[1])
                            print ("Hashtag List:",hashTagsList)
                            ## have write into a file
                            if len(hashTagsList) > 0:
                                if len(hashTagsList) == 1:
                                    hashTagsList = hashTagsList.replace('\\',"")
                                    hashTagURLFile.write(str(hashTagsList).strip('"'))
                                else:
                                    for item in hashTagsList:
                                        item = item.replace('\\',"")
                                        hashTagURLFile.write(item.strip('"'))
                                hashTagURLFile.write('\n')
                            else:
                                print ("No hash tags found in this tweet:",line_split)
                        elif ("http" in _char) or ("www" in _char):
                            urlList = self.parseURL(_char)
                            ## have write into a file
                            print ("URL List:",urlList)
                            if len(urlList) > 0:
                                if len(urlList) == 1:
                                    hashTagURLFile.write(urlList.strip('"'))
                                else:
                                    for item in urlList:
                                        hashTagURLFile.write(item.strip('"'))
                                hashTagURLFile.write('\n')
                            else:
                                print ("No hash urls found in this tweet:",line_split)
                        
                        
        except:
            print("Error occured..")
            hashTagURLFile.close()
            jsonFile.close()
        hashTagURLFile.close()
        jsonFile.close()
    def parseHashTags(self, data_value):
        data = ""
        try:
            print ("Parsing for the hash tags..")
            hashTagdata = data_value.split(' ')
            for hashtag in hashTagdata:
                if "#" in hashtag[0]:
                    data = data + hashtag +','## adding data to the list
                    print ("The  hash tag:",hashtag)
        except:
            print("Exception found while parsing for the hash tags")
            data =""
            return data
        return data
    
    def parseURL(self,  data_value):
        urlValues = ""
        try:
            urldata = data_value.split('":"')
            for url in urldata:
                if ("https:" in url) or ("http:" in url) or ("www" in url):
                    url = url.replace('\\',"")
                    if ("https" not in url[0:5]) or ("http" not in url[0:4]) or ("www" not in url[0:3]):
                        url_list = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)
                        for _url in (url_list):               
                            urlValues = urlValues + _url + ','
                    else:
                        urlValues = urlValues + url +','
        except: 
            print ("Exception occurred while parsing the url")
            urlValues = ""
            return urlValues
        return urlValues
                    

parserObj =jsonFileParser()
parserObj.parseJsonData("/home/student/Installations/TwitterProject/twittertweets.json")

