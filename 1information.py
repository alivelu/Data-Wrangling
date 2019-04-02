#Take the whole Shakopee.osm file for analysis
#As the city is small , If I use a small file, it's difficult to get correct information.
#If you want to really use a small file named "smallersample.osm":
# Run the program in the file "1.1samplefileextractionlocalosm.py"
# Change the k value
#Because smaller k value gives large osm files
#Bigger k value gives small osm files
#So depending on the original file size, choose a k number
# Run the file below
# Name of the file: 1samplefileextractionlocalosm.py
# smallersample.osm should be in your directory
#Note: I have used Shakopee.osm file

### Information about the Data:


T#This project wrangles the data of Shakopee, MN area.
#I have lived in Minnesota for nearly a decade. So It's like my home town.

####
#The structure of this file is as follows:
#1. Information
#2.OSM File preparation or XML file Preperation
#3. Data exploration
#4. Data auditing
#5. Data fixing (based on audit results)
#6. Data shaping, validating and exporting to .csv format (for running SQL quries)
#7. Connecting to database and running sql queries
#8. Finally Report of my findings
#9. Individual functions I have used in my file named "3myexplorationandaudit"
#10. "5Databasecreation_sqlqueries.py" runs only basic sql queries
#11. "5Databasecreation_sqlqueries.ipynb" runs more sql queries with visualizations..
#12. Shakopee_MN_US1.db extracted from python file.(basic sql queries)
#13. Shakopee_MN_US.db extracted from ipynb file.(more visualizations etc)
# Note:
# * The methods I have used to extract files, and related problems are discussed in very detail in a file named "7methodstoextractfiles". 
# * As of now for this project I have used a file named "Shakopee.osm". This file is directly downloaded from openstreetmap.org.
# * Another sample file "smallersample.osm" is extracted from "2samplefileextractionlocalosm.py", Which is located in "Finalproject" folder.
# OSM format files are working fine. So I have decided to use Shakopee.osm or smallersample.osm for my analysis.
# Individual function like cities.py, states.py etc are also in the Folder.

