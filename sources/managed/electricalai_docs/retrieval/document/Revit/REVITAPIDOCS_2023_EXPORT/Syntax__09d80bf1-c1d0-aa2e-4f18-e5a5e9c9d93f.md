[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetEntity Method

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Returns the existing entity corresponding to the Schema if it has been saved in the Element, or an invalid entity otherwise.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public Entity GetEntity( 	Schema schema ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetEntity ( _ 	schema As Schema _ ) As Entity ``` |

 

| Visual C++ |
| --- |
| ``` public: Entity^ GetEntity( 	Schema^ schema ) ``` |

#### Parameters

schema
:   Type:  [Autodesk.Revit.DB.ExtensibleStorage Schema](9817e7db-8367-ea4e-1769-0488f3faa37f.htm)    
     The Schema describing the Entity.

#### Return Value

The returned Entity.

# Remarks

The Entity that is returned is a copy of the stored data (with copy-on-write optimization). Modifying it is allowed (even with restricted write), but to save your changes you must call SetEntity.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Reading of Entities of this Schema is not allowed to the current add-in. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)