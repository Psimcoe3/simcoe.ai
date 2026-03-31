[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementMulticlassFilter Class

---



|  |
| --- |
| [Members](e299ef73-413f-2484-caa4-9e98296e825d.htm)   [See Also](#seeAlsoToggle) |

A filter used to match elements by their class, where more than one class of element may be passed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class ElementMulticlassFilter : ElementQuickFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ElementMulticlassFilter _ 	Inherits ElementQuickFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ElementMulticlassFilter : public ElementQuickFilter ``` |

# Remarks

This filter is a quick filter. Quick filters operate only on the ElementRecord, a low-memory class which has a limited interface to read element properties. Elements which are rejected by a quick filter will not be expanded in memory.

Only elements whose class is an exact match to one of the input classes, or elements whose type is derived from the input class will pass the collector.

There is a small subset of Element subclasses in the API that are not supported by this filter. These classes exist in the API, but not in Revit's native object model, which means that this filter doesn't support them. In order to use a class filter to find elements of these types, it is necessary to use a higher level class and then process the results further to find elements matching only the subclass. For a list of subclasses affected by this restriction, consult the documentation for  [!:Autodesk::Revit::DB::ElementClassFilter]  .

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  [Autodesk.Revit.DB ElementQuickFilter](ebc95d82-11fc-69f6-2df1-52331dd36443.htm)    
  Autodesk.Revit.DB ElementMulticlassFilter

# See Also

[ElementMulticlassFilter Members](e299ef73-413f-2484-caa4-9e98296e825d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)