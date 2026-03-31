---
created: 2026-01-28T21:00:55 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Example_Retrieve_Geometry_Data_from_a_Wall_html
author: 
---

# Help | Example: Retrieve Geometry Data from a Wall | Autodesk

> ## Excerpt
> This walkthrough illustrates how to get geometry data from a wall. The following information is covered:

---
This walkthrough illustrates how to get geometry data from a wall. The following information is covered:

-   Getting the wall geometry edges.
-   Getting the wall geometry faces.

Note Retrieving the geometry data from Element in this example is limited because Instance is not considered. For example, sweeps included in the wall are not available in the sample code. The goal for this walkthrough is to give you a basic idea of how to retrieve geometry data but not cover all conditions. For more information about retrieving geometry data from Element, refer to [Example: Retrieve Geometry Data from a Beam](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Example_Retrieve_Geometry_Data_from_a_Beam_html).

### Create Geometry Options

In order to get the wall's geometry information, you must create a Geometry.Options object which provides detailed customized options. The code is as follows:

<table summary="" id="GUID-96A0E5EC-D9AD-42F2-901D-CC902ADD0BED__TABLE_18738B75657F43469B5FC720790D5FAE"><tbody><tr><td><b>Code Region 20-1: Creating Geometry.Options</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateOptions</span><span>(</span><span>Application</span><span> application</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Options</span><span> geomOption </span><span>=</span><span> application</span><span>.</span><span>Create</span><span>.</span><span>NewGeometryOptions</span><span>();</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> geomOption</span><span>)</span><span>
        </span><span>{</span><span>
                geomOption</span><span>.</span><span>ComputeReferences</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
                geomOption</span><span>.</span><span>DetailLevel</span><span> </span><span>=</span><span> </span><span>ViewDetailLevel</span><span>.</span><span>Fine</span><span>;</span><span>

                </span><span>// Either the DetailLevel or the View can be set, but not both</span><span>
                </span><span>//geomOption.View = commandData.Application.ActiveUIDocument.Document.ActiveView;</span><span>

                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Geometry Option created successfully."</span><span>);</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Retrieve Faces and Edges

Wall geometry is a solid made up of faces and edges. Complete the following steps to get the faces and edges:

1.  Retrieve a Geometry.Element instance using the Wall class Geometry property. This instance contains all geometry objects in the Object property, such as a solid, a line, and so on.
2.  Iterate the Object property to get a geometry solid instance containing all geometry faces and edges in the Faces and Edges properties.
3.  Iterate the Faces property to get all geometry faces.
4.  Iterate the Edges property to get all geometry edges.

The sample code follows:

<table summary="" id="GUID-96A0E5EC-D9AD-42F2-901D-CC902ADD0BED__TABLE_21C9DC7D16314EE58CD93BAD609215AD"><tbody><tr><td><b>Code Region 20-2: Retrieving faces and edges</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>GetFacesAndEdges</span><span>(</span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>String</span><span> faceInfo </span><span>=</span><span> </span><span>""</span><span>;</span><span>

        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Options</span><span> opt </span><span>=</span><span> </span><span>new</span><span> </span><span>Options</span><span>();</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geomElem </span><span>=</span><span> wall</span><span>.</span><span>get_Geometry</span><span>(</span><span>opt</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> geomObj </span><span>in</span><span> geomElem</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>Solid</span><span> geomSolid </span><span>=</span><span> geomObj </span><span>as</span><span> </span><span>Solid</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> geomSolid</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>int</span><span> faces </span><span>=</span><span> </span><span>0</span><span>;</span><span>
                        </span><span>double</span><span> totalArea </span><span>=</span><span> </span><span>0</span><span>;</span><span>
                        </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> geomFace </span><span>in</span><span> geomSolid</span><span>.</span><span>Faces</span><span>)</span><span>
                        </span><span>{</span><span>
                                faces</span><span>++;</span><span>
                                faceInfo </span><span>+=</span><span> </span><span>"Face "</span><span> </span><span>+</span><span> faces </span><span>+</span><span> </span><span>" area: "</span><span> </span><span>+</span><span> geomFace</span><span>.</span><span>Area</span><span>.</span><span>ToString</span><span>()</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
                                totalArea </span><span>+=</span><span> geomFace</span><span>.</span><span>Area</span><span>;</span><span>
                        </span><span>}</span><span>
                        faceInfo </span><span>+=</span><span> </span><span>"Number of faces: "</span><span> </span><span>+</span><span> faces </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
                        faceInfo </span><span>+=</span><span> </span><span>"Total area: "</span><span> </span><span>+</span><span> totalArea</span><span>.</span><span>ToString</span><span>()</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
                        </span><span>foreach</span><span> </span><span>(</span><span>Edge</span><span> geomEdge </span><span>in</span><span> geomSolid</span><span>.</span><span>Edges</span><span>)</span><span>
                        </span><span>{</span><span>
                                </span><span>// get wall's geometry edges</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> faceInfo</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
