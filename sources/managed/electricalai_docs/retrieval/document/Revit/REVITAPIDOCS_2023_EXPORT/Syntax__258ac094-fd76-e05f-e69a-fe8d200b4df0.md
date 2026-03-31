[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBuildingConstructionOverride Method

---



|  |
| --- |
| [MEPBuildingConstruction Class](3468e6dd-c676-cf39-b851-052b3e3a2f95.htm)   [See Also](#seeAlsoToggle) |

Gets the Building Construction override for a ConstructionType.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool GetBuildingConstructionOverride( 	ConstructionType constructionType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBuildingConstructionOverride ( _ 	constructionType As ConstructionType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool GetBuildingConstructionOverride( 	ConstructionType constructionType ) ``` |

#### Parameters

constructionType
:   Type:  [Autodesk.Revit.DB.Analysis ConstructionType](5f6be035-3a2d-77ad-8402-4d6b87dec818.htm)    
     The ConstructionType override value to get.

#### Return Value

True if analytical construction properties specified in Constructions.xml are used for the given ConstructionType, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The ConstructionType is invalid. |

# See Also

[MEPBuildingConstruction Class](3468e6dd-c676-cf39-b851-052b3e3a2f95.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)