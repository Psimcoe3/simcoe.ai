[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetByMassSubCategoryId Method

---



|  |
| --- |
| [ConceptualSurfaceType Class](b79ddf97-2888-ceda-a2c4-222dab08163e.htm)   [See Also](#seeAlsoToggle) |

Get the ConceptualSurfaceType by its mass subcategory id.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static ConceptualSurfaceType GetByMassSubCategoryId( 	Document cda, 	ElementId massSubCategoryId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetByMassSubCategoryId ( _ 	cda As Document, _ 	massSubCategoryId As ElementId _ ) As ConceptualSurfaceType ``` |

 

| Visual C++ |
| --- |
| ``` public: static ConceptualSurfaceType^ GetByMassSubCategoryId( 	Document^ cda,  	ElementId^ massSubCategoryId ) ``` |

#### Parameters

cda
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

massSubCategoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The mass subcategory id to get the ConceptualSurfaceType for.

#### Return Value

Returns ConceptualSurfaceType associated with input id or NULL.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The mass sub-category is none of the OST\_MassInteriorWall, OST\_MassExteriorWall, OST\_MassExteriorWallUnderground, OST\_MassRoof, OST\_MassFloor, OST\_MassSlab, OST\_MassShade, OST\_MassGlazing, OST\_MassSkylights, or OST\_MassOpening. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ConceptualSurfaceType Class](b79ddf97-2888-ceda-a2c4-222dab08163e.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)