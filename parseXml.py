from xml.dom import minidom


INPUT_FILE_PATH = '/media/vesper/DATA/stackoverflow-data/divided-files/1.xml'


xmldoc = minidom.parse(INPUT_FILE_PATH)

itemlist = xmldoc.getElementsByTagName('row')

for s in itemlist:
    if ('Tags' in s.attributes):
        print(s.attributes['Tags'].value)

    # if 'Body' in  s.attributes:
    #     print(s.attributes['Body'].value)
    #
    # if 'Title' in  s.attributes:
    #     print(s.attributes['Title'].value)


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

