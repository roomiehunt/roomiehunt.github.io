import json

f = open('data.txt', 'r')
lines = f.read();
lines = lines.split('\n')
json_file = open('..//templates//data//data_universities.json','w')
foutput = open('data_output.txt','w')
json.dump(lines,json_file)
for elem in lines:
	line = "\"" + elem + "\"" + ","
	foutput.write(line)
foutput.close()
json_file.close()
f.close()