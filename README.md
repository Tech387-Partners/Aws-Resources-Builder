# Goblin

If you have ever used AWS tools and services to develop a project, you have probably encountered their advantages, but also their disadvantages.<br/>
When building complex projects, we often found ourselves in a situation where we had to adjust resources, and pre-existing resources often created special problems that required subsequent adjustment.<br/>
We realized that the best practice for complex projects is to create permanently customized resources.<br/>
This job required manual changes to the GraphQL schema, as well as the creation of other resources such as resolver functions or the CustomResources.json file, which serves as a configuration for linking resources.<br/>
Most of this content used the same pattern, so we were often in a situation where we would copy large parts of the content and modify certain segments, which often resulted in errors that created a lot of headaches.<br/>

<br/>

Goblin was created with the idea of creating and maintaining resources based on a configuration, map or schema, such as GraphQL, in order to significantly shorten the creation time and avoid risks such as maintenance errors or unsynchronized subsequent added functionalities.<br/>

<br/>

Goblin is a demo version of an application that contains a large part of the mentioned functionalities, but it is still a prototype, so additional development is required to fulfill the given goals.<br/>


<br>

## <a>How does Goblin work?</a>

By launching Goblin, the `schema.gob` map will be loaded, based on which a detailed JSON configuration will be created for building resources.<br/>
After Goblin translates the `schema.gob` map into JSON content, it will start building resources.<br/> 
Goblin will create `schema.graphql`, `CustomResources.json`, and a group of resolver functions.<br/>

<br>
<br>

## <a>Goblin map (schema.gob)</a>

<br>

schema.gob is the basic map from which Goblin loads data and directives it works with.<br/> 
It is designed following GraphQL but for the purpose of extended functionalities.<br/>
The syntax and protocol by which the Goblin map is created are an internal standard.<br/>
This way was chosen as a readable and tidy solution that can fit a lot of commands into a relatively small text structure so that the instructions for creating resources could be written as simply and precisely as possible.<br/>
<br>

<details id="#schema.gob">
<summary><a href="#schema.gob"> 👉 👇 </a> schema.gob <a href="https://github.com/Tech387-Partners/Aws-Resources-Builder/blob/master/Goblin/Sources/schema.gob"> 🔗 link</a></summary>

<br>

Here is an example of the basic schema.gob map.<br/>
Currently, it does not support states such as comments, blank lines, and the like, so the map with details and description is in the following section.<br/>

<div>
    <img src="https://github.com/Tech387-Partners/Aws-Resources-Builder/blob/master/doc/src/Goblin-db.svg" alt="drawing" width="350"/>
</div>

<div>
    <img src="https://github.com/Tech387-Partners/Aws-Resources-Builder/blob/master/doc/src/Goblin.png" alt="drawing" width="350"/>
</div>


```text
[START_ENUMS]
[start_enum] Package
KG
PCS
[end_enum]
[END_ENUMS]
[START_MODELS]
[start_model] Supplier C+ U+ D- G+ L-
companyName String m! ci! ui?
contactName String m! ci! ui?
city String m! ci! ui?
country String m? ci? ui?
phone String m! ci! ui?
fax String m! ci! ui?
email String m! ci! ui? {"index":{"name":"SupplierByEmail","factor":"Email","inputArgs":[]}}
products [Product] m? ci- ui- {"hasMany":{"indexName":"ProductBySupplier","fields":["id"]}}
[end_model]
[start_model] Customer C+ U+ D- G+ L-
firstName String m! ci! ui?
lastName String m! ci! ui?
city String m! ci! ui?
country String m? ci? ui?
phone String m! ci! ui?
email String m! ci! ui? {"index":{"name":"customerByEmail","factor":"Email","inputArgs":[]}}
orders [Order] m? ci- ui- {"hasMany":{"indexName":"OrderByCustomer","fields":["id"]}}
[end_model]
[start_model] Product C+ U+ D- G+ L-
name String m! ci! ui?
suplierID ID m! ci! ui- 
unitPrice Float m! ci! ui?
package Package m! ci! ui?
isDiscounted Boolean m! ci! ui?
[end_model]
[start_model] Order C+ U+ D- G+ L-
date AWSDateTime m! ci! ui? 
customerID ID m! ci! ui-
totalAmount Float m! ci! ui?
[end_model]
[start_model] OrderItem C+ U+ D- G+ L-
orderID ID m! ci! ui-
productID ID m! ci! ui-
unitPrice Float m! ci! ui?
quantity Float m! ci! ui-
[end_model]
[END_MODELS]
```

