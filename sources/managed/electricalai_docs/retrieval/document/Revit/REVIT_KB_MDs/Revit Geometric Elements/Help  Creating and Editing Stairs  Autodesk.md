---
created: 2026-01-28T21:04:10 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Stairs_and_Railings_Creating_and_Editing_Stairs_html
author: 
---

# Help | Creating and Editing Stairs | Autodesk

> ## Excerpt
> As with other types of elements in the Revit document, a Transaction is necessary to edit stairs and stairs components. However, to create new components such as runs and landings, or to create new stairs themselves, it is necessary to use an Autodesk.Revit.DB.StairsEditScope object which maintains a stairs-editing session.

---
### StairsEditScope

As with other types of elements in the Revit document, a Transaction is necessary to edit stairs and stairs components. However, to create new components such as runs and landings, or to create new stairs themselves, it is necessary to use an Autodesk.Revit.DB.StairsEditScope object which maintains a stairs-editing session.

StairsEditScope acts like a TransactionGroup. After a StairsEditScope is started, you can start transactions and edit the stairs. Individual transactions created inside StairsEditScope will not appear in the undo menu. All transactions committed during the edit mode will be merged into a single one which will bear the name passed into the StairsEditScope constructor.

StairsEditScope has two Start methods. One takes the ElementId for an existing Stairs object for which it starts a stairs-editing session. The second Start method takes the ElementIds for base and top levels and creates a new empty stairs element with a default stairs type in the specified levels and then starts a stairs edit mode for the new stairs.

After runs and landings have been added to the Stairs and editing is complete, call StairsEditScope.Commit() to end the stairs-editing session.

### Adding Runs

The StairsRun class has three static methods for creating new runs for a Stairs object:

-   **CreateSketchedRun** - Creates a sketched run by providing a group of boundary curves and riser curves.
-   **CreateStraightRun** - Creates a straight run.
-   **CreateSpiralRun** - Creates a spiral run by providing the center, start angle and included angle.
    
    ### Adding Landings
    

Either automatic or sketched landings can be added between two runs. The static method StairsLanding.CanCreateAutomaticLanding() will check whether two stairs runs meet restriction to create automatic landing(s). The static StairsLanding.CreateAutomaticLanding() method will return the Ids of all landings created between the two stairs runs.

The static StairsLanding.CreateSketchedLanding method creates a customized landing between two runs by providing the closed boundary curves of the landing. One of the inputs to the CreateSketchedLanding method is a double value for the base elevation. The elevation has following restriction:

-   The base elevation is relative to the base elevation of the stairs.
-   The base elevation will be rounded automatically to a multiple of the riser height.
-   The base elevation should be equal to or greater than half of the riser height.
    
    ### Example
    

The following example creates a new Stairs object, two runs (one sketched, one straight) and a landing between them.

