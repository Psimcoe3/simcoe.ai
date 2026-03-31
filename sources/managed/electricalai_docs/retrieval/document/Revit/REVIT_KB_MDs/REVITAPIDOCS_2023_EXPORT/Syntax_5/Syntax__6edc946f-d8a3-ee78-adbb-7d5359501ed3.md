[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetShapeId Method

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

Returns the id of the RebarShape element that defines the shape of the rebar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2009

# Syntax

| C# |
| --- |
| ``` public ElementId GetShapeId() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetShapeId As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetShapeId() ``` |

# Remarks

A Free Form Rebar that has Workshop Instructions set to Bent is considered to have multiple shapes and this method will throw exception.

A Free Form Rebar that has Workshop Instructions set to Straight or a Shape Driven is considered to have only one shape and this method will return the id of that shape.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This Rebar is matched with multiple shapes. |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)