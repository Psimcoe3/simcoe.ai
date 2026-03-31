[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRequesters Method

---



|  |
| --- |
| [WorksharingTooltipInfo Class](64e2bf53-2787-6cb7-ac29-b73777892ed3.htm)   [See Also](#seeAlsoToggle) |

The ordered list of unique user names of users who have outstanding editing requests for the specified element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IList<string> GetRequesters() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRequesters As IList(Of String) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<String^>^ GetRequesters() ``` |

#### Return Value

The ordered list of unique user names.

# Remarks

The list is ordered by who placed the earliest request. If the list is empty it means that nobody is currently requesting the specified element.

# See Also

[WorksharingTooltipInfo Class](64e2bf53-2787-6cb7-ac29-b73777892ed3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)