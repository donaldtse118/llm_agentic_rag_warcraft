character_details = {
    "paladin":{
        "strength":80,
        "agility":10,
    }
}

def lookup_stats_for_character(character):
    return character_details.get(character)