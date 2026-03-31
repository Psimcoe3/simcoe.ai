---
created: 2026-01-28T20:59:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_Managing_family_types_and_parameters_html
author: 
---

# Help | Managing family types and parameters | Autodesk

> ## Excerpt
> Family documents provide access to the FamilyManager property. The FamilyManager class provides access to family types and parameters. Using this class you can add and remove types, add and remove family and shared parameters, set the value for parameters in different family types, and define formulas to drive parameter values.

---
Family documents provide access to the FamilyManager property. The FamilyManager class provides access to family types and parameters. Using this class you can add and remove types, add and remove family and shared parameters, set the value for parameters in different family types, and define formulas to drive parameter values.

### Getting Types in a Family

The FamilyManager can be used to iterate through the types in a family, as the following example demonstrates.

<table summary="" id="GUID-F57B09C0-1AFD-4BE5-8288-A187EC983797__TABLE_2945ADD5B47740C7B630C19EB1AEB007"><tbody><tr><td><b>Code Region 13-11: Getting the types in a family</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetFamilyTypesInFamily</span><span>(</span><span>Document</span><span> familyDoc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>if</span><span> </span><span>(</span><span>familyDoc</span><span>.</span><span>IsFamilyDocument</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>FamilyManager</span><span> familyManager </span><span>=</span><span> familyDoc</span><span>.</span><span>FamilyManager</span><span>;</span><span>

        </span><span>// get types in family</span><span>
        </span><span>string</span><span> types </span><span>=</span><span> </span><span>"Family Types: "</span><span>;</span><span>
        </span><span>FamilyTypeSet</span><span> familyTypes </span><span>=</span><span> familyManager</span><span>.</span><span>Types</span><span>;</span><span>
        </span><span>FamilyTypeSetIterator</span><span> familyTypesItor </span><span>=</span><span> familyTypes</span><span>.</span><span>ForwardIterator</span><span>();</span><span>
        familyTypesItor</span><span>.</span><span>Reset</span><span>();</span><span>
        </span><span>while</span><span> </span><span>(</span><span>familyTypesItor</span><span>.</span><span>MoveNext</span><span>())</span><span>
        </span><span>{</span><span>
            </span><span>FamilyType</span><span> familyType </span><span>=</span><span> familyTypesItor</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>FamilyType</span><span>;</span><span>
            types </span><span>+=</span><span> </span><span>"\n"</span><span> </span><span>+</span><span> familyType</span><span>.</span><span>Name</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>types</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-60AB2EDC-BC4E-4E08-8922-38ECF4B7F991-low.png)**Figure 53: Family types in Concrete-Rectangular-Column family**

### Editing FamilyTypes

FamilyManager provides the ability to iterate through existing types in a family, and add and modify types and their parameters.

The following example shows how to add a new type, set its parameters and then assign the new type to a FamilyInstance. Type editing is done on the current type by using the Set() function. The current type is available from the CurrentType property. The CurrentType property can be used to set the current type before editing, or use the NewType() function which creates a new type and sets it to the current type for editing.

Note that once the new type is created and modified, Document.LoadFamily() is used to load the family back into the Revit project to make the new type available.

<table summary="" id="GUID-F57B09C0-1AFD-4BE5-8288-A187EC983797__TABLE_06358C4D5C5F41C382BE2BD5EBB8E9E9"><tbody><tr><td><b>Code Region 13-12: Editing Family Types</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>EditFamilyTypes</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> familyInstance</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// example works best when familyInstance is a rectangular concrete element</span><span>

    </span><span>if</span><span> </span><span>((</span><span>null</span><span> </span><span>==</span><span> document</span><span>)</span><span> </span><span>||</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> familyInstance</span><span>.</span><span>Symbol</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span>;</span><span>   </span><span>// invalid arguments</span><span>
    </span><span>}</span><span>

    </span><span>// Get family associated with this</span><span>
    </span><span>Family</span><span> family </span><span>=</span><span> familyInstance</span><span>.</span><span>Symbol</span><span>.</span><span>Family</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> family</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span>;</span><span>    </span><span>// could not get the family</span><span>
    </span><span>}</span><span>

    </span><span>// Get Family document for family</span><span>
    </span><span>Document</span><span> familyDoc </span><span>=</span><span> document</span><span>.</span><span>EditFamily</span><span>(</span><span>family</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> familyDoc</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span>;</span><span>    </span><span>// could not open a family for edit</span><span>
    </span><span>}</span><span>

    </span><span>FamilyManager</span><span> familyManager </span><span>=</span><span> familyDoc</span><span>.</span><span>FamilyManager</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> familyManager</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span>;</span><span>  </span><span>// cuould not get a family manager</span><span>
    </span><span>}</span><span>

    </span><span>// Start transaction for the family document</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> newFamilyTypeTransaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>familyDoc</span><span>,</span><span> </span><span>"Add Type to Family"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>int</span><span> changesMade </span><span>=</span><span> </span><span>0</span><span>;</span><span>
        newFamilyTypeTransaction</span><span>.</span><span>Start</span><span>();</span><span>

        </span><span>// add a new type and edit its parameters</span><span>
        </span><span>FamilyType</span><span> newFamilyType </span><span>=</span><span> familyManager</span><span>.</span><span>NewType</span><span>(</span><span>"2X2"</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>newFamilyType </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// look for 'b' and 'h' parameters and set them to 2 feet</span><span>
            </span><span>FamilyParameter</span><span> familyParam </span><span>=</span><span> familyManager</span><span>.</span><span>get_Parameter</span><span>(</span><span>"b"</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> familyParam</span><span>)</span><span>
            </span><span>{</span><span>
                familyManager</span><span>.</span><span>Set</span><span>(</span><span>familyParam</span><span>,</span><span> </span><span>2.0</span><span>);</span><span>
                changesMade </span><span>+=</span><span> </span><span>1</span><span>;</span><span>
            </span><span>}</span><span>

            familyParam </span><span>=</span><span> familyManager</span><span>.</span><span>get_Parameter</span><span>(</span><span>"h"</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> familyParam</span><span>)</span><span>
            </span><span>{</span><span>
                familyManager</span><span>.</span><span>Set</span><span>(</span><span>familyParam</span><span>,</span><span> </span><span>2.0</span><span>);</span><span>
                changesMade </span><span>+=</span><span> </span><span>1</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>if</span><span> </span><span>(</span><span>2</span><span> </span><span>==</span><span> changesMade</span><span>)</span><span>   </span><span>// set both paramaters?</span><span>
        </span><span>{</span><span>
            newFamilyTypeTransaction</span><span>.</span><span>Commit</span><span>();</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>   </span><span>// could not make the change -&gt; should roll back </span><span>
        </span><span>{</span><span>
            newFamilyTypeTransaction</span><span>.</span><span>RollBack</span><span>();</span><span>
        </span><span>}</span><span>

        </span><span>// if could not make the change or could not commit it, we return</span><span>
        </span><span>if</span><span> </span><span>(</span><span>newFamilyTypeTransaction</span><span>.</span><span>GetStatus</span><span>()</span><span> </span><span>!=</span><span> </span><span>TransactionStatus</span><span>.</span><span>Committed</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>return</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// now update the Revit project with Family which has a new type</span><span>
    </span><span>LoadOpts</span><span> loadOptions </span><span>=</span><span> </span><span>new</span><span> </span><span>LoadOpts</span><span>();</span><span>

    </span><span>// This overload is necessary for reloading an edited family</span><span>
    </span><span>// back into the source document from which it was extracted</span><span>
    family </span><span>=</span><span> familyDoc</span><span>.</span><span>LoadFamily</span><span>(</span><span>document</span><span>,</span><span> loadOptions</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> family</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// find the new type and assign it to FamilyInstance</span><span>
        </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> familySymbolIds </span><span>=</span><span> family</span><span>.</span><span>GetFamilySymbolIds</span><span>();</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> familySymbolIds</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>FamilySymbol</span><span> familySymbol </span><span>=</span><span> family</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>)</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
            </span><span>if</span><span> </span><span>((</span><span>null</span><span> </span><span>!=</span><span> familySymbol</span><span>)</span><span> </span><span>&amp;&amp;</span><span> familySymbol</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"2X2"</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> changeSymbol </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Change Symbol Assignment"</span><span>))</span><span>
                </span><span>{</span><span>
                    changeSymbol</span><span>.</span><span>Start</span><span>();</span><span>
                    familyInstance</span><span>.</span><span>Symbol</span><span> </span><span>=</span><span> familySymbol</span><span>;</span><span>
                    changeSymbol</span><span>.</span><span>Commit</span><span>();</span><span>
                </span><span>}</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>class</span><span> </span><span>LoadOpts</span><span> </span><span>:</span><span> </span><span>IFamilyLoadOptions</span><span>
</span><span>{</span><span>
    </span><span>public</span><span> </span><span>bool</span><span> </span><span>OnFamilyFound</span><span>(</span><span>bool</span><span> familyInUse</span><span>,</span><span> </span><span>out</span><span> </span><span>bool</span><span> overwriteParameterValues</span><span>)</span><span>
    </span><span>{</span><span>
        overwriteParameterValues </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        </span><span>return</span><span> </span><span>true</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>bool</span><span> </span><span>OnSharedFamilyFound</span><span>(</span><span>Family</span><span> sharedFamily</span><span>,</span><span> </span><span>bool</span><span> familyInUse</span><span>,</span><span> </span><span>out</span><span> </span><span>FamilySource</span><span> source</span><span>,</span><span> </span><span>out</span><span> </span><span>bool</span><span> overwriteParameterValues</span><span>)</span><span>
    </span><span>{</span><span>
        source </span><span>=</span><span> </span><span>FamilySource</span><span>.</span><span>Family</span><span>;</span><span>
        overwriteParameterValues </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        </span><span>return</span><span> </span><span>true</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The FamilyManager class provides access to all the family parameters. This includes family built-in parameters, category built-in parameters and shared parameters associated to the family types. There are two ways to get the family parameters:

-   Parameters property - gets all parameters in the family
-   GetParameters() - gets all the parameters in the family in order in which they appear in the Revit UI When using the GetParameters() method, the Revit UI order is determined first by group and next by the order of the individual parameters.

Family parameters can be reordered (within their groups) from the API for a given family (with the exception of the Rebar Shape family which does not support reordering parameters). This allows for parameters to be presented to the user in the most logical order. Sorting only affects visible parameters within the same parameter group. Parameters that belong to different groups will remain separated, and the groups' order will not be affected.

The simplest way to reorder parameters is using the FamilyManager.SortParameters() method, which takes a parameter indicating the desired sort order. The sample below sorts the parameters in ascending order.

| Code Region: Sort family parameters |
| --- |
| 
```
private void DisplayParametersInAscendingOrder(Document familyDoc)
{
    FamilyManager familyManager = familyDoc.FamilyManager;
    familyManager.SortParameters(ParametersOrder.Ascending);
}
```

 |

Note: The sort is a one-time operation. When new parameters are added they will not be automatically sorted.

For more control over how parameters are sorted, use the FamilyManager.ReorderParameters() method which takes a list of family parameters in the new order. This list must include all the parameters returned by the GetParameters() method, including any invisible parameters, or an exception will be thrown.
