[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsSourceElement Method

---



|  |
| --- |
| [PartMaker Class](ec5be0eb-bf10-0f05-83a4-77daa2cfb0fd.htm)   [See Also](#seeAlsoToggle) |

Is the element a source for this PartMaker

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool IsSourceElement( 	ElementId elemId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsSourceElement ( _ 	elemId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsSourceElement( 	ElementId^ elemId ) ``` |

#### Parameters

elemId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

#### Return Value

Returns true if elemId is among the source elements of this PartMaker

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartMaker Class](ec5be0eb-bf10-0f05-83a4-77daa2cfb0fd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)