[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFullGeometryForView Method

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

Generates full geometry for the Rebar for a specific view.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public GeometryElement GetFullGeometryForView( 	View view ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFullGeometryForView ( _ 	view As View _ ) As GeometryElement ``` |

 

| Visual C++ |
| --- |
| ``` public: GeometryElement^ GetFullGeometryForView( 	View^ view ) ``` |

#### Parameters

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view in which the geometry is generated.

#### Return Value

The generated geometry of the Rebar before cutting is applied.

# Remarks

The result of this method differs from Element.Geometry in that Element.Geometry will return the rebar geometry cut by the view extents (such as the section box). In this method the entire Rebar geometry is returned for the given view, before cutting.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)