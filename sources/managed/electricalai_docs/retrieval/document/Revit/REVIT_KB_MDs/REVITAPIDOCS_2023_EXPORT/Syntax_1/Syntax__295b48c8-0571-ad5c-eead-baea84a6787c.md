[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UIDocument Class

---



|  |
| --- |
| [Members](11b32aa0-ad45-b2ed-d617-33b7ed027f73.htm)   [See Also](#seeAlsoToggle) |

An object that represents an Autodesk Revit project opened in the Revit user interface.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public class UIDocument : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class UIDocument _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class UIDocument : IDisposable ``` |

# Remarks

This class represents a document opened in the user interface and therefore offers interfaces to work with settings and operations in the UI (for example, the active selection). Revit can have multiple projects open and multiple views to those projects. The active or top most view will be the active project and hence the active document which is available from the UIApplication object.

Obtain the database level Document (which contains interfaces not related to the UI) via the Document property. If you have a database level Document and need to access it from the UI, you can construct a new UIDocument from that object (the document must be open and visible in the UI to allow the methods to work successfully).

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.UI UIDocument    
  [Autodesk.Revit.UI.Macros DocumentEntryPoint](35587825-07cb-c541-40d6-3c648cbb5d08.htm)

# See Also

[UIDocument Members](11b32aa0-ad45-b2ed-d617-33b7ed027f73.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)