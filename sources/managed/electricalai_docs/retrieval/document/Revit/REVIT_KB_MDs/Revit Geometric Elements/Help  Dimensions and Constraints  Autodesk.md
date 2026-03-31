---
created: 2026-01-28T21:00:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_Dimensions_and_Constraints_html
author: 
---

# Help | Dimensions and Constraints | Autodesk

> ## Excerpt
> The Dimension class represents permanent dimensions and dimension-related constraint elements. Temporary dimensions created while editing an element in the UI are not accessible. Spot elevation and spot coordinate are represented by the SpotDimension class.

---
The Dimension class represents permanent dimensions and dimension-related constraint elements. Temporary dimensions created while editing an element in the UI are not accessible. Spot elevation and spot coordinate are represented by the SpotDimension class.

The following code sample illustrates, near the end, how to distinguish permanent dimensions from constraint elements.

<table summary="" id="GUID-B3F3A810-5372-49E8-8E00-DDBD729EA49E__TABLE_494C6C114DD54245AD084F2CE53B7F60"><tbody><tr><td><b>Code Region 16-1: Distinguishing permanent dimensions from constraints</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetInfo_Dimension</span><span>(</span><span>Dimension</span><span> dimension</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>string</span><span> message </span><span>=</span><span> </span><span>"Dimension : "</span><span>;</span><span>
    </span><span>// Get Dimension name</span><span>
    message </span><span>+=</span><span> </span><span>"\nDimension name is : "</span><span> </span><span>+</span><span> dimension</span><span>.</span><span>Name</span><span>;</span><span>

    </span><span>// Get Dimension Curve</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Curve</span><span> curve </span><span>=</span><span> dimension</span><span>.</span><span>Curve</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>curve </span><span>!=</span><span> </span><span>null</span><span> </span><span>&amp;&amp;</span><span> curve</span><span>.</span><span>IsBound</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Get curve start point</span><span>
        message </span><span>+=</span><span> </span><span>"\nCurve start point:("</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
        </span><span>// Get curve end point</span><span>
        message </span><span>+=</span><span> </span><span>"; Curve end point:("</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>// Get Dimension type name</span><span>
    message </span><span>+=</span><span> </span><span>"\nDimension type name is : "</span><span> </span><span>+</span><span> dimension</span><span>.</span><span>DimensionType</span><span>.</span><span>Name</span><span>;</span><span>

    </span><span>// Get Dimension view name</span><span>
    message </span><span>+=</span><span> </span><span>"\nDimension view name is : "</span><span> </span><span>+</span><span> dimension</span><span>.</span><span>View</span><span>.</span><span>Name</span><span>;</span><span>

    </span><span>// Get Dimension reference count</span><span>
    message </span><span>+=</span><span> </span><span>"\nDimension references count is "</span><span> </span><span>+</span><span> dimension</span><span>.</span><span>References</span><span>.</span><span>Size</span><span>;</span><span>

    </span><span>if</span><span> </span><span>((</span><span>int</span><span>)</span><span>BuiltInCategory</span><span>.</span><span>OST_Dimensions </span><span>==</span><span> dimension</span><span>.</span><span>Category</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>)</span><span>
    </span><span>{</span><span>
        message </span><span>+=</span><span> </span><span>"\nDimension is a permanent dimension."</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span> </span><span>if</span><span> </span><span>((</span><span>int</span><span>)</span><span>BuiltInCategory</span><span>.</span><span>OST_Constraints </span><span>==</span><span> dimension</span><span>.</span><span>Category</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>)</span><span>
    </span><span>{</span><span>
        message </span><span>+=</span><span> </span><span>"\nDimension is a constraint element."</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>message</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Dimensions

There are five kinds of permanent dimensions:

-   Linear dimension
-   Radial dimension
-   Diameter Dimension
-   Angular dimension
-   Arc length dimension

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/Dims.png)**Figure 66: Permanent dimensions**

The BuiltInCategory for all permanent dimensions is OST\_Dimensions. There is not an easy way to distinguish the four dimensions using the API.

Except for radial and diameter dimensions, every dimension has one dimension line. Dimension lines are available from the Dimension.Curve property which is always unbound. In other words, the dimension line does not have a start-point or end-point. Based on the previous picture:

-   A Line object is returned for a linear dimension.
-   An arc object is returned for a radial dimension or angular dimension.
-   A radial dimension returns null.
-   A diamter diimension returns null.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4C8DCD73-DFD8-4185-A1EA-2C890D176FBF-low.png)**Figure 67: Dimension references**

A dimension is created by selecting geometric references as the previous picture shows. Geometric references are represented as a Reference class in the API. The following dimension references are available from the References property. For more information about Reference, please see [Geometry Helper Classes](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Helper_Classes_html) in the [Geometry](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_html) section.

-   Radial and diameter dimensions - One Reference object for the curve is returned
-   Angular and arc length dimensions - Two Reference objects are returned.
-   Linear dimensions - Two or more Reference objects are returned. In the following picture, the linear dimension has five Reference objects.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-A976B817-2D4B-471B-BF79-27E9262A8A85-low.png)**Figure 68: Linear dimension references**