</details>

<br>

<details id="#schema.gob">
<summary><a href="#schema.gob"> 👉 👇 </a> schema.gob with description </summary>


```text
[START_ENUMS]                    # Beginning of the field with configuration for enumerative types and values
[start_enum] Package             # Beginning of one enum type
KG                               # Enum value/case ...
PCS
[end_enum]                       # End of one enum type
[END_ENUMS]                      # End of the field with configuration for enums
[START_MODELS]                                                                                  # Beginning of the field with configuration for models
[start_model] Supplier C+ U+ D- G+ L-                                                           # Beginning/header of one model
companyName String m! ci! ui?                                                                   # Model argument
contactName String m! ci! ui?
city String m! ci! ui?
country String m? ci? ui?
phone String m! ci! ui?
fax String m! ci! ui?
email String m! ci! ui? {"index":{"name":"SupplierByEmail","factor":"Email","inputArgs":[]}}    # Argument with extended settings
products [Product] m? ci- ui- {"hasMany":{"indexName":"ProductBySupplier","fields":["id"]}}     # List argument with extended settings
[end_model]                                                                                     # End of the model
[start_model] Customer C+ U+ D- G+ L-
firstName String m! ci! ui?
lastName String m! ci! ui?
city String m! ci! ui?
country String m? ci? ui?
phone String m! ci! ui?
email String m! ci! ui? {"index":{"name":"customerByEmail","factor":"Email","inputArgs":[]}}
orders [Order] m? ci- ui- {"hasMany":{"indexName":"OrderByCustomer","fields":["id"]}}
[end_model]
[start_model] Product C+ U+ D- G+ L-
name String m! ci! ui?
suplierID ID m! ci! ui- 
unitPrice Float m! ci! ui?
package Package m! ci! ui?
isDiscounted Boolean m! ci! ui?
[end_model]
[start_model] Order C+ U+ D- G+ L-
date AWSDateTime m! ci! ui? 
customerID ID m! ci! ui-
totalAmount Float m! ci! ui?
[end_model]
[start_model] OrderItem C+ U+ D- G+ L-
orderID ID m! ci! ui-
productID ID m! ci! ui-
unitPrice Float m! ci! ui?
quantity Float m! ci! ui-
[end_model]
[END_MODELS]
```


**Model header** <a>[start_model] Supplier C+ U+ D- G+ L-</a>
* [start_model] -> Starting marker of the field that contains information about one model
* Supplier -> Name of the model
* C+ -> Marker for the existence of a customized CREATE segment (`+` - exists, `-` does not exist)
* U+ -> Marker for the existence of a customized UPDATE segment (`+` - exists, `-` does not exist)
* D- -> Marker for the existence of a customized DELETE segment (`+` - exists, `-` does not exist)
* G+ -> Marker for the existence of a customized GET segment (`+` - exists, `-` does not exist)
* L- -> Marker for the existence of a customized LIST segment (`+` - exists, `-` does not exist)

**Example of an argument** <a>companyName String m! ci! ui? </a>
* companyName -> Argument name
* String -> Data type
* m! -> Status marker of the argument (m! NOT_NULL, m? NULL)
* ci! -> Status marker in the create input model (ci! - mandatory, ci? - optional, ci- does not exist in the create input structure)
* ui? -> Status marker in the update input model (ui! - mandatory, ui? - optional, ui- does not exist in the update input structure)

