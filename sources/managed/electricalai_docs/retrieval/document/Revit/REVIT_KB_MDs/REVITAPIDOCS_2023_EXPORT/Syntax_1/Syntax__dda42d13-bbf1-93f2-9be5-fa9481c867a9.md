[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetPointCloudRegionOverrideSettings Method (ElementId, PointCloudOverrideSettings, String, Document)

---



|  |
| --- |
| [PointCloudOverrides Class](c39d51e3-cc31-ecae-fa41-d00c435cb700.htm)   [See Also](#seeAlsoToggle) |

Assigns override settings to a particular region within a PointCloudInstance element.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetPointCloudRegionOverrideSettings( 	ElementId elementId, 	PointCloudOverrideSettings newSettings, 	string regionTag, 	Document doc ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetPointCloudRegionOverrideSettings ( _ 	elementId As ElementId, _ 	newSettings As PointCloudOverrideSettings, _ 	regionTag As String, _ 	doc As Document _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetPointCloudRegionOverrideSettings( 	ElementId^ elementId,  	PointCloudOverrideSettings^ newSettings,  	String^ regionTag,  	Document^ doc ) ``` |

#### Parameters

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of the element to be overridden.

newSettings
:   Type:  [Autodesk.Revit.DB.PointClouds PointCloudOverrideSettings](48196ce4-89a6-8f23-a82c-190f0113380d.htm)    
     Override settings to be assigned.

regionTag
:   Type:  System String    
     The tag identifying the particular region within the PointCloudInstance element. Tags can be obtained from PointCloudInstance via method getRegions.

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document containing the element to be overridden.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when supplied regionTag is not empty while doc is NULL |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The override settings are not valid. |

# See Also

[PointCloudOverrides Class](c39d51e3-cc31-ecae-fa41-d00c435cb700.htm)

[SetPointCloudRegionOverrideSettings Overload](c76cff6e-d5bc-36e7-4928-65da94519536.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)