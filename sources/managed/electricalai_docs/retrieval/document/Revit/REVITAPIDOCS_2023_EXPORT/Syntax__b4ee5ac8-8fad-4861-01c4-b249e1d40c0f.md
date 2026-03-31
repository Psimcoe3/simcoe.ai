[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetVertexStreamPositionNormalColored Method

---



|  |
| --- |
| [VertexBuffer Class](329e5617-ce46-a993-1131-85c64f0842f2.htm)   [See Also](#seeAlsoToggle) |

Gets a stream that can be used to write vertices of type  [VertexPositionNormalColored](aa354e03-2b25-b5a4-5634-c3518518c0d3.htm)  into the buffer.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public VertexStreamPositionNormalColored GetVertexStreamPositionNormalColored() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetVertexStreamPositionNormalColored As VertexStreamPositionNormalColored ``` |

 

| Visual C++ |
| --- |
| ``` public: VertexStreamPositionNormalColored^ GetVertexStreamPositionNormalColored() ``` |

#### Return Value

The stream that can be used to write into this buffer.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if the buffer is not mapped. -or- Thrown if the buffer has insufficient space. |

# See Also

[VertexBuffer Class](329e5617-ce46-a993-1131-85c64f0842f2.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)