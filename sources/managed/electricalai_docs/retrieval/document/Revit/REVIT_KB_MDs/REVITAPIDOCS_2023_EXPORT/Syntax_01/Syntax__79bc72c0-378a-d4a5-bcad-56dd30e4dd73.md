[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddCurve Method

---



|  |
| --- |
| [WireframeBuilder Class](ae9e719b-5d13-45c5-22d8-49111edfcfc4.htm)   [See Also](#seeAlsoToggle) |

Add a curve to the shape representation stored in this WireframeBuilder.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void AddCurve( 	Curve GCurve ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddCurve ( _ 	GCurve As Curve _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddCurve( 	Curve^ GCurve ) ``` |

#### Parameters

GCurve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The curve to be added.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | GCurve is not acceptable for a wireframe shape representation. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[WireframeBuilder Class](ae9e719b-5d13-45c5-22d8-49111edfcfc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)