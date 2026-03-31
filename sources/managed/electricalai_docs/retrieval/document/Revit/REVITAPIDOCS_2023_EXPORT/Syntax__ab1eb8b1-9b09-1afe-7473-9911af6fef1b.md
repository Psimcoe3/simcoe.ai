[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ToolTipImage Property

---



|  |
| --- |
| [RibbonItemData Class](eb399d25-88cb-c3a1-c445-37077b3a5aa1.htm)   [See Also](#seeAlsoToggle) |

The image to show as a part of the button extended tooltip

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ImageSource ToolTipImage { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ToolTipImage As ImageSource 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ImageSource^ ToolTipImage { 	ImageSource^ get (); 	void set (ImageSource^ value); } ``` |

# Remarks

Shown when the cursor hovers over the command. If neither this property nor LongDescription is supplied, the button will not have an extended tooltip. Maximum height or width is 355 pixels. SplitButton and RadioButtonGroup cannot display the tooltip set by this method. SplitButton shows the current PushButton tooltip and RadioButtonGroup has no tooltip.

# See Also

[RibbonItemData Class](eb399d25-88cb-c3a1-c445-37077b3a5aa1.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)