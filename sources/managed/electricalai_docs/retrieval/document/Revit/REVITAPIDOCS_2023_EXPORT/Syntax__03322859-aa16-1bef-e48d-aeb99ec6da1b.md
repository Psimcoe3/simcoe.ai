[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MainInstruction Property

---



|  |
| --- |
| [TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)   [See Also](#seeAlsoToggle) |

The large primary text that appears at the top of a task dialog.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public string MainInstruction { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MainInstruction As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ MainInstruction { 	String^ get (); 	void set (String^ value); } ``` |

# Remarks

It should concisely sum up the problem or situation that is causing the message to display. Follow these guidelines:

* Every task dialog includes a main instruction.
* Text should not exceed three lines.
* Text should use plain language and be jargon free.
* Main instructions should be written in sentence format – normal capitalization and punctuation.
* Address the user directly as "you" when appropriate.
* When presented with multiple command link options the standard final line for the main instructions should be, "What do you want to do?"

Revit will automatically break lines to make the message fit well. "\n" also breaks down to the next line. For a paragraph break, use "\n\n".

Hyperlinks added to the main instructions will not be enabled when the dialog is shown on Vista.

# See Also

[TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)