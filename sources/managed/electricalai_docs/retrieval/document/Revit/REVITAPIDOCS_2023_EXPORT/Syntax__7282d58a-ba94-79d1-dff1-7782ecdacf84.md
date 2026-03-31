[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsAvailable Method

---



|  |
| --- |
| [DrawContext Class](b9244325-08c8-8bbd-a9f3-5d91d638d85d.htm)   [See Also](#seeAlsoToggle) |

Checks whether the facilities of this class are available for use in the current scope.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static bool IsAvailable() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsAvailable As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsAvailable() ``` |

#### Return Value

True if the DrawContext is available for rendering, false otherwise.

# Remarks

This class can perform drawing operations and access the state of parameters related to drawing only in lock-step with rendering inside of Revit. As a consequence, the facilities of this class are not available for use outside of the scope determined by the callback  [RenderScene(View, DisplayStyle)](d8e515cc-5b81-e835-5d60-5b409e0706d8.htm)  . Certain methods of other DirectContext3D objects, e.g., VertexBuffer::Map() are similarly restricted by the same scope.

# See Also

[DrawContext Class](b9244325-08c8-8bbd-a9f3-5d91d638d85d.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)