<table summary="" id="GUID-C60041FB-069E-4C89-BE67-A0593E790995__TABLE_34819D8D077E4D78BDCE1BBF877EC614"><tbody><tr><td><b>Code Region: Creating Stairs, Runs and a Landing</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>StairCreation</span><span>
</span><span>{</span><span>
    </span><span>// FailurePreprocessor class required for StairsEditScope</span><span>
    </span><span>class</span><span> </span><span>StairsFailurePreprocessor</span><span> </span><span>:</span><span> </span><span>IFailuresPreprocessor</span><span>
    </span><span>{</span><span>
        </span><span>public</span><span> </span><span>FailureProcessingResult</span><span> </span><span>PreprocessFailures</span><span>(</span><span>FailuresAccessor</span><span> failuresAccessor</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// Use default failure processing</span><span>
            </span><span>return</span><span> </span><span>FailureProcessingResult</span><span>.</span><span>Continue</span><span>;</span><span> 
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>private</span><span> </span><span>ElementId</span><span> </span><span>CreateStairs</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Level</span><span> levelBottom</span><span>,</span><span> </span><span>Level</span><span> levelTop</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>ElementId</span><span> newStairsId </span><span>=</span><span> </span><span>null</span><span>;</span><span>

        </span><span>using</span><span> </span><span>(</span><span>StairsEditScope</span><span> newStairsScope </span><span>=</span><span> </span><span>new</span><span> </span><span>StairsEditScope</span><span>(</span><span>document</span><span>,</span><span> </span><span>"New Stairs"</span><span>))</span><span>
        </span><span>{</span><span>
            newStairsId </span><span>=</span><span> newStairsScope</span><span>.</span><span>Start</span><span>(</span><span>levelBottom</span><span>.</span><span>Id</span><span>,</span><span> levelTop</span><span>.</span><span>Id</span><span>);</span><span>

            </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> stairsTrans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Add Runs and Landings to Stairs"</span><span>))</span><span>
            </span><span>{</span><span>
                stairsTrans</span><span>.</span><span>Start</span><span>();</span><span>

                </span><span>// Create a sketched run for the stairs</span><span>
                </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> bdryCurves </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;();</span><span>
                </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> riserCurves </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;();</span><span>
                </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> pathCurves </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;();</span><span>
                XYZ pnt1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                XYZ pnt2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>15</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                XYZ pnt3 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                XYZ pnt4 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>15</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>

                </span><span>// boundaries       </span><span>
                bdryCurves</span><span>.</span><span>Add</span><span>(</span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>pnt1</span><span>,</span><span> pnt2</span><span>));</span><span>
                bdryCurves</span><span>.</span><span>Add</span><span>(</span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>pnt3</span><span>,</span><span> pnt4</span><span>));</span><span>

                </span><span>// riser curves</span><span>
                </span><span>const</span><span> </span><span>int</span><span> riserNum </span><span>=</span><span> </span><span>20</span><span>;</span><span>
                </span><span>for</span><span> </span><span>(</span><span>int</span><span> ii </span><span>=</span><span> </span><span>0</span><span>;</span><span> ii </span><span>&lt;=</span><span> riserNum</span><span>;</span><span> ii</span><span>++)</span><span>
                </span><span>{</span><span>
                    XYZ end0 </span><span>=</span><span> </span><span>(</span><span>pnt1 </span><span>+</span><span> pnt2</span><span>)</span><span> </span><span>*</span><span> ii </span><span>/</span><span> </span><span>(</span><span>double</span><span>)</span><span>riserNum</span><span>;</span><span>
                    XYZ end1 </span><span>=</span><span> </span><span>(</span><span>pnt3 </span><span>+</span><span> pnt4</span><span>)</span><span> </span><span>*</span><span> ii </span><span>/</span><span> </span><span>(</span><span>double</span><span>)</span><span>riserNum</span><span>;</span><span>
                    XYZ end2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>end1</span><span>.</span><span>X</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                    riserCurves</span><span>.</span><span>Add</span><span>(</span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>end0</span><span>,</span><span> end2</span><span>));</span><span>
                </span><span>}</span><span>

                </span><span>//stairs path curves</span><span>
                XYZ pathEnd0 </span><span>=</span><span> </span><span>(</span><span>pnt1 </span><span>+</span><span> pnt3</span><span>)</span><span> </span><span>/</span><span> </span><span>2.0</span><span>;</span><span>
                XYZ pathEnd1 </span><span>=</span><span> </span><span>(</span><span>pnt2 </span><span>+</span><span> pnt4</span><span>)</span><span> </span><span>/</span><span> </span><span>2.0</span><span>;</span><span>
                pathCurves</span><span>.</span><span>Add</span><span>(</span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>pathEnd0</span><span>,</span><span> pathEnd1</span><span>));</span><span>

                </span><span>StairsRun</span><span> newRun1 </span><span>=</span><span> </span><span>StairsRun</span><span>.</span><span>CreateSketchedRun</span><span>(</span><span>document</span><span>,</span><span> newStairsId</span><span>,</span><span> levelBottom</span><span>.</span><span>Elevation</span><span>,</span><span> bdryCurves</span><span>,</span><span> riserCurves</span><span>,</span><span> pathCurves</span><span>);</span><span>

                </span><span>// Add a straight run</span><span>
                </span><span>Line</span><span> locationLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>20</span><span>,</span><span> </span><span>-</span><span>5</span><span>,</span><span> newRun1</span><span>.</span><span>TopElevation</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>35</span><span>,</span><span> </span><span>-</span><span>5</span><span>,</span><span> newRun1</span><span>.</span><span>TopElevation</span><span>));</span><span>
                </span><span>StairsRun</span><span> newRun2 </span><span>=</span><span> </span><span>StairsRun</span><span>.</span><span>CreateStraightRun</span><span>(</span><span>document</span><span>,</span><span> newStairsId</span><span>,</span><span> locationLine</span><span>,</span><span> </span><span>StairsRunJustification</span><span>.</span><span>Center</span><span>);</span><span>
                newRun2</span><span>.</span><span>ActualRunWidth</span><span> </span><span>=</span><span> </span><span>10</span><span>;</span><span>

                </span><span>// Add a landing between the runs</span><span>
                </span><span>CurveLoop</span><span> landingLoop </span><span>=</span><span> </span><span>new</span><span> </span><span>CurveLoop</span><span>();</span><span>
                XYZ p1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>15</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span> 
                XYZ p2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>20</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                XYZ p3 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>20</span><span>,</span><span> </span><span>-</span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                XYZ p4 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>15</span><span>,</span><span> </span><span>-</span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                </span><span>Line</span><span> curve_1 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p1</span><span>,</span><span> p2</span><span>);</span><span>
                </span><span>Line</span><span> curve_2 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p2</span><span>,</span><span> p3</span><span>);</span><span>
                </span><span>Line</span><span> curve_3 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p3</span><span>,</span><span> p4</span><span>);</span><span>
                </span><span>Line</span><span> curve_4 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p4</span><span>,</span><span> p1</span><span>);</span><span>

                landingLoop</span><span>.</span><span>Append</span><span>(</span><span>curve_1</span><span>);</span><span>
                landingLoop</span><span>.</span><span>Append</span><span>(</span><span>curve_2</span><span>);</span><span>
                landingLoop</span><span>.</span><span>Append</span><span>(</span><span>curve_3</span><span>);</span><span>
                landingLoop</span><span>.</span><span>Append</span><span>(</span><span>curve_4</span><span>);</span><span>
                </span><span>StairsLanding</span><span> newLanding </span><span>=</span><span> </span><span>StairsLanding</span><span>.</span><span>CreateSketchedLanding</span><span>(</span><span>document</span><span>,</span><span> newStairsId</span><span>,</span><span> landingLoop</span><span>,</span><span> newRun1</span><span>.</span><span>TopElevation</span><span>);</span><span>

                stairsTrans</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
            </span><span>// A failure preprocessor is to handle possible failures during the edit mode commitment process.</span><span>
            newStairsScope</span><span>.</span><span>Commit</span><span>(</span><span>new</span><span> </span><span>StairsFailurePreprocessor</span><span>());</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> newStairsId</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The stairs resulting from the above example:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/stairs.jpg)

