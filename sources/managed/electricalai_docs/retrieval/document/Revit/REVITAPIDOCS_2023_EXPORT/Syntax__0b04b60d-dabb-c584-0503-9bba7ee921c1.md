[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddVertex Method

---



|  |
| --- |
| [VertexStreamPositionNormal Class](fc9b191e-cbd9-844c-0289-b58ccc19ac8b.htm)   [See Also](#seeAlsoToggle) |

Inserts a  [VertexStreamPositionNormal](fc9b191e-cbd9-844c-0289-b58ccc19ac8b.htm)  into the stream and associated buffer.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void AddVertex( 	VertexPositionNormal vertex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddVertex ( _ 	vertex As VertexPositionNormal _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddVertex( 	VertexPositionNormal^ vertex ) ``` |

#### Parameters

vertex
:   Type:  [Autodesk.Revit.DB.DirectContext3D VertexPositionNormal](a40efda7-6e2f-a455-f65e-02b10b0bc1b4.htm)    
     The vertex to be inserted.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if the associated buffer is not mapped. -or- Thrown if the associated buffer has insufficient space. |

# See Also

[VertexStreamPositionNormal Class](fc9b191e-cbd9-844c-0289-b58ccc19ac8b.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)