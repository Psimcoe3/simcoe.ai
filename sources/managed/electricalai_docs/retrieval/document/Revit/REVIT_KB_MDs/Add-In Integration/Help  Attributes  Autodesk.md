---
created: 2026-01-28T20:40:16 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Attributes | Autodesk

> ## Excerpt
> The Revit API provides several attributes for configuring ExternalCommand and ExternalApplication behavior.

---
The Revit API provides several attributes for configuring ExternalCommand and ExternalApplication behavior.

### TransactionAttribute

The custom attribute Autodesk.Revit.Attributes.TransactionMode must be applied to your implementation class of the IExternalCommand interface to control transaction behavior for the external command. There is no default for this option. This mode controls how the API framework expects transactions to be used when the command is invoked. The supported values are:

-   _TransactionMode.Manual_ - Revit will not create a transaction (but it will create an outer transaction group to roll back all changes if the external command returns a failure). Instead, you may use combinations of Transactions, SubTransactions, and TransactionGroups as you please. You will have to follow all rules regarding use of transactions and related classes. You will have to give your transactions names which will then appear in the Undo menu. Revit will check that all transactions (also groups and sub-transactions) are properly closed upon return from an external command. If not, Revit will discard all changes made to the model.
-   _TransactionMode.ReadOnly_ - No transaction (nor group) will be created, and no transaction may be created for the lifetime of the command. The External Command may only use methods that read from the model. Exceptions will be thrown if the command either tries to start a transaction (or group) or attempts to write to the model.

In either mode, the TransactionMode applies only to the active document. You may open other documents during the course of the command, and you may have complete control over the creation and use of Transactions, SubTransactions, and TransactionGroups on those other documents (even in ReadOnly mode).

For example, to set an external command to use manual transaction mode:

<table summary="" id="GUID-D1F0F04D-B4EA-49FA-806E-84153C507D7F__TABLE_65884741F68E479C9B980EB3AAE52155"><tbody><tr><td><b>Code Region 3-18: TransactionAttribute</b></td></tr><tr><td><pre><code><span>[</span><span>Transaction</span><span>(</span><span>TransactionMode</span><span>.</span><span>Manual</span><span>)]</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>CommandTransaction</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>
                </span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span>
                </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementSet</span><span> elements</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>// Command implementation, which modifies the active document directly </span><span>
                </span><span>// after starting a new transaction</span><span>
                </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

See [Transactions](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_html).

### JournalingAttribute

The custom attribute Autodesk.Revit.Attributes.JournalingAttribute can optionally be applied to your implementation class of the IExternalCommand interface to control the journaling behavior during the external command execution. There are two options for journaling:

-   _JournalMode.NoCommandData_ - Contents of the ExternalCommandData.JournalData map are not written to the Revit journal. This option allows Revit API calls to write to the journal as needed. This option allows commands which invoke the Revit UI for selection or responses to task dialogs to replay correctly.
-   _JournalMode.UsingCommandData_ - Uses the IDictionary<String, String> supplied in the command data. This will hide all Revit journal entries between the external command invocation and the IDictionary<String, String< entry. Commands which invoke the Revit UI for selection or responses to task dialogs may not replay correctly. This is the default if the JournalingAttribute is not specified.

<table summary="" id="GUID-D1F0F04D-B4EA-49FA-806E-84153C507D7F__TABLE_3E4CD54AC560492CB105A4375171A8A6"><tbody><tr><td><b>Code Region 3-19: JournalingAttribute</b></td></tr><tr><td><pre><code><span>[</span><span>Journaling</span><span>(</span><span>JournalingMode</span><span>.</span><span>UsingCommandData</span><span>)]</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>CommandJournal</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>
                </span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span> 
                </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementSet</span><span> elements</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
