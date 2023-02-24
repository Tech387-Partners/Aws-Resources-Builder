from config import CRUDInputType

def getModel(template):
    """
    @model(mutations: { delete: "deleteArtistAlbums", update: "updateArtistAlbums" }, queries: { list: "listUsers" })
    """
    model = """
type @modelName@ @model@model_params@ {
  id: ID!""".replace("@modelName@",template['name'])

    for arg in template['args']:
        isRequired = "!" if arg['isRequired'] else ""

        a = f"{arg['name']}: {arg['data_type']}{isRequired}"
        # index content
        if 'index' in arg:
            index = f" @index(name: \"{arg['index']['name']}\", sortKeyFields: @sort_key_fields@, queryField: @query_field@)"
            if 'sortKeyFields' in arg['index']:
                flds = "["
                for f in arg['index']['sortKeyFields']:
                    flds += f"\"{f}\""
                flds += "]"
                index = index.replace("@sort_key_fields@",f"{flds}")
            else:
                index = index.replace(", sortKeyFields: @sort_key_fields@","")
            if 'queryField' in arg['index']:
                index = index.replace("@query_field@",f"\"{arg['index']['queryField']}\"")
            else:
                index = index.replace(", queryField: @query_field@","")
            a += index

        # hasMany content
        if 'hasMany' in arg:
            flds = "["
            for f in arg['hasMany']['fields']:
                flds += f"\"{f}\""
            flds += "]"
            a +=  f" @hasMany(indexName: \"{arg['hasMany']['indexName']}\", fields: {flds})"

        if "belongsTo" in arg:
            flds = "["
            for f in arg['belongsTo']['fields']:
                flds += f"\"{f}\""
            flds += "]"
            a += f" @belongsTo(fields: {flds})"


        model += "\n  " + a

    def modelParams():
        params = "(mutations: @mutations@, queries: @queries@)"
        mtt = "{ create: @mtt_create@, update: @mtt_update@, delete: @mtt_delete@ }"
        quu = "{ get: @quu_get@, list: @quu_list@ }"

        if template["CREATE"] == "DEFAULT":
            """"""
            mtt = mtt.replace("@mtt_create@",f"\"create{template['name']}\"")
        else:
            """"""
            mtt = mtt.replace(" create: @mtt_create@,","")
        if template["UPDATE"] == "DEFAULT":
            """"""
            mtt = mtt.replace("@mtt_update@",f"\"update{template['name']}\"")
        else:
            """"""
            mtt = mtt.replace(" update: @mtt_update@,","")
        if template["DELETE"] == "DEFAULT":
            """"""
            mtt = mtt.replace("@mtt_delete@", f"\"delete{template['name']}\"")
        else:
            """"""
            mtt = mtt.replace("delete: @mtt_delete@","")
        if template["GET"] == "DEFAULT":
            """"""
            quu = quu.replace("@quu_get@",f"\"get{template['name']}\"")
        else:
            """"""
            quu = quu.replace(" get: @quu_get@,","")
        if template["LIST"] == "DEFAULT":
            """"""
            n = template['name']
            if n[-1] != 's':
                n += "s"

            quu = quu.replace("@quu_list@",f"\"list{n}\"")
        else:
            """"""
            quu = quu.replace("list: @quu_list@","")



        if 'create:' in mtt or 'update:' in mtt or 'delete:' in mtt:
            params = params.replace("@mutations@",mtt)

        else:
            params = params.replace("mutations: @mutations@","")

        if 'get:' in quu or 'list:' in quu:
            params = params.replace("@queries@",quu)
        else:
            params = params.replace(", queries: @queries@","")

        if params == "()":
            params = ""
        return params



    model = model.replace("@model_params@", modelParams())
    
    return model + "\n}"








def getInput(modelName, args, crudType=CRUDInputType.DELETE):

    input = """
input @type@@modelName@Input {
  @id@"""

    id = "id: ID" if crudType == CRUDInputType.UPDATE else "id: ID!"
    input = input.replace("@type@",crudType.getTitle()).replace("@modelName@",modelName).replace("@id@",id)

    if crudType == CRUDInputType.DELETE:
        input += "\n}"
        return input

    for arg in args:
        isRequired = arg['create_isRequired'] if crudType == CRUDInputType.CREATE else arg['update_isRequired']
        if isRequired is not None:
            required = "!" if isRequired else ""
            row = f"""\n  {arg["name"]}: {arg['data_type']}{required}"""
            input += row
    input += "\n}"

    return input



        







# ===================================
def generateEnums(enumsTemplates):
    return ""


def generateGraphql(modelTemplates):
    """
        Generisace i vratiti graphql u stringu
    """

    models = """"""

    input = """"""

    queries = """"""

    mutations = """"""

    subscriptions = """"""

    for model in modelTemplates:

        models += "\n" + getModel(model)

        if model["CREATE"] == "CUSTOM" or model["UPDATE"] == "CUSTOM" or model["DELETE"] == "CUSTOM":
            input += f"\n#===================== [ START ] Input {model['name']} ===================== ]"
        input += "" if model["CREATE"] != "CUSTOM" else getInput(model['name'], model['args'], CRUDInputType.CREATE) + "\n"
        input += "" if model["UPDATE"] != "CUSTOM" else getInput(model['name'], model['args'], CRUDInputType.UPDATE) + "\n"
        input += "" if model["DELETE"] != "CUSTOM" else getInput(model['name'], model['args'], CRUDInputType.DELETE) + "\n"
        if model["CREATE"] == "CUSTOM" or model["UPDATE"] == "CUSTOM" or model["DELETE"] == "CUSTOM":
            input += f"#====================== [ END ] Input {model['name']} ====================== ]\n"

        if model["CREATE"] == "CUSTOM":
            mutations += f"\n  create{model['name']}(input: Create{model['name']}Input!): {model['name']} @aws_api_key @aws_cognito_user_pools"
            subscriptions += f"\n  onCreate{model['name']}: {model['name']} @aws_subscribe(mutations: [\"create{model['name']}\"]) @aws_api_key @aws_cognito_user_pools"
            # Resolver REQ
            # Resolver RES
        else:
            """
            """

        if model["UPDATE"] == "CUSTOM":
            mutations += f"\n  update{model['name']}(input: Update{model['name']}Input!): {model['name']} @aws_api_key @aws_cognito_user_pools"
            subscriptions += f"\n  onUpdate{model['name']}: {model['name']} @aws_subscribe(mutations: [\"update{model['name']}\"]) @aws_api_key @aws_cognito_user_pools"
            # Resolver REQ
            # Resolver RES

        if model["DELETE"] == "CUSTOM":
            mutations += f"\n  delete{model['name']}(input: Delete{model['name']}Input!): {model['name']} @aws_api_key @aws_cognito_user_pools"
            subscriptions += f"\n  onDelete{model['name']}: {model['name']} @aws_subscribe(mutations: [\"delete{model['name']}\"]) @aws_api_key @aws_cognito_user_pools"
            # Resolver REQ
            # Resolver RES
        else:
            """
            """

        if model["GET"] == "CUSTOM":
            """"""
            queries += f"\n  get{model['name']}(id: ID!): {model['name']} @aws_api_key @aws_cognito_user_pools"
            # Resolver REQ
            # Resolver RES
        else:
            """"""

        if model["LIST"] == "CUSTOM":
            """"""
            queries += f"\n  listSongs(filter: Model{model['name']}FilterInput, limit: Int, nextToken: String): Model{model['name']}Connection @aws_api_key @aws_cognito_user_pools"
            #### TODO TODO TODO - Generisati Model{model['name']}FilterInput i Model{model['name']}Connection inace nece raditi
            # Resolver REQ
            # Resolver RES
            print(" 🆘 🆘 🆘 Genrisanje Model{model['name']}FilterInput i Model{model['name']}Connection nije implemetirano, LIST GENERATOR NIJE POTPUN")
        else:
            """
            """

        for argument in model['args']:
            if 'index' in argument:
                if "factor" in argument['index']:
                    if "inputArgs" in argument['index']:
                        factor = argument['index']["factor"]
                        con = "("
                        for ar in argument['index']["inputArgs"]:
                            con += "," + ar if con != "(" else ar
                        con += ")"
                        queries += f"\n  get{model['name']}By{factor}{con}: {model['name']} @aws_api_key @aws_cognito_user_pools"
                        

    return """

@model@

@input@

type Mutation {@mutation@
}

type Subscription {@subscription@
}

type Query {@query@
}


""".replace("@model@",models).replace("@input@",input).replace("@mutation@",mutations).replace("@subscription@",subscriptions).replace("@query@",queries)
        

def getGraphql(ctx):
    graphql = """"""
    if 'enums' in ctx:
        graphql += generateEnums(ctx['enums'])
    if 'models' in ctx:
        graphql += generateGraphql(ctx['models'])
    return graphql