**Example of an argument with extended settings** <a>companyName String m! ci! ui? {"index":{"name":"SupplierByEmail","factor":"Email","inputArgs":[]}}</a>
* companyName -> Argument name
* String -> Data type
* m! -> Status marker of the argument (m! NOT_NULL, m? NULL)
* ci! -> Status marker in the create input model (ci! - mandatory, ci? - optional, ci- does not exist in the create input structure)
* ui? -> Status marker in the update input model (ui! - mandatory, ui? - optional, ui- does not exist in the update input structure)
* {"index":{"name":"SupplierByEmail","factor":"Email","inputArgs":[]}} -> Data required to create GSI and related structures

**Example of a list argument with extended settings** <a>products [Product] m? ci- ui- {"hasMany":{"indexName":"ProductBySupplier","fields":["id"]}}</a>
* products -> Argument name
* [Product] -> Data type
* m? -> Status marker of the argument (m! NOT_NULL, m? NULL)
* ci- -> Status marker in the create input model **Always disabled**
* ui- -> Status marker in the update input model **Always disabled**
* {"hasMany":{"indexName":"ProductBySupplier","fields":["id"]}} -> Data required to create a GSI relationship


</details>


<br>
<br>

## <a>Launch/Activation</a>

Currently, the launch is performed by calling the index.py file using the command `python3 index.py` or `python index.py`.

<br>
<br>

## <a>Results</a>

<br>

Goblin will create a directory named "Results" if it does not already exist, and for each run, it will create a new directory within the Results directory named after the current time, and place the generated results inside it.

<br>

<details id="#schema.graphql">
<summary><a href="#schema.graphql"> 👉 👇 </a> schema.graphql </summary>

A file named schema.graphql will be created with a clearly defined structure of models, input entities for creating, updating, and deleting items, as well as precisely crafted subscriptions mutations and queries.<br/>
If we take a closer look, we will see that schema.graphql is generated exactly according to the directives from the schema.gob map where it is clearly defined which resources will be customized and which ones GraphQL will create by default.<br/><br/>


