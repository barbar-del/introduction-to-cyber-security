import Diver_Club

def get_all_divers_names_and_id(club):
  #  Return a list of names and IDs of all divers in the club.
    return [(diver.name, diver.id) for diver in club.divers]

def get_all_instructors_names_and_id(club):
  #  Return a list of names and IDs of all instructors in the club.
    return [(instructor.name, instructor.id) for instructor in club.instructors]

