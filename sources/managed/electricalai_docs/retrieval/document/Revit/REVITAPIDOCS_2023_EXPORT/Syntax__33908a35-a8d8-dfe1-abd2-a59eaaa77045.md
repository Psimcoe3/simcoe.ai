[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAllStructuralConnectionTypeIds Method

---



|  |
| --- |
| [StructuralConnectionType Class](e3b74cf3-71d8-a230-7fb6-0fdc4c81fca2.htm)   [See Also](#seeAlsoToggle) |

Collects the ids of all StructuralConnectionTypes in the document.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static void GetAllStructuralConnectionTypeIds( 	Document cda, 	out ICollection<ElementId> ids ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub GetAllStructuralConnectionTypeIds ( _ 	cda As Document, _ 	<OutAttribute> ByRef ids As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void GetAllStructuralConnectionTypeIds( 	Document^ cda,  	[OutAttribute] ICollection<ElementId^>^% ids ) ``` |

#### Parameters

cda
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

ids
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)   %

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[StructuralConnectionType Class](e3b74cf3-71d8-a230-7fb6-0fdc4c81fca2.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)