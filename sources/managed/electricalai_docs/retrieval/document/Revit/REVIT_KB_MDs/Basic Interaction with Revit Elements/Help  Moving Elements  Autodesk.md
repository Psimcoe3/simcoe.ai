---
created: 2026-01-28T20:50:35 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Moving_Elements_html
author: 
---

# Help | Moving Elements | Autodesk

> ## Excerpt
> The ElementTransformUtils class provides two static methods to move one or more elements from one place to another.

---
The ElementTransformUtils class provides two static methods to move one or more elements from one place to another.

**Table 19: Move Methods**

|  |  |
| --- | --- |
| Member | Description |
| `MoveElement( Document, ElementId, XYZ)` | Move an element in the document by a specified vector. |
| `MoveElements(Document, ICollection<ElementId>, XYZ)` | Move several elements by a set of IDs in the document by a specified vector. |

Note: When you use the MoveElement() or MoveElements() methods, the following rules apply.

-   The methods cannot move a level-based element up or down from the level. When the element is level-based, you cannot change the Z coordinate value. However, you can place the element at any location in the same level. As well, some level based elements have an offset instance parameter you can use to move them in the Z direction.For example, if you create a new column at the original location (0, 0, 0) in Level1, and then move it to the new location (10, 20, 30), the column is placed at the location (10, 20, 0) instead of (10, 20, 30).
    
    <table summary="" id="GUID-CD3B9A83-8DBC-418E-8099-D655AB3DA010__TABLE_AE46ADAF23A64DEB8AB387ACFCCD32D5"><tbody><tr><td><b>Code Region 10-1: Using MoveElement()</b></td></tr><tr><td></td></tr></tbody></table>
    

```
public void MoveColumn(Autodesk.Revit.DB.Document document, FamilyInstance column)
{
        // get the column current location
        LocationPoint columnLocation = column.Location as LocationPoint;

        XYZ oldPlace = columnLocation.Point;

        // Move the column to new location.
        XYZ newPlace = new XYZ(10, 20, 30);
        ElementTransformUtils.MoveElement(document, column.Id, newPlace);

        // now get the column's new location
        columnLocation = column.Location as LocationPoint;
        XYZ newActual = columnLocation.Point;

        string info = "Original Z location: " + oldPlace.Z + 
                        "\nNew Z location: " + newActual.Z;

        TaskDialog.Show("Revit",info);
}
```

```
</td>

</tr>

</tbody>

</table>
```

-   When you move one or more elements, associated elements are moved. For example, if a wall with windows is moved, the windows are also moved.
-   [Pinned Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Pinned_Elements_html) cannot be moved.

Another way to move an element in Revit is to use Location and its derivative objects. In the Revit Platform API, the Location object provides the ability to translate and rotate elements. More location information and control is available using the Location object derivatives such as LocationPoint or LocationCurve. If the Location element is downcast to a LocationCurve object or a LocationPoint object, move the curve or the point to a new place directly.

<table summary="" id="GUID-CD3B9A83-8DBC-418E-8099-D655AB3DA010__TABLE_AF33E1AB2AEC436096E2BD1C6B962793"><tbody><tr><td><b>Code Region 10-2: Moving using Location</b></td></tr><tr><td><pre><code><span>bool</span><span> </span><span>MoveUsingLocationCurve</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application</span><span>,</span><span> </span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>LocationCurve</span><span> wallLine </span><span>=</span><span> wall</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
        XYZ translationVec </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>20</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        </span><span>return</span><span> </span><span>(</span><span>wallLine</span><span>.</span><span>Move</span><span>(</span><span>translationVec</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

When you move the element, note that the vector (10, 20, 0) is not the destination but the offset. The following picture illustrates the wall position before and after moving.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-CA323378-0ABA-4B2B-B242-2D98C01F0A78-low.png)**Figure 30: Move a wall using the LocationCurve**

In addition, you can use the LocationCurve Curve property or the LocationPoint Point property to move one element in Revit.

Use the Curve property to move a curve-driven element to any specified position. Many elements are curve-driven, such as walls, beams, and braces. Also use the property to resize the length of the element.

<table summary="" id="GUID-CD3B9A83-8DBC-418E-8099-D655AB3DA010__TABLE_1D166EBA33324A2398067CD862BE6F1C"><tbody><tr><td><b>Code Region 10-3: Moving using Curve</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>MoveUsingCurveParam</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application</span><span>,</span><span> </span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>LocationCurve</span><span> wallLine </span><span>=</span><span> wall</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
    XYZ p1 </span><span>=</span><span> XYZ</span><span>.</span><span>Zero</span><span>;</span><span>
    XYZ p2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>20</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Line</span><span> newWallLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p1</span><span>,</span><span> p2</span><span>);</span><span>

    </span><span>// Change the wall line to a new line.</span><span>
    wallLine</span><span>.</span><span>Curve</span><span> </span><span>=</span><span> newWallLine</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

You can also get or set a curve-based element's join properties with the LocationCurve.JoinType property.

Use the LocationPoint Point property to set the element's physical location.

<table summary="" id="GUID-CD3B9A83-8DBC-418E-8099-D655AB3DA010__TABLE_76091AAAC4C04143BB5F5B2EACBE99E5"><tbody><tr><td><b>Code Region 10-4: Moving using Point</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>LocationMove</span><span>(</span><span>FamilyInstance</span><span> column</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>LocationPoint</span><span> columnPoint </span><span>=</span><span> column</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationPoint</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> columnPoint</span><span>)</span><span>
        </span><span>{</span><span>
                XYZ newLocation </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>20</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                </span><span>// Move the column to the new location</span><span>
                columnPoint</span><span>.</span><span>Point</span><span> </span><span>=</span><span> newLocation</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
