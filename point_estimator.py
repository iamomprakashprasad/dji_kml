import geopy.distance
from constants import cordinate_output_file, trigger_distance, final_coordinates
import geopy
import numpy
import math

initial_coordinates = []
with open(cordinate_output_file, "r") as f:
    for each_line in f.readlines():
        initial_coordinates.append(tuple(map(float, each_line[:-1].split(", "))))

print(f"{initial_coordinates=}")

# remove take off point from list
take_off_coordinate = initial_coordinates.pop(0)
print(f"{take_off_coordinate=}")


def convert_points_to_float(points):
    final_points = []
    for each_point in points:
        # print(f"{each_point=}")
        final_points.append((round(float(each_point[0]), 6), round(float(each_point[1]), 6)))
    # print((final_points))
    return final_points


def get_extra_points(initial_coodinate, final_coodinate) -> list:
    print(f"{initial_coodinate=}, {final_coodinate=}")
    distance = geopy.distance.geodesic(initial_coodinate, final_coodinate).meters
    print(f"{distance=}")
    point_required = distance/trigger_distance
    point_required = math.ceil(point_required)
    print(f"{point_required=}")
    if point_required:
        points = list(zip(numpy.linspace(initial_coodinate[0], final_coodinate[0], point_required+1),
                          numpy.linspace(initial_coodinate[1], final_coodinate[1], point_required+1)))
        points = convert_points_to_float(points=points)
        print(len(points))
        return points
    return [initial_coodinate, final_coodinate]

for i in range(len(initial_coordinates)-1):
    extra_points = get_extra_points(initial_coodinate=initial_coordinates[i],
                                    final_coodinate=initial_coordinates[i+1])
    with open(final_coordinates, "a") as f:
        for i in extra_points:
            f.write(f"{i[0]}, {i[1]}\n")