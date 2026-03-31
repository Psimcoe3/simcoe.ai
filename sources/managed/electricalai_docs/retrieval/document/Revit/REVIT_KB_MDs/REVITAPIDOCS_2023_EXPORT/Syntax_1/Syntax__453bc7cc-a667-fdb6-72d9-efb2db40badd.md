[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidConceptualConstructionTypeElement Method

---



|  |
| --- |
| [MassLevelData Class](c1e62aaf-b7af-ad0c-60d5-4a1a9c1bed79.htm)   [See Also](#seeAlsoToggle) |

Checks if the ElementId is an acceptable conceptual construction type ElementId for the MassLevelData (Mass Floor).

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool IsValidConceptualConstructionTypeElement( 	ElementId id ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidConceptualConstructionTypeElement ( _ 	id As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidConceptualConstructionTypeElement( 	ElementId^ id ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ElementId to be checked.

#### Return Value

True if the ElementId is an acceptable conceptual construction type ElementId, false otherwise.

# Remarks

In the case that 'conceptualConstructionIsByEnergyData' is true, invalidElementId is also acceptable input.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MassLevelData Class](c1e62aaf-b7af-ad0c-60d5-4a1a9c1bed79.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)