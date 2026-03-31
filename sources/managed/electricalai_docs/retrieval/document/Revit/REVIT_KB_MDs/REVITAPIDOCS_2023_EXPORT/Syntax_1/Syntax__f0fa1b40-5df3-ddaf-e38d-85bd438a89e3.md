[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FailureMessageKey Class

---



|  |
| --- |
| [Members](842251c5-afcf-25aa-2a60-a08b9a8e0eac.htm)   [See Also](#seeAlsoToggle) |

A unique key assigned to each posted failure message

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class FailureMessageKey : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FailureMessageKey _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FailureMessageKey : IDisposable ``` |

# Remarks

When a failure message is posted, it gets a unique key assigned and returned to the caller. The key is guaranteed to be unique in the Revit session. The key can be used to unpost (delete) previously posted failure message if it is no longer valid.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB FailureMessageKey

# See Also

[FailureMessageKey Members](842251c5-afcf-25aa-2a60-a08b9a8e0eac.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)