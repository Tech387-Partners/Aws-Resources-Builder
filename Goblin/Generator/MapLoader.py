import json

def loadMap(path):

    """
    Ucitava sadrzaj iz kakoste datoteke, te kreira i vraca json.
    """

    content = {
        "models":[],
        "enums":[]
    }
    with open(path, "r") as f:
        lines = f.readlines()
        item = None
        for line in lines:
            line = line.replace("    "," ").replace("   "," ").replace("  "," ")

            ## Save and RESET ITEM
            if '[end_model]' in line:
                content["models"].append(item)
                item = None
            if '[end_enum]' in line:
                content["enums"].append(item)
                item = None

            ## BUILD ITEM
            if item is not None:
                elements = line.split(" ")
                if item['type'] == "model":
                    arg = {
                        "name": elements[0],
                        "data_type": elements[1],
                        "isRequired": True if elements[2] == "m!" else False,
                        "create_isRequired": True if elements[3] == "ci!" else False if elements[3] == "ci?" else None,
                        "update_isRequired": True if "ui!" in elements[4] else False if "ui?" in elements[4] else None
                    }

                    if len(elements) > 5:
                        for key in ["index", "hasMany", "belongsTo"]:
                            if key in elements[5]:
                                try:
                                    j = json.loads(elements[5])
                                    arg[key] = j[key]
                                except Exception as e:
                                    """"""

                    item["args"].append(arg)

                if item['type'] == "enum":
                    item["cases"].append(line.replace("\n",""))

            ## INIT ITEM
            if '[start_enum]' in line:
                elements = line.split(" ")
                item = {
                    "type": "enum",
                    "name": elements[1].replace("\n",""),
                    "cases":[]
                }

            if '[start_model]' in line:
                elements = line.split(" ")
                item = {
                    "type": "model",
                    "name": elements[1],
                    "auth": {},
                    "credentials":{},

                    "CREATE": "CUSTOM" if elements[2] == "C+" else "DEFAULT",
                    "UPDATE": "CUSTOM" if elements[3] == "U+" else "DEFAULT",
                    "DELETE": "CUSTOM" if elements[4] == "D+" else "DEFAULT",
                    "GET":    "CUSTOM" if elements[5] == "G+" else "DEFAULT",
                    "LIST":   "CUSTOM" if "L+" in elements[6] else "DEFAULT",

                    "args":[]
                }
    return content