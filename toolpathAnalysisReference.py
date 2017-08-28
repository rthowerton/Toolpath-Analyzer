#str = "X100";
#temp = str.split("X")
#str = temp[1];
#print(int(str)+1);
int count = 0; #store the size of the tool path
fyle = open("C:/Users/howertonr/AppData/Local/Programs/Python/Python36-32/Cornerstone_test_panel_single_quadrant.900");
for lyne in fyle:
	if lyne[0] == ' ':
		count++; #find the size of the tool path
for lyne in fyle :
	lyne = lyne.rstrip(); #remove unnecessary leading or trailing characters
	if lyne[0] == ' ':
		tempArray = lyne.split(' '); #split the coordinates and store them
		lyne = (tempArray[1] + tempArray[2]);
		print(lyne);
	#print("length of lyne: ", len(lyne));
fyle.close();