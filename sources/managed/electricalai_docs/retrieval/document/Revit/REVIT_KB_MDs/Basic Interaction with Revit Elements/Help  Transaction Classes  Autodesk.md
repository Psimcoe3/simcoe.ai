---
created: 2026-01-28T20:53:30 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_Transaction_Classes_html
author: 
---

# Help | Transaction Classes | Autodesk

> ## Excerpt
> All three transaction objects share some common methods:

---
All three transaction objects share some common methods:

**Table 51: Common Transaction Object Methods**

<table summary="" id="GUID-BECA30DB-23B4-4E71-BE24-DC4DD176E52D__TABLE_34C100F27C4A4D70A1FFD309A7947A69"><tbody><tr><td><b>Method</b></td><td><b>Description</b></td></tr><tr><td>Start</td><td>Will start the context</td></tr><tr><td>Commit</td><td>Ends the context and commits all changes to the document</td></tr><tr><td>Rollback</td><td>Ends the context and discards all changes to the document</td></tr><tr><td>GetStatus</td><td>Returns the current status of the transaction object</td></tr></tbody></table>

In addition to the GetStatus() method returning the current status, the Start, Commit and RollBack methods also return a TransactionStatus indicating whether or not the method was successful. Available TransactionStatus values include:

**Table 52: TransactionStatus values**

<table summary="" id="GUID-BECA30DB-23B4-4E71-BE24-DC4DD176E52D__TABLE_C9A92B297B574CD18C8F55169F018EAC"><tbody><tr><td><b>Status</b></td><td><b>Description</b></td></tr><tr><td>Uninitialized</td><td>The initial value after object is instantiated; the context has not started yet</td></tr><tr><td>Started</td><td>Transaction object has successfully started (Start was called)</td></tr><tr><td>RolledBack</td><td>Transaction object was successfully rolled back (Rollback was called)</td></tr><tr><td>Committed</td><td>Transaction object was successfully committed (Commit was called)</td></tr><tr><td>Pending</td><td>Transaction object was attempted to be either submitted or rolled back, but due to failures that process could not be finished yet and is waiting for the end-user's response (in a modeless dialog). Once the failure processing is finished, the status will be automatically updated (to either Committed or RolledBack status).</td></tr></tbody></table>

### Transaction

A transaction is a context required in order to make any changes to a Revit model. Only one transaction can be open at a time; nesting is not allowed. Each transaction must have a name, which will be listed on the Undo menu in Revit once a transaction is successfully committed.

