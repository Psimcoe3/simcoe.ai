---
created: 2026-01-28T21:20:05 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Worksets_html
author: 
---

# Help | Worksets | Autodesk

> ## Excerpt
> Worksets are a way to divide a set of elements in the Revit document into subsets for worksharing. There may be one or many worksets in a document.

---
Worksets are a way to divide a set of elements in the Revit document into subsets for worksharing. There may be one or many worksets in a document.

## Accessing worksets in the document

The document contains a WorksetTable which is a table containing references to all the worksets contained in that document. There is one WorksetTable for each document. There will be at least one default workset in the table, even if worksharing has not been enabled in the document. The Document.IsWorkshared property can be used to determine if worksharing has been enabled in the document. The WorksetTable class can be used to get the active workset (as shown in the example below) and to set the active workset, by calling SetActiveWorksetId()

<table summary="" id="GUID-4BC148EC-6288-495A-A6DD-1524F326B32C__TABLE_CF10A43D2F08444BA805431BFDFBA24F"><tbody><tr><td><b>Code Region: Get Active Workset</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Workset</span><span> </span><span>GetActiveWorkset</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
     </span><span>// Get the workset table from the document</span><span>
     </span><span>WorksetTable</span><span> worksetTable </span><span>=</span><span> doc</span><span>.</span><span>GetWorksetTable</span><span>();</span><span>
     </span><span>// Get the Id of the active workset</span><span>
     </span><span>WorksetId</span><span> activeId </span><span>=</span><span> worksetTable</span><span>.</span><span>GetActiveWorksetId</span><span>();</span><span>
     </span><span>// Find the workset with that Id</span><span>
     </span><span>Workset</span><span> workset </span><span>=</span><span> worksetTable</span><span>.</span><span>GetWorkset</span><span>(</span><span>activeId</span><span>);</span><span>
     </span><span>return</span><span> workset</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Filtering worksets

Since the Workset class is not derived from Element, use FilteredWorksetCollector to search, filter and iterate through a set of worksets. Conditions can be assigned to filter the worksets that are returned. If no condition is applied, this filter will access all of the worksets in the document. The WorksetKind enumerator is useful for filtering worksets as shown in the next example. The WorksetKind identifies the subdivision of worksets:

-   **User** - user managed worksets for 3D instance elements
-   **Family** - where family symbols & families are kept
-   **Standard** - where project standards live including system family types
-   **Other** - internally used worksets which should not typically be considered by applications
-   **View** - contain views and view-specific elements

<table summary="" id="GUID-4BC148EC-6288-495A-A6DD-1524F326B32C__TABLE_90B564C0C5184D3B9D796E987FC5E2F8"><tbody><tr><td><b>Code Region: Filtering Worksets</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetWorksetsInfo</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>String</span><span> message </span><span>=</span><span> </span><span>String</span><span>.</span><span>Empty</span><span>;</span><span>
    </span><span>// Enumerating worksets in a document and getting basic information for each</span><span>
    </span><span>FilteredWorksetCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredWorksetCollector</span><span>(</span><span>doc</span><span>);</span><span>

    </span><span>// find all user worksets</span><span>
    collector</span><span>.</span><span>OfKind</span><span>(</span><span>WorksetKind</span><span>.</span><span>UserWorkset</span><span>);</span><span>
    </span><span>IList</span><span>&lt;</span><span>Workset</span><span>&gt;</span><span> worksets </span><span>=</span><span> collector</span><span>.</span><span>ToWorksets</span><span>();</span><span>

    </span><span>// get information for each workset</span><span>
    </span><span>int</span><span> count </span><span>=</span><span> </span><span>3</span><span>;</span><span> </span><span>// show info for 3 worksets only</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Workset</span><span> workset </span><span>in</span><span> worksets</span><span>)</span><span>
    </span><span>{</span><span>
        message </span><span>+=</span><span> </span><span>"Workset : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>Name</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nUnique Id : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>UniqueId</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nOwner : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>Owner</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nKind : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>Kind</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nIs default : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>IsDefaultWorkset</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nIs editable : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>IsEditable</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nIs open : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>IsOpen</span><span>;</span><span>
        message </span><span>+=</span><span> </span><span>"\nIs visible by default : "</span><span> </span><span>+</span><span> workset</span><span>.</span><span>IsVisibleByDefault</span><span>;</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"GetWorksetsInfo"</span><span>,</span><span> message</span><span>);</span><span>

        </span><span>if</span><span> </span><span>(</span><span>0</span><span> </span><span>==</span><span> </span><span>--</span><span>count</span><span>)</span><span>
            </span><span>break</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Workset properties

The Workset class represents a workset in a Revit document. As is shown in the filtering worksets example above, the Workset class provides many properties to get information about a given workset, such as the owner and whether or not the workset is editable. These properties are read-only. To change the name of an existing workset, use the static method WorksetTable.RenameWorkset().

## Creating worksets

The static Workset.Create() method can be used to create a new workset in a given document with a specified name. Worksets can only be created in a document that has worksharing enabled and the name must be unique. The static method WorksetTable.IsWorksetNameUnique() will confirm if a given name is unique in the document. The following example demonstrates how to create a new workset.

<table summary="" id="GUID-4BC148EC-6288-495A-A6DD-1524F326B32C__TABLE_8BCDCF63042C4D0199A4E6312122F8A7"><tbody><tr><td><b>Code Region: Create a new workset</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Workset</span><span> </span><span>CreateWorkset</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Workset</span><span> newWorkset </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>// Worksets can only be created in a document with worksharing enabled</span><span>
    </span><span>if</span><span> </span><span>(</span><span>document</span><span>.</span><span>IsWorkshared</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>string</span><span> worksetName </span><span>=</span><span> </span><span>"New Workset"</span><span>;</span><span>
        </span><span>// Workset name must not be in use by another workset</span><span>
        </span><span>if</span><span> </span><span>(</span><span>WorksetTable</span><span>.</span><span>IsWorksetNameUnique</span><span>(</span><span>document</span><span>,</span><span> worksetName</span><span>))</span><span>
        </span><span>{</span><span>
            </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> worksetTransaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Set preview view id"</span><span>))</span><span>
            </span><span>{</span><span>
                worksetTransaction</span><span>.</span><span>Start</span><span>();</span><span>
                newWorkset </span><span>=</span><span> </span><span>Workset</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> worksetName</span><span>);</span><span>
                worksetTransaction</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> newWorkset</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
