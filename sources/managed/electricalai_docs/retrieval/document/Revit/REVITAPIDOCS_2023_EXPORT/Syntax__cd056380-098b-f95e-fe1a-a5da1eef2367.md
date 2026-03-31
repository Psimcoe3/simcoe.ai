[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddItems Method

---



|  |
| --- |
| [RadioButtonGroup Class](ab5af3a0-2a19-603c-57c6-f28dd78c5f9c.htm)   [See Also](#seeAlsoToggle) |

Adds new ToggleButtons to the RadioButtonGroup.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public IList<ToggleButton> AddItems( 	IList<ToggleButtonData> buttonData ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddItems ( _ 	buttonData As IList(Of ToggleButtonData) _ ) As IList(Of ToggleButton) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ToggleButton^>^ AddItems( 	IList<ToggleButtonData^>^ buttonData ) ``` |

#### Parameters

buttonData
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [ToggleButtonData](ca92168b-f675-ce48-f1e3-fd5640762ad8.htm)    
     A list of objects containing the data needed to construct the ToggleButtons.

#### Return Value

The newly added ToggleButtons.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when buttonData is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when button with buttonData.Name already exists in the group. |

# See Also

[RadioButtonGroup Class](ab5af3a0-2a19-603c-57c6-f28dd78c5f9c.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)