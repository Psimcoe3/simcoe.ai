[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Entity Constructor (Schema)

---



|  |
| --- |
| [Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.htm)   [See Also](#seeAlsoToggle) |

Creates a new Entity corresponding to the Schema.

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public Entity( 	Schema schema ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	schema As Schema _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: Entity( 	Schema^ schema ) ``` |

#### Parameters

schema
:   Type:  [Autodesk.Revit.DB.ExtensibleStorage Schema](9817e7db-8367-ea4e-1769-0488f3faa37f.htm)

# Remarks

You can store the newly created Entity in an Element or in another Entity. If you do not have write access to the Schema, an exception will be thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Writing of Entities of this Schema is not allowed to the current add-in. |

# See Also

[Entity Class](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.htm)

[Entity Overload](b9fcfb42-c3e4-857f-1825-d2e85b1e57fe.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)