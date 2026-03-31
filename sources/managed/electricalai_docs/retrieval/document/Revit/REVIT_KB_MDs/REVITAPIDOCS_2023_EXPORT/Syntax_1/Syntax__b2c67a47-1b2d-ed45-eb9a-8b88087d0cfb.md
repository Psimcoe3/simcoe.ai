[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ComputeDrivingCurves Method

---



|  |
| --- |
| [RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)   [See Also](#seeAlsoToggle) |

Compute the driving curves.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public IList<Curve> ComputeDrivingCurves() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ComputeDrivingCurves As IList(Of Curve) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Curve^>^ ComputeDrivingCurves() ``` |

#### Return Value

Returns an empty array if an error is encountered.

# Remarks

The driving curves are the ones that appear in rebar sketch mode. They include lines and arcs that drive the shape, but exclude fillets and hooks. They always lie in a plane-- if the bar is 3D, these curves are a subset or a projection. They are also used for shape matching.

# See Also

[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)