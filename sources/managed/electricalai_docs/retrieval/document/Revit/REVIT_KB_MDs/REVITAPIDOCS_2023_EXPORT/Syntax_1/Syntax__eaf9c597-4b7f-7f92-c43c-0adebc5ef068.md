[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UpdateControl Method

---



|  |
| --- |
| [TemporaryGraphicsManager Class](1dd29f70-d381-fa60-8ffa-1076eac55ed7.htm)   [See Also](#seeAlsoToggle) |

Updates the in-canvas control identified by the unique index.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void UpdateControl( 	int index, 	InCanvasControlData data ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub UpdateControl ( _ 	index As Integer, _ 	data As InCanvasControlData _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void UpdateControl( 	int index,  	InCanvasControlData^ data ) ``` |

#### Parameters

index
:   Type:  System Int32    
     Unique index of the control to be updated.

data
:   Type:  [Autodesk.Revit.DB InCanvasControlData](5fdf010d-7dbb-332d-4704-8e067f2338dc.htm)    
     data to generate in-canvas control appearance.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | index is out of range of TemporaryGraphicsManager managed objects, or the indexed object has been removed from the document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Failed to load the image from specified path. |

# See Also

[TemporaryGraphicsManager Class](1dd29f70-d381-fa60-8ffa-1076eac55ed7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)