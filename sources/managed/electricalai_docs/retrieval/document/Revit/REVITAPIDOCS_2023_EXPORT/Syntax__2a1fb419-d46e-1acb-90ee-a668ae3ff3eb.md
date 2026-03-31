[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [PointCloudType Class](b7ba9b9c-fd96-7506-1585-6fc2b327e0e9.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new point cloud type for a given point cloud engine.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static PointCloudType Create( 	Document document, 	string engineIdentifier, 	string typeIdentifier ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	engineIdentifier As String, _ 	typeIdentifier As String _ ) As PointCloudType ``` |

 

| Visual C++ |
| --- |
| ``` public: static PointCloudType^ Create( 	Document^ document,  	String^ engineIdentifier,  	String^ typeIdentifier ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which to create the point cloud.

engineIdentifier
:   Type:  System String    
     The string identifying the engine to be invoked. It should be the file extension or engine identifier registered by the third party.

typeIdentifier
:   Type:  System String    
     The file name or the identification string for a non-file based engine.

#### Return Value

The newly created PointCloudType object to be used to create instances of this point cloud.

# Remarks

A list of supported engine identifiers and whether they are file-based or not can be obtained from PointCloudEngineRegistry. The method GetSupportedEngines() returns a list of the identifiers registered for engines.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private PointCloudInstance CreatePointCloud(Document doc)
{
    PointCloudType type = PointCloudType.Create(doc, "rcs", "c:\\32_cafeteria.rcs");
    return (PointCloudInstance.Create(doc, type.Id, Transform.Identity));
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Function CreatePointCloud(doc As Document) As PointCloudInstance
    Dim type As PointCloudType = PointCloudType.Create(doc, "rcs", "c:\32_cafeteria.rcs")
    Return (PointCloudInstance.Create(doc, type.Id, Transform.Identity))
End Function
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The engine identifier was not found in the Revit session. -or- document is not a project document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions FileNotFoundException](73250198-dbc6-e760-4297-ec062f00f574.htm) | The external file could not be found or loaded. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Unable to create a point cloud from the third party engine. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[PointCloudType Class](b7ba9b9c-fd96-7506-1585-6fc2b327e0e9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)