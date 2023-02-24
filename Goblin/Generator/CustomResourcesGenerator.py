from config import CategoryType
from config import ActionType
from config import SourceType

import os, json

def generateSourceItem(sourceContent, modelName, categoryType=CategoryType.MUTATION, actionType=ActionType.CREATE, sourceType=SourceType.PIPELINE, indexFactor=""):
    """
    """

    indexFactor = indexFactor if actionType == ActionType.GET_BY else ""
    ## FunctionGetSongBy\s\Email

    """
    FunctionCreateSong -> getBigFunctionName(self, modelName, indexFactor="")
    createSong -> functionName(self, modelName, indexFactor="")
    Mutation_createSong_Function -> getCloudFunctionName(self, modelName, categoryType, indexFactor="")
    Mutation.createSong -> getVtlFunctionName(self, modelName, categoryType, indexFactor="")
    PipelineCreateSong -> getPipelineName(self, modelName, indexFactor="")
    """


    functionName =  actionType.getBigFunctionName(modelName, indexFactor) 
    sourceContent[functionName] = {
        "Type": "AWS::AppSync::FunctionConfiguration",
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "Name": actionType.getCloudFunctionName(modelName, categoryType, indexFactor),
            "DataSourceName": f"{modelName}Table",
            "FunctionVersion": "2018-05-29",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/" + f"{actionType.getVtlFunctionName(modelName, categoryType, indexFactor)}.req.vtl",
                    {
                        "S3DeploymentBucket": {
                            "Ref": "S3DeploymentBucket"
                        },
                        "S3DeploymentRootKey": {
                            "Ref": "S3DeploymentRootKey"
                        }
                    } 
                ]
            },
            "ResponseMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/" + f"{actionType.getVtlFunctionName(modelName, categoryType, indexFactor)}.res.vtl",
                    {
                    "S3DeploymentBucket": {
                        "Ref": "S3DeploymentBucket"
                    },
                    "S3DeploymentRootKey": {
                        "Ref": "S3DeploymentRootKey"
                    }
                    }
                ]
            }
        }
    }
    if sourceType == SourceType.PIPELINE:
        sourceContent[actionType.getPipelineName(modelName, indexFactor)] = {
            "Type": "AWS::AppSync::Resolver",
            "Properties": {
                "ApiId": {
                    "Ref": "AppSyncApiId"
                },
                "Kind": "PIPELINE",
                "PipelineConfig": {
                    "Functions": [
                        {
                            "Fn::GetAtt": [
                                f"{functionName}",
                                "FunctionId"
                            ]
                        }
                    ]
                },
                "TypeName": f"{categoryType.value.capitalize()}",
                "FieldName": actionType.functionName(modelName, indexFactor),
                "RequestMappingTemplate": "{}",
                "ResponseMappingTemplate": "$util.toJson($ctx.result)"
            },
            "DependsOn": [
                f"{functionName}"
            ]
        }
    return sourceContent


def generate(path, template):
    """
    """

    sourceContent = {}

    for model in template:
        if model["CREATE"] == "CUSTOM":
            sourceContent = generateSourceItem(sourceContent, model["name"], categoryType=CategoryType.MUTATION, actionType=ActionType.CREATE, sourceType=SourceType.PIPELINE)
        if model["UPDATE"] == "CUSTOM":
            sourceContent = generateSourceItem(sourceContent, model["name"], categoryType=CategoryType.MUTATION, actionType=ActionType.UPDATE, sourceType=SourceType.PIPELINE)
        if model["DELETE"] == "CUSTOM":
            sourceContent = generateSourceItem(sourceContent, model["name"], categoryType=CategoryType.MUTATION, actionType=ActionType.DELETE, sourceType=SourceType.PIPELINE)
        if model["GET"] == "CUSTOM":
            sourceContent = generateSourceItem(sourceContent, model["name"], categoryType=CategoryType.QUERY, actionType=ActionType.GET, sourceType=SourceType.PIPELINE)
        if model["LIST"] == "CUSTOM":
            sourceContent = generateSourceItem(sourceContent, model["name"], categoryType=CategoryType.QUERY, actionType=ActionType.LIST, sourceType=SourceType.PIPELINE)

        for arg in model['args']:
            if 'index' in arg:
                if 'factor' in arg['index']:
                    sourceContent = generateSourceItem(sourceContent, model["name"], categoryType=CategoryType.QUERY, actionType=ActionType.GET_BY, sourceType=SourceType.PIPELINE, indexFactor=arg['index']['factor'])

    with open(os.path.join(path, "CustomResources.json"), "w") as outfile:
        outfile.write(json.dumps(sourceContent, indent=4, sort_keys=True))