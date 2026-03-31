[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetOffset Method

---



|  |
| --- |
| [IPointCloudAccess Interface](d5e8d1d7-9375-ce6b-ff4f-6d4764c92736.htm)   [See Also](#seeAlsoToggle) |

Implement this method to return the offset stored in the point cloud.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` XYZ GetOffset() ``` |

 

| Visual Basic |
| --- |
| ``` Function GetOffset As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` XYZ^ GetOffset() ``` |

#### Return Value

The offset vector of this point cloud's coordinate system.

# Remarks

All points are assumed to be offset by the same offset vector. The offset should be expressed in the same units as used by the point coordinates (the scale conversion factor is not applied). The offset will be used by Revit if the user chooses to place an instance relative to another point cloud (the "Auto - Origin To Last Placed" placement option).

# See Also

[IPointCloudAccess Interface](d5e8d1d7-9375-ce6b-ff4f-6d4764c92736.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)