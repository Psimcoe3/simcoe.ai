---
created: 2026-01-28T21:09:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Structural_Columns_Beams_and_Braces_html
author: 
---

# Help | Structural Columns, Beams and Braces | Autodesk

> ## Excerpt
> Structural column, beam, and brace elements are all represented by the FamilyInstance class. They are distinguished by the StructuralType property.

---
Structural column, beam, and brace elements are all represented by the FamilyInstance class. They are distinguished by the StructuralType property.

<table summary="" id="GUID-396E80E1-6E5D-4D10-9DE8-06A6AFCCEA36__TABLE_1B1A460E99DF46CB919556B2D14BC4F1"><tbody><tr><td><b>Code Region 29-1: Distinguishing between column, beam and brace</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetStructuralType</span><span>(</span><span>FamilyInstance</span><span> familyInstance</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>string</span><span> message </span><span>=</span><span> </span><span>""</span><span>;</span><span>
    </span><span>switch</span><span> </span><span>(</span><span>familyInstance</span><span>.</span><span>StructuralType</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>case</span><span> </span><span>StructuralType</span><span>.</span><span>Beam</span><span>:</span><span>
            message </span><span>=</span><span> </span><span>"FamilyInstance is a beam."</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>case</span><span> </span><span>StructuralType</span><span>.</span><span>Brace</span><span>:</span><span>
            message </span><span>=</span><span> </span><span>"FamilyInstance is a brace."</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>case</span><span> </span><span>StructuralType</span><span>.</span><span>Column</span><span>:</span><span>
            message </span><span>=</span><span> </span><span>"FamilyInstance is a column."</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>case</span><span> </span><span>StructuralType</span><span>.</span><span>Footing</span><span>:</span><span>
            message </span><span>=</span><span> </span><span>"FamilyInstance is a footing."</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>default</span><span>:</span><span>
            message </span><span>=</span><span> </span><span>"FamilyInstance is non-structural or unknown framing."</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>message</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

You can filter out FamilySymbol objects corresponding to structural columns, beams, and braces by using categories. The category for structural beams and braces is BuiltInCategory.OST\_StructuralFraming. The category for structural columns is BuiltInCategory.OST\_StructuralColumns.

<table summary="" id="GUID-396E80E1-6E5D-4D10-9DE8-06A6AFCCEA36__TABLE_FD81547DF68B4F1D9A2410E37BCB8AF1"><tbody><tr><td><b>Code Region 29-2: Using BuiltInCategory.OST_StructuralFraming</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetBeamAndColumnSymbols</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>List</span><span>&lt;</span><span>FamilySymbol</span><span>&gt;</span><span> columnTypes </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>FamilySymbol</span><span>&gt;();</span><span>
    </span><span>List</span><span>&lt;</span><span>FamilySymbol</span><span>&gt;</span><span> framingTypes </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>FamilySymbol</span><span>&gt;();</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> elements </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Family</span><span>)).</span><span>ToElements</span><span>();</span><span>

    </span><span>foreach</span><span>(</span><span>Element</span><span> element </span><span>in</span><span> elements</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Family</span><span> family </span><span>=</span><span> element </span><span>as</span><span> </span><span>Family</span><span>;</span><span>
        </span><span>Category</span><span> category </span><span>=</span><span> family</span><span>.</span><span>FamilyCategory</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> category</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> familySymbolIds </span><span>=</span><span> family</span><span>.</span><span>GetFamilySymbolIds</span><span>();</span><span>
            </span><span>if</span><span> </span><span>((</span><span>int</span><span>)</span><span>BuiltInCategory</span><span>.</span><span>OST_StructuralColumns </span><span>==</span><span> category</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> familySymbolIds</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>FamilySymbol</span><span> symbol </span><span>=</span><span> family</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>)</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
                    columnTypes</span><span>.</span><span>Add</span><span>(</span><span>symbol</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span> </span><span>if</span><span> </span><span>((</span><span>int</span><span>)</span><span>BuiltInCategory</span><span>.</span><span>OST_StructuralFraming </span><span>==</span><span> category</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> familySymbolIds</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>FamilySymbol</span><span> symbol </span><span>=</span><span> family</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>)</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
                    framingTypes</span><span>.</span><span>Add</span><span>(</span><span>symbol</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>string</span><span> message </span><span>=</span><span> </span><span>"Column Types: "</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>FamilySymbol</span><span> familySymbol </span><span>in</span><span> columnTypes</span><span>)</span><span>
    </span><span>{</span><span>
        message </span><span>+=</span><span> </span><span>"\n"</span><span> </span><span>+</span><span> familySymbol</span><span>.</span><span>Name</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>message</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

You can get and set beam setback properties with the FamilyInstance.ExtensionUtility property. If this property returns null, the beam setback can't be modified.

## BeamSystem

BeamSystem provides full access and edit ability to beam systems. You can get and set all of its properties, such as BeamSystemType, BeamType, Direction, and Level. BeamSystem.Direction is not limited to one line of edges. It can be set to any XYZ coordinate on the same plane with the BeamSystem.

Note: You cannot change the StructuralBeam AnalyticalModel after the Elevation property is changed in the UI or by the API. In the following picture the analytical model lines stay in the original location after BeamSystem Elevation is changed to 10 feet.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-95C4AA28-3733-4A65-A75B-0DA398063722-low.png)**Figure 156: Change BeamSystem elevation**
