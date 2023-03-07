import os, json

from datetime import datetime

class GeneratorConfig:

    def __init__(self, location):
        self.__currentPath = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
        self.__baseLocation = os.path.split(location)[0]
        self.__location = location
        self.__resultsPath = f"{self.__baseLocation}/Results"
        self.__sourcesPath = f"{self.__baseLocation}/Sources"
        self.mapSrcPath = f"{self.__sourcesPath}/schema.gob"

        os.makedirs(os.path.join(self.__baseLocation, "Results"), exist_ok=True)
        os.makedirs(os.path.join(self.__baseLocation, "Sources"), exist_ok=True)

        os.makedirs(os.path.join(self.__resultsPath, self.__currentPath), exist_ok=True)

        #{BASE}/Results/{CURRENT}/
        os.makedirs(os.path.join(self.__resultsPath, self.__currentPath, "resolvers"), exist_ok=True)
        os.makedirs(os.path.join(self.__resultsPath, self.__currentPath, "graphql"), exist_ok=True)
        os.makedirs(os.path.join(self.__resultsPath, self.__currentPath, "resources"), exist_ok=True)


        print(self.__baseLocation)
        print(self.__location)
        print(self.__resultsPath)
        print(self.__sourcesPath)
        print(self.__currentPath)


    def getResolversPath(self):
        return f"{self.__resultsPath}/{self.__currentPath}/resolvers"
    
    def getCustomResourcesPath(self):
        return f"{self.__resultsPath}/{self.__currentPath}/resources"


    def saveJsonScheme(self, ctx):
        """
        """
        with open(os.path.join(self.__resultsPath, self.__currentPath, "graphql", "schema.json"), "w") as outfile:
            outfile.write(json.dumps(ctx, indent=4, sort_keys=True)) 

    def saveGraphqlScheme(self, ctx):
        """"""
        with open(os.path.join(self.__resultsPath, self.__currentPath, "graphql", "schema.graphql"), "w") as outfile:
            outfile.write(ctx) 