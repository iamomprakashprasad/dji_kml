from constants import q_ground_kml_file
from constants import cordinate_output_file

from fastkml import kml

with open(q_ground_kml_file) as myfile:
    doc = myfile.read()
k = kml.KML()
k.from_string(doc)

outerFeature = list(k.features())
innerFeature = list(outerFeature[0].features())

placemarks = list(innerFeature[0].features())
all_cordinates = []
for p in placemarks:
    all_cordinates.append((p.geometry.x, p.geometry.y))

print("all cordinates")
print(all_cordinates)
print(len(all_cordinates))


with open(cordinate_output_file, "w+") as coord_file:
    for each_coordinate in all_cordinates:
        print(f"{each_coordinate[0]=}")
        coord_file.write(f"{each_coordinate[0]}, {each_coordinate[1]}\n")
