---
created: 2026-01-28T21:02:24 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_GeometryObject_Class_Solids_Faces_and_Edges_Face_Splitting_html
author: 
---

# Help | Face Splitting | Autodesk

> ## Excerpt
> A face may be split into regions by the Split Face command. The Face.HasRegions property will report if the face contains regions created with the Split Face command, while the Face.GetRegions() method will return a list of faces, one for the main face of the object hosting the Split Face (such as wall of floor) and one face for each Split Face region.

---
A face may be split into regions by the Split Face command. The Face.HasRegions property will report if the face contains regions created with the Split Face command, while the Face.GetRegions() method will return a list of faces, one for the main face of the object hosting the Split Face (such as wall of floor) and one face for each Split Face region.

The FaceSplitter class represents an element that splits a face. The FaceSplitter.SplitElementId property provides the id of the element whose face is split by this element. The FaceSplitter class can be used to filter and find these faces by type as shown below.

<table summary="" id="GUID-A7308E03-F3C3-433E-8AD5-3C31EDD81387__TABLE_9599826CA311409FAC73A8C065C7B0AA"><tbody><tr><td><b>Code Region: Find face splitting elements</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>FindSplitting</span><span>(</span><span>Application</span><span> app</span><span>,</span><span> </span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Options</span><span> opt </span><span>=</span><span> app</span><span>.</span><span>Create</span><span>.</span><span>NewGeometryOptions</span><span>();</span><span>
    opt</span><span>.</span><span>ComputeReferences</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    opt</span><span>.</span><span>IncludeNonVisibleObjects</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>FaceSplitter</span><span>&gt;</span><span> splitElements </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FaceSplitter</span><span>)).</span><span>Cast</span><span>&lt;</span><span>FaceSplitter</span><span>&gt;().</span><span>ToList</span><span>();</span><span>
    </span><span>foreach</span><span>(</span><span>FaceSplitter</span><span> faceSplitter </span><span>in</span><span> splitElements</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Element</span><span> splitElement </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>faceSplitter</span><span>.</span><span>SplitElementId</span><span>);</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geomElem </span><span>=</span><span> faceSplitter</span><span>.</span><span>get_Geometry</span><span>(</span><span>opt</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> geomObj </span><span>in</span><span> geomElem</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>Line</span><span> line </span><span>=</span><span> geomObj </span><span>as</span><span> </span><span>Line</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>line </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                XYZ end1 </span><span>=</span><span> line</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>);</span><span>
                XYZ end2 </span><span>=</span><span> line</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>);</span><span>
                </span><span>double</span><span> length </span><span>=</span><span> line</span><span>.</span><span>ApproximateLength</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
