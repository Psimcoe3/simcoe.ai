[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValid Method

---



|  |
| --- |
| [VertexBuffer Class](329e5617-ce46-a993-1131-85c64f0842f2.htm)   [See Also](#seeAlsoToggle) |

Tests whether the buffer is valid for rendering.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public bool IsValid() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValid As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValid() ``` |

#### Return Value

True if the buffer is valid for rendering, false otherwise.

# Remarks

The buffers are internally associated with low-level graphics state and may become invalidated when the state changes. Therefore, an application should test each buffer for validity before submitting its contents for rendering. If the buffer becomes invalid, the application should re-create its contents and write them to a new buffer.

# See Also

[VertexBuffer Class](329e5617-ce46-a993-1131-85c64f0842f2.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)