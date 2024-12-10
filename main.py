import nationstates
import csv



api = nationstates.Nationstates("puppet dbid finder by Ducky used by") # put your main nation name here



mode = input("press enter if you would like the output to be a text file with only the IDs (use this if you're using my website), or type 'csv' for a csv file in 'nation,id' format: ")

if mode.lower() == "csv":
	print("writing to csv file")
	with open('puppet.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		output_csv = open("output.csv", "w")
		for row in csv_reader:
			nation = api.nation(row[0])
			output_csv.write(f"{row[0]},{nation.dbid}\n")
		print("output is in output.csv")

else:
	print("writing to text file")
	with open('puppet.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		output_txt = open("output.txt", "w")
		for row in csv_reader:
			nation = api.nation(row[0])
			output_txt.write(f"{nation.dbid}\n")
		print("output is in output.txt, go to https://ducky4life.pages.dev/cardfinder/ to generate the card links!")