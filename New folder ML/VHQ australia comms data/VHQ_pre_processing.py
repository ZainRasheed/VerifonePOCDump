# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
for data pre-processing of VHQ data
"""
#%% Block 1 IMPORTS
import pandas as pd
import xml.etree.ElementTree as et
#%%

#"""
#FAILED
rawData = pd.read_csv("C:/Users/mohammeds2/OneDrive - Verifone/Desktop/New folder (4) ML/VHQ australia comms data/VHQAustraliaPost_DeviceCommunicationHistory.csv", sep=',')
rawData.info()
rawData.count()

#TEST to find cert
digit = 0
word = 0
for row in rawData.iterrows():
    if(row[1]["HistoryId"].isdigit()):
        #print(row[1]["HistoryId"])
        digit+=1
    else:
        word+=1
print(digit, word)
#    if (row[0] < 200): 
#        print(row[1].str.contains("[a-zA-Z]"))    
for row in rawData.iterrows():
    cleaned_data_bool = row[1]["HistoryId"].isdigit()

#hist_ID_bool = rawData["HistoryId"].str.isdigit()
#cleaned_data = rawData[hist_ID_bool]
#cleaned_data.info()
    
#TEST to confirm the excluson of cert rows
hist_ID_bool_not = ~ hist_ID_bool
cert = rawData[hist_ID_bool_not]
cert.info() 

#TEST to find split xmls in "Rasheed" column   
for row in cleaned_data.iterrows():
    index = row[0]
    data =row[1]
    print(data["Rasheed"])
    if(pd.notna(data["Rasheed"])):
        digit+=1
print(digit)

#TEST solving the slipt cells by concatinating DOESN't WORK
for row in cleaned_data.iterrows():
    index = row[0]
    data = row[1]
    if(pd.notna(data["Rasheed"])):
        data["InputXML"] = str(data["InputXML"]) +";"+ str(data["Rasheed"])

#%% Block 2 Function to convert XML
def convertxmltodict(xml, column_name = "", xml_dictionary = {}):
    #TODO do the if thingy
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
#%%
 
#To clean the certificate text from rows DON'T NEED THIS
#hist_ID_bool = rawData["HistoryId"].str.isdigit()
#cleaned_data = rawData[hist_ID_bool]
#cleaned_data.info()

#To concat the broken XML DON'T NEED THIS
#rasheed_bool = cleaned_data["Rasheed"].notna()
#rasheed_bool.value_counts()
#cleaned_data_test = cleaned_data.copy()
#cleaned_data_test.loc[rasheed_bool, "InputXML"] =  cleaned_data.loc[rasheed_bool,"InputXML"] +"      "+ cleaned_data.loc[rasheed_bool,"Rasheed"]
    
#To truncate the cert text and combine the cert XML
#%% Block 3 Read the csv
rawData = pd.read_csv("C:/Users/mohammeds2/OneDrive - Verifone/Desktop/New folder (4) ML/VHQ australia comms data/VHQAustraliaPost_DeviceCommunicationHistory.csv")
print(rawData["HistoryId"].loc[0])
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
    #if not "nan" in str(row["Rasheed"]):
        #rawData["InputXML"].loc[index] = row["InputXML"] + " " + row["Rasheed"]
        #rawData["InputXML"].loc[index] = row["InputXML"].join(row["Rasheed"])
        
#%%  Block 5 Convert the List of XML
vhq_df = pd.DataFrame()
for data in rawData.iterrows():
    index = data[0]
    row = data[1]
    if str(row["InputXML"]) != "nan":
        if  str(row["Rasheed"]) != "nan":    
            XML_string = row["InputXML"] + " " + row["Rasheed"]
            XML_true = et.fromstring(XML_string)
            empty_dictionary = {}
            xml_as_dict_row = convertxmltodict(XML_true, xml_dictionary = empty_dictionary)
            final_row = dict(row)
            final_row.update(xml_as_dict_row)            
            vhq_df = vhq_df.append(final_row, ignore_index=True)
        else:
            XML_true = et.fromstring(row["InputXML"])
            empty_dictionary = {}            
            xml_as_dict_row = convertxmltodict(XML_true, xml_dictionary = empty_dictionary)
            final_row = dict(row)                        
            final_row.update(xml_as_dict_row)
            vhq_df = vhq_df.append(final_row, ignore_index=True)    
    else:
        final_row = dict(row)                        
        final_row.update({})        
        vhq_df = vhq_df.append(final_row, ignore_index=True)

        
#%% NOT NEEDED Block 6 Combine dataframe with generated XML table 

final_vhq_df = pd.DataFrame()
final_vhq_df = pd.concat([rawData, vhq_df.reindex(rawData.index)], axis=1)
#%% 

#Concating the xml and usinf the CONVERT XML FUNCTION DON'T NEED THIS
#iterator = 0
vhq_df = pd.DataFrame()
for data in cleaned_data.iterrows():
    index = data[0]
    row = data[1]
    #iterator+=1
    if str(row["InputXML"]) != "nan":
        if  str(row["Rasheed"]) != "nan":    
            xml_string = str(row["InputXML"])+" "+str(row["Rasheed"])
            truexml = et.fromstring(xml_string)
            vhq_df = vhq_df.append(convertxmltodict(truexml), ignore_index=True)
        else:
            truexml = et.fromstring(str(row["InputXML"]))
            vhq_df = vhq_df.append(convertxmltodict(truexml), ignore_index=True)
    else:
        vhq_df = vhq_df.append({}, ignore_index=True)
        
#%%
        

rawDataDevice = pd.read_csv("C:/Users/mohammeds2/OneDrive - Verifone/Desktop/New folder (4) ML/VHQ australia comms data/VHQAustraliaPost_DeviceCommunicationHistory.csv",
                      #skipinitialspace = True,
                      usecols = ["UniqueDeviceId"])

rawXMLData = pd.read_csv("C:/Users/mohammeds2/OneDrive - Verifone/Desktop/New folder (4) ML/VHQ australia comms data/VHQAustraliaPost_DeviceCommunicationHistory.csv",
                      #skipinitialspace = True,
                      usecols = ["InputXML"])

"""
rawData = pd.DataFrame("C:/Users/mohammeds2/OneDrive - Verifone/Desktop/New folder (4) ML/VHQ australia comms data/VHQAustraliaPost_DeviceCommunicationHistory.csv",
                       columns = ['HistoryId'])
"""   