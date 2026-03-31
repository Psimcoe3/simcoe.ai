[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetDiagramSettings Method

---



|  |
| --- |
| [AnalysisDisplayStyle Class](927357e1-9874-8b73-72c8-ff2bb78bfa82.htm)   [See Also](#seeAlsoToggle) |

Set diagram settings object for the style.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void SetDiagramSettings( 	AnalysisDisplayDiagramSettings diagramSettings ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetDiagramSettings ( _ 	diagramSettings As AnalysisDisplayDiagramSettings _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetDiagramSettings( 	AnalysisDisplayDiagramSettings^ diagramSettings ) ``` |

#### Parameters

diagramSettings
:   Type:  [Autodesk.Revit.DB.Analysis AnalysisDisplayDiagramSettings](57e0c5ff-555c-7345-ac24-3592207a4d70.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | diagram settings were not created with the object. |

# See Also

[AnalysisDisplayStyle Class](927357e1-9874-8b73-72c8-ff2bb78bfa82.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)