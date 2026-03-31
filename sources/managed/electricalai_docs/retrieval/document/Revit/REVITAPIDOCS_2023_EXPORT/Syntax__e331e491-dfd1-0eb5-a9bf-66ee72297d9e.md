[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetWallConstructionType Method

---



|  |
| --- |
| [ConceptualConstructionType Class](59d96c60-67ae-cb70-d3a6-59e18a434eca.htm)   [See Also](#seeAlsoToggle) |

Get a Wall ConceptualConstructionType by its ConceptualConstructionWallType.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static ElementId GetWallConstructionType( 	Document ccda, 	ConceptualConstructionWallType typeEnum ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetWallConstructionType ( _ 	ccda As Document, _ 	typeEnum As ConceptualConstructionWallType _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ GetWallConstructionType( 	Document^ ccda,  	ConceptualConstructionWallType typeEnum ) ``` |

#### Parameters

ccda
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The Document.

typeEnum
:   Type:  [Autodesk.Revit.DB.Analysis ConceptualConstructionWallType](f02d8d2d-735a-30d3-2a94-5ca37d8c05d0.htm)    
     The ConceptualConstructionWallType to get the ConceptualConstructionType for.

#### Return Value

Returns ElementId of a ConceptualConstructionType.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The enum is invalid for ConceptualConstructionWallType. -or- A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ConceptualConstructionType Class](59d96c60-67ae-cb70-d3a6-59e18a434eca.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)