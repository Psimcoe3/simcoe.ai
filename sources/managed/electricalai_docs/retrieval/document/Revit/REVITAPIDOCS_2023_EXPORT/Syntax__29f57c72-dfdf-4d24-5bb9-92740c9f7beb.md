[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RevitLinkOperations Class

---



|  |
| --- |
| [Members](442149fc-b0d0-c839-9d7a-07ba46c198de.htm)   [See Also](#seeAlsoToggle) |

This class is used to extend the IExternalResourceServer interface with methods to support operations specifically related to Revit links.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public class RevitLinkOperations : LinkOperations ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RevitLinkOperations _ 	Inherits LinkOperations ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RevitLinkOperations : public LinkOperations ``` |

# Remarks

The class owns single-method interfaces which are used as callbacks to perform specific operations on Revit link external resources.

An empty RevitLinkOperations instance is passed to an IExternalResourceServer (inside an ExternalResourceServerExtensions object) via the GetTypeSpecificServerOperations method. The server provider can then add their own implemented interface objects to the RevitLinkOperations, thus making them available to Revit to use as callbacks.

Supporting these additional, type-specific operations is not absolutely required, but is strongly recommended in order for users to be able to perform all the same operations they would with locally-accessed Revit links.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB LinkOperations](882834db-0bdc-4a40-ac75-4135d27bfb46.htm)    
  Autodesk.Revit.DB RevitLinkOperations

# See Also

[RevitLinkOperations Members](442149fc-b0d0-c839-9d7a-07ba46c198de.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)