[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TemporaryGraphicsManager Class

---



|  |
| --- |
| [Members](c309a69d-ffb1-8705-2585-7fb47223c53d.htm)   [See Also](#seeAlsoToggle) |

A class that provides functionality to create temporary graphics in a Revit model.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public class TemporaryGraphicsManager : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class TemporaryGraphicsManager _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class TemporaryGraphicsManager : IDisposable ``` |

# Remarks

The graphics created by this class are temporary or transient. They are not subject to undo and are not saved. It's caller's responsiblity to manage their lifetime, creation and destruction, though Revit will destroy all of them when closing the model.

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB TemporaryGraphicsManager

# See Also

[TemporaryGraphicsManager Members](c309a69d-ffb1-8705-2585-7fb47223c53d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)