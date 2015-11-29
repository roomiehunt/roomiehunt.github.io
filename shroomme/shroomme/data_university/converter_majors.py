f = open('data_majors.txt', 'r')
lines = f.read();
lines = lines.split('\n')
foutput = open('data_majors_output.txt','w')
for elem in lines:
	if len(elem) == 1 or len(elem) == 0:
		continue
	paren = elem.find('(')
	if paren == -1:	
		line = "\"" + elem + "\"" + ","
		foutput.write(line)
	else:
		line = "\"" + elem[0:(paren-1)] + "\"" + ","
		foutput.write(line)



foutput.close()
f.close()