[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasElevationProfile Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

Identifies if the wall has a sketched elevation profile.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool HasElevationProfile( 	Wall pVWall ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function HasElevationProfile ( _ 	pVWall As Wall _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool HasElevationProfile( 	Wall^ pVWall ) ``` |

#### Parameters

pVWall
:   Type:  [Autodesk.Revit.DB Wall](b5891733-c602-12df-beab-da414b58d608.htm)    
     The wall.

#### Return Value

True if the wall has a sketch elevation profile, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)