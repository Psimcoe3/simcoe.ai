[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetOrientation Method

---



|  |
| --- |
| [View3D Class](d795a238-fc24-1875-e64f-a2bef56ae949.htm)   [See Also](#seeAlsoToggle) |

Sets the temporary orientation of the View3D. The new orientation is not saved in the document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetOrientation( 	ViewOrientation3D newViewOrientation3D ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetOrientation ( _ 	newViewOrientation3D As ViewOrientation3D _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetOrientation( 	ViewOrientation3D^ newViewOrientation3D ) ``` |

#### Parameters

newViewOrientation3D
:   Type:  [Autodesk.Revit.DB ViewOrientation3D](027b44d6-a473-4e99-4b43-c938847ea7e3.htm)    
     The new orientation to set.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | View is locked and cannot be reoriented. |

# See Also

[View3D Class](d795a238-fc24-1875-e64f-a2bef56ae949.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)