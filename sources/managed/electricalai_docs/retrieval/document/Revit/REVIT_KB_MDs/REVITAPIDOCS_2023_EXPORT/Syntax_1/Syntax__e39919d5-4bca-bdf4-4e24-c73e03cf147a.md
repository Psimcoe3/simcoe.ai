[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetValidTypes Method

---



|  |
| --- |
| [Subelement Class](2d15bb45-70af-5f84-e899-322742591251.htm)   [See Also](#seeAlsoToggle) |

Obtains a set of types that are valid for this subelement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public ISet<ElementId> GetValidTypes() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetValidTypes As ISet(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ISet<ElementId^>^ GetValidTypes() ``` |

#### Return Value

A set of element IDs of types that are valid for this subelement or an empty set if subelement cannot have type assigned.

# Remarks

A type is valid for a subelement if it can be assigned to the subelement.

# See Also

[Subelement Class](2d15bb45-70af-5f84-e899-322742591251.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)