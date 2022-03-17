# scrapergsc
The code is designed to receive a keyword from a user, enter the keyword into the Google Scholar search field, iterate throughout a number of set pages, scrape all the data from the search pages and output an end note file, in the form of a txt and a csv file. The files are then interpreted by the code and split into a word bank in which a histogram is generated from.

you need to install beautifulsoup4
this can be done on conda, through cmd.exe by using : conda install -c anaconda beautifulsoup4
or through pip : pip install beautifulsoup4

also wordcloud in native windows cmd.exe
pip: pip install WordCloud
conda: conda install -c conda-forge wordcloud
