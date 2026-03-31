[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsElementWithoutSketch Method

---



|  |
| --- |
| [SketchEditScope Class](8538b361-08df-9fd2-93bb-1790a09130f7.htm)   [See Also](#seeAlsoToggle) |

Validates if an element can have a sketch but currently does not.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public bool IsElementWithoutSketch( 	ElementId elementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsElementWithoutSketch ( _ 	elementId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsElementWithoutSketch( 	ElementId^ elementId ) ``` |

#### Parameters

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element id to be checked.

#### Return Value

True if the element doesn't have a sketch, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SketchEditScope Class](8538b361-08df-9fd2-93bb-1790a09130f7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)