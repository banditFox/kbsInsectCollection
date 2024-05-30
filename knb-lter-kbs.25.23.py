# Package ID: knb-lter-kbs.25.23 Cataloging System:https://pasta.lternet.edu.
# Data set title: KBS Insect Collections at the Kellogg Biological Station, Hickory Corners, MI .
# Data set creator:    -  
# Contact:    - Information Manager LTER Network Office  - tech-support@lternet.edu
# Contact:    - Data Manager Kellogg Biological Station  - lter.data.manager@kbs.msu.edu
# Metadata Link: https://portal.lternet.edu/nis/metadataviewer?packageid=knb-lter-kbs.25.23
# Stylesheet v1.0 for metadata conversion into program: John H. Porter, Univ. Virginia, jporter@virginia.edu      
# 
# This program creates numbered PANDA dataframes named dt1,dt2,dt3...,
# one for each data table in the dataset. It also provides some basic
# summaries of their contents. NumPy and Pandas modules need to be installed
# for the program to run. 

import numpy as np
import pandas as pd 

infile1  ="https://pasta.lternet.edu/package/data/eml/knb-lter-kbs/25/23/c10afa286d33a94c221b1dfd3b05de09".strip() 
infile1  = infile1.replace("https://","http://")
                 
dt1 =pd.read_csv(infile1 
          ,skiprows=41
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "Order",     
                    "Family",     
                    "Genus",     
                    "SpecificEpithet",     
                    "Author",     
                    "CommonName",     
                    "Comments",     
                    "IdentifyingCharacteristics",     
                    "CommonGroup",     
                    "FunctionalGroup",     
                    "Hosts",     
                    "LifeHistory",     
                    "Habitat",     
                    "GeographicDistribution",     
                    "Origin",     
                    "Species",     
                    "Specimen",     
                    "StorageLocation",     
                    "Stage_Sex",     
                    "Treatment",     
                    "Replicate",     
                    "Collector",     
                    "img_src"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'Order':'str' ,  
#             'Family':'str' ,  
#             'Genus':'str' ,  
#             'SpecificEpithet':'str' ,  
#             'Author':'str' ,  
#             'CommonName':'str' ,  
#             'Comments':'str' ,  
#             'IdentifyingCharacteristics':'str' ,  
#             'CommonGroup':'str' ,  
#             'FunctionalGroup':'str' ,  
#             'Hosts':'str' ,  
#             'LifeHistory':'str' ,  
#             'Habitat':'str' ,  
#             'GeographicDistribution':'str' ,  
#             'Origin':'str' ,  
#             'Species':'str' ,  
#             'Specimen':'str' ,  
#             'StorageLocation':'str' ,  
#             'Stage_Sex':'str' ,  
#             'Treatment':'str' ,  
#             'Replicate':'str' ,  
#             'Collector':'str' ,  
#             'img_src':'str'  
#        }
    )
# Coerce the data into the types specified in the metadata  
dt1.Order=dt1.Order.astype('category')  
dt1.Family=dt1.Family.astype('category')  
dt1.Genus=dt1.Genus.astype('category')  
dt1.SpecificEpithet=dt1.SpecificEpithet.astype('category')  
dt1.Author=dt1.Author.astype('category')  
dt1.CommonName=dt1.CommonName.astype('category')  
dt1.Comments=dt1.Comments.astype('category')  
dt1.IdentifyingCharacteristics=dt1.IdentifyingCharacteristics.astype('category')  
dt1.CommonGroup=dt1.CommonGroup.astype('category')  
dt1.FunctionalGroup=dt1.FunctionalGroup.astype('category')  
dt1.Hosts=dt1.Hosts.astype('category')  
dt1.LifeHistory=dt1.LifeHistory.astype('category')  
dt1.Habitat=dt1.Habitat.astype('category')  
dt1.GeographicDistribution=dt1.GeographicDistribution.astype('category')  
dt1.Origin=dt1.Origin.astype('category')  
dt1.Species=dt1.Species.astype('category')  
dt1.Specimen=dt1.Specimen.astype('category')  
dt1.StorageLocation=dt1.StorageLocation.astype('category')  
dt1.Stage_Sex=dt1.Stage_Sex.astype('category')  
dt1.Treatment=dt1.Treatment.astype('category')  
dt1.Replicate=dt1.Replicate.astype('category')  
dt1.Collector=dt1.Collector.astype('category')  
dt1.img_src=dt1.img_src.astype('category') 
      
