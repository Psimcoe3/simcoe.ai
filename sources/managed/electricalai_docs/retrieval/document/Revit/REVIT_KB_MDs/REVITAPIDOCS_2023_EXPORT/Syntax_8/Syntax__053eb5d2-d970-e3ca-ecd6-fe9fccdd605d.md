[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetHtmlDescription Method

---



|  |
| --- |
| [IPipePlumbingFixtureFlowServer Interface](ef369072-84eb-cace-a564-335aed35626b.htm)   [See Also](#seeAlsoToggle) |

The method that Revit will invoke to get an HTML formatted description of the server.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` string GetHtmlDescription() ``` |

 

| Visual Basic |
| --- |
| ``` Function GetHtmlDescription As String ``` |

 

| Visual C++ |
| --- |
| ``` String^ GetHtmlDescription() ``` |

#### Return Value

The HTML format description of the server.

# Remarks

The HTML description is used by Revit unless it is empty or the server is not available, in which case, Revit will use the plain text description from IExternalServer.GetDescription().

# See Also

[IPipePlumbingFixtureFlowServer Interface](ef369072-84eb-cace-a564-335aed35626b.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)