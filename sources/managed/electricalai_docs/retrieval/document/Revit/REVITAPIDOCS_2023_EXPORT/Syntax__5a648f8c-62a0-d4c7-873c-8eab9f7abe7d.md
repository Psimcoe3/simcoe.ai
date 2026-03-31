[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Export Method (View)

---



|  |
| --- |
| [CustomExporter Class](d2437433-9183-cbb1-1c67-dedd86db5b5a.htm)   [See Also](#seeAlsoToggle) |

Exports one 3D or 2D view

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void Export( 	View view ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Export ( _ 	view As View _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Export( 	View^ view ) ``` |

#### Parameters

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     An instance of the view to export

# Remarks

Note that the actual export process may differ depending on the type of export context used. For example, when the  [IModelExportContext](4309af43-f04e-4e42-2539-3fd1d64cdc6d.htm)  is used, Revit is likely to perform several rounds of traversing each view, which may result in invoking the OnViewBegin/OnViewEnd method multiple times for every one view. It is because Revit draws objects in several layers (model layer, annotation layer, etc.) and will traverse each layer individually. In the most common scenario the user will receive two invocations of OnViewBegin/OnViewEnd: In the first round, all model entities will be received, while in the second round all text annotation elements will be received, if any present in the given view.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The view is not exportable, such as a template view or wrong type view, for example. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The instance of IExportContext is not valid. -or- Rendering is currently not supported in the running instance of Revit. One reason for that to happen is that rendering and material libraries are not currently available. |

# See Also

[CustomExporter Class](d2437433-9183-cbb1-1c67-dedd86db5b5a.htm)

[Export Overload](da0f2a1b-6ba3-583b-9cb6-9dcef35951bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)