print("Here is a description of the data frame dt1 and number of lines\n")
print(dt1.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt1\n")
print(dt1.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt1.Order.describe())               
print("--------------------\n\n")
                    
print(dt1.Family.describe())               
print("--------------------\n\n")
                    
print(dt1.Genus.describe())               
print("--------------------\n\n")
                    
print(dt1.SpecificEpithet.describe())               
print("--------------------\n\n")
                    
print(dt1.Author.describe())               
print("--------------------\n\n")
                    
print(dt1.CommonName.describe())               
print("--------------------\n\n")
                    
print(dt1.Comments.describe())               
print("--------------------\n\n")
                    
print(dt1.IdentifyingCharacteristics.describe())               
print("--------------------\n\n")
                    
print(dt1.CommonGroup.describe())               
print("--------------------\n\n")
                    
print(dt1.FunctionalGroup.describe())               
print("--------------------\n\n")
                    
print(dt1.Hosts.describe())               
print("--------------------\n\n")
                    
print(dt1.LifeHistory.describe())               
print("--------------------\n\n")
                    
print(dt1.Habitat.describe())               
print("--------------------\n\n")
                    
print(dt1.GeographicDistribution.describe())               
print("--------------------\n\n")
                    
print(dt1.Origin.describe())               
print("--------------------\n\n")
                    
print(dt1.Species.describe())               
print("--------------------\n\n")
                    
print(dt1.Specimen.describe())               
print("--------------------\n\n")
                    
print(dt1.StorageLocation.describe())               
print("--------------------\n\n")
                    
print(dt1.Stage_Sex.describe())               
print("--------------------\n\n")
                    
print(dt1.Treatment.describe())               
print("--------------------\n\n")
                    
print(dt1.Replicate.describe())               
print("--------------------\n\n")
                    
print(dt1.Collector.describe())               
print("--------------------\n\n")
                    
print(dt1.img_src.describe())               
print("--------------------\n\n")
                    
                    
                 

infile2  ="https://pasta.lternet.edu/package/data/eml/knb-lter-kbs/25/23/61b96c58746cf9fb64070614bbdc96dc".strip() 
infile2  = infile2.replace("https://","http://")
                 
dt2 =pd.read_csv(infile2 
          ,skiprows=26
            ,sep=","  
                ,quotechar='"' 
           , names=[
                    "order",     
                    "family",     
                    "genus",     
                    "specific_epithet",     
                    "photographer",     
                    "photo_description",     
                    "specimen_id",     
                    "img_href"    ]
# data type checking is commented out because it may cause data
# loads to fail if the data contains inconsistent values. Uncomment 
# the following lines to enable data type checking
         
#            ,dtype={  
#             'order':'str' ,  
#             'family':'str' ,  
#             'genus':'str' ,  
#             'specific_epithet':'str' ,  
#             'photographer':'str' ,  
#             'photo_description':'str' ,  
#             'specimen_id':'str' ,  
#             'img_href':'str'  
#        }
    )
# Coerce the data into the types specified in the metadata  
dt2.order=dt2.order.astype('category')  
dt2.family=dt2.family.astype('category')  
dt2.genus=dt2.genus.astype('category')  
dt2.specific_epithet=dt2.specific_epithet.astype('category')  
dt2.photographer=dt2.photographer.astype('category')  
dt2.photo_description=dt2.photo_description.astype('category')  
dt2.specimen_id=dt2.specimen_id.astype('category')  
dt2.img_href=dt2.img_href.astype('category') 
      
print("Here is a description of the data frame dt2 and number of lines\n")
print(dt2.info())
print("--------------------\n\n")                
print("Here is a summary of numerical variables in the data frame dt2\n")
print(dt2.describe())
print("--------------------\n\n")                
                         
print("The analyses below are basic descriptions of the variables. After testing, they should be replaced.\n")                 

print(dt2.order.describe())               
print("--------------------\n\n")
                    
print(dt2.family.describe())               
print("--------------------\n\n")
                    
print(dt2.genus.describe())               
print("--------------------\n\n")
                    
print(dt2.specific_epithet.describe())               
print("--------------------\n\n")
                    
print(dt2.photographer.describe())               
print("--------------------\n\n")
                    
print(dt2.photo_description.describe())               
print("--------------------\n\n")
                    
print(dt2.specimen_id.describe())               
print("--------------------\n\n")
                    
print(dt2.img_href.describe())               
print("--------------------\n\n")
                    
                    
                




