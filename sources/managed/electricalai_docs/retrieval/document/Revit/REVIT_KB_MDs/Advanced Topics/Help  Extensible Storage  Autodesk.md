---
created: 2026-01-28T21:17:25 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Storing_Data_in_the_Revit_model_Extensible_Storage_html
author: 
---

# Help | Extensible Storage | Autodesk

> ## Excerpt
> Create your own class-like Schema data structures and attach instances of them to any Element in a Revit model.

---
Create your own class-like Schema data structures and attach instances of them to any Element in a Revit model.

Schema-based data is saved with the Revit model and allows for higher-level, metadata-enhanced, object-oriented data structures. Schema data can be configured to be readable and/or writable to all users, just a specific application vendor, or just a specific application from a vendor.

The following steps are necessary to store data with Elements in Revit:

1.  Create and name a new schema
2.  Set the read/write access for the schema
3.  Define one or more fields of data for the schema
4.  Create an entity based on the schema
5.  Assign values to the fields for the entity
6.  Associate the entity with a Revit element
    
    ### Schemas and SchemaBuilder
    

The first step to creating extensible storage is to define the schema. A schema is similar to a class in an object-oriented programming language. Use the SchemaBuilder class constructor to create a new schema. SchemaBuilder is a helper class used to create schemas. Once a schema is finalized using SchemaBuilder, the Schema class is used to access properties of the schema. At that stage, the schema is no longer editable.

Although the SchemaBuilder constructor takes a GUID which is used to identify the schema, a schema name is also required. After creating the schema, call SchemaBuilder.SetSchemaName() to assign a user-friendly identifier for the schema. The schema name is useful to identify a schema in an error message.

The read and write access levels of entities associated with the schema can be set independently. The options are Public, Vendor, or Application. If either the read or write access level is set to Vendor, the VendorId of the third-party vendor that may access entities of the schema must be specified. If either access level is set to Application, the GUID of the application or add-in that may access entities of the schema must be supplied.

Note: Schemas are stored with the document and any Revit API add-in may read the available schemas in the document, as well as some data of the schema. However, access to the fields of a schema is restricted based on the read access defined in the schema and the actual data in the entities stored with specific elements is restricted based on the read and write access levels set in the schema when it is defined.

### Fields and FieldBuilder

Once the schema has been created, fields may be defined. A field is similar to a property of a class. It contains a name, documentation, value type and unit type. Fields can be a simple type, an array, or a map. The following simple data types are allowed:

<table summary="" id="GUID-113B09CA-DBBB-41A7-8021-005663B267AE__TABLE_0E949AA5AB7F45FA9C786263C927A687"><tbody><tr><td><b>Type</b></td><td><b>Default Value</b></td></tr><tr><td>int</td><td>0</td></tr><tr><td>short</td><td>0</td></tr><tr><td>byte</td><td>0</td></tr><tr><td>double</td><td>0.0</td></tr><tr><td>float</td><td>0.0</td></tr><tr><td>bool</td><td>false</td></tr><tr><td>string</td><td>Empty string ("")</td></tr><tr><td>GUID</td><td>Guid.Empty {00000000-0000-0000-0000-000000000000}</td></tr><tr><td>ElementId</td><td>ElementId.InvalidElementId</td></tr><tr><td>Autodesk.Revit.DB.XYZ</td><td>(0.0,0.0,0.0)</td></tr><tr><td>Autodesk.Revit.DB.UV</td><td>(0.0,0.0)</td></tr></tbody></table>

Additionally, a field may be of type Autodesk.Revit.DB.ExtensibleStorage.Entity. In other words, an instance of another Schema, also known as a SubSchema or SubEntity. The default value for a field of this type is Entity with null schema, and guid of Guid.Empty.

When using string fields, note that Revit has a 16mb limit on string objects.

A simple field can be created using the SchemaBuilder.AddSimpleField() method to specify a name and type for the field. AddSimpleField() returns a FieldBuilder, which is a helper class for defining Fields. If the type of the field was specified as Entity, use FieldBuilder.SetSubSchemaGUID() to specify the GUID of the schema of the Entities that are to be stored in this field.

Use the SchemaBuilder.AddArrayField() method to create a field containing an array of values in the Schema, with a given name and type of contained values. Array fields can have all the same types as simple fields.

Use the SchemaBuilder.AddMapField() method to create a field containing an ordered key-value map in the Schema, with given name, type of key and type of contained values. Supported types for values are the same as for simple fields. Supported types for keys are limited to int, short, byte, string, bool, ElementId and GUID.

Once the schema is finalized using SchemaBuilder, fields can no longer be edited using FieldBuilder. At that stage, the Schema class provides methods to get a Field by name, or a list of all Fields defined in the Schema.

### Entities

After all fields have been defined for the schema, SchemaBuilder.Finish() will return the finished Schema. A new Entity can be created using that schema. For each Field in the Schema, the value can be stored using Entity.Set(), which takes a Field and a value (whose type is dependent on the field type). Once all applicable fields have been set for the entity, it can be assigned to an element using the Element.SetEntity() method.

To retrieve the data later, call Element.GetEntity() passing in the corresponding Schema. If no entity based on that schema was saved with the Element, an invalid Entity will be returned. To check that a valid Entity was returned, call the Entity.IsValid() method. Field values from the entity can be obtained using the Entity.Get() method.

To remove an extensible storage entity from an Element, call Element.DeleteEntity() passing in the Schema that was used to create it.

