# DOTV-RM-Parser
A group of things I've made to parse Dragons Of The Void Raid Manager CSV files. All files written in node js to make it easy for web page views and shiz.


Commands used
```python executables/preprocess.py < examples/raidLootData-Example.csv > examples/raidLootData-Example-pre-processed.txt```
To generate the pre-processed file.

Then I used the following to remove any data that has no sp.
```python executables/analyseSP.py < examples/raidLootData-Example-pre-processed.txt > examples/raidLootData-Example-SP.txt```
