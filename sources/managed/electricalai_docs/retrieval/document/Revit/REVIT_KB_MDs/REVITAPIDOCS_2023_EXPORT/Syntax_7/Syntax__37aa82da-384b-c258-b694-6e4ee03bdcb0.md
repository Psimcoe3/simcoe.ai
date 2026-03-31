[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ItemText Property

---



|  |
| --- |
| [RibbonItem Class](79225f03-1633-3722-15b0-752c91a3740d.htm)   [See Also](#seeAlsoToggle) |

Gets or sets the text displayed on the item.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual string ItemText { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Property ItemText As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property String^ ItemText { 	String^ get (); 	void set (String^ value); } ``` |

# Remarks

The text can be changed at run time.    a null reference (  Nothing  in Visual Basic)  or empty string is not allowed.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when setting the text to empty or to the string contains "%". |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when setting the text to    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[RibbonItem Class](79225f03-1633-3722-15b0-752c91a3740d.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)