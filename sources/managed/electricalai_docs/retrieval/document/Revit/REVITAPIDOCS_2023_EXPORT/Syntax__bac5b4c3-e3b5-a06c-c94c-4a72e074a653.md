[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetSubSchemaGUID Method

---



|  |
| --- |
| [FieldBuilder Class](13cd8e7c-acc8-af6e-0ae6-a9b77fcd913c.htm)   [See Also](#seeAlsoToggle) |

Sets the GUID of the Schema of the Entities that are intended to be stored in this field.

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public FieldBuilder SetSubSchemaGUID( 	Guid guid ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetSubSchemaGUID ( _ 	guid As Guid _ ) As FieldBuilder ``` |

 

| Visual C++ |
| --- |
| ``` public: FieldBuilder^ SetSubSchemaGUID( 	Guid guid ) ``` |

#### Parameters

guid
:   Type:  [System Guid](http://msdn2.microsoft.com/en-us/library/cey1zx63)    
     The GUID of the subschema.

#### Return Value

The FieldBuilder object may be used to add more details to the field.

# Remarks

Fields of type Entity - subentities - need to specify their Schema. The framework will prevent subentities with incorrect schemas from being stored in the entity. Additionally, the access level of the subschema will be checked against the currently executing add-in and access to restricted subentities will be prevented.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The SchemaBuilder has already finished building the Schema. -or- The field type does not utilize SubSchemas. |

# See Also

[FieldBuilder Class](13cd8e7c-acc8-af6e-0ae6-a9b77fcd913c.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)