Dimensions, like other Annotation Elements, are view-specific. They display only in the view where they are added. The Dimension.View property returns the specific view.

### Constraint Elements

Dimension objects with Category Constraints (BuitInCategory.OST\_Constraints) represent two kinds of dimension-related constraints:

-   Linear and radial dimension constraints
-   Equality constraints

In the following picture, two kinds of locked constraints correspond to linear and radial dimension. In the application, they appear as padlocks with green dashed lines. (The green dashed line is available from the Dimension.Curve property.) Both linear and radial dimension constraints return two Reference objects from the Dimension.References property.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-370D4754-3BC7-4A6C-8531-41B7A5B424D9-low.png)**Figure 69: Linear and Radial dimension constraints**

Constraint elements are not view-specific and can display in different views. Therefore, the View property always returns null. In the following picture, the constraint elements in the previous picture are also visible in the 3D view.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-8365F25E-7304-413D-BABE-1C495BD8ADAD-low.png)**Figure 70: Linear and Radial dimension constraints in 3D view**

Although equality constraints are based on dimensions, they are also represented by the Dimension class. There is no direct way to distinguish linear dimension constraints from equality constraints in the API using a category or DimensionType. Equality constraints return three or more References while linear dimension constraints return two or more References.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-FB6F70CD-8913-4C3A-A036-2108550BA25C-low.png)**Figure 71: Equality constraints**

Note: Not all constraint elements are represented by the Dimension class but all belong to a Constraints (OST\_Constraints) category such as alignment constraint. ### Spot Dimensions

Spot coordinates and spot elevations are represented by the SpotDimension class and are distinguished by category. Like the permanent dimension, spot dimensions are view-specific. The type and category for each spot dimension are listed in the following table:

**Table 35: Spot dimension Type and Category**

<table summary="" id="GUID-B3F3A810-5372-49E8-8E00-DDBD729EA49E__TABLE_6C4FFE8D1C7A414F830F2B214A20E229"><tbody><tr><td><b>Type</b></td><td><b>Category</b></td></tr><tr><td>Spot Coordinates</td><td>OST_SpotCoordinates</td></tr><tr><td>Spot Elevations</td><td>OST_SpotElevations</td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-BDB09C60-D4AC-4F6A-8100-6BA2FA165228-low.png)**Figure 72: SpotCoordinates and SpotElevations**

The SpotDimension Location can be downcast to LocationPoint so that the point coordinate that the spot dimension points to is available from the LocationPoint.Point property.

-   SpotDimensions have no dimension curve so their Curve property always returns null.
-   The SpotDimension References property returns one Reference representing the point or the edge referenced by the spot dimension.
-   To control the text and tag display style, modify the SpotDimension and SpotDimensionType Parameters.

Information about the leader of a spot dimension is accessible with:

-   SpotDimension.LeaderElbowPosition
-   SpotDimension.LeaderHasElbow

### Comparison

The following table compares different kinds of dimensions and constraints in the API:

**Table 36: Dimension Category Comparison**

