f = open('data.txt', 'r')
lines = f.read();
lines = lines.split('\n')
foutput = open('data_output.txt','w')
for elem in lines:
	line = "\"" + elem + "\"" + ","
	foutput.write(line)
foutput.close()
f.close()