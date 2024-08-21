from constants import q_ground_kml_file
from constants import cordinate_output_file


from fastkml import geometry
from fastkml import kml

# kml_filename = "foo.kml"
kml_file = '/home/sachin/flight_planners/survey-flight-planner/top_view.kml'

with open(kml_file) as kml_file:
    doc = kml_file.read().encode('utf-8')
    k = kml.KML()
    k.from_string(doc)
    print(f"{k=}")
    all_coordinates = []
    for feature0 in k.features():
        print(f"{feature0=}")
        print("{}, {}".format(feature0.name, feature0.description))
        for feature1 in feature0.features():
            # print(type(feature1.geometry))
            if isinstance(feature1.geometry, geometry.Point):
                point = feature1.geometry
                for coord in point.coords:
                    # these are long, lat tuples
                    all_coordinates.append(coord)
# Example usage

with open("all_coordinates.txt", "w") as coord_file:
    for each_coord in all_coordinates:
        coord_file.write(f'{each_coord[0]}, {each_coord[1]}, {each_coord[2]}\n')
