[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VertexStream Class

---



|  |
| --- |
| [Members](fc0616b9-8da1-3ccf-3b29-5ddaccf95930.htm)   [See Also](#seeAlsoToggle) |

The base class for DirectContext3D vertex streams, which are used to write vertex data into buffers.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public class VertexStream : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class VertexStream _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class VertexStream : IDisposable ``` |

# Remarks

This base class cannot be used directly. Instead, a steam that is specific for each type of vertex must be used.

* Use  [VertexStreamPosition](b6576b22-59f1-5cd1-962c-d65f17c198fb.htm)  to insert  [VertexPosition](718e49aa-9e17-6f2d-2013-141b5cfeefdd.htm)  instances.
* Use  [VertexStreamPositionColored](588e57a7-b43e-50f0-47ba-11154cae9a24.htm)  to insert  [VertexPositionColored](f99deacd-3167-46ff-6abf-5d27bdbd2c6a.htm)  instances.
* Use  [VertexStreamPositionNormal](fc9b191e-cbd9-844c-0289-b58ccc19ac8b.htm)  to insert  [VertexPositionNormal](a40efda7-6e2f-a455-f65e-02b10b0bc1b4.htm)  instances.
* Use  [VertexStreamPositionNormalColored](2b52610e-fbc2-d983-d28c-6fd05a7a215e.htm)  to insert  [VertexPositionNormalColored](aa354e03-2b25-b5a4-5634-c3518518c0d3.htm)  instances.

The process of putting vertex data into a buffer involves using a stream-buffer pair as follows:

1. Map the vertex buffer.
2. Get a stream of the appropriate type from the buffer.
3. Add vertices of the same type to the stream. They will be written into the buffer that was used to create the stream.
4. Unmap the buffer.

As an alternative to using streams, it is possible to write data into a buffer using a handle to its mapped memory.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.DirectContext3D VertexStream    
  [Autodesk.Revit.DB.DirectContext3D VertexStreamPosition](b6576b22-59f1-5cd1-962c-d65f17c198fb.htm)    
  [Autodesk.Revit.DB.DirectContext3D VertexStreamPositionColored](588e57a7-b43e-50f0-47ba-11154cae9a24.htm)    
  [Autodesk.Revit.DB.DirectContext3D VertexStreamPositionNormal](fc9b191e-cbd9-844c-0289-b58ccc19ac8b.htm)    
  [Autodesk.Revit.DB.DirectContext3D VertexStreamPositionNormalColored](2b52610e-fbc2-d983-d28c-6fd05a7a215e.htm)

# See Also

[VertexStream Members](fc0616b9-8da1-3ccf-3b29-5ddaccf95930.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)