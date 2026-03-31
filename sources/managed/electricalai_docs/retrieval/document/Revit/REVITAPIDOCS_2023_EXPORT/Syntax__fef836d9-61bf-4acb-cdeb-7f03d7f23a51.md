[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Set(FieldType) Method (Field, FieldType)

---



|  |
| --- |
| [Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.htm)   [See Also](#seeAlsoToggle) |

Stores the value of the field in the entity.

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void Set<FieldType>( 	Field field, 	FieldType value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Set(Of FieldType) ( _ 	field As Field, _ 	value As FieldType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: generic<typename FieldType> void Set( 	Field^ field,  	FieldType value ) ``` |

#### Parameters

field
:   Type:  [Autodesk.Revit.DB.ExtensibleStorage Field](0aeabd09-5c61-0439-e4c7-e1d68d0e1a3b.htm)    
     The field to update.

value
:   Type:   FieldType

# Type Parameters

FieldType
:   The type of the field

# Remarks

The template parameter must match the type of the field (specified when creating the Schema) exactly; this method does not perform data type conversions. The types for containers are IList for arrays and IDictionary for maps.

Note that when string values are specified as map keys, they are case-insensitive.

This method only modifies your copy of the Entity. Store the Entity in an element or another Entity to save the new value. Write access check is not performed on each call to Set. Instead, write access is checked when you try to save the Entity in an Element or another Entity.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was NULL |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The Field belongs to a different Schema from this Entity, or this Entity is invalid. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Requested type does not match the field type. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | For floating-point fields, use the overload taking a ForgeTypeId parameter. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This field's subschema prevents writing. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Invalid floating-point value. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | String is too long; exceeds max length of 16mb characters. |

# See Also

[Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.htm)

[Set Overload](ca7fbcad-94aa-40a0-f77d-1f78c5ecf705.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)