---
created: 2026-01-28T21:01:47 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Meshes_html
author: 
---

# Help | Meshes | Autodesk

> ## Excerpt
> A mesh is a collection of triangular boundaries which collectively forms a 3D shape. Meshes are typically encountered inside Revit element geometry if those elements were created from certain import operations and also are used in some native Revit elements such as TopographySurface. You can also obtain Meshes as the result of calls to Face.Triangulate() for any given Revit face. The property Mesh.IsClosed checks if each edge in the mesh belongs to at least two faces.

---
A mesh is a collection of triangular boundaries which collectively forms a 3D shape. Meshes are typically encountered inside Revit element geometry if those elements were created from certain import operations and also are used in some native Revit elements such as TopographySurface. You can also obtain Meshes as the result of calls to Face.Triangulate() for any given Revit face. The property `Mesh.IsClosed` checks if each edge in the mesh belongs to at least two faces.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/mesh.png)A mesh representing a torus

The following code sample illustrates how to get the geometry of a Revit face as a Mesh:

<table summary="" id="GUID-A4E51A50-60EF-4D49-9944-4935FA88CD11__TABLE_C299BDB28BE54C97B22ABA4BD31FC845"><tbody><tr><td><b>Code region: Extracting the geometry of a mesh</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetTrianglesFromFace</span><span>(</span><span>Face</span><span> face</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Get mesh</span><span>
        </span><span>Mesh</span><span> mesh </span><span>=</span><span> face</span><span>.</span><span>Triangulate</span><span>();</span><span>
        </span><span>for</span><span> </span><span>(</span><span>int</span><span> i </span><span>=</span><span> </span><span>0</span><span>;</span><span> i </span><span>&lt;</span><span> mesh</span><span>.</span><span>NumTriangles</span><span>;</span><span> i</span><span>++)</span><span>
        </span><span>{</span><span>
               </span><span>MeshTriangle</span><span> triangle </span><span>=</span><span> mesh</span><span>.</span><span>get_Triangle</span><span>(</span><span>i</span><span>);</span><span>
               XYZ vertex1 </span><span>=</span><span> triangle</span><span>.</span><span>get_Vertex</span><span>(</span><span>0</span><span>);</span><span>
               XYZ vertex2 </span><span>=</span><span> triangle</span><span>.</span><span>get_Vertex</span><span>(</span><span>1</span><span>);</span><span>
               XYZ vertex3 </span><span>=</span><span> triangle</span><span>.</span><span>get_Vertex</span><span>(</span><span>2</span><span>);</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: The approximation tolerance used for Revit display purposes is used by the parameterless overload of the Triangulate() method (used above) when constructing the Mesh. The overload of Triangulate() that takes a double allows a level of detail to be set between 0 (coarser) and 1 (finer).