To determine Entities stored with an element, use the Element.GetEntitySchemaGuids() method, which returns the Schema guids of any Entities for the Element. The Schema guids can be used with the static method Schema.Lookup() to retrieve the corresponding Schemas.

The following is an example of defining an extensible storage Schema, creating an Entity, setting its values, assigning it to an Element, and retrieving the data.

<table summary="" id="GUID-113B09CA-DBBB-41A7-8021-005663B267AE__TABLE_5ADE5BC497BC47A5B2203B87CA13070D"><tbody><tr><td><b>Code Region 22-9: Extensible Storage</b></td></tr><tr><td><pre><code><span>// Create a data structure, attach it to a wall, populate it with data, and retrieve the data back from the wall</span><span>
</span><span>void</span><span> </span><span>StoreDataInWall</span><span>(</span><span>Wall</span><span> wall</span><span>,</span><span> XYZ dataToStore</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Transaction</span><span> createSchemaAndStoreData </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>wall</span><span>.</span><span>Document</span><span>,</span><span> </span><span>"tCreateAndStore"</span><span>);</span><span>
        createSchemaAndStoreData</span><span>.</span><span>Start</span><span>();</span><span>
        </span><span>SchemaBuilder</span><span> schemaBuilder </span><span>=</span><span> 
                </span><span>new</span><span> </span><span>SchemaBuilder</span><span>(</span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"720080CB-DA99-40DC-9415-E53F280AA1F0"</span><span>));</span><span>
        schemaBuilder</span><span>.</span><span>SetReadAccessLevel</span><span>(</span><span>AccessLevel</span><span>.</span><span>Public</span><span>);</span><span> </span><span>// allow anyone to read the object</span><span>
        schemaBuilder</span><span>.</span><span>SetWriteAccessLevel</span><span>(</span><span>AccessLevel</span><span>.</span><span>Vendor</span><span>);</span><span> </span><span>// restrict writing to this vendor only</span><span>
        schemaBuilder</span><span>.</span><span>SetVendorId</span><span>(</span><span>"ADSK"</span><span>);</span><span> </span><span>// required because of restricted write-access</span><span>
        schemaBuilder</span><span>.</span><span>SetSchemaName</span><span>(</span><span>"WireSpliceLocation"</span><span>);</span><span>
        </span><span>// create a field to store an XYZ</span><span>
        </span><span>FieldBuilder</span><span> fieldBuilder </span><span>=</span><span> 
                schemaBuilder</span><span>.</span><span>AddSimpleField</span><span>(</span><span>"WireSpliceLocation"</span><span>,</span><span> </span><span>typeof</span><span>(</span><span>XYZ</span><span>));</span><span> 
        fieldBuilder</span><span>.</span><span>SetSpec</span><span>(</span><span>SpecTypeId</span><span>.</span><span>Length</span><span>);</span><span>
        fieldBuilder</span><span>.</span><span>SetDocumentation</span><span>(</span><span>"A stored location value representing a wiring splice in a wall."</span><span>);</span><span>

        </span><span>Schema</span><span> schema </span><span>=</span><span> schemaBuilder</span><span>.</span><span>Finish</span><span>();</span><span> </span><span>// register the Schema object</span><span>
        </span><span>Entity</span><span> entity </span><span>=</span><span> </span><span>new</span><span> </span><span>Entity</span><span>(</span><span>schema</span><span>);</span><span> </span><span>// create an entity (object) for this schema (class)</span><span>
        </span><span>// get the field from the schema</span><span>
        </span><span>Field</span><span> fieldSpliceLocation </span><span>=</span><span> schema</span><span>.</span><span>GetField</span><span>(</span><span>"WireSpliceLocation"</span><span>);</span><span> 
        </span><span>// set the value for this entity</span><span>
        entity</span><span>.</span><span>Set</span><span>&lt;</span><span>XYZ</span><span>&gt;(</span><span>fieldSpliceLocation</span><span>,</span><span> dataToStore</span><span>,</span><span> </span><span>UnitTypeId</span><span>.</span><span>Meters</span><span>);</span><span>
        wall</span><span>.</span><span>SetEntity</span><span>(</span><span>entity</span><span>);</span><span> </span><span>// store the entity in the element</span><span>

        </span><span>// get the data back from the wall</span><span>
        </span><span>Entity</span><span> retrievedEntity </span><span>=</span><span> wall</span><span>.</span><span>GetEntity</span><span>(</span><span>schema</span><span>);</span><span>
        XYZ retrievedData </span><span>=</span><span> 
                retrievedEntity</span><span>.</span><span>Get</span><span>&lt;</span><span>XYZ</span><span>&gt;(</span><span>schema</span><span>.</span><span>GetField</span><span>(</span><span>"WireSpliceLocation"</span><span>),</span><span>
                </span><span>UnitTypeId</span><span>.</span><span>Meters</span><span>);</span><span>
        createSchemaAndStoreData</span><span>.</span><span>Commit</span><span>();</span><span>  
</span><span>}</span></code></pre></td></tr></tbody></table>

## Advantages

#### Self Documenting and Self-Defining

Creating a schema by adding fields, units, sub-entities, and description strings is not only a means for storing data. It is also implicit documentation for other users and a way for others to create entities of the same schema later with an easy adoption path.

#### Takes Advantage of Locality

Because schema entities are stored on a per-element basis, there is no need to necessarily read all extensible storage data in a document (e.g. all data from all beam family instances) when an application might only need data for the currently selected beam. This allows the potential for more specifically targeted data access code and better data access performance overall.
