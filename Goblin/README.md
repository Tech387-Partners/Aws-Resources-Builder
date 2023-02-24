# Goblin

Many developers who use AWS tools such as AppSync and GraphQL are familiar with their shortcomings. When creating a complex project or application, you often need to customize</br> resources, which adds extra work and complexity as you move through different development environments. This process often involves writing extensive code or configuration that</br> repeats across multiple stages or versions of the project.</br></br>

It has been shown that isolating and customizing resources is the best practice and can be used in various ways. This is where Goblin comes in as a helpful tool for generating the</br> necessary resources from the GraphQL schema, through the CustomResources.json configuration, to the VTL functions.</br></br>

The first version of this tool had the capability to generate GraphQL with all elements, models (types) with defined default and customized resources, required inputs, enums, as</br> well as the complete structure of mutations, subscriptions, and queries. After creating the schema.graphql, it generates a CustomResources.json file with a resolver for each</br> specified mutation or query, as well as a basic function. All VTL resolver functions would also be created with a basic code structure.</br>

Initially, it was necessary to create a JSON configuration based on which the tool worked. However, due to the large amount of data, it was not practical to use configuration</br> structures such as JSON, YAML, or TOML. A decision was made to create a separate data structure with a unique syntax that is very practical and simple, based on which the basic JSON</br> structure would be created. The current version also has the ability to create specific resources based on GSI settings.</br></br>

The short-term vision is for the tool to become a platform that can create and maintain projects, while for a later version it can be improved as a controller for project tracking</br> in all environments, as well as automating the publishing of new versions.</br>

The reason for developing Goblin is to provide a solution for the challenges developers face when customizing AWS AppSync and GraphQL resources for their projects, by providing an</br> efficient and easy-to-use tool for generating the necessary resources.</br>
