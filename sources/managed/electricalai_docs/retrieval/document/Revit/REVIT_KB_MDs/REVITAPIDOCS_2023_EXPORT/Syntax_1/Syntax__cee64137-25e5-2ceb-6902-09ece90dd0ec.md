[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSystemsAnalysisWorkflows Method

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Returns name and path information identifying systems analysis workflow files.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public IDictionary<string, string> GetSystemsAnalysisWorkflows() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSystemsAnalysisWorkflows As IDictionary(Of String, String) ``` |

 

| Visual C++ |
| --- |
| ``` public: IDictionary<String^, String^>^ GetSystemsAnalysisWorkflows() ``` |

#### Return Value

The map of systems analysis workflows.

# Remarks

The map that is returned contains a key that is the name of the systems analysis workflow, and the value is the path to the workflow file.

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)