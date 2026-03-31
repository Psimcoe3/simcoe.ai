[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPointCloudRegionOverrideSettings Method (ElementId)

---



|  |
| --- |
| [PointCloudOverrides Class](c39d51e3-cc31-ecae-fa41-d00c435cb700.htm)   [See Also](#seeAlsoToggle) |

Gets region override settings assigned to the whole PointCloudInstance element.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public PointCloudOverrideSettings GetPointCloudRegionOverrideSettings( 	ElementId elementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPointCloudRegionOverrideSettings ( _ 	elementId As ElementId _ ) As PointCloudOverrideSettings ``` |

 

| Visual C++ |
| --- |
| ``` public: PointCloudOverrideSettings^ GetPointCloudRegionOverrideSettings( 	ElementId^ elementId ) ``` |

#### Parameters

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of the overridden element.

#### Return Value

The override settings assigned to the element, if present, or a default override settings if nothing was found.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PointCloudOverrides Class](c39d51e3-cc31-ecae-fa41-d00c435cb700.htm)

[GetPointCloudRegionOverrideSettings Overload](93cbe2df-facc-dfb8-ef2b-26b637153c2c.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)