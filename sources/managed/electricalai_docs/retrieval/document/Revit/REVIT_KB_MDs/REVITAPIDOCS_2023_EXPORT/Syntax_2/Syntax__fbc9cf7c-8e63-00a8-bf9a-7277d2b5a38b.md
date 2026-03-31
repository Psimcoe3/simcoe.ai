[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ActivateControlsAndDimensionsOnMultiSelect Property

---



|  |
| --- |
| [SelectionUIOptions Class](a87989f8-c37e-e5c6-7836-ff5014a66513.htm)   [See Also](#seeAlsoToggle) |

Indicates whether controls and temporary dimensions are activated on selection of multiple elements.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool ActivateControlsAndDimensionsOnMultiSelect { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ActivateControlsAndDimensionsOnMultiSelect As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool ActivateControlsAndDimensionsOnMultiSelect { 	bool get (); 	void set (bool value); } ``` |

# Remarks

Revit always shows certain controls and temporary dimensions for a single selected element When this option is set Revit also shows these controls and dimensions when multiple elements are selected. Note that this setting takes effect on the next selection change. To have this change take effect immediately use 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
Selection.SetElementIds(Selection.GetElementIds());
```

# See Also

[SelectionUIOptions Class](a87989f8-c37e-e5c6-7836-ff5014a66513.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)