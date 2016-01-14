import fromheretothere as fh

start = "40.748416,-73.9856605" # empire state building
stop = "37.8113798,-122.4773046" # golden gate bridge


elv = fh.get_elevation_array(start, stop, 500)

points = []
i = 0
for e in elv:
    points.append("v {} {} 0".format(i, e))
    i += 1

output = points[:]

for i in range(len(points)):
    output.append("f {} {}".format(i, i+1))


print "\n".join(output)
