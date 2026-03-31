[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsSynchronizedWithCurrentItem Property

---



|  |
| --- |
| [SplitButton Class](5301a4c6-ba0f-1f66-61c3-8d0909ab0fe6.htm)   [See Also](#seeAlsoToggle) |

Indicates whether the top PushButton on the SplitButton changes based on the CurrentButton property.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool IsSynchronizedWithCurrentItem { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IsSynchronizedWithCurrentItem As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsSynchronizedWithCurrentItem { 	bool get (); 	void set (bool value); } ``` |

# Remarks

If this property is true the SplitButton uses the current PushButton's properties to display the image, text, tooltip, etc. and executes the current item when clicked. If it is false the first listed PushButton in the GetItems() return is shown, and executes this PushButton when clicked. If it is false the items in drop down list can only be executed by opening the drop down list and clicking an item in the list. The default value is true.

# See Also

[SplitButton Class](5301a4c6-ba0f-1f66-61c3-8d0909ab0fe6.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)