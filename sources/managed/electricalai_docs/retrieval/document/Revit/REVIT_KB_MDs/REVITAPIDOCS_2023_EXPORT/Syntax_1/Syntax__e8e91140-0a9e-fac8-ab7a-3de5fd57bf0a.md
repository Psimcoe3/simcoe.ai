[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsNotEmpty Method

---



|  |
| --- |
| [DisplacementElement Class](08113547-eaaa-5ec1-5ff1-de609fe7c29c.htm)   [See Also](#seeAlsoToggle) |

Validates that the input set of element ids is valid for a DisplacementElement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static bool IsNotEmpty( 	ICollection<ElementId> elementIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsNotEmpty ( _ 	elementIds As ICollection(Of ElementId) _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsNotEmpty( 	ICollection<ElementId^>^ elementIds ) ``` |

#### Parameters

elementIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     A set of element ids.

#### Return Value

True if the set of element ids is not empty.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DisplacementElement Class](08113547-eaaa-5ec1-5ff1-de609fe7c29c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)