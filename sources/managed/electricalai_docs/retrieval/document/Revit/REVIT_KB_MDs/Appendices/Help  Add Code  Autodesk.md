---
created: 2026-01-28T21:27:02 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_Hello_World_for_VB_NET_Add_Code_html
author: 
---

# Help | Add Code | Autodesk

> ## Excerpt
> Add the following code to create the add-in. When writing the code in VB.NET, you must pay attention to key letter capitalization.

---
Add the following code to create the add-in. When writing the code in VB.NET, you must pay attention to key letter capitalization.

<table summary="" id="GUID-7B115A30-7186-41CE-82AE-5EDF315C47DD__TABLE_270359D4D0644072A6A1832957800CC2"><tbody><tr><td><b>Code Region 30-9: Hello World in VB.NET</b></td></tr><tr><td><pre><code><span>Imports</span><span> </span><span>System</span><span>

</span><span>Imports</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI
</span><span>Imports</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB

</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>Transaction</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>TransactionMode</span><span>.</span><span>ReadOnly</span><span>)&gt;</span><span> _
</span><span>Public</span><span> </span><span>Class</span><span> </span><span>HelloWorld</span><span>
</span><span>Implements</span><span> </span><span>IExternalCommand</span><span>
        </span><span>Public</span><span> </span><span>Function</span><span> </span><span>Execute</span><span>(</span><span>ByVal</span><span> revit </span><span>As</span><span> </span><span>ExternalCommandData</span><span>,</span><span> </span><span>ByRef</span><span> message </span><span>As</span><span> </span><span>String</span><span>,</span><span> _
                                                        </span><span>ByVal</span><span> elements </span><span>As</span><span> </span><span>ElementSet</span><span>)</span><span> </span><span>As</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> _
                                                        </span><span>Implements</span><span> </span><span>IExternalCommand</span><span>.</span><span>Execute</span><span>

                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Hello World"</span><span>)</span><span>
                </span><span>Return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Succeeded</span><span>

        </span><span>End</span><span> </span><span>Function</span><span>
</span><span>End</span><span> </span><span>Class</span></code></pre></td></tr></tbody></table>
