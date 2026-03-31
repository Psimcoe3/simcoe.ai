[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSpatialElementBoundaryLocation Method

---



|  |
| --- |
| [AreaVolumeSettings Class](6282b3c9-3717-5c8f-7501-8a282244ce09.htm)   [See Also](#seeAlsoToggle) |

Gets the spatial element boundary location based on spatial element type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public SpatialElementBoundaryLocation GetSpatialElementBoundaryLocation( 	SpatialElementType spType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSpatialElementBoundaryLocation ( _ 	spType As SpatialElementType _ ) As SpatialElementBoundaryLocation ``` |

 

| Visual C++ |
| --- |
| ``` public: SpatialElementBoundaryLocation GetSpatialElementBoundaryLocation( 	SpatialElementType spType ) ``` |

#### Parameters

spType
:   Type:  [Autodesk.Revit.DB SpatialElementType](80080af1-a780-e983-a178-4fe889194275.htm)    
     The spatial element type.

#### Return Value

The boundary location.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[AreaVolumeSettings Class](6282b3c9-3717-5c8f-7501-8a282244ce09.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)