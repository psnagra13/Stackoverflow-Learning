from xml.dom import minidom
import csv
from os import listdir
from os.path import isfile, join

INPUT_FILE_PATH = 'data/'
OUTPUT_FOLDER_PATH = 'output/extractedFromXML/'
def parseXMLFile(filePath):
    xmldoc = minidom.parse(filePath)
    itemlist = xmldoc.getElementsByTagName('row')
    return itemlist


def extractData(rows):
    dataList = []
    tagCount = 0
    TitleCount = 0
    IdCount = 0
    BodyCount = 0
    ViewCountCount  = 0
    CreationDateCount = 0
    totalRowCount = 0
    title_tag_count = 0
    title_body_tag_count = 0
    body_tag_count = 0
    for s in rows:
        isTag = False
        isId = False
        isBody = False
        isTitle = False
        isCreationDate = False
        isViewCount =False
        Tags = ''
        Title = ''
        Body = ''
        Id = ''
        CreationDate= ''
        ViewCount = ''
        totalRowCount+=1
        if ('Tags' in s.attributes ):
            Tags = s.attributes['Tags'].value
            isTag = True
        if ('Id' in s.attributes ):
            Id = s.attributes['Id'].value
            isId = True
        if ('Body' in s.attributes ):
            Body = s.attributes['Body'].value
            isBody = True
        if ('Title' in s.attributes ):
            Title = s.attributes['Title'].value
            isTitle = True
        if ('CreationDate' in s.attributes):
            CreationDate = s.attributes['CreationDate'].value
            isCreationDate = True
        if ('ViewCount' in s.attributes ):
            ViewCount = s.attributes['ViewCount'].value
            isViewCount = True
        dataList.append( {'Tags':Tags , 'Title':Title, 'Body':Body, 'Id':Id, 'CreationDate':CreationDate })

        if (isCreationDate):
            CreationDateCount += 1
        if (isId):
            IdCount+=1
        if (isTag):
             tagCount += 1
        if (isBody):
            BodyCount+=1
        if (isTitle):
            TitleCount+=1
        if (isViewCount):
            ViewCountCount+=1

        if (isTitle and isTag):
            title_tag_count+=1

        if (isTitle and isBody and isTag):
            title_body_tag_count +=1

        if (isBody and isTag):
            body_tag_count+=1


    print ("Total Rows = " + str(totalRowCount))
    print("Total Rows with Tags  = " + str(tagCount))
    print("Total Rows with Id  = " + str(IdCount))
    print("Total Rows with Title  = " + str(TitleCount))
    print("Total Rows with CreationDate  = " + str(CreationDateCount))
    print("Total Rows with Body  = " + str(BodyCount))
    print("Total Rows with ViewCount  = " + str(ViewCountCount))
    print("Total Rows with Title and Tag Both  = " + str(title_tag_count))
    print("Total Rows with Body and tag both   = " + str(body_tag_count))
    print("Total Rows with Body, Title and tag    = " + str(title_body_tag_count))
    return dataList

def writeToCsv(dataList, filePath):
    with open(filePath, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Id', 'Title', 'Body', 'Tags', 'CreationDate'])
        for row in dataList:
            writer.writerow([row['Id'], row['Title'],row['Body'],row['Tags'],row['CreationDate']])

def getAllFilesInFolder(FolderPath):
    fileNames = [f for f in listdir(FolderPath) if isfile(join(FolderPath, f))]
    return fileNames


if __name__ == '__main__':

    fileNames = getAllFilesInFolder(INPUT_FILE_PATH)

    print ("Total number of files found = " + str(len(fileNames)))

    for fileName in fileNames:
        rows = parseXMLFile(INPUT_FILE_PATH + fileName)
        dataList = extractData(rows)
        writeToCsv(dataList, OUTPUT_FOLDER_PATH + fileName.replace('.xml', '.csv'))







'''
<row Id="6" 
    PostTypeId="1" 
    AcceptedAnswerId="31" 
    CreationDate="2008-07-31T22:08:08.620" 
    Score="261" 
    ViewCount="16799" 
    Body="&lt;p&gt;I have an absolutely positioned &lt;code&gt;div&lt;/code&gt; containing several children, one of which is a relatively positioned &lt;code&gt;div&lt;/code&gt;. When I use a &lt;strong&gt;percentage-based width&lt;/strong&gt; on the child &lt;code&gt;div&lt;/code&gt;, it collapses to '0' width on &lt;a href=&quot;http://en.wikipedia.org/wiki/Internet_Explorer_7&quot; rel=&quot;noreferrer&quot;&gt;Internet&amp;nbsp;Explorer&amp;nbsp;7&lt;/a&gt;, but not on Firefox or Safari.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;If I use &lt;strong&gt;pixel width&lt;/strong&gt;, it works. If the parent is relatively positioned, the percentage width on the child works.&lt;/p&gt;&#xA;&#xA;&lt;ol&gt;&#xA;&lt;li&gt;Is there something I'm missing here?&lt;/li&gt;&#xA;&lt;li&gt;Is there an easy fix for this besides the &lt;em&gt;pixel-based width&lt;/em&gt; on the&#xA;child?&lt;/li&gt;&#xA;&lt;li&gt;Is there an area of the CSS specification that covers this?&lt;/li&gt;&#xA;&lt;/ol&gt;&#xA;" 
    OwnerUserId="9" 
    LastEditorUserId="63550" 
    LastEditorDisplayName="Rich B" 
    LastEditDate="2016-03-19T06:05:48.487" 
    LastActivityDate="2018-10-16T16:54:34.953" 
    Title="Percentage width child element in absolutely positioned parent on Internet Explorer 7" 
    Tags="&lt;html&gt;&lt;css&gt;&lt;css3&gt;&lt;internet-explorer-7&gt;" 
    AnswerCount="6" 
    CommentCount="0" 
    FavoriteCount="12" />
'''

