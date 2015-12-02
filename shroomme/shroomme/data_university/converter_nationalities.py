f = open('data_nationalities.txt', 'r')
lines = f.read();
lines = lines.split('\n')
foutput = open('data_nationalities_output.txt','w')
for elem in lines:
	elem = elem.split('\t');
	line = "\"" + elem[0] + "\"" + ","
	foutput.write(line)
foutput.close()
f.close()