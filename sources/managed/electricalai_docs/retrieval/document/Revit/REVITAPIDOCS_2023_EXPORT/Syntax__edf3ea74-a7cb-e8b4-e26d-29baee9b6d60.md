[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetEdgeNumber Method

---



|  |
| --- |
| [RebarConstrainedHandle Class](08b4c4a3-3bb9-0801-9cc8-cd5420a306d9.htm)   [See Also](#seeAlsoToggle) |

If the RebarConstrainedHandle's RebarHandleType is 'Edge', then this function will return the number of the edge that is driven by the handle.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public int GetEdgeNumber() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetEdgeNumber As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int GetEdgeNumber() ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | RebarConstrainedHandle is no longer valid. -or- The RebarConstrainedHandle is not of RebarHandleType 'Edge'. |

# See Also

[RebarConstrainedHandle Class](08b4c4a3-3bb9-0801-9cc8-cd5420a306d9.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)