[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetSketchyLines Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Sets the sketchy lines settings for the view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void SetSketchyLines( 	ViewDisplaySketchyLines sketchyLines ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetSketchyLines ( _ 	sketchyLines As ViewDisplaySketchyLines _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetSketchyLines( 	ViewDisplaySketchyLines^ sketchyLines ) ``` |

#### Parameters

sketchyLines
:   Type:  [Autodesk.Revit.DB ViewDisplaySketchyLines](c92b463b-1b59-695d-f06b-a76dacfaf2f0.htm)    
     Sketchy Lines settings to set.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This view does not contain display-related properties. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)