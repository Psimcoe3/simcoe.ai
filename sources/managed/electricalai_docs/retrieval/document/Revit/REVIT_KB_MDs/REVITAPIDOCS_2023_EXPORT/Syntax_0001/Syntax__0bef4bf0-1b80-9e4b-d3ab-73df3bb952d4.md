[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Get(FieldType) Method (Field, ForgeTypeId)

---



|  |
| --- |
| [Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.htm)   [See Also](#seeAlsoToggle) |

Retrieves the value of the field in the entity.

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public FieldType Get<FieldType>( 	Field field, 	ForgeTypeId unitTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Get(Of FieldType) ( _ 	field As Field, _ 	unitTypeId As ForgeTypeId _ ) As FieldType ``` |

 

| Visual C++ |
| --- |
| ``` public: generic<typename FieldType> FieldType Get( 	Field^ field,  	ForgeTypeId^ unitTypeId ) ``` |

#### Parameters

field
:   Type:  [Autodesk.Revit.DB.ExtensibleStorage Field](0aeabd09-5c61-0439-e4c7-e1d68d0e1a3b.htm)    
     The field to retrieve.

unitTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     Identifier of the unit to which the value will be converted before returning. Must be compatible with the spec specified when creating the Schema.

# Type Parameters

FieldType
:   The type of the field

# Remarks

The template parameter must match the type of the field (specified when creating the Schema) exactly; this method does not perform data type conversions. The types for containers are IList for arrays and IDictionary for maps.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was NULL |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The Field belongs to a different Schema from this Entity, or this Entity is invalid. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Requested type does not match the field type. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The unitTypeId value is not compatible with the field description. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This field's subschema prevents reading. |

# See Also

[Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.htm)

[Get Overload](08a1c6b1-4635-dd3a-e18a-c4ca56bb7a8b.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)