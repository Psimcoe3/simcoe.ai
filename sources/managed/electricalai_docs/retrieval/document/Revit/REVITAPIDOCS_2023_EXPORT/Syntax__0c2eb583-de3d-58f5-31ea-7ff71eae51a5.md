[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MainContent Property

---



|  |
| --- |
| [TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)   [See Also](#seeAlsoToggle) |

MainContent is the smaller text that appears just below the main instructions.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public string MainContent { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MainContent As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ MainContent { 	String^ get (); 	void set (String^ value); } ``` |

# Remarks

The Main Content is optional. It should be used to give further explanation to the user, such as how to correct the problem or work around the situation. It displays in a smaller black font below the main instructions. Follow these guidelines:

* Text should be clear and jargon free.
* Main content should not simply restate the main instructions in a different way, they should contain additional information that builds upon or reinforces the main instructions.
* Main content should be written in sentence format (normal capitalization and punctuation).
* Address the user directly as "you" when needed.

# See Also

[TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)