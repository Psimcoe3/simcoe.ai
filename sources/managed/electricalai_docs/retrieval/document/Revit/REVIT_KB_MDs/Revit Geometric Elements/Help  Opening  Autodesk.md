---
created: 2026-01-28T21:05:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_Opening_html
author: 
---

# Help | Opening | Autodesk

> ## Excerpt
> In the Revit Platform API, the Opening object is derived from the Element object and contains all of the Element object properties and methods. To retrieve all Openings in a project, use Document.ElementIterator to find the Elements.Opening objects.

---
In the Revit Platform API, the Opening object is derived from the Element object and contains all of the Element object properties and methods. To retrieve all Openings in a project, use Document.ElementIterator to find the Elements.Opening objects.

## General Properties

This section explains how to use the Opening properties.

-   IsRectBoundary - Identifies whether the opening has a rectangular boundary.
    
    -   If true, it means the Opening has a rectangular boundary and you can get an `IList<XYZ>` collection from the Opening BoundaryRect property. Otherwise, the property returns null.
    -   If false, you can get a CurveArray object from the BoundaryCurves property.
-   BoundaryCurves - If the opening boundary is not a rectangle, this property retrieves geometry information; otherwise it returns null. The property returns a CurveArray object containing the curves that represent the Opening object boundary.For more details about Curve, refer to [Geometry](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_html).
    
-   BoundaryRect - If the opening boundary is a rectangle, you can get the geometry information using this property; otherwise it returns null.
    
    -   The property returns an `IList<XYZ>` collection containing the XYZ coordinates.
    -   The `IList<XYZ>` collection usually contains the rectangle boundary minimum (lower left) and the maximum (upper right) coordinates.
-   Host - The host property retrieves the Opening host element. The host element is the element cut by the Opening object.
    
    Note: Note If the Opening object's category is Shaft Openings, the Opening host is null.
    

The following example illustrates how to retrieve the existing Opening properties.

<table summary="" id="GUID-CA1FB5D9-49BE-40D6-B9AA-BFDE21B10C8D__TABLE_6359220C1A1B44E8843360E673ED5623"><tbody><tr><td><b>Code Region 11-6: Retrieving existing opening properties</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>Getinfo_Opening</span><span>(</span><span>Opening</span><span> opening</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>string</span><span> message </span><span>=</span><span> </span><span>"Opening:"</span><span>;</span><span>

    </span><span>//get the host element of this opening</span><span>
    message </span><span>+=</span><span> </span><span>"\nThe id of the opening's host element is : "</span><span> </span><span>+</span><span> opening</span><span>.</span><span>Host</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>;</span><span>

    </span><span>//get the information whether the opening has a rect boundary</span><span>
    </span><span>//If the opening has a rect boundary, we can get the geometry information from BoundaryRect property.</span><span>
    </span><span>//Otherwise we should get the geometry information from BoundaryCurves property</span><span>
    </span><span>if</span><span> </span><span>(</span><span>opening</span><span>.</span><span>IsRectBoundary</span><span>)</span><span>
    </span><span>{</span><span>
        message </span><span>+=</span><span> </span><span>"\nThe opening has a rectangular boundary."</span><span>;</span><span>
        </span><span>//array contains two XYZ objects: the max and min coords of boundary</span><span>
        </span><span>IList</span><span>&lt;</span><span>XYZ</span><span>&gt;</span><span> boundaryRect </span><span>=</span><span> opening</span><span>.</span><span>BoundaryRect</span><span>;</span><span>

        </span><span>//get the coordinate value of the min coordinate point</span><span>
        XYZ point </span><span>=</span><span> opening</span><span>.</span><span>BoundaryRect</span><span>[</span><span>0</span><span>];</span><span>
        message </span><span>+=</span><span> </span><span>"\nMin coordinate point:("</span><span> </span><span>+</span><span> point</span><span>.</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                                </span><span>+</span><span> point</span><span>.</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> point</span><span>.</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>

        </span><span>//get the coordinate value of the Max coordinate point</span><span>
        point </span><span>=</span><span> opening</span><span>.</span><span>BoundaryRect</span><span>[</span><span>1</span><span>];</span><span>
        message </span><span>+=</span><span> </span><span>"\nMax coordinate point: ("</span><span> </span><span>+</span><span> point</span><span>.</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                                </span><span>+</span><span> point</span><span>.</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> point</span><span>.</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        message </span><span>+=</span><span> </span><span>"\nThe opening doesn't have a rectangular boundary."</span><span>;</span><span>
        </span><span>// Get curve number</span><span>
        </span><span>int</span><span> curves </span><span>=</span><span> opening</span><span>.</span><span>BoundaryCurves</span><span>.</span><span>Size</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nNumber of curves is : "</span><span> </span><span>+</span><span> curves</span><span>;</span><span>
        </span><span>for</span><span> </span><span>(</span><span>int</span><span> i </span><span>=</span><span> </span><span>0</span><span>;</span><span> i </span><span>&lt;</span><span> curves</span><span>;</span><span> i</span><span>++)</span><span>
        </span><span>{</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Curve</span><span> curve </span><span>=</span><span> opening</span><span>.</span><span>BoundaryCurves</span><span>.</span><span>get_Item</span><span>(</span><span>i</span><span>);</span><span>
            </span><span>// Get curve start point</span><span>
            message </span><span>+=</span><span> </span><span>"\nCurve start point: "</span><span> </span><span>+</span><span> </span><span>XYZToString</span><span>(</span><span>curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>));</span><span>
            </span><span>// Get curve end point</span><span>
            message </span><span>+=</span><span> </span><span>"; Curve end point: "</span><span> </span><span>+</span><span> </span><span>XYZToString</span><span>(</span><span>curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>));</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>message</span><span>);</span><span>
