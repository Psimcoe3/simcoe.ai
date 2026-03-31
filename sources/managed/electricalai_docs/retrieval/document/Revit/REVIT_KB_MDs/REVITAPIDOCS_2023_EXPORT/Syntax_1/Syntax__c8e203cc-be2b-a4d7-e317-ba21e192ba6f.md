[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MaterialType Property

---



|  |
| --- |
| [MassZone Class](da242463-3097-290a-9c10-afdf54d96649.htm)   [See Also](#seeAlsoToggle) |

Indicates how the material of MassZone faces is determined.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public MassZoneMaterialType MaterialType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MaterialType As MassZoneMaterialType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property MassZoneMaterialType MaterialType { 	MassZoneMaterialType get (); 	void set (MassZoneMaterialType value); } ``` |

# Remarks

The material of the MassZone faced will be determined in the following ways based on the material type. MassZoneMaterialTypeMaterialBySurfaceType: Each MassZone face will use the material defined by the object style of the subcategory of the Element returned by getMassDataElementIdForZoneFaceReference(..). MassZoneMaterialTypeNormalMaterial: If the materialId is InvalidElementId, then the material defined by the object style of the MassZone subcategory will be used for all faces of the MassZone. MassZoneMaterialTypeNormalMaterial: If the materialId is the id of a Material element, that material id will be used for all faces of the MassZone.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The material type does not fall within an appropriate range. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[MassZone Class](da242463-3097-290a-9c10-afdf54d96649.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)