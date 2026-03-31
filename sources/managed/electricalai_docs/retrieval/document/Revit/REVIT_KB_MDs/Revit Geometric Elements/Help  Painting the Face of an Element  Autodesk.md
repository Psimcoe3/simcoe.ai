---
created: 2026-01-28T21:04:01 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_Painting_the_Face_of_an_Element_html
author: 
---

# Help | Painting the Face of an Element | Autodesk

> ## Excerpt
> The Paint tool functionality is available through the Revit API. Faces of elements such as walls, floors, and roofs can be painted with a material to change their appearance. It does not change the structure of the element.

---
The Paint tool functionality is available through the Revit API. Faces of elements such as walls, floors, and roofs can be painted with a material to change their appearance. It does not change the structure of the element.

The methods related to painting elements are part of the Document class. Document.Paint() applies a material to a specified face of an element. Document.RemovePaint() will remove the applied material. Additionally, the IsPainted() and GetPaintedMaterial() methods return information about the face of an element.

<table summary="" id="GUID-BE4672C9-E8BB-4157-8A2C-9067113FC55E__TABLE_655A1D7E49E047EFAAA240A9C52D9D5C"><tbody><tr><td><b>Code Region: Paint faces of a wall</b></td></tr><tr><td><pre><code><span>// Paint any unpainted faces of a given wall</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>PaintWallFaces</span><span>(</span><span>Wall</span><span> wall</span><span>,</span><span> </span><span>ElementId</span><span> matId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> wall</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>GeometryElement</span><span> geometryElement </span><span>=</span><span> wall</span><span>.</span><span>get_Geometry</span><span>(</span><span>new</span><span> </span><span>Options</span><span>());</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> geometryObject </span><span>in</span><span> geometryElement</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>geometryObject </span><span>is</span><span> </span><span>Solid</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>Solid</span><span> solid </span><span>=</span><span> geometryObject </span><span>as</span><span> </span><span>Solid</span><span>;</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> face </span><span>in</span><span> solid</span><span>.</span><span>Faces</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>doc</span><span>.</span><span>IsPainted</span><span>(</span><span>wall</span><span>.</span><span>Id</span><span>,</span><span> face</span><span>)</span><span> </span><span>==</span><span> </span><span>false</span><span>)</span><span>
                </span><span>{</span><span>
                    doc</span><span>.</span><span>Paint</span><span>(</span><span>wall</span><span>.</span><span>Id</span><span>,</span><span> face</span><span>,</span><span> matId</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
