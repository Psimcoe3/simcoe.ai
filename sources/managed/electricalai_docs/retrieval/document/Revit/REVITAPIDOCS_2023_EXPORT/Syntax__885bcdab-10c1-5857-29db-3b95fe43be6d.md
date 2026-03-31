[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetTrussMemberInfo Method

---



|  |
| --- |
| [Truss Class](e0cdc591-cac6-57c7-6190-f0d48cc0e4a9.htm)   [See Also](#seeAlsoToggle) |

Query if a given element is a member of a truss, its lock status and its usage, etc.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public TrussMemberInfo GetTrussMemberInfo( 	ElementId elemId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetTrussMemberInfo ( _ 	elemId As ElementId _ ) As TrussMemberInfo ``` |

 

| Visual C++ |
| --- |
| ``` public: TrussMemberInfo^ GetTrussMemberInfo( 	ElementId^ elemId ) ``` |

#### Parameters

elemId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The querying element.

#### Return Value

A struct TrussMemberInfo that contains the querying element's host truss, whether to lock to the truss, usage type, etc.

# See Also

[Truss Class](e0cdc591-cac6-57c7-6190-f0d48cc0e4a9.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)