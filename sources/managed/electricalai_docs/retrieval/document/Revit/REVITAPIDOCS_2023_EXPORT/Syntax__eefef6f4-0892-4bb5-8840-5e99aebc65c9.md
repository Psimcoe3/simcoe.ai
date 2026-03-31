[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WorksetConfiguration Class

---



|  |
| --- |
| [Members](d3fa498f-5d2e-b5d0-5555-d373f289ebfc.htm)   [See Also](#seeAlsoToggle) |

A configuration class that is passed in to methods that open Revit documents to specify which user-created worksets are opened/closed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class WorksetConfiguration : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class WorksetConfiguration _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class WorksetConfiguration : IDisposable ``` |

# Remarks

Once an instance of this class is created, it can be further modified by calling any of the other methods in any order. It is a specification of a setting for model open; the methods of this class just adjust the specification, and do not themselves open or close worksets.

Only user-created worksets can be specified to be opened or closed. All system worksets are automatically open. An open workset allows its elements can be expanded and displayed. For a closed workset, Revit tries to not expand its elements, and to that end, does not display them. This is intended to help with performance by reducing Revit's memory footprint.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB WorksetConfiguration

# See Also

[WorksetConfiguration Members](d3fa498f-5d2e-b5d0-5555-d373f289ebfc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)