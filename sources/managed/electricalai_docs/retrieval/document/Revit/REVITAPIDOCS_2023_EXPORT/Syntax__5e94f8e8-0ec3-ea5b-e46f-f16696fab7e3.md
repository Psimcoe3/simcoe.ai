[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsTypeOf Method

---



|  |
| --- |
| [IFCAnyHandle Class](8b893943-70fa-94bf-90be-1523d516ecb3.htm)   [See Also](#seeAlsoToggle) |

Determines whether the instance is an instance of exactly the specified instance type.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool IsTypeOf( 	string typeName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsTypeOf ( _ 	typeName As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsTypeOf( 	String^ typeName ) ``` |

#### Parameters

typeName
:   Type:  System String    
     The instance type name.

#### Return Value

True if the instance is an instance of the specified instance type, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCAnyHandle Class](8b893943-70fa-94bf-90be-1523d516ecb3.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)