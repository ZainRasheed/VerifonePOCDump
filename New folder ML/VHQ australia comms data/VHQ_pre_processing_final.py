# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a final script file.
for data pre-processing of VHQ data
"""
#%% Block 1 IMPORTS
import pandas as pd
import xml.etree.ElementTree as et

#%% Block 2 Function to convert XML
def convertxmltodict(xml, column_name = "", xml_dictionary = {}):
    column_name = column_name+"_"+xml.tag
    for keyy in xml.keys():
        c_k_name = column_name+"_"+str(keyy)
        if c_k_name in xml_dictionary.keys():
            xml_dictionary.update({c_k_name : int(xml_dictionary[c_k_name])+1})
        else:
            xml_dictionary.update({c_k_name : int(1)})
    if(xml.find("./") != None):
        for child_tag in xml:
            convertxmltodict(child_tag, column_name, xml_dictionary)
    return xml_dictionary

#%% Block 3 Read the csv
rawData = pd.read_csv("C:/Users/mohammeds2/OneDrive - Verifone/Desktop/New folder (4) ML/VHQ australia comms data/VHQAustraliaPost_DeviceCommunicationHistory.csv")

#%% Block 4 Clean the cert
deleted_data = pd.DataFrame()
for data in rawData.iterrows():
    index = data[0]
    row = data[1]   
    print(">>>>>>>>>> " +str(index))     
    if "--BEGIN CERTIFICATE--" in row["HistoryId"]:
        iterator = index + 1
        while not "END CERTIFICATE" in rawData["HistoryId"].loc[iterator]:
            deleted_data = deleted_data.append(rawData.loc[iterator])
            rawData = rawData.drop(iterator) 
            iterator+=1
    if "<EncrAgentKeys" in str(row["InputXML"]):
        iterator = index + 1
        while not "</EncrAgentKey" in rawData["HistoryId"].loc[iterator]:
            deleted_data = deleted_data.append(rawData.loc[iterator])
            rawData = rawData.drop(iterator) 
            iterator+=1  
    if "<EncrAgentKeysSig" in row["HistoryId"]:
        iterator = index + 1
        while not "</EncrAgentKeysSig" in rawData["HistoryId"].loc[iterator]:
            if "</EncrAgentKeysSig" in row["HistoryId"]:
                break
            deleted_data = deleted_data.append(rawData.loc[iterator])
            rawData = rawData.drop(iterator) 
            iterator+=1


concat = False
for data in rawData.iterrows():
    index = data[0]
    row = data[1]
    print("---------- " +str(index))     
    if concat:
        string_concat = string_concat + str(row["HistoryId"])
        deleted_data = deleted_data.append(rawData.loc[index])  
        rawData = rawData.drop(index)
    if "<EncrAgentKeys" in str(row["InputXML"]):
        iterator = index
        string_concat = str(row["InputXML"])
        concat = True
    if "</EncrAgentKeysSig" in row["HistoryId"]:
        concat = False
        rawData["InputXML"].loc[iterator] = string_concat

#%%  Block 5 Convert the List of XML
vhq_df = pd.DataFrame()
for data in rawData.iterrows():
    print(data[0])
    row = data[1]
    final_row = dict(row)
    if str(row["InputXML"]) != "nan":
        if  str(row["Rasheed"]) != "nan":    
            XML_string = row["InputXML"] + " " + row["Rasheed"]
            XML_true = et.fromstring(XML_string)
        else:
            XML_true = et.fromstring(row["InputXML"])
        empty_dictionary = {}
        xml_as_dict_row = convertxmltodict(XML_true, xml_dictionary = empty_dictionary)
        final_row.update(xml_as_dict_row)                 
    vhq_df = vhq_df.append(final_row, ignore_index=True)
#%% BLOCK 6 Extraction of Excel sheet
vhq_df.to_csv(r"C:/Users/mohammeds2/OneDrive - Verifone/Desktop/New folder (4) ML/VHQ australia comms data/VHQAustraliaPost_OUTPUT_DeviceCommunicationHistory.csv", header = True)