```graphql
type Supplier @model(mutations: { delete: "deleteSupplier" }, queries: { list: "listSuppliers" }) {
  id: ID!
  companyName: String!
  contactName: String!
  city: String!
  country: String
  phone: String!
  fax: String!
  email: String! @index(name: "SupplierByEmail")
  products: [Product] @hasMany(indexName: "ProductBySupplier", fields: ["id"])
}

type Customer @model(mutations: { delete: "deleteCustomer" }, queries: { list: "listCustomers" }) {
  id: ID!
  firstName: String!
  lastName: String!
  city: String!
  country: String
  phone: String!
  email: String! @index(name: "customerByEmail")
  orders: [Order] @hasMany(indexName: "OrderByCustomer", fields: ["id"])
}

type Product @model(mutations: { delete: "deleteProduct" }, queries: { list: "listProducts" }) {
  id: ID!
  name: String!
  suplierID: ID!
  unitPrice: Float!
  package: Package!
  isDiscounted: Boolean!
}

type Order @model(mutations: { delete: "deleteOrder" }, queries: { list: "listOrders" }) {
  id: ID!
  date: AWSDateTime!
  customerID: ID!
  totalAmount: Float!
}

type OrderItem @model(mutations: { delete: "deleteOrderItem" }, queries: { list: "listOrderItems" }) {
  id: ID!
  orderID: ID!
  productID: ID!
  unitPrice: Float!
  quantity: Float!
}


#===================== [ START ] Input Supplier ===================== ]
input CreateSupplierInput {
  id: ID!
  companyName: String!
  contactName: String!
  city: String!
  country: String
  phone: String!
  fax: String!
  email: String!
}

input UpdateSupplierInput {
  id: ID
  companyName: String
  contactName: String
  city: String
  country: String
  phone: String
  fax: String
  email: String
}
#====================== [ END ] Input Supplier ====================== ]

#===================== [ START ] Input Customer ===================== ]
input CreateCustomerInput {
  id: ID!
  firstName: String!
  lastName: String!
  city: String!
  country: String
  phone: String!
  email: String!
}

input UpdateCustomerInput {
  id: ID
  firstName: String
  lastName: String
  city: String
  country: String
  phone: String
  email: String
}
#====================== [ END ] Input Customer ====================== ]

#===================== [ START ] Input Product ===================== ]
input CreateProductInput {
  id: ID!
  name: String!
  suplierID: ID!
  unitPrice: Float!
  package: Package!
  isDiscounted: Boolean!
}

input UpdateProductInput {
  id: ID
  name: String
  unitPrice: Float
  package: Package
  isDiscounted: Boolean
}
#====================== [ END ] Input Product ====================== ]

#===================== [ START ] Input Order ===================== ]
input CreateOrderInput {
  id: ID!
  date: AWSDateTime!
  customerID: ID!
  totalAmount: Float!
}

input UpdateOrderInput {
  id: ID
  date: AWSDateTime
  totalAmount: Float
}
#====================== [ END ] Input Order ====================== ]

#===================== [ START ] Input OrderItem ===================== ]
input CreateOrderItemInput {
  id: ID!
  orderID: ID!
  productID: ID!
  unitPrice: Float!
  quantity: Float!
}

input UpdateOrderItemInput {
  id: ID
  unitPrice: Float
}
#====================== [ END ] Input OrderItem ====================== ]


type Mutation {
  createSupplier(input: CreateSupplierInput!): Supplier @aws_api_key @aws_cognito_user_pools
  updateSupplier(input: UpdateSupplierInput!): Supplier @aws_api_key @aws_cognito_user_pools
  createCustomer(input: CreateCustomerInput!): Customer @aws_api_key @aws_cognito_user_pools
  updateCustomer(input: UpdateCustomerInput!): Customer @aws_api_key @aws_cognito_user_pools
  createProduct(input: CreateProductInput!): Product @aws_api_key @aws_cognito_user_pools
  updateProduct(input: UpdateProductInput!): Product @aws_api_key @aws_cognito_user_pools
  createOrder(input: CreateOrderInput!): Order @aws_api_key @aws_cognito_user_pools
  updateOrder(input: UpdateOrderInput!): Order @aws_api_key @aws_cognito_user_pools
  createOrderItem(input: CreateOrderItemInput!): OrderItem @aws_api_key @aws_cognito_user_pools
  updateOrderItem(input: UpdateOrderItemInput!): OrderItem @aws_api_key @aws_cognito_user_pools
}

type Subscription {
  onCreateSupplier: Supplier @aws_subscribe(mutations: ["createSupplier"]) @aws_api_key @aws_cognito_user_pools
  onUpdateSupplier: Supplier @aws_subscribe(mutations: ["updateSupplier"]) @aws_api_key @aws_cognito_user_pools
  onCreateCustomer: Customer @aws_subscribe(mutations: ["createCustomer"]) @aws_api_key @aws_cognito_user_pools
  onUpdateCustomer: Customer @aws_subscribe(mutations: ["updateCustomer"]) @aws_api_key @aws_cognito_user_pools
  onCreateProduct: Product @aws_subscribe(mutations: ["createProduct"]) @aws_api_key @aws_cognito_user_pools
  onUpdateProduct: Product @aws_subscribe(mutations: ["updateProduct"]) @aws_api_key @aws_cognito_user_pools
  onCreateOrder: Order @aws_subscribe(mutations: ["createOrder"]) @aws_api_key @aws_cognito_user_pools
  onUpdateOrder: Order @aws_subscribe(mutations: ["updateOrder"]) @aws_api_key @aws_cognito_user_pools
  onCreateOrderItem: OrderItem @aws_subscribe(mutations: ["createOrderItem"]) @aws_api_key @aws_cognito_user_pools
  onUpdateOrderItem: OrderItem @aws_subscribe(mutations: ["updateOrderItem"]) @aws_api_key @aws_cognito_user_pools
}

type Query {
  getSupplier(id: ID!): Supplier @aws_api_key @aws_cognito_user_pools
  getSupplierByEmail(): Supplier @aws_api_key @aws_cognito_user_pools
  getCustomer(id: ID!): Customer @aws_api_key @aws_cognito_user_pools
  getCustomerByEmail(): Customer @aws_api_key @aws_cognito_user_pools
  getProduct(id: ID!): Product @aws_api_key @aws_cognito_user_pools
  getOrder(id: ID!): Order @aws_api_key @aws_cognito_user_pools
  getOrderItem(id: ID!): OrderItem @aws_api_key @aws_cognito_user_pools
}
```

