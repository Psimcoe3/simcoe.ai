[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetDefaultLengthUnit Method

---



|  |
| --- |
| [ShapeImporter Class](d6120e08-f260-577d-b6cf-3fe5b042a54e.htm)   [See Also](#seeAlsoToggle) |

Sets the length unit to be used when the input is a unitless SAT file.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2017\_subscription\_update

# Syntax

| C# |
| --- |
| ``` public ShapeImporter SetDefaultLengthUnit( 	ImportUnit defaultLengthUnit ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetDefaultLengthUnit ( _ 	defaultLengthUnit As ImportUnit _ ) As ShapeImporter ``` |

 

| Visual C++ |
| --- |
| ``` public: ShapeImporter^ SetDefaultLengthUnit( 	ImportUnit defaultLengthUnit ) ``` |

#### Parameters

defaultLengthUnit
:   Type:  [Autodesk.Revit.DB ImportUnit](7801f4fd-83aa-65b4-5cd9-d3564d48f147.htm)    
     The length unit to be used for when the input is a unitless SAT file.

# Remarks

Values ImportUnit::Default and ImportUnit::Custom are ignored. ImportUnit::Centimeter is used instead.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ShapeImporter Class](d6120e08-f260-577d-b6cf-3fe5b042a54e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)