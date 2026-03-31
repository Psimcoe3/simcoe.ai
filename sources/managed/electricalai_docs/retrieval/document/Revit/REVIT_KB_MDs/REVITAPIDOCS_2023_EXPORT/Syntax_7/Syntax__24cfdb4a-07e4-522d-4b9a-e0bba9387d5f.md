[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilySymbolFilter Class

---



|  |
| --- |
| [Members](9b253b91-7840-7fdc-50c2-68851ef70e36.htm)   [See Also](#seeAlsoToggle) |

A filter used to find all family symbols of the given family.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class FamilySymbolFilter : ElementQuickFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FamilySymbolFilter _ 	Inherits ElementQuickFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FamilySymbolFilter : public ElementQuickFilter ``` |

# Remarks

This filter is a quick filter. Quick filters operate only on the ElementRecord, a low-memory class which has a limited interface to read element properties. Elements which are rejected by a quick filter will not be expanded in memory.

Note that it may be faster to get a list of symbol ids from  [GetFamilySymbolIds](8989a269-c516-0ace-5365-864a61df1103.htm)  rather than to iterate all of the contents of a document with this filter applied.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  [Autodesk.Revit.DB ElementQuickFilter](ebc95d82-11fc-69f6-2df1-52331dd36443.htm)    
  Autodesk.Revit.DB FamilySymbolFilter

# See Also

[FamilySymbolFilter Members](9b253b91-7840-7fdc-50c2-68851ef70e36.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)