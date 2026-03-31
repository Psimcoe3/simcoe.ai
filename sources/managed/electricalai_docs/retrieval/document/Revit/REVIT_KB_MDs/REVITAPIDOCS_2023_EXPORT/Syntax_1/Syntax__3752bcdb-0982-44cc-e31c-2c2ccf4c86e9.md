[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAllConceptualConstructionsForCategory Method

---



|  |
| --- |
| [ConceptualConstructionType Class](59d96c60-67ae-cb70-d3a6-59e18a434eca.htm)   [See Also](#seeAlsoToggle) |

Get all the ids of constructions applicable to the input massSubCategory

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> GetAllConceptualConstructionsForCategory( 	Document ccda, 	ElementId massSubCategoryId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetAllConceptualConstructionsForCategory ( _ 	ccda As Document, _ 	massSubCategoryId As ElementId _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ GetAllConceptualConstructionsForCategory( 	Document^ ccda,  	ElementId^ massSubCategoryId ) ``` |

#### Parameters

ccda
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

massSubCategoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ElementId of the mass subcategory.

#### Return Value

Returns a set of ElementIds that for the ConceptualConstructionTypes that are appropriate for the subcategory.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The mass sub-category is none of the OST\_MassInteriorWall, OST\_MassExteriorWall, OST\_MassExteriorWallUnderground, OST\_MassWallsAll, OST\_MassRoof, OST\_MassFloor, OST\_MassSlab, OST\_MassFloorsAll, OST\_MassShade, OST\_MassGlazing, OST\_MassSkylights, OST\_MassGlazingAll or OST\_MassOpening. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ConceptualConstructionType Class](59d96c60-67ae-cb70-d3a6-59e18a434eca.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)