[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ArePhasesModifiable Method

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Returns true if the properties CreatedPhaseId and DemolishedPhaseId can be modified for this Element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool ArePhasesModifiable() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ArePhasesModifiable As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool ArePhasesModifiable() ``` |

#### Return Value

True if the properties CreatedPhaseId and DemolishedPhaseId can be modified for this Element, false otherwise.

# Remarks

Acts as a validator for setting the properties CreatedPhaseId and DemolishedPhaseId.

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)