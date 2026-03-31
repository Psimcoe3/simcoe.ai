[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Cancel Method

---



|  |
| --- |
| [ProgressChangedEventArgs Class](11e76066-82f3-21c7-6c1f-dfbbf0a1abd9.htm)   [See Also](#seeAlsoToggle) |

Requests to cancel the progress bar's operation.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void Cancel() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Cancel ``` |

 

| Visual C++ |
| --- |
| ``` public: void Cancel() ``` |

# Remarks

Note that an operation may only be cancelled if its stage is 'Unchanged' or if its stage is 'PositionChanged' and the 'Cancellable' property is 'true.'

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The operation cannot be cancelled. |

# See Also

[ProgressChangedEventArgs Class](11e76066-82f3-21c7-6c1f-dfbbf0a1abd9.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)