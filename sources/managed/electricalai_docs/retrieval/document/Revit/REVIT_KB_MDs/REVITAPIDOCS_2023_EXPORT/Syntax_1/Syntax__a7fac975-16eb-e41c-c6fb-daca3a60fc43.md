[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsViewIdValidForPreview Method

---



|  |
| --- |
| [DocumentPreviewSettings Class](e38ea350-9951-ee05-5e3d-ab7f31815fb3.htm)   [See Also](#seeAlsoToggle) |

Identifies if the view id is valid as a preview view id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool IsViewIdValidForPreview( 	ElementId viewId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsViewIdValidForPreview ( _ 	viewId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsViewIdValidForPreview( 	ElementId^ viewId ) ``` |

#### Parameters

viewId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The view id.

#### Return Value

True if the view id is valid for preview, false otherwise.

# Remarks

Only graphical views (3d or 2d) are valid for use as a preview view. Other views (such as view templates) will not pass this method. InvalidElementId is accepted by this method as this id means that no special view is set for the preview.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DocumentPreviewSettings Class](e38ea350-9951-ee05-5e3d-ab7f31815fb3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)