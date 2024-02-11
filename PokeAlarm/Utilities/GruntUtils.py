# Standard Library Imports
import json

# 3rd Party Imports
# Local Imports
from PokeAlarm.Utils import get_path, get_type_id, Unknown


# Returns the grunt gender id
def get_grunt_gender_id(grunt_id):
    # Check if info attribute exists, if not, initialize and load data from invasions data
    if not hasattr(get_grunt_gender_id, "info"):
        get_grunt_gender_id.info = {}
        file_ = get_path("data/invasions.json")
        with open(file_, "r") as f:
            j = json.load(f)
            f.close()
        # Populate info dictionary based on data from invasions data
        for id_ in j:
            get_grunt_gender_id.info[int(id_)] = j[id_]["gender"]

    return get_grunt_gender_id.info.get(grunt_id, Unknown.TINY)


# Returns the mon types used by a grunt
def get_grunt_mon_type_id(grunt_id):
    # Check if info attribute exists, if not, initialize and load data from invasions data
    if not hasattr(get_grunt_mon_type_id, "info"):
        get_grunt_mon_type_id.info = {}
        file_ = get_path("data/invasions.json")
        with open(file_, "r") as f:
            j = json.load(f)
            f.close()
        # Populate info dictionary with mon types based on data from invasions data
        for id_ in j:
            get_grunt_mon_type_id.info[int(id_)] = get_type_id(j[id_].get("type"))

    return get_grunt_mon_type_id.info.get(grunt_id, Unknown.TINY)


# Returns the grunt name
def get_grunt_name(grunt_id):
    # Check if info attribute exists, if not, initialize and load data from invasions data
    if not hasattr(get_grunt_name, "info"):
        get_grunt_name.info = {}
        file_ = get_path("data/invasions.json")
        with open(file_, "r") as f:
            j = json.load(f)
            f.close()
        # Populate info dictionary with grunt names based on data from invasions data
        for id_ in j:
            if "grunt" in j[id_] and j[id_]["grunt"] != "Grunt":
                get_grunt_name.info[int(id_)] = j[id_]["grunt"]
            else:
                get_grunt_name.info[int(id_)] = j[id_]["type"]

    return get_grunt_name.info.get(grunt_id, Unknown.REGULAR)


# Returns the possible mon id rewards
def get_grunt_reward_mon_id(grunt_id):
    # Check if info attribute exists, if not, initialize and load data from invasions data
    if not hasattr(get_grunt_reward_mon_id, "info"):
        get_grunt_reward_mon_id.info = {}
        file_ = get_path("data/invasions.json")
        with open(file_, "r") as f:
            j = json.load(f)
            f.close()
        # Populate info dictionary with mon id rewards based on data from invasions data
        for id_ in j:
            get_grunt_reward_mon_id.info[int(id_)] = []
            if "encounters" in j[id_]:
                if j[id_]["firstReward"]:
                    for item in j[id_]["encounters"]["first"]:
                        if item['id'] not in get_grunt_reward_mon_id.info[int(id_)]:
                            get_grunt_reward_mon_id.info[int(id_)].append(item['id'])
                if j[id_]["secondReward"]:
                    for item in j[id_]["encounters"]["second"]:
                        if item['id'] not in get_grunt_reward_mon_id.info[int(id_)]:
                            get_grunt_reward_mon_id.info[int(id_)].append(item['id'])
                if j[id_]["thirdReward"]:
                    for item in j[id_]["encounters"]["third"]:
                        if item['id'] not in get_grunt_reward_mon_id.info[int(id_)]:
                            get_grunt_reward_mon_id.info[int(id_)].append(item['id'])

    return get_grunt_reward_mon_id.info.get(grunt_id, [])


# Returns the possible mon id for each battle
def get_grunt_mon_battle(grunt_id, battle_num):
    # Check if info attribute exists, if not, initialize and load data from invasions data
    if not hasattr(get_grunt_mon_battle, "info"):
        get_grunt_mon_battle.info = {}
        file_ = get_path("data/invasions.json")
        with open(file_, "r") as f:
            j = json.load(f)
            f.close()
        # Populate info dictionary with mon id for each battle based on data from invasions data
        for id_ in j:
            if "encounters" in j[id_]:
                get_grunt_mon_battle.info[f"{id_}_1"] = [
                    item['id'] for item in j[id_]["encounters"]["first"]]
                get_grunt_mon_battle.info[f"{id_}_2"] = [
                    item['id'] for item in j[id_]["encounters"]["second"]]
                get_grunt_mon_battle.info[f"{id_}_3"] = [
                    item['id'] for item in j[id_]["encounters"]["third"]]

    return get_grunt_mon_battle.info.get(f"{grunt_id}_{battle_num}", [])
