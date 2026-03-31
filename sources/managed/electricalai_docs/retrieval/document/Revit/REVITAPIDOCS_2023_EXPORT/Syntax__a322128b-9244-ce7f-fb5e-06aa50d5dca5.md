[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDefaultElementTypeIdValid Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Checks whether the element type id is valid for the give DefaultElmentType id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool IsDefaultElementTypeIdValid( 	ElementTypeGroup defaultTypeId, 	ElementId typeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsDefaultElementTypeIdValid ( _ 	defaultTypeId As ElementTypeGroup, _ 	typeId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsDefaultElementTypeIdValid( 	ElementTypeGroup defaultTypeId,  	ElementId^ typeId ) ``` |

#### Parameters

defaultTypeId
:   Type:  [Autodesk.Revit.DB ElementTypeGroup](f5b57d98-c551-9693-9009-8eb17fef8a14.htm)    
     The default element type id.

typeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element type id.

#### Return Value

True if the element type id is valid for the give DefaultElmentType id, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)