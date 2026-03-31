[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LongDescription Property

---



|  |
| --- |
| [RibbonItemData Class](eb399d25-88cb-c3a1-c445-37077b3a5aa1.htm)   [See Also](#seeAlsoToggle) |

Long description of the command tooltip

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public string LongDescription { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LongDescription As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ LongDescription { 	String^ get (); 	void set (String^ value); } ``` |

# Remarks

It will be used as part of the button's extended tooltip. This tooltip is shown when the mouse hovers over the command for a long amount of time. You can split the text of this option into multiple paragraphs by placing <p> tags around each paragraph. Optional. If neither of this property and TooltipImage is supplied, the button will not have an extended tooltip. SplitButton and RadioButtonGroup cannot display the tooltip set by this method, the SplitButton will always show the current PushButton tooltip, and RadioButtonGroup has no tooltip.

# See Also

[RibbonItemData Class](eb399d25-88cb-c3a1-c445-37077b3a5aa1.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)