<table summary="" id="GUID-B3F3A810-5372-49E8-8E00-DDBD729EA49E__TABLE_BB38A40A891647BCA63FD2814EEEC0C4"><tbody><tr><td><b><i>Dimension or Constraint</i></b></td><td><b><i>Dimension or Constraint</i></b></td><td><b><i>API Class</i></b></td><td><b><i>BuiltInCategory</i></b></td><td><b><i>Curve</i></b></td><td><b><i>Geometry Helper Classes</i></b></td><td><b><i>View</i></b></td><td><b><i>Location</i></b></td></tr><tr><td>Permanent Dimension</td><td>linear dimension</td><td>Dimension</td><td>OST_Dimensions</td><td>A Line</td><td>=2</td><td>Specific view</td><td>null</td></tr><tr><td>Permanent Dimension</td><td>radial dimension</td><td>Dimension</td><td>OST_Dimensions</td><td>Null</td><td>1</td><td>Specific view</td><td>null</td></tr><tr><td>Permanent Dimension</td><td>diameter dimension</td><td>Dimension</td><td>OST_Dimensions</td><td>Null</td><td>1</td><td>Specific view</td><td>null</td></tr><tr><td>Permanent Dimension</td><td>angular dimension</td><td>Dimension</td><td>OST_Dimensions</td><td>An Arc</td><td>2</td><td>Specific view</td><td>null</td></tr><tr><td>Permanent Dimension</td><td>arc length dimension</td><td>Dimension</td><td>OST_Dimensions</td><td>An Arc</td><td>2</td><td>Specific view</td><td>null</td></tr><tr><td>Dimension Constraint</td><td>linear dimension constraint</td><td>Dimension</td><td>OST_Constraints</td><td>An Arc</td><td>2</td><td>&nbsp;</td><td>null</td></tr><tr><td>Dimension Constraint</td><td>angular dimension</td><td>Dimension</td><td>OST_Constraints</td><td>An Arc</td><td>2</td><td>&nbsp;</td><td>null</td></tr><tr><td>Equality Constraint</td><td>Equality Constraint</td><td>Dimension</td><td>OST_Constraints</td><td>A Line</td><td>=3</td><td>&nbsp;</td><td>null</td></tr></tbody></table>

### Create and Delete

The NewDimension() method is available in the Creation.Document class. This method can create a linear dimension only.

<table summary="" id="GUID-B3F3A810-5372-49E8-8E00-DDBD729EA49E__TABLE_721E2A5AFB174B41A2CFBF054DC78750"><tbody><tr><td><b>Code Region 16-2: NewDimension()</b></td></tr><tr><td><p><code>public Dimension NewDimension (View view, Line line, ReferenceArray references)</code></p></td></tr><tr><td><p><code>public Dimension NewDimension (View view, Line line, ReferenceArray references, DimensionType dimensionType)</code></p></td></tr></tbody></table>

Using the NewDimension() method input parameters, you can define the visible View, dimension line, and References (two or more). However, there is no easy way to distinguish a linear dimension DimensionType from other types. The overloaded NewDimension() method with the DimensionType parameter is rarely used.

The following code illustrates how to use the NewDimension() method to duplicate a dimension.

<table summary="" id="GUID-B3F3A810-5372-49E8-8E00-DDBD729EA49E__TABLE_7BD6B8CE504A44C6863806DCEB8FED48"><tbody><tr><td><b>Code Region 16-3: Duplicating a dimension with NewDimension()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>DuplicateDimension</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Dimension</span><span> dimension</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Line</span><span> line </span><span>=</span><span> dimension</span><span>.</span><span>Curve</span><span> </span><span>as</span><span> </span><span>Line</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> line</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>View</span><span> view </span><span>=</span><span> dimension</span><span>.</span><span>View</span><span>;</span><span>
                </span><span>ReferenceArray</span><span> references </span><span>=</span><span> dimension</span><span>.</span><span>References</span><span>;</span><span>
                </span><span>Dimension</span><span> newDimension </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewDimension</span><span>(</span><span>view</span><span>,</span><span> line</span><span>,</span><span> references</span><span>);</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Though only linear dimensions are created, you can delete all dimensions and constraints represented by Dimension and SpotDimension using the Document.Delete() method.

### Manipulating Dimension Text and Leader

