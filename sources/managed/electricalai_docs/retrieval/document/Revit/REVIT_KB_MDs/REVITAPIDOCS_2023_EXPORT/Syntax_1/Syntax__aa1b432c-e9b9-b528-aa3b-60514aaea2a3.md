[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MessageBoxShowingEventArgs Class

---



|  |
| --- |
| [Members](92846ad4-4c5e-bfd8-6f02-aa2e80f2b4ef.htm)   [See Also](#seeAlsoToggle) |

The event arguments used by the DialogBoxShowing event when a Windows message box is about to be displayed in Revit.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public class MessageBoxShowingEventArgs : DialogBoxShowingEventArgs ``` |

 

| Visual Basic |
| --- |
| ``` Public Class MessageBoxShowingEventArgs _ 	Inherits DialogBoxShowingEventArgs ``` |

 

| Visual C++ |
| --- |
| ``` public ref class MessageBoxShowingEventArgs : public DialogBoxShowingEventArgs ``` |

# Remarks

When the application receives this object, a simple message box is about to be displayed in Revit that requires user interaction. The OverrideResult function can be used to cause the dialog to be dismissed and return a desired result code.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System EventArgs](http://msdn2.microsoft.com/en-us/library/118wxtk3)    
  [Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPreEventArgs](14097470-c9d9-0143-dc1b-b93a60a460e6.htm)    
  [Autodesk.Revit.UI.Events DialogBoxShowingEventArgs](8b6b969f-45d2-5b90-ca6d-593348ddf8d4.htm)    
  Autodesk.Revit.UI.Events MessageBoxShowingEventArgs

# See Also

[MessageBoxShowingEventArgs Members](92846ad4-4c5e-bfd8-6f02-aa2e80f2b4ef.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)