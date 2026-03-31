[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FooterText Property

---



|  |
| --- |
| [TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)   [See Also](#seeAlsoToggle) |

FooterText is used in the footer area of the task dialog.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public string FooterText { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FooterText As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ FooterText { 	String^ get (); 	void set (String^ value); } ``` |

# Remarks

HTML Hyperlink tags can be used when specifying Footertext. These will work like normal hyperlinks where clicking them will launch the default browser to the location specified. Revit special cases hyperlinks containing the single character '#' to indicate to launch Revit's contextual help for the dialog. The Topic passed for the contextul help takes the form H[id] where id is the Id for the task dialog.

# See Also

[TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)