[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FieldValues Constructor (IList(VectorAtPoint))

---



|  |
| --- |
| [FieldValues Class](728c3aac-0a10-027d-95e5-eb08665561a6.htm)   [See Also](#seeAlsoToggle) |

Creates object from an array of domain point vectors

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public FieldValues( 	IList<VectorAtPoint> vectorAtPoint ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	vectorAtPoint As IList(Of VectorAtPoint) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: FieldValues( 	IList<VectorAtPoint^>^ vectorAtPoint ) ``` |

#### Parameters

vectorAtPoint
:   Type:  System.Collections.Generic IList   [VectorAtPoint](fcda8b78-e0a7-d99f-6e4e-e53e3e26fc8c.htm)    
     Array of vectors, each corresponding to a domain point

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Members of vectorAtPoint contain different numbers of measurements |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FieldValues Class](728c3aac-0a10-027d-95e5-eb08665561a6.htm)

[FieldValues Overload](fa39b62a-a785-2fcc-fafe-53e60a88b1a0.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)