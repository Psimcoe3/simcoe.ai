---
created: 2026-01-28T20:35:38 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Walkthrough: Retrieve Selected Elements | Autodesk

> ## Excerpt
> This section introduces you to an add-in application that gets selected elements from Revit.

---
This section introduces you to an add-in application that gets selected elements from Revit.

In add-in applications, you can perform a specific operation on a specific element. For example, you can get or change an element's parameter value. Complete the following steps to get a parameter value:

1.  Create a new project and add the references as summarized in the previous walkthroughs.
2.  Use the UIApplication.ActiveUIDocument.Selection.GetElementIds() method to retrieve the selected elements.
3.  Create a .addin file as explained in previous walkthroughs.

GetElementIds() returns a collection of ElementIds of the selected elements. It can be iterated with a foreach loop. Use the Document.GetElement() method to get the Element object for each ElementId in the selection.

The following code is an example of how to retrieve the ids of the selected element.

<table summary="" id="GUID-C67BE1BC-50D6-403C-8458-61BEBADFC6CE__TABLE_302F3DC2772F4788A5FEE2300F6F2C3A"><tbody><tr><td><b>Code Region 2-7: Retrieving selected elements</b></td></tr><tr><td><pre><code><span>[</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>Transaction</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>TransactionMode</span><span>.</span><span>ReadOnly</span><span>)]</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>Document_Selection</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
    </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span>
        </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>try</span><span>
        </span><span>{</span><span>
            </span><span>// Select some elements in Revit before invoking this command</span><span>

            </span><span>// Get the handle of current document.</span><span>
            </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>.</span><span>ActiveUIDocument</span><span>;</span><span>

            </span><span>// Get the element selection of current document.</span><span>
            </span><span>Selection</span><span> selection </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>;</span><span>
            </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>

            </span><span>if</span><span> </span><span>(</span><span>0</span><span> </span><span>==</span><span> selectedIds</span><span>.</span><span>Count</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// If no elements selected.</span><span>
                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"You haven't selected any elements."</span><span>);</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span>
            </span><span>{</span><span>
                </span><span>String</span><span> info </span><span>=</span><span> </span><span>"Ids of selected elements in the document are: "</span><span>;</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
                </span><span>{</span><span>
                    info </span><span>+=</span><span> </span><span>"\n\t"</span><span> </span><span>+</span><span> id</span><span>.</span><span>IntegerValue</span><span>;</span><span>
                </span><span>}</span><span>

                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>info</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>catch</span><span> </span><span>(</span><span>Exception</span><span> e</span><span>)</span><span>
        </span><span>{</span><span>
            message </span><span>=</span><span> e</span><span>.</span><span>Message</span><span>;</span><span>
            </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Failed</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>/// &lt;/ExampleMethod&gt;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

After you get the selected elements, you can get the properties or parameters for the elements. For more information, see [Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_html).
