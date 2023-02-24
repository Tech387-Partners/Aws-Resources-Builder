from config import CategoryType
from config import ActionType

import os



def getByIndexRequest(fieldname, indexname):
    """
    :param fieldname / email
    :param indexname / UserByEmail

    :return req vtl function content
    """
    return """
$util.toJson({
  "version": "2018-05-29",
  "operation": "Query",
  "limit": 10000,
  "query": {
      "expression":"#@fieldname@ = :@fieldname@",
      "expressionNames":{
         "#@fieldname@":"@fieldname@"
      },
      "expressionValues":{
         ":@fieldname@":{
            "S":"$@fieldname@"
         }
      }
   },
  "index": "@index_name@",
  "scanIndexForward": true
})
""".replace("@index_name@",indexname).replace("@fieldname@",fieldname)





def getByIndexResponse(fieldName, saveName):
    """
    :param fieldName / getUserByEmail
    :param saveName / userByEmail

    :return res vtl function content
    """
    return f"""
#if( $ctx.error )
  $util.error($ctx.error.message, $ctx.error.type)
#end
#if( !$ctx.result.items.isEmpty() && $ctx.result.scannedCount >= 1 )
  $util.qr($ctx.stash.put("{saveName}", $ctx.result.items[0]))
  #if( $ctx.info.fieldName != "{fieldName}" )
    $util.toJson(null)
  #else
    $util.toJson($ctx.result)
  #end
#else
  #if( $ctx.result.items.isEmpty() && $ctx.result.scannedCount >= 1 )
$util.unauthorized()
  #end
  $util.toJson(null)
#end
"""





def generate(path, template):

    """
    """

    for model in template:

        if model["CREATE"] == "CUSTOM":
            """""" ## TODO: create resolver function
        if model["UPDATE"] == "CUSTOM":
            """""" ## TODO: update resolver function
        if model["DELETE"] == "CUSTOM":
            """""" ## TODO: delete resolver function
        if model["GET"] == "CUSTOM":
            """""" ## TODO: get resolver function
        if model["LIST"] == "CUSTOM":
            """""" ## TODO: list resolver function

        for arg in model['args']:
            if 'index' in arg:
                if 'factor' in arg['index']:
                    #fieldname = arg['name']
                    #indexname = arg['index']['name']
                    #reqContent = getByIndexRequest(arg['name'], arg['index']['name'])
                    #action = ActionType.GET_BY
                    fn = ActionType.GET_BY.getVtlFunctionName(model['name'], CategoryType.QUERY, arg['index']['factor']) + ".req.vtl"

                    with open(os.path.join(path, fn), "w") as outfile:
                        outfile.write(getByIndexRequest(arg['name'], arg['index']['name']))

                    #fieldName = ActionType.GET_BY.functionName(model['name'], arg['index']['factor'])
                    mName = model['name'][0].lower() + model['name'][1:]
                    #saveName = f"{mName}By{arg['index']['factor']}"
                    #resContent = getByIndexResponse(ActionType.GET_BY.functionName(model['name'], arg['index']['factor']), f"{mName}By{arg['index']['factor']}")
                    fn = ActionType.GET_BY.getVtlFunctionName(model['name'], CategoryType.QUERY, arg['index']['factor']) + ".res.vtl"

                    with open(os.path.join(path, fn), "w") as outfile:
                        outfile.write(getByIndexResponse(ActionType.GET_BY.functionName(model['name'], arg['index']['factor']), f"{mName}By{arg['index']['factor']}"))


    """
{
                    "name": "sourceAppleID",                        # naziv argumenta
                    "data_type": GraphqlDataType.String,            # data type
                    "isRequired": True,                             # is required attribute in Model
                    "create_isRequired": True,                      # True = is required attribute in create input, False = no required attribute in create input, None = Remove from create input
                    "update_isRequired": False,                     # True = is required attribute in update input, False = no required attribute in update input, None = Remove from update input
                    "index":{                                       # GSI config
                        "name": "SongBySourceAppleID"               # GSI Name
                        ,"factor": "SourceAppleID"                  # Index Factor Name. Ako postoji ovaj faktor, automatski se kreira Query.getSongBy{factor}
                        # ,"sortKeyFields":["createdAt"]            # 
                        # ,"queryField":"listSongsBySourceAppleID"  # 
                    }
                }
    """
