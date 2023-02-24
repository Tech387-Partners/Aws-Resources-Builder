import os

from GeneratorConfig import GeneratorConfig

import MapLoader
import Graphql
import VtlGenerator
import CustomResourcesGenerator


config = GeneratorConfig(os.path.abspath(os.path.dirname(__file__)))

## < json context >
ctx = MapLoader.loadMap(config.mapSrcPath)
## < save json context >
config.saveJsonScheme(ctx)

## graphql as string
graphql = Graphql.getGraphql(ctx)
## save scheme.graphql
config.saveGraphqlScheme(graphql)

## resolvers generator
VtlGenerator.generate(config.getResolversPath(), ctx['models'])

## CustomResources.json generator
CustomResourcesGenerator.generate(config.getCustomResourcesPath(), ctx['models'])