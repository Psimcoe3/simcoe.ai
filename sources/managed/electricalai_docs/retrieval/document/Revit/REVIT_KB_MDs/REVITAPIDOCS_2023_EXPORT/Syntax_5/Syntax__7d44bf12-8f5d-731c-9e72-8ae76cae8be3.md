[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetPipeSlopes Method

---



|  |
| --- |
| [PipeSettings Class](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.htm)   [See Also](#seeAlsoToggle) |

Set pipe slope values.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void SetPipeSlopes( 	IList<double> slopes ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetPipeSlopes ( _ 	slopes As IList(Of Double) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetPipeSlopes( 	IList<double>^ slopes ) ``` |

#### Parameters

slopes
:   Type:  System.Collections.Generic IList   Double    
     Pipe slope values. Revit stores the slope value as a percentage (0-100).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Each value of the slopes must be between 0 and 100. Slope value is stored in percentage. e.g. 100 means 100%, and it is 45 degree. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This operation failed. |

# See Also

[PipeSettings Class](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)