</span><span>}</span><span>

</span><span>// output the point's three coordinates</span><span>
</span><span>string</span><span> </span><span>XYZToString</span><span>(</span><span>XYZ point</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>return</span><span> </span><span>"("</span><span> </span><span>+</span><span> point</span><span>.</span><span>X </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> point</span><span>.</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> point</span><span>.</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Create Opening

In the Revit Platform API, use the Document.NewOpening() method to create an opening in your project. There are four method overloads you can use to create openings in different host elements:

<table summary="" id="GUID-CA1FB5D9-49BE-40D6-B9AA-BFDE21B10C8D__TABLE_D5371F4390C94C50ADF221D5615F7BB0"><tbody><tr><td><b>Code Region 11-7: NewOpening()</b></td></tr><tr><td><pre><code><span>//Create a new Opening in a beam, brace and column. </span><span>
</span><span>public</span><span> </span><span>Opening</span><span> </span><span>NewOpening</span><span>(</span><span>Element</span><span> famInstElement</span><span>,</span><span> </span><span>CurveArray</span><span> profile</span><span>,</span><span> eRefFace iFace</span><span>);</span><span> </span></code></pre></td></tr><tr><td><pre><code><span>//Create a new Opening in a roof, floor and ceiling. </span><span>
</span><span>public</span><span> </span><span>Opening</span><span> </span><span>NewOpening</span><span>(</span><span>Element</span><span> hostElement</span><span>,</span><span> </span><span>CurveArray</span><span> profile</span><span>,</span><span> </span><span>bool</span><span> bPerpendicularFace</span><span>);</span></code></pre></td></tr><tr><td><pre><code><span>//Create a new Opening Element. </span><span>
</span><span>public</span><span> </span><span>Opening</span><span> </span><span>NewOpening</span><span>(</span><span>Level</span><span> bottomLevel</span><span>,</span><span> </span><span>Level</span><span> topLevel</span><span>,</span><span> </span><span>CurveArray</span><span>  profile</span><span>);</span></code></pre></td></tr><tr><td><pre><code><span>//Create an opening in a straight wall or arc wall. </span><span>
</span><span>public</span><span> </span><span>Opening</span><span> </span><span>NewOpening</span><span>(</span><span>Wall</span><span> wall</span><span>,</span><span> XYZ pntStart</span><span>,</span><span> XYZ pntEnd</span><span>);</span></code></pre></td></tr></tbody></table>

-   Create an Opening in a Beam, Brace, or Column - Use to create an opening in a family instance. The iFace parameter indicates the face on which the opening is placed.
    
-   Create a Roof, Floor, or Ceiling Opening - Use to create an opening in a roof, floor, or ceiling.
    
-   The bPerpendicularFace parameter indicates whether the opening is perpendicular to the face or vertical.
    
-   If the parameter is true, the opening is perpendicular to the host element face. See the following picture: ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-EED350DF-2DD4-4562-998D-C020C739D6F8-low.png)**Figure 39: Opening cut perpendicular to the host element face**
    
    ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-BF04D2D0-A6EA-4D99-9936-615D1C13DB8D-low.png)**Figure 40: Opening cut vertically to the host element**
    
-   Create a New Opening Element - Use to create a shaft opening in your project. However, make sure the topLevel is higher than the bottomLevel; otherwise an exception is thrown.
    
-   Create an Opening in a Straight Wall or Arc Wall - Use to create a rectangle opening in a wall. The coordinates of pntStart and pntEnd should be corner coordinates that can shape a rectangle. For example, the lower left corner and upper right corner of a rectangle. Otherwise an exception is thrown.
    

Note: Using the Opening command you can only create a rectangle shaped wall opening. To create some holes in a wall, edit the wall profile instead of the Opening command.
