[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreThinLinesEnabled Property

---



|  |
| --- |
| [ThinLinesOptions Class](1d348cae-3e60-f890-5262-da795d927ea4.htm)   [See Also](#seeAlsoToggle) |

A static property defining if the 'Thin Lines' setting is on or off in current Revit Application Session.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2015 Subscription Update

# Syntax

| C# |
| --- |
| ``` public static bool AreThinLinesEnabled { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Property AreThinLinesEnabled As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: static property bool AreThinLinesEnabled { 	bool get (); 	void set (bool value); } ``` |

# Remarks

If user started multiple Revit sessions, and the 'Thin Lines' setting might be different in each session. Revit.ini file stores the lastest setting no matter what the Revit session is. The setting will be writen to Revit.ini if user set the value.

# See Also

[ThinLinesOptions Class](1d348cae-3e60-f890-5262-da795d927ea4.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)