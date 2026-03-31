[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method (String)

---



|  |
| --- |
| [Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.htm)   [See Also](#seeAlsoToggle) |

Resets the field to its default value.

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void Clear( 	string fieldName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Clear ( _ 	fieldName As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Clear( 	String^ fieldName ) ``` |

#### Parameters

fieldName
:   Type:  System String    
     The name of the field to clear.

# Remarks

The default value is zero for numeric fields, invalid value for identifiers and entities, and empty for strings and containers. This method is a shortcut that will look up the field by name. If you want to call it on many entities, it is faster if you look up the field yourself.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The name matches no field in this Entity's Schema. -or- This field's subschema prevents writing. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This Entity is invalid. |

# See Also

[Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.htm)

[Clear Overload](8b013f12-46fb-d303-a9af-aa176f088cae.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)