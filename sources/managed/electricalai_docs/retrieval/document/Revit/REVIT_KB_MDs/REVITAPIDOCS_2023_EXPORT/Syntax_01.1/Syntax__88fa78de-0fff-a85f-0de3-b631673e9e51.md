[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Cancel Method

---



|  |
| --- |
| [RevitAPIPreEventArgs Class](14097470-c9d9-0143-dc1b-b93a60a460e6.htm)   [See Also](#seeAlsoToggle) |

When the event is cancellable, may call the Cancel() method to cancel it.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void Cancel() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Cancel ``` |

 

| Visual C++ |
| --- |
| ``` public: void Cancel() ``` |

# Remarks

Not every event is cancellable. Whether or not an event may be cancelled is indicated by IsCancellable() method.

# See Also

[RevitAPIPreEventArgs Class](14097470-c9d9-0143-dc1b-b93a60a460e6.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)