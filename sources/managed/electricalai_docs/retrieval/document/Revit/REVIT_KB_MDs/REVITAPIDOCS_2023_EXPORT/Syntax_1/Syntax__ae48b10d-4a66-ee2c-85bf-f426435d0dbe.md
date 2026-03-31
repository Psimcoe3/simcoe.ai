[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsPhaseCreatedValid Method

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Returns true if createdPhaseId is an allowed value for the property CreatedPhaseId in this Element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool IsPhaseCreatedValid( 	ElementId createdPhaseId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsPhaseCreatedValid ( _ 	createdPhaseId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsPhaseCreatedValid( 	ElementId^ createdPhaseId ) ``` |

#### Parameters

createdPhaseId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of a Phase.

#### Return Value

True if createdPhaseId is an allowed value for the property CreatedPhaseId in this Element, false otherwise.

# Remarks

Acts as a validator for setting the property CreatedPhaseId.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)