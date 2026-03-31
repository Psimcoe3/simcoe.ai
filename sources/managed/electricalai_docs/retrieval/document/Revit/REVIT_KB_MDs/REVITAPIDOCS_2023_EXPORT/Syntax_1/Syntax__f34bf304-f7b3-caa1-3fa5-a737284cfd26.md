[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsMain Method

---



|  |
| --- |
| [MEPSection Class](a618b793-4084-a631-191a-043aac84d039.htm)   [See Also](#seeAlsoToggle) |

Check whether the type of fitting in this section is main.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool IsMain( 	ElementId fittingId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsMain ( _ 	fittingId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsMain( 	ElementId^ fittingId ) ``` |

#### Parameters

fittingId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element id which can be duct fitting and pipe fitting.

#### Return Value

True if the type of fitting in this section is main False if the type of fitting in this section is branch

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The ElementId fittingId does not correspond to a valid section fitting member. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MEPSection Class](a618b793-4084-a631-191a-043aac84d039.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)