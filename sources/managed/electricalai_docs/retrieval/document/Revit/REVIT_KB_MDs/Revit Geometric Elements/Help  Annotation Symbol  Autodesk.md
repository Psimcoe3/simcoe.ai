---
created: 2026-01-28T21:00:42 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_Annotation_Symbol_html
author: 
---

# Help | Annotation Symbol | Autodesk

> ## Excerpt
> An annotation symbol is a symbol applied to a family to uniquely identify that family in a project.

---
An annotation symbol is a symbol applied to a family to uniquely identify that family in a project.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-75864163-28D5-496D-9077-98DFECA07E75-low.png)**Figure 76: Annotation Symbol with two leaders**

### Create and Delete

Annotation symbols can be created using the following overload of the Creation.Document.NewFamilyInstance() method:

<table summary="" id="GUID-83D2CDC1-19FE-4BEE-B915-015D7B0BD72D__TABLE_8B7650612D22449C9FBC0D3E9238C245"><tbody><tr><td><b>Code Region 16-6: Create a new Annotation Symbol</b></td></tr><tr><td><p><code>public FamilyInstance NewFamilyInstance Method (XYZ origin, FamilySymbol symbol, View specView)</code></p></td></tr></tbody></table>

The annotation symbol can be deleted using the Document.Delete() method.

### Add and Remove Leader

Add and remove leaders using the addLeader() and removeLeader() methods.

<table summary="" id="GUID-83D2CDC1-19FE-4BEE-B915-015D7B0BD72D__TABLE_A2E9307AE06C42289884199FEED72D32"><tbody><tr><td><b>Code Region 16-7: Using addLeader() and removeLeader()</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>AddAndRemoveLeaders</span><span>(</span><span>AnnotationSymbol</span><span> symbol</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// check if there are any leaders currently attached, and remove them</span><span>
    </span><span>IList</span><span>&lt;</span><span>Leader</span><span>&gt;</span><span> leaders </span><span>=</span><span> symbol</span><span>.</span><span>GetLeaders</span><span>();</span><span>

    </span><span>if</span><span> </span><span>(</span><span>leaders </span><span>!=</span><span> </span><span>null</span><span> </span><span>&amp;&amp;</span><span> leaders</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>for</span><span> </span><span>(</span><span>int</span><span> i </span><span>=</span><span> leaders</span><span>.</span><span>Count</span><span>;</span><span> i </span><span>&gt;</span><span> </span><span>0</span><span>;</span><span> i</span><span>--)</span><span>
        </span><span>{</span><span>
            symbol</span><span>.</span><span>removeLeader</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// add one new leader instead</span><span>
    symbol</span><span>.</span><span>addLeader</span><span>();</span><span>                                                    
</span><span>}</span></code></pre></td></tr></tbody></table>