### Multistory Stairs

The MultistoryStairs class allows stairs to span multiple levels. A multistory stairs element may contain multiple stairs whose extents are governed by base and top levels.

This element will contain one or more Stairs elements. Stairs elements are either:

-   a reference instance which is copied to each level covered by groups of identical stairs instances which share the same level height,
-   or individual Stairs instances which are not connected to a group with the same level height.

By default, when adding new levels to the multistory stair, new stairs will be added to the group. For groups of duplicate stairs at different levels, the instances can be found as Subelements of the Stairs element.Stairs in a connected group can be edited together by modifying the associated Stairs instance. For specific floors that need special designs, stairs can be separated from the group with the Unpin method - changes made to the unpinned Stairs will not affect other any other instance in the element. The stairs can later be added back into the group with the Pin method, however any changes made to the stair will be lost since the stair's properties will be overridden by the group specifications.

<table summary="" id="GUID-C60041FB-069E-4C89-BE67-A0593E790995__TABLE_5A15394B6A7F461183B0F3F352AD4E65"><tbody><tr><td><b>Code Region: Create Multistory Stairs</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateMultiStory</span><span>(</span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> doc </span><span>=</span><span> stairs</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>// create new MultistoryStairs </span><span>
    </span><span>MultistoryStairs</span><span> multistoryStairs </span><span>=</span><span> </span><span>MultistoryStairs</span><span>.</span><span>Create</span><span>(</span><span>stairs</span><span>);</span><span>

    </span><span>// get all levels that can be connected to this multistoryStairs</span><span>
    </span><span>IEnumerable</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> levelIds </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>).</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Level</span><span>)).</span><span>Cast</span><span>&lt;</span><span>Level</span><span>&gt;().</span><span>Where</span><span>(</span><span>q </span><span>=&gt;</span><span> multistoryStairs</span><span>.</span><span>CanConnectLevel</span><span>(</span><span>q</span><span>.</span><span>Id</span><span>))</span><span>
    </span><span>.</span><span>Select</span><span>(</span><span>q </span><span>=&gt;</span><span> q</span><span>.</span><span>Id</span><span>);</span><span>

    </span><span>// Connect the levels to the multistoryStairs</span><span>
    </span><span>// The input to ConnectLevels is a HashSet or SortedSet, so a HashSet is created from the IEnumerable returned by FilteredElementCollector</span><span>
    multistoryStairs</span><span>.</span><span>ConnectLevels</span><span>(</span><span>new</span><span> </span><span>HashSet</span><span>&lt;</span><span>ElementId</span><span>&gt;(</span><span>levelIds</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

When new stairs are created using the StairsEditScope.Start(ElementId, ElementId) method, they have default railings associated with them. However, the Railing.Create() method can be used to create new railings with the specified railing type on all sides of a stairs element for stairs without railings. Unlike run and landing creation which require the use of StairsEditScope, railing creation cannot be performed inside an open stairs editing session.

Since railings cannot be created for Stairs that already have railings associated with them, the following example deletes the existing railings associated with a Stairs object before creating new railings.

<table summary="" id="GUID-C60041FB-069E-4C89-BE67-A0593E790995__TABLE_98420E0FE5DF4223B8A16C10216E7078"><tbody><tr><td><b>Code Region: Create Railings</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CreateRailing</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Stairs</span><span> stairs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> trans </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Create Railings"</span><span>))</span><span>
    </span><span>{</span><span>
        trans</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// Delete existing railings</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> railingIds </span><span>=</span><span> stairs</span><span>.</span><span>GetAssociatedRailings</span><span>();</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> railingId </span><span>in</span><span> railingIds</span><span>)</span><span>
        </span><span>{</span><span>
            document</span><span>.</span><span>Delete</span><span>(</span><span>railingId</span><span>);</span><span>
        </span><span>}</span><span>
        </span><span>// Find RailingType</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> </span><span>RailingTypeIds</span><span> </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>RailingType</span><span>)).</span><span>ToElementIds</span><span>();</span><span>
        </span><span>Railing</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> stairs</span><span>.</span><span>Id</span><span>,</span><span> </span><span>RailingTypeIds</span><span>.</span><span>First</span><span>(),</span><span> </span><span>RailingPlacementPosition</span><span>.</span><span>Treads</span><span>);</span><span>
        trans</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
