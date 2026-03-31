[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetProjectionToSheetTransform Method

---



|  |
| --- |
| [Viewport Class](5991dc40-234a-4835-cc06-07524d2e61a4.htm)   [See Also](#seeAlsoToggle) |

Returns the transform from the view's projection space to the sheet space.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public Transform GetProjectionToSheetTransform() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetProjectionToSheetTransform As Transform ``` |

 

| Visual C++ |
| --- |
| ``` public: Transform^ GetProjectionToSheetTransform() ``` |

#### Return Value

The transform from the view's projection space to the sheet space.

# Remarks

This transform accounts for the position and rotation of a viewport on a sheet.

The transforms from the model space to the view projection space are returned by  [!:View.GetModelToProjectionTransforms()]  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The viewport is not on a sheet. -or- The viewport does not have transforms. |

# See Also

[Viewport Class](5991dc40-234a-4835-cc06-07524d2e61a4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)