</details>

<br>

<details id="#CustomResources.json">
<summary><a href="#CustomResources.json"> 👉 👇 </a> CustomResources.json 👉 A file that imports all customized resources. </summary>

<br/>

As can be seen in the generated example, Goblin has created a CustomResources.json configuration that imports all customized resources into the Amplify project.<br/>
What is important to emphasize is how much manual effort it takes to create such a structure with the risk of writing errors, while Goblin creates it almost instantly and without errors.<br/>
It is also important to note for this example that Goblin has created items that previously had to be created completely manually, such as 'get' functions based on GSI. <br/><br/>

<br>

```json
{
    "FunctionCreateCustomer": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "CustomerTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Mutation_createCustomer_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.createCustomer.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.createCustomer.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionCreateOrder": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "OrderTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Mutation_createOrder_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.createOrder.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.createOrder.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionCreateOrderItem": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "OrderItemTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Mutation_createOrderItem_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.createOrderItem.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.createOrderItem.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionCreateProduct": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "ProductTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Mutation_createProduct_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.createProduct.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.createProduct.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionCreateSupplier": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "SupplierTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Mutation_createSupplier_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.createSupplier.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.createSupplier.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionGetCustomer": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "CustomerTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Query_getCustomer_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Query.getCustomer.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Query.getCustomer.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionGetCustomerByEmail": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "CustomerTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Query_getCustomerByEmail_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Query.getCustomerByEmail.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Query.getCustomerByEmail.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionGetOrder": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "OrderTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Query_getOrder_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Query.getOrder.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Query.getOrder.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionGetOrderItem": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "OrderItemTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Query_getOrderItem_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Query.getOrderItem.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Query.getOrderItem.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionGetProduct": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "ProductTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Query_getProduct_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Query.getProduct.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Query.getProduct.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionGetSupplier": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "SupplierTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Query_getSupplier_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Query.getSupplier.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Query.getSupplier.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionGetSupplierByEmail": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "SupplierTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Query_getSupplierByEmail_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Query.getSupplierByEmail.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Query.getSupplierByEmail.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionUpdateCustomer": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "CustomerTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Mutation_updateCustomer_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.updateCustomer.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.updateCustomer.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionUpdateOrder": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "OrderTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Mutation_updateOrder_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.updateOrder.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.updateOrder.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionUpdateOrderItem": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "OrderItemTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Mutation_updateOrderItem_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.updateOrderItem.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.updateOrderItem.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionUpdateProduct": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "ProductTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Mutation_updateProduct_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.updateProduct.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.updateProduct.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "FunctionUpdateSupplier": {
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "DataSourceName": "SupplierTable",
            "FunctionVersion": "2018-05-29",
            "Name": "Mutation_updateSupplier_Function",
            "RequestMappingTemplateS3Location": {
                "Fn::Sub": [
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.updateSupplier.req.vtl",
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
                    "s3://${S3DeploymentBucket}/${S3DeploymentRootKey}/resolvers/Mutation.updateSupplier.res.vtl",
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
        },
        "Type": "AWS::AppSync::FunctionConfiguration"
    },
    "PipelineCreateCustomer": {
        "DependsOn": [
            "FunctionCreateCustomer"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "createCustomer",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionCreateCustomer",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Mutation"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineCreateOrder": {
        "DependsOn": [
            "FunctionCreateOrder"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "createOrder",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionCreateOrder",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Mutation"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineCreateOrderItem": {
        "DependsOn": [
            "FunctionCreateOrderItem"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "createOrderItem",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionCreateOrderItem",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Mutation"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineCreateProduct": {
        "DependsOn": [
            "FunctionCreateProduct"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "createProduct",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionCreateProduct",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Mutation"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineCreateSupplier": {
        "DependsOn": [
            "FunctionCreateSupplier"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "createSupplier",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionCreateSupplier",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Mutation"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineGetCustomer": {
        "DependsOn": [
            "FunctionGetCustomer"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "getCustomer",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionGetCustomer",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Query"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineGetCustomerByEmail": {
        "DependsOn": [
            "FunctionGetCustomerByEmail"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "getCustomerByEmail",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionGetCustomerByEmail",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Query"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineGetOrder": {
        "DependsOn": [
            "FunctionGetOrder"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "getOrder",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionGetOrder",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Query"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineGetOrderItem": {
        "DependsOn": [
            "FunctionGetOrderItem"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "getOrderItem",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionGetOrderItem",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Query"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineGetProduct": {
        "DependsOn": [
            "FunctionGetProduct"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "getProduct",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionGetProduct",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Query"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineGetSupplier": {
        "DependsOn": [
            "FunctionGetSupplier"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "getSupplier",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionGetSupplier",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Query"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineGetSupplierByEmail": {
        "DependsOn": [
            "FunctionGetSupplierByEmail"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "getSupplierByEmail",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionGetSupplierByEmail",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Query"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineUpdateCustomer": {
        "DependsOn": [
            "FunctionUpdateCustomer"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "updateCustomer",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionUpdateCustomer",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Mutation"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineUpdateOrder": {
        "DependsOn": [
            "FunctionUpdateOrder"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "updateOrder",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionUpdateOrder",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Mutation"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineUpdateOrderItem": {
        "DependsOn": [
            "FunctionUpdateOrderItem"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "updateOrderItem",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionUpdateOrderItem",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Mutation"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineUpdateProduct": {
        "DependsOn": [
            "FunctionUpdateProduct"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "updateProduct",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionUpdateProduct",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Mutation"
        },
        "Type": "AWS::AppSync::Resolver"
    },
    "PipelineUpdateSupplier": {
        "DependsOn": [
            "FunctionUpdateSupplier"
        ],
        "Properties": {
            "ApiId": {
                "Ref": "AppSyncApiId"
            },
            "FieldName": "updateSupplier",
            "Kind": "PIPELINE",
            "PipelineConfig": {
                "Functions": [
                    {
                        "Fn::GetAtt": [
                            "FunctionUpdateSupplier",
                            "FunctionId"
                        ]
                    }
                ]
            },
            "RequestMappingTemplate": "{}",
            "ResponseMappingTemplate": "$util.toJson($ctx.result)",
            "TypeName": "Mutation"
        },
        "Type": "AWS::AppSync::Resolver"
    }
}
```
</details>

