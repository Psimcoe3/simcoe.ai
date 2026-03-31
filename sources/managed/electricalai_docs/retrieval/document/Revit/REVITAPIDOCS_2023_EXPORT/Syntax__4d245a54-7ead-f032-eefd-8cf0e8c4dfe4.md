[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddPoint Method

---



|  |
| --- |
| [IndexStreamPoint Class](b2ab0423-2e31-d5a2-ef70-197ca1bf9687.htm)   [See Also](#seeAlsoToggle) |

Inserts a  [IndexPoint](cd53f076-2011-ce3a-f92e-3b384f21b8ec.htm)  into the stream and associated buffer.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void AddPoint( 	IndexPoint point ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddPoint ( _ 	point As IndexPoint _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddPoint( 	IndexPoint^ point ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB.DirectContext3D IndexPoint](cd53f076-2011-ce3a-f92e-3b384f21b8ec.htm)    
     The point to be inserted.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if the associated buffer is not mapped. -or- Thrown if the associated buffer has insufficient space. |

# See Also

[IndexStreamPoint Class](b2ab0423-2e31-d5a2-ef70-197ca1bf9687.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)