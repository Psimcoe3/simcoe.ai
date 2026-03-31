[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CheckConstructionSetElement Method

---



|  |
| --- |
| [EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)   [See Also](#seeAlsoToggle) |

Checks that the construction set ElementId is acceptable.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool CheckConstructionSetElement( 	ElementId constructionSetElementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CheckConstructionSetElement ( _ 	constructionSetElementId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CheckConstructionSetElement( 	ElementId^ constructionSetElementId ) ``` |

#### Parameters

constructionSetElementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The construction set ElementId to be checked.

#### Return Value

True if the construction set ElementId is a valid construction set element, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)