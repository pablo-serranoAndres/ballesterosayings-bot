from typing import List
from db.repository import handle_db
from models.saying import Saying


def count_sayings():
    count_sayings_DTO = handle_db("count_sayings")
    rows = count_sayings_DTO.fetchone()

    return rows[0] if rows else 0

def format_sayings(sayings_DTO):
    sayings_formatted: List[Saying] = []

    for saying_DTO in sayings_DTO: 
        sayings_formatted.append(
            Saying(saying_DTO[0], saying_DTO[1], saying_DTO[2], saying_DTO[3]))
    
    return sayings_formatted

def get_all_sayings(offset = 0, limit = 10):
    sayings_DTO = handle_db("select_all_sayings", limit=limit, offset=offset)
    
    return format_sayings(sayings_DTO)

def insert_new_saying(saying: Saying, user_id: int):
    handle_db(action="insert_new_saying",saying=saying, user_id=user_id)

def get_saying_by_id(saying_id:int, used_id):
    saying_DTO = handle_db("select_by_id", saying_id=saying_id)

    if (saying_DTO) :
        saying_selected_to_eliminate = Saying (
            id= saying_DTO[0],
            title= saying_DTO[1],
            description= saying_DTO[2],
            author= saying_DTO[3],
            )
        return saying_selected_to_eliminate
    
def delete_saying_by_id (user_id, saying_id): 
    handle_db(action="delete_saying",saying_id=saying_id)