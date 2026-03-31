[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidType Method (ElementId)

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Checks if given type is valid for this element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool IsValidType( 	ElementId typeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidType ( _ 	typeId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidType( 	ElementId^ typeId ) ``` |

#### Parameters

typeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     ElementId of the type to check.

#### Return Value

True if element can have a type assigned and this type is valid for this element, false otherwise.

# Remarks

A type is valid for an element if it can be assigned to the element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[IsValidType Overload](40c3c3f4-3f80-1f2d-c831-a65400367a55.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)