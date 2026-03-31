[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SketchId Property

---



|  |
| --- |
| [AnalyticalSurfaceBase Class](9cad2b9c-a5d2-f434-2d9a-3c9183a55ada.htm)   [See Also](#seeAlsoToggle) |

Sketch associated to this Revit element.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public ElementId SketchId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property SketchId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ SketchId { 	ElementId^ get (); } ``` |

# Remarks

Analytical Element may not have a valid sketch. To edit the sketch profile you can use  [SetOuterContour(CurveLoop)](800767fc-e58e-1992-3505-ee1ca45717f0.htm)  or  [!:Autodesk::Revit::DB::SketchEditScope]  .

# See Also

[AnalyticalSurfaceBase Class](9cad2b9c-a5d2-f434-2d9a-3c9183a55ada.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)