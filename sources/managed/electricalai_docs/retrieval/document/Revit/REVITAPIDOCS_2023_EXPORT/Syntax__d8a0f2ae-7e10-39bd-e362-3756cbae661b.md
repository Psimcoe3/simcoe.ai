[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SharedParameterElement Class

---



|  |
| --- |
| [Members](c6280bdf-81ea-5a41-07ad-b93092b5a470.htm)   [See Also](#seeAlsoToggle) |

An element that stores the definition of a shared parameter which is loaded into the document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public class SharedParameterElement : ParameterElement ``` |

 

| Visual Basic |
| --- |
| ``` Public Class SharedParameterElement _ 	Inherits ParameterElement ``` |

 

| Visual C++ |
| --- |
| ``` public ref class SharedParameterElement : public ParameterElement ``` |

# Remarks

Shared parameters are user-defined parameters that can be shared by multiple Revit documents. A shared parameter is identified by a GUID. Basic information of the shared parameter are accessed through GetDefinition().

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ParameterElement](2ad60b36-07d6-6aed-62c7-89f388f05ffb.htm)    
  Autodesk.Revit.DB SharedParameterElement

# See Also

[SharedParameterElement Members](c6280bdf-81ea-5a41-07ad-b93092b5a470.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)