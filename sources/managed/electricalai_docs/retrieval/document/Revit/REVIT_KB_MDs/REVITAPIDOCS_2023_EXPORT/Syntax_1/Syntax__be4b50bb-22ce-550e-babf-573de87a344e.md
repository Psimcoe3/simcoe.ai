[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSpecificFittingAngles Method

---



|  |
| --- |
| [PipeSettings Class](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.htm)   [See Also](#seeAlsoToggle) |

Gets the list of specific fitting angles.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public IList<double> GetSpecificFittingAngles() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSpecificFittingAngles As IList(Of Double) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<double>^ GetSpecificFittingAngles() ``` |

#### Return Value

Angles (in degrees).

# Remarks

Revit will only use the angles specified during the pipe layout or modifying the pipe layout. When laying out the pipes, if the angle between two pipes is close to the allowed angle, the specific angle is used for that pipe fitting.

# See Also

[PipeSettings Class](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)