import json

f = open('data_nationalities.txt', 'r')
lines = f.read();
lines = lines.split('\n')
foutput = open('data_nationalities_output.txt','w')
json_file = open('..//templates//data//data_nationalities.json','w')
json_list = []
for elem in lines:
	elem = elem.split('\t');
	line = "\"" + elem[0] + "\"" + ","
	json_list.append(elem[0])
	foutput.write(line)
foutput.close()
json.dump(json_list,json_file)
json_file.close()
f.close()