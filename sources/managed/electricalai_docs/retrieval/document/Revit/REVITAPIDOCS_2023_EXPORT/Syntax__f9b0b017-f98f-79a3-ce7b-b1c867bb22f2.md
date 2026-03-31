[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PerformanceAdviser Class

---



|  |
| --- |
| [Members](91ed9cc8-d8d9-4a68-b141-23fdc0072853.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

The tool to report performance problems in a given document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class PerformanceAdviser : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class PerformanceAdviser _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class PerformanceAdviser : IDisposable ``` |

# Remarks

Class is an application-wide singleton that performs a dual role: it is a repository of rules to run in order to detect potential performance problems as well as an access point to execute checks.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
//Get the name of each registered PerformanceRule and then execute all of them.
foreach (PerformanceAdviserRuleId id in PerformanceAdviser.GetPerformanceAdviser().GetAllRuleIds())
{
    string ruleName = PerformanceAdviser.GetPerformanceAdviser().GetRuleName(id);
}
PerformanceAdviser.GetPerformanceAdviser().ExecuteAllRules(document);
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
'Get the name of each registered PerformanceRule and then execute all of them.
For Each id As PerformanceAdviserRuleId In PerformanceAdviser.GetPerformanceAdviser().GetAllRuleIds()
    Dim ruleName As String = PerformanceAdviser.GetPerformanceAdviser().GetRuleName(id)
Next
PerformanceAdviser.GetPerformanceAdviser().ExecuteAllRules(document)
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB PerformanceAdviser

# See Also

[PerformanceAdviser Members](91ed9cc8-d8d9-4a68-b141-23fdc0072853.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)