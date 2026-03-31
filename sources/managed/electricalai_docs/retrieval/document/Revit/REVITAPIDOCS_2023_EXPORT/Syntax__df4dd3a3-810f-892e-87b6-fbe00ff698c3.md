[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### As3DCurveInXYPlane Method

---



|  |
| --- |
| [CurveUV Class](2d1d9c1f-afb6-fc09-f461-54cf0d511bf0.htm)   [See Also](#seeAlsoToggle) |

Returns a 3D curve lying in the XY plane in XYZ coordinates, representing the 2D curve with its UV coordinates identified with XY coordinates.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public Curve As3DCurveInXYPlane() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function As3DCurveInXYPlane As Curve ``` |

 

| Visual C++ |
| --- |
| ``` public: Curve^ As3DCurveInXYPlane() ``` |

#### Return Value

3D curve lying in the XY plane in XYZ coordinates, representing the 2D curve with its UV coordinates identified with XY coordinates.

# Remarks

Ideally, this function should only be used in cases when the 2D curve needs to be used in a context that does not support 2D curves, but can represent them as 3D curves with Z = 0 everywhere (for example, converting the 2D curve to another CAD system that does not support 2D curves).

# See Also

[CurveUV Class](2d1d9c1f-afb6-fc09-f461-54cf0d511bf0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)