<br>

<details id="#vtl-resolvers">
<summary><a href="#vtl-resolvers"> 👉 👇 </a> Resolvers </summary>

<br>

One of the segments for which Goblin is responsible is the resolvers segment.<br/>
In the results, Goblin will create vtl req-res functions for you in the resolvers directory.<br/>
The example includes functions that always require manual access, but instead of your developer, Goblin will create functions based on the specified GSI if it is specified in the map for an argument of a model.<br/>

<br>

```java
$util.toJson({
  "version": "2018-05-29",
  "operation": "Query",
  "limit": 10000,
  "query": {
      "expression":"#email = :email",
      "expressionNames":{
         "#email":"email"
      },
      "expressionValues":{
         ":email":{
            "S":"$email"
         }
      }
   },
  "index": "customerByEmail",
  "scanIndexForward": true
})
```

<br>

```java
#if( $ctx.error )
  $util.error($ctx.error.message, $ctx.error.type)
#end
#if( !$ctx.result.items.isEmpty() && $ctx.result.scannedCount >= 1 )
  $util.qr($ctx.stash.put("customerByEmail", $ctx.result.items[0]))
  #if( $ctx.info.fieldName != "getCustomerByEmail" )
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
```

<br>

</details>

<br>
<br>

## <a>Vision</a>

Our goal is to have a tool in the future that is capable of creating and maintaining an unlimited number of projects with full status control on all environments.<br/>
The need for integration with other services is inevitable.<br/>
Currently, customized resolver structures are being developed to provide complete control over related functions that will share data, as well as the creation and connection of other types of functions such as lambda resources or auth.<br/>

<br><br><br>