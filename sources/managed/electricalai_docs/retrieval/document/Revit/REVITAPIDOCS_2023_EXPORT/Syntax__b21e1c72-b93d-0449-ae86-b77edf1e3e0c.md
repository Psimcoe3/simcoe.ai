[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreatePointCloudAccess Method

---



|  |
| --- |
| [IPointCloudEngine Interface](c444fe12-e214-eac3-e934-bd3aa84b70ca.htm)   [See Also](#seeAlsoToggle) |

Implement this method to construct the IPointCloudAccess interface for the point cloud designated by the identifier. This method is called once during the creation of a PointCloudType.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` IPointCloudAccess CreatePointCloudAccess( 	string identifier ) ``` |

 

| Visual Basic |
| --- |
| ``` Function CreatePointCloudAccess ( _ 	identifier As String _ ) As IPointCloudAccess ``` |

 

| Visual C++ |
| --- |
| ``` IPointCloudAccess^ CreatePointCloudAccess( 	String^ identifier ) ``` |

#### Parameters

identifier
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     An identifier unique to the point cloud. This will be a file name if the engine was registered as file-based, or an arbitrary identifier if the engine is not file-based.

#### Return Value

The object that can be used to create iterators and interrogate the point cloud for its features.

# Remarks

The instance of the returned IPointCloudAccess is then used by Revit to display instances of the point cloud in Revit graphics and in the user interface.

# See Also

[IPointCloudEngine Interface](c444fe12-e214-eac3-e934-bd3aa84b70ca.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)