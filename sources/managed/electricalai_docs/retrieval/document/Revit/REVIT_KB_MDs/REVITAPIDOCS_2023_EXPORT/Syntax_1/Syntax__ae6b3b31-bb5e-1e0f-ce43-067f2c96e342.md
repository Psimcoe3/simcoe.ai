[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAction Method

---



|  |
| --- |
| [DoubleClickOptions Class](910f7cb7-9027-ed13-8502-2bfb9c347aee.htm)   [See Also](#seeAlsoToggle) |

Returns the active user's desired action for a particular double-click target.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public DoubleClickAction GetAction( 	DoubleClickTarget target ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAction ( _ 	target As DoubleClickTarget _ ) As DoubleClickAction ``` |

 

| Visual C++ |
| --- |
| ``` public: DoubleClickAction GetAction( 	DoubleClickTarget target ) ``` |

#### Parameters

target
:   Type:  [Autodesk.Revit.UI DoubleClickTarget](65ef60c8-d523-b2d0-4d3a-b9f2f4266f38.htm)    
     The target to check.

#### Return Value

The user's desired action for the specified target.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[DoubleClickOptions Class](910f7cb7-9027-ed13-8502-2bfb9c347aee.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)