Access to several attributes of the dimension are available with:

-   DimensionType.Prefix
-   DimensionType.Suffix
-   Dimension.TextPosition
-   Dimension.LeaderEndPosition
-   Dimension.HasLeader

Dimension and DimensionSegment classes provide similar properties and methods for querying and adjusting the position of the text relative to the dimension curve.

Dimension.Origin returns the XYZ value of the midpoint of the dimension curve, with DimensionSegment.Origin will return the midpoint of the line that makes up the segment.

Determine if text position of a Dimension or DimensionSegment is adjustable by calling the method IsTextPositionAdjustable() which will indicate whether the text and leader positions may be set.

Query or modify the position of text or the leader (of a dimension or dimension segment) by using the properties TextPosition and LeaderEndPosition.

Reset the text to its default position on a dimension by calling the method ResetTextPosition().

Note: TextPosition and LeaderEndPosition are not necessarily applicable to all dimensions (e.g., spot dimensions, multi-segment dimensions using the equality constraint, when dimension style is ordinate). If these values are not applicable they will return Null and not allow setting a value.

<table summary="" id="GUID-B3F3A810-5372-49E8-8E00-DDBD729EA49E__TABLE_C549BB7C6DA14A06ABF34AC24C3077E6"><tbody><tr><td><b>Code Region: Reposition dimension text</b></td></tr><tr><td><pre><code><span>// Moves all of the text in this dimension one unit in the Y direction</span><span>
</span><span>public</span><span> </span><span>bool</span><span> </span><span>DimensionTextReposition</span><span>(</span><span>Dimension</span><span> dimToModify</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> modified </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>dimToModify </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>return</span><span> </span><span>false</span><span>;</span><span>

    </span><span>// Check to see if we have a non-multisegment dimension and if text position is adjustable</span><span>
    </span><span>if</span><span> </span><span>(</span><span>dimToModify</span><span>.</span><span>NumberOfSegments</span><span> </span><span>==</span><span> </span><span>0</span><span> </span><span>&amp;&amp;</span><span> dimToModify</span><span>.</span><span>IsTextPositionAdjustable</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>// Get the current text XYZ position</span><span>
        XYZ currentTextPosition </span><span>=</span><span> dimToModify</span><span>.</span><span>TextPosition</span><span>;</span><span>
        </span><span>// Calculate a new XYZ position by transforming the current text position</span><span>
        XYZ newTextPosition </span><span>=</span><span> </span><span>Transform</span><span>.</span><span>CreateTranslation</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0.0</span><span>,</span><span> </span><span>1.0</span><span>,</span><span> </span><span>0.0</span><span>)).</span><span>OfPoint</span><span>(</span><span>currentTextPosition</span><span>);</span><span>
        </span><span>// Set the new text position</span><span>
        dimToModify</span><span>.</span><span>TextPosition</span><span> </span><span>=</span><span> newTextPosition</span><span>;</span><span>

        modified </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>dimToModify</span><span>.</span><span>NumberOfSegments</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>DimensionSegment</span><span> currentSegment </span><span>in</span><span> dimToModify</span><span>.</span><span>Segments</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>currentSegment </span><span>!=</span><span> </span><span>null</span><span> </span><span>&amp;&amp;</span><span> currentSegment</span><span>.</span><span>IsTextPositionAdjustable</span><span>())</span><span>
            </span><span>{</span><span>
                modified </span><span>=</span><span> </span><span>true</span><span>;</span><span>
                </span><span>// Get the current text XYZ position</span><span>
                XYZ currentTextPosition </span><span>=</span><span> currentSegment</span><span>.</span><span>TextPosition</span><span>;</span><span>
                </span><span>// Calculate a new XYZ position by transforming the current text position</span><span>
                XYZ newTextPosition </span><span>=</span><span> </span><span>Transform</span><span>.</span><span>CreateTranslation</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>)).</span><span>OfPoint</span><span>(</span><span>currentTextPosition</span><span>);</span><span>
                </span><span>// Set the new text position for the segment's text</span><span>
                currentSegment</span><span>.</span><span>TextPosition</span><span> </span><span>=</span><span> newTextPosition</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>return</span><span> modified</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
