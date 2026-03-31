[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateTransformed Method

---



|  |
| --- |
| [Curve Class](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)   [See Also](#seeAlsoToggle) |

Crates a new instance of a curve as a transformation of this curve.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public Curve CreateTransformed( 	Transform transform ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CreateTransformed ( _ 	transform As Transform _ ) As Curve ``` |

 

| Visual C++ |
| --- |
| ``` public: Curve^ CreateTransformed( 	Transform^ transform ) ``` |

#### Parameters

transform
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     The transform to apply.

#### Return Value

The new curve.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | transform is not conformal. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was NULL |

# See Also

[Curve Class](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)