<table summary="" id="GUID-BECA30DB-23B4-4E71-BE24-DC4DD176E52D__TABLE_9B632B9A88174C848731232B27649C6E"><tbody><tr><td><b>Code Region 23-1: Using transactions</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreatingModelLines</span><span>(</span><span>UIApplication</span><span> uiApplication</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document </span><span>=</span><span> uiApplication</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> application </span><span>=</span><span> uiApplication</span><span>.</span><span>Application</span><span>;</span><span>

    </span><span>// Create a few geometry lines. These lines are not elements,</span><span>
    </span><span>// therefore they do not need to be created inside a document transaction.</span><span>
    XYZ </span><span>Point1</span><span> </span><span>=</span><span> XYZ</span><span>.</span><span>Zero</span><span>;</span><span>
    XYZ </span><span>Point2</span><span> </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ </span><span>Point3</span><span> </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ </span><span>Point4</span><span> </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>);</span><span>

    </span><span>Line</span><span> geomLine1 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>Point1</span><span>,</span><span> </span><span>Point2</span><span>);</span><span>
    </span><span>Line</span><span> geomLine2 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>Point4</span><span>,</span><span> </span><span>Point3</span><span>);</span><span>
    </span><span>Line</span><span> geomLine3 </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>Point1</span><span>,</span><span> </span><span>Point4</span><span>);</span><span>

    </span><span>// This geometry plane is also transaction and does not need a transaction</span><span>
    XYZ origin </span><span>=</span><span> XYZ</span><span>.</span><span>Zero</span><span>;</span><span>
    XYZ normal </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>);</span><span>
    </span><span>Plane</span><span> geomPlane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>CreateByNormalAndOrigin</span><span>(</span><span>normal</span><span>,</span><span> origin</span><span>);</span><span>

    </span><span>// In order to a sketch plane with model curves in it, we need</span><span>
    </span><span>// to start a transaction because such operations modify the model.</span><span>

    </span><span>// All and any transaction should be enclosed in a 'using'</span><span>
    </span><span>// block or guarded within a try-catch-finally blocks</span><span>
    </span><span>// to guarantee that a transaction does not out-live its scope.</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>transaction</span><span>.</span><span>Start</span><span>(</span><span>"Create model curves"</span><span>)</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Started</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// Create a sketch plane in current document</span><span>
            </span><span>SketchPlane</span><span> sketch </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span>geomPlane</span><span>);</span><span>

            </span><span>// Create a ModelLine elements using the geometry lines and sketch plane</span><span>
            </span><span>ModelLine</span><span> line1 </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewModelCurve</span><span>(</span><span>geomLine1</span><span>,</span><span> sketch</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelLine</span><span>;</span><span>
            </span><span>ModelLine</span><span> line2 </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewModelCurve</span><span>(</span><span>geomLine2</span><span>,</span><span> sketch</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelLine</span><span>;</span><span>
            </span><span>ModelLine</span><span> line3 </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewModelCurve</span><span>(</span><span>geomLine3</span><span>,</span><span> sketch</span><span>)</span><span> </span><span>as</span><span> </span><span>ModelLine</span><span>;</span><span>

            </span><span>// Ask the end user whether the changes are to be committed or not</span><span>
            </span><span>TaskDialog</span><span> taskDialog </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Revit"</span><span>);</span><span>
            taskDialog</span><span>.</span><span>MainContent</span><span> </span><span>=</span><span> </span><span>"Click either [OK] to Commit, or [Cancel] to Roll back the transaction."</span><span>;</span><span>
            </span><span>TaskDialogCommonButtons</span><span> buttons </span><span>=</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>Ok</span><span> </span><span>|</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>Cancel</span><span>;</span><span>
            taskDialog</span><span>.</span><span>CommonButtons</span><span> </span><span>=</span><span> buttons</span><span>;</span><span>

            </span><span>if</span><span> </span><span>(</span><span>TaskDialogResult</span><span>.</span><span>Ok</span><span> </span><span>==</span><span> taskDialog</span><span>.</span><span>Show</span><span>())</span><span>
            </span><span>{</span><span>
                </span><span>// For many various reasons, a transaction may not be committed</span><span>
                </span><span>// if the changes made during the transaction do not result a valid model.</span><span>
                </span><span>// If committing a transaction fails or is canceled by the end user,</span><span>
                </span><span>// the resulting status would be RolledBack instead of Committed.</span><span>
                </span><span>if</span><span> </span><span>(</span><span>TransactionStatus</span><span>.</span><span>Committed</span><span> </span><span>!=</span><span> transaction</span><span>.</span><span>Commit</span><span>())</span><span>
                </span><span>{</span><span>
                    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Failure"</span><span>,</span><span> </span><span>"Transaction could not be committed"</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span>
            </span><span>{</span><span>
                transaction</span><span>.</span><span>RollBack</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### SubTransaction

A SubTransaction can be used to enclose a set of model-modifying operations. Sub-transactions are optional. They are not required in order to modify the model. They are a convenience tool to allow logical splitting of larger tasks into smaller ones. Sub-transactions can only be created within an already opened transaction and must be closed (either committed or rolled back) before the transaction is closed (committed or rolled back). Unlike transactions, sub-transaction may be nested, but any nested sub-transaction must be closed before the enclosing sub-transaction is closed. Sub-transactions do not have a name, for they do not appear on the Undo menu in Revit.

### TransactionGroup

TransactionGroup allows grouping together several independent transactions, which gives the owner of a group an opportunity to address many transactions at once. When a transaction group is to be closed, it can be rolled back, which means that all previously committed transactions belonging to the group will be rolled back. If not rolled back, a group can be either committed or assimilated. In the former case, all committed transactions (within the group) will be left as they were. In the later case, transactions within the group will be merged together into one single transaction that will bear the group's name.

A transaction group can only be started when there is no transaction open yet, and must be closed only after all enclosed transactions are closed (rolled back or committed). Transaction groups can be nested, but any nested group must be closed before the enclosing group is closed. Transaction groups are optional. They are not required in order to make modifications to a model.

The following example shows the use of a TransactionGroup to combine two separate Transactions using the Assimilate() method. The following code will result in a single Undo item added to the Undo menu with the name "Level and Grid".

<table summary="" id="GUID-BECA30DB-23B4-4E71-BE24-DC4DD176E52D__TABLE_8FDAAAA048F842039B2B6820C17EB28E"><tbody><tr><td><b>Code Region 23-2: Combining multiple transactions into a TransactionGroup</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CompoundOperation</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// All and any transaction group should be enclosed in a 'using' block or guarded within</span><span>
    </span><span>// a try-catch-finally blocks to guarantee that the group does not out-live its scope.</span><span>
    </span><span>using</span><span> </span><span>(</span><span>TransactionGroup</span><span> transGroup </span><span>=</span><span> </span><span>new</span><span> </span><span>TransactionGroup</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Level and Grid"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>transGroup</span><span>.</span><span>Start</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Started</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// We are going to call two methods, each having its own local transaction.</span><span>
            </span><span>// For our compound operation to be considered successful, both the individual</span><span>
            </span><span>// transactions must succeed. If either one fails, we will roll our group back,</span><span>
            </span><span>// regardless of what transactions might have already been committed.</span><span>

            </span><span>if</span><span> </span><span>(</span><span>CreateLevel</span><span>(</span><span>document</span><span>,</span><span> </span><span>25.0</span><span>)</span><span> </span><span>&amp;&amp;</span><span> </span><span>CreateGrid</span><span>(</span><span>document</span><span>,</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span>0</span><span>,</span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span>0</span><span>,</span><span>0</span><span>)))</span><span>
            </span><span>{</span><span>
                </span><span>// The process of assimilating will merge the two (or any number of) committed</span><span>
                </span><span>// transaction together and will assign the grid's name to the one resulting transaction,</span><span>
                </span><span>// which will become the only item from this compound operation appearing in the undo menu.</span><span>
                transGroup</span><span>.</span><span>Assimilate</span><span>();</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span>
            </span><span>{</span><span>
                </span><span>// Since we could not successfully finish at least one of the individual</span><span>
                </span><span>// operation, we are going to roll the entire group back, which will</span><span>
                </span><span>// undo any transaction already committed while this group was open.</span><span>
                transGroup</span><span>.</span><span>RollBack</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>bool</span><span> </span><span>CreateLevel</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>double</span><span> elevation</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// All and any transaction should be enclosed in a 'using'</span><span>
    </span><span>// block or guarded within a try-catch-finally blocks</span><span>
    </span><span>// to guarantee that a transaction does not out-live its scope.</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Creating Level"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>// Must start a transaction to be able to modify a document</span><span>

        </span><span>if</span><span>(</span><span> </span><span>TransactionStatus</span><span>.</span><span>Started</span><span> </span><span>==</span><span> transaction</span><span>.</span><span>Start</span><span>())</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> </span><span>Level</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> elevation</span><span>))</span><span>
            </span><span>{</span><span>
                </span><span>// For many various reasons, a transaction may not be committed</span><span>
                </span><span>// if the changes made during the transaction do not result a valid model.</span><span>
                </span><span>// If committing a transaction fails or is canceled by the end user,</span><span>
                </span><span>// the resulting status would be RolledBack instead of Committed.</span><span>
                </span><span>return</span><span> </span><span>(</span><span>TransactionStatus</span><span>.</span><span>Committed</span><span> </span><span>==</span><span> transaction</span><span>.</span><span>Commit</span><span>());</span><span>
            </span><span>}</span><span>

            </span><span>// For we were unable to create the level, we will roll the transaction back</span><span>
            </span><span>// (although on this simplified case we know there weren't any other changes)</span><span>

            transaction</span><span>.</span><span>RollBack</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>return</span><span> </span><span>false</span><span>;</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>bool</span><span> </span><span>CreateGrid</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> XYZ p1</span><span>,</span><span> XYZ p2</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// All and any transaction should be enclosed in a 'using'</span><span>
    </span><span>// block or guarded within a try-catch-finally blocks</span><span>
    </span><span>// to guarantee that a transaction does not out-live its scope.</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Creating Grid"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>// Must start a transaction to be able to modify a document</span><span>
        </span><span>if</span><span> </span><span>(</span><span>TransactionStatus</span><span>.</span><span>Started</span><span> </span><span>==</span><span> transaction</span><span>.</span><span>Start</span><span>())</span><span>
        </span><span>{</span><span>
            </span><span>// We create a line and use it as an argument to create a grid</span><span>
            </span><span>Line</span><span> gridLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>p1</span><span>,</span><span> p2</span><span>);</span><span>

            </span><span>if</span><span> </span><span>((</span><span>null</span><span> </span><span>!=</span><span> gridLine</span><span>)</span><span> </span><span>&amp;&amp;</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> </span><span>Grid</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> gridLine</span><span>)))</span><span>
            </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>TransactionStatus</span><span>.</span><span>Committed</span><span> </span><span>==</span><span> transaction</span><span>.</span><span>Commit</span><span>())</span><span>
                </span><span>{</span><span>
                </span><span>return</span><span> </span><span>true</span><span>;</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>

            </span><span>// For we were unable to create the grid, we will roll the transaction back</span><span>
            </span><span>// (although on this simplified case we know there weren't any other changes)</span><span>

            transaction</span><span>.</span><span>RollBack</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>return</span><span> </span><span>false</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
