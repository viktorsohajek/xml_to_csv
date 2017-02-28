
# coding: utf-8
# author: Viktor Sohajek


import pandas as pd
import xml.etree.ElementTree as ET


input_path='criteo.xml'
output_path='criteo.csv'


### /FUNCTION DECLARATION ###
#fcn finds 'rows' element and cycles throuhg it. 
#Initialy it creates header and appends the rows to a Pandas DataFrame.
def create_dataframe(data):
    rows_index=find_index(data,'rows')
    df = pd.DataFrame(columns=data[rows_index][0].attrib.keys())
    for i in range(len(data[rows_index])-1):
            row=pd.Series(list(data[rows_index])[i].attrib)
            df=df.append(row,ignore_index=True)
    return df

# fcn finds index of given string element in etree structure (on the level of etree).
def find_index(etree,elemnt):
    i=0
    for child in list(etree):
        if (child.tag==elemnt):
            index=i
        i=i+1    
    return index
### FUNCTION DECLARATION/ ###



#load the etree interpretation of xlm file
etree = ET.fromstring(open(input_path).read())
#finds 'table' element
table_index=find_index(etree,'table')
# sets the etree of a 'table' element
table=etree[table_index]

# call the main fcn
df=create_dataframe(table)
#store the data to csv
df.to_csv(output_path,index=False)
