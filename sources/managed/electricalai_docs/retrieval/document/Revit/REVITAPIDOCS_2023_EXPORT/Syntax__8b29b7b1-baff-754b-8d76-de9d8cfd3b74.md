[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HelpTopicUrl Property

---



|  |
| --- |
| [ContextualHelp Class](4126f1e6-8055-a42a-166d-511c4a794a8d.htm)   [See Also](#seeAlsoToggle) |

The help topic URL.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public string HelpTopicUrl { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property HelpTopicUrl As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ HelpTopicUrl { 	String^ get (); 	void set (String^ value); } ``` |

# Remarks

Applies only to objects of type ContextualHelpType.ChmFile. If empty or    a null reference (  Nothing  in Visual Basic)  , the default page of the help file will be displayed.   
 Obtain the URL by:

1. Open the chm file and go to the page you want to show.
2. Right click on the page, and choose the Properties command.
3. In the middle of properties page there is a property called: Address (URL). The end of the URL contains the topic URL used to open the help file to the correct page. Here is an example: mk:@MSITStore:C:\RevitAPI2013.chm::/WhatsNew.htm The help topic URL of this page is "WhatsNew.htm". Another example: mk:@MSITStore:C:\RevitAPI2013.chm::/html/329b02eb-5ee4-1715-2fbf-2cbbc0d3ff2a.htm The help topic URL of this page is "html/329b02eb-5ee4-1715-2fbf-2cbbc0d3ff2a.htm".

# See Also

[ContextualHelp Class](4126f1e6-8055-a42a-166d-511c4a794a8d.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)