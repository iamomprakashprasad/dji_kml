"""Parse points coordinates from kml file."""
from constants import kml_file


def get_coodinates_from_kml(kml_file_path: str, ):
    with open(kml_file, "r") as kml_file_ptr:
        coordinates_file = kml_file_ptr.read()

    if coordinates_file.count("<Placemark") and coordinates_file.count("<Placemark") > 1:
        raise ValueError("More than one polygon or path found in kml file.")

    if not coordinates_file.count("<Placemark"):
        raise ValueError("No path or polygon found in provided kml file.")

    coordinates = ''
    coordinates_in_next_line = False
    with open(kml_file, "r") as kml_file_ptr:
        while x := kml_file_ptr.readline():
            x = x.replace("\t", '').replace("\n", "").strip()
            if coordinates_in_next_line:
                coordinates = x
                break
            if "<coordinate" in x:
                coordinates_in_next_line = True

    coordinates = coordinates.split(" ")
    return coordinates


def format_and_validate_coordinates(coordinates, format_in_dict: bool = True) -> dict:

    """If format_in_dict is False it will return coodinates in tuple
        response = {
            false_coordinates: list,
            formatted_coordinates: dict or tuple
        }
    """

    formatted_coordinates = []
    false_coordinates = []
    for each_coordinate in coordinates:
        temp_coordinate = each_coordinate.split(',')
        if format_in_dict:
            if len(temp_coordinate) < 2 or len(temp_coordinate) > 3:
                false_coordinates.append(temp_coordinate)
                continue
            elif len(temp_coordinate) == 3 and not isinstance(temp_coordinate[2], type(None)):
                formatted_coordinates.append(
                    {
                        "latitude": round(float(temp_coordinate[0]), 5),
                        "longitude": round(float(temp_coordinate[1]), 5),
                        "altitude": round(float(temp_coordinate[2]), 5)
                    }
                )
            else:
                formatted_coordinates.append(
                    {
                        "latitude": round(float(temp_coordinate[0]), 5),
                        "longitude": round(float(temp_coordinate[1]), 5)
                    }
                )
        else:
            formatted_coordinates.append((
                round(float(temp_coordinate[0]), 5),
                round(float(temp_coordinate[1]), 5)
            ))

