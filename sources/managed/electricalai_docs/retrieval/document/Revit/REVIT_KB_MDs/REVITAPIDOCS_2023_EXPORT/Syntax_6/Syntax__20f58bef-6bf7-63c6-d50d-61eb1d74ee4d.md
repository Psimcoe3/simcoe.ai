[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAllowed Method

---



|  |
| --- |
| [RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.htm)   [See Also](#seeAlsoToggle) |

Check whether a bar type can be used with this RebarShape. Bar types are allowed by default.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2009

# Syntax

| C# |
| --- |
| ``` public bool GetAllowed( 	RebarBarType barType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAllowed ( _ 	barType As RebarBarType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool GetAllowed( 	RebarBarType^ barType ) ``` |

#### Parameters

barType
:   Type:  [Autodesk.Revit.DB.Structure RebarBarType](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)    
     A bar type in the same document as this shape.

#### Return Value

True if this shape may be combined with this barType.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)