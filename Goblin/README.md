# Goblin

If you've ever worked with AWS tools and services as a developer, you've probably quickly become familiar with their advantages and disadvantages. If your project is complex, you'll likely need to customize most of the resources to fit your needs. Isolating and customizing resources has proven to be the best practice, but it requires additional coding or other structures where code or configuration is usually repeated.

Goblin was created as a prototype based on the idea of providing a generator for valid content of the necessary resources in order to significantly shorten time, ensure quality and secure content, and ensure its maintenance.

## How Goblin Works

To execute its task, Goblin requires input data on which to work. The initial idea was to use JSON, YAML, or TOML, but because of the need to simplify voluminous information, it was decided to create a completely new standard and syntax for writing the Goblin map. This is the `scheme.gob` file, created on the basis of the `scheme.graphql` file but with much more information formatted according to the protocol.

When started, Goblin loads the `scheme.gob` file and uses the read data to create a JSON object with detailed information on which to continue creating all targeted resources. The items that will be created include:

- GraphQL (schema.graphql) with defined models, inputs, mutations, subscriptions, and queries
- VTL resolvers VTL request & response functions
- CustomResources.json file with configuration that links the created resources.

The created content will be located in the `Results` directory.

As already noted, Goblin is currently a product prototype, and the goal is for Goblin to one day be developed to the point where it is capable of maintaining full control over projects, as well as their maintenance.
