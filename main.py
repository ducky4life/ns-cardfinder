import nationstates
import csv

api = nationstates.Nationstates("puppet dbid finder by Ducky used by") # put your main nation name here!!

with open('puppet.csv') as csv_file:
	csv_reader = csv.reader(csv_file)
	for row in csv_reader:
		nation = api.nation(row[0])
		print(nation.dbid)