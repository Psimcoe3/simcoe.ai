---
created: 2026-01-28T20:53:44 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_Getting_Element_Geometry_and_AnalyticalModel_html
author: 
---

# Help | Getting Element Geometry and AnalyticalElement | Autodesk

> ## Excerpt
> After new elements are created or elements are modified, regeneration and auto-joining of elements is required to propagate the changes throughout the model. Without a regeneration (and auto-join, when relevant), the Geometry property and the AnalyticalElement for Elements are either unobtainable (in the case of creating a new element) or they may be invalid. It is important to understand how and when regeneration occurs before accessing the Geometry or AnalyticalElement of an Element.

---
After new elements are created or elements are modified, regeneration and auto-joining of elements is required to propagate the changes throughout the model. Without a regeneration (and auto-join, when relevant), the Geometry property and the AnalyticalElement for Elements are either unobtainable (in the case of creating a new element) or they may be invalid. It is important to understand how and when regeneration occurs before accessing the Geometry or AnalyticalElement of an Element.

Although regeneration and auto-join are necessary to propagate changes made in the model, it can be time consuming. It is best if these events occur only as often as necessary.

Regeneration and auto-joining occur automatically when a transaction that modifies the model is committed successfully, or whenever the Document.Regenerate() or Document.AutoJoinElements() methods are called. Regenerate() and AutoJoinElements() may only be called inside an open transaction. It should be noted that the Regeneration() method can fail, in which case the RegenerationFailedException will be thrown. If this happens, the changes to the document need to be rolled back by rolling back the current transaction or subtransaction.

For more information, see [Analytical Element](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Analytical_Model_html) and [Geometry](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_html).

The following sample program demonstrates how a transaction populates these properties:

<table summary="" id="GUID-37357B53-1A5F-4913-BD59-BD4171BABE5E__TABLE_6E16CB4DD4D045479B35CBC78998C92E"><tbody><tr><td><b>Code Region 23-3: Transaction populating Geometry and AnalyticalPanel properties</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>TransactionDuringElementCreation</span><span>(</span><span>UIApplication</span><span> uiApplication</span><span>,</span><span> </span><span>Level</span><span> level</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document </span><span>=</span><span> uiApplication</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>

    </span><span>// Build a location line for the wall creation</span><span>
    XYZ start </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ </span><span>end</span><span> </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Line</span><span> geomLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>start</span><span>,</span><span> </span><span>end</span><span>);</span><span>

    </span><span>// All and any transaction should be enclosed in a 'using'</span><span>
    </span><span>// block or guarded within a try-catch-finally blocks</span><span>
    </span><span>// to guarantee that a transaction does not out-live its scope.</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> wallTransaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Creating wall"</span><span>))</span><span>
    </span><span>{</span><span>
       </span><span>// To create a wall, a transaction must be first started</span><span>
       </span><span>if</span><span> </span><span>(</span><span>wallTransaction</span><span>.</span><span>Start</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Started</span><span>)</span><span>
       </span><span>{</span><span>
           </span><span>// Create a wall using the location line</span><span>
           </span><span>Wall</span><span> wall </span><span>=</span><span> </span><span>Wall</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> geomLine</span><span>,</span><span> level</span><span>.</span><span>Id</span><span>,</span><span> </span><span>true</span><span>);</span><span>

           </span><span>// the transaction must be committed before you can</span><span>
           </span><span>// get the value of Geometry and AnalyticalPanel.</span><span>

           </span><span>if</span><span> </span><span>(</span><span>wallTransaction</span><span>.</span><span>Commit</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Committed</span><span>)</span><span>
           </span><span>{</span><span>
               </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Options</span><span> options </span><span>=</span><span> uiApplication</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewGeometryOptions</span><span>();</span><span>
               </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geoelem </span><span>=</span><span> wall</span><span>.</span><span>get_Geometry</span><span>(</span><span>options</span><span>);</span><span>
               </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Structure</span><span>.</span><span>AnalyticalPanel</span><span> analyticalPanel </span><span>=</span><span> </span><span>(</span><span>AnalyticalPanel</span><span>)</span><span>document</span><span>.</span><span>GetElement</span><span>(</span><span>AnalyticalToPhysicalAssociationManager</span><span>.</span><span>GetAnalyticalToPhysicalAssociationManager</span><span>(</span><span>document</span><span>).</span><span>GetAssociatedElementId</span><span>(</span><span>wall</span><span>.</span><span>Id</span><span>));</span><span>
           </span><span>}</span><span>
       </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The transaction timeline for this sample is as follows:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-A7296713-19E7-4C50-A7B6-F3F7893A8EDD-low.png)**Figure 134: Transaction timeline**
