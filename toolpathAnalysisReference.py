import math
#str = "X100";
#temp = str.split("X")
#str = temp[1];
#print(int(str)+1);
int count = 0, distance, minDistance; #store the size of the tool path
float xNew, yNew, xPrev, yPrev;
fyle = open("C:/Users/howertonr/AppData/Local/Programs/Python/Python36-32/Cornerstone_test_panel_single_quadrant.900");
for lyne in fyle:
	if lyne[0] == ' ':
		count++; #find the size of the tool path
for lyne in fyle :
	lyne = lyne.rstrip(); #remove unnecessary trailing characters
	if lyne[0] == ' ':
		tempArray = lyne.split(' '); #split the coordinates and store them
		if len(tempArray) == 3:
			xPrev = xNew;
			xNew = float(tempArray[1][1:]);
			yPrev = yNew;
			yNew = float(tempArray[2][1:]);
		elif tempArray[1][0] == 'X':
			xPrev = xNew;
			xNew = float(tempArray[1][1:]);
			
		elif tempArray[1][0] == 'Y':
			yPrev = yNew;
			yNew = float(tempArray[1][1:]);
	distance = math.sqrt( ((abs(xNew - xPrev)) ** 2) + ((abs(yNew - yPrev)) ** 2) );
	if distance <= minDistance:
		minDistance = distance;
		#lyne = (tempArray[1] + tempArray[2]);
		#print(lyne);
	#print("length of lyne: ", len(lyne));
print(minDistance);
fyle.close();