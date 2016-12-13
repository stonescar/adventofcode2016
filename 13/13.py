grid = []
for i in range(50):
	grid.append([])
	
def pr_gr():
	for i in grid:
		print "".join(i)

def find_wall(x, y):
	if str(bin((x*x+3*x+2*x*y+y+y*y)+1350)[2:]).count("1") %2 == 0:
		return " "
	else:
		return u"\u2588"
		
for i in range(len(grid)):
	for j in range(len(grid)):
		grid[i].append(find_wall(i, j))

grid[31][39] = u"\u2591"

pr_gr()