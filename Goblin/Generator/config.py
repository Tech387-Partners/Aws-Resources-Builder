from enum import Enum

class CategoryType(Enum):
    MUTATION = "MUTATION"
    QUERY = "QUERY"

class ActionType(Enum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    LIST = "LIST"
    GET = "GET"
    GET_BY = "GET_BY"

    def getBigFunctionName(self, modelName, indexFactor=""):
        """
        Examples:
        FunctionCreateSong
        FunctionGetSong
        FunctionGetSongByFactor
        """
        if self == ActionType.LIST:
            if modelName[-1] != 's':
                modelName += "s"
        if self == ActionType.GET_BY:
            return f"FunctionGet{modelName}By{indexFactor}"
        return f"Function{self.value.capitalize()}{modelName}"

    def functionName(self, modelName, indexFactor=""):
        """
        Examples:
            createSong
            getSong
            listSongs
            getSongByFactor
        """
        if self == ActionType.LIST:
            if modelName[-1] != 's':
                modelName += "s"
        if self == ActionType.GET_BY:
            return f"get{modelName}By{indexFactor}"
        return f"{self.value.lower()}{modelName}"

    def getCloudFunctionName(self, modelName, categoryType, indexFactor=""):
        """
        Examples:
        Mutation_createSong_Function
        Query_listSongs_Function
        Query_getSong_Function
        Query_getSongByFactor_Function
        """
        fn = self.getVtlFunctionName(modelName=modelName, categoryType=categoryType, indexFactor=indexFactor).replace(".","_")
        return f"{fn}_Function"

    def getVtlFunctionName(self, modelName, categoryType, indexFactor=""):
        """
        Examples:
        Mutation.createSong
        Query.listSongs
        Query.getSong
        Query.getSongByFactor
        """
        return f"{categoryType.value.capitalize()}.{self.functionName(modelName, indexFactor=indexFactor)}"

    def getPipelineName(self, modelName, indexFactor=""):
        """
        Examples:
        PipelineCreateSong
        PipelineListSongs
        PipelineGetSong
        PipelineGetSongByFactor
        """
        if self == ActionType.LIST:
            if modelName[-1] != 's':
                modelName += "s"
        if self == ActionType.GET_BY:
            return f"PipelineGet{modelName}By{indexFactor}"
        return f"Pipeline{self.value.capitalize()}{modelName}"

    


class SourceType(Enum):
    PIPELINE = "PIPELINE"
    FUNCTION = "FUNCTION"

class GraphqlDataType(Enum):
    String = "String"
    ID = "ID"
    Int = "Int"
    Boolean = "Boolean"
    AWSDateTime = "AWSDateTime"
    Float = "Float"
class CreateDirective(Enum):
    DEFAULT = "DEFAULT"
    CUSTOM = "CUSTOM"

class CRUDInputType(Enum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"

    def getTitle(self):
        if self == CRUDInputType.CREATE:
            return "Create"
        if self == CRUDInputType.UPDATE:
            return "Update"
        if self == CRUDInputType.DELETE:
            return "Delete"