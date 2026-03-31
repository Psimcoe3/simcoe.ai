[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeVertex Class

---



|  |
| --- |
| [Members](30cf472f-1274-300b-1727-997ee79bd169.htm)   [See Also](#seeAlsoToggle) |

A bend between segments of a rebar shape definition.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class RebarShapeVertex : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RebarShapeVertex _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RebarShapeVertex : IDisposable ``` |

# Remarks

A RebarShapeVertex is part of a RebarShapeDefinitionBySegments object. There is one vertex between each pair of adjacent segments, plus one at each end of the overall shape. The end vertices currently are ignored by the shape definition, even if they have constraints.

A bend may have the default radius of the bar type referenced by the Rebar element, or it may have a radius defined by a parameter.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.Structure RebarShapeVertex

# See Also

[RebarShapeVertex Members](30cf472f-1274-300b-1727-997ee79bd169.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)