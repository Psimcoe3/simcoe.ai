[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetHookOrientationAngle Method

---



|  |
| --- |
| [RebarUpdateCurvesData Class](ff847aea-8397-8b79-b039-16a72e479c9f.htm)   [See Also](#seeAlsoToggle) |

Get the hook orientation angle at end that is currently in the rebar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public double GetHookOrientationAngle( 	int end ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetHookOrientationAngle ( _ 	end As Integer _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetHookOrientationAngle( 	int end ) ``` |

#### Parameters

end
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The end of bar. Should be 0 for start or 1 for end.

#### Return Value

The hook orientation angle at end that is currently in the rebar.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Invalid end. |

# See Also

[RebarUpdateCurvesData Class](ff847aea-8397-8b79-b039-16a72e479c9f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)