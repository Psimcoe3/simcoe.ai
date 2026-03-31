---
created: 2026-01-28T21:20:25 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Workshared_File_Management_html
author: 
---

# Help | Workshared File Management | Autodesk

> ## Excerpt
> There are several Document methods for use with a workshared project file.

---
There are several Document methods for use with a workshared project file.

### Enable Worksharing

If a document is not already workshared, which can be determined from the Document.IsWorkshared property, worksharing can be enabled via the Revit API using the Document.EnableWorksharing() method. The document's Undo history will be cleared by this command, therefore this command and others executed before it cannot be undone. Additionally, all transaction phases (e.g. transactions, transaction groups and sub-transactions) that were explicitly started must be finished prior to calling EnableWorksharing().

#### Worksharing in the Cloud

-   Document.EnableCloudWorksharing() converts a cloud model into a workshared cloud model.
-   Document.CanEnableCloudWorksharing() can be used to check whether this operation is valid on a given model.

### Reload Latest

The method Document.ReloadLatest() retrieves changes from the central model (due to one or more synchronizations with central) and merges them into the current session.

The following examples uses ReloadLatest() to update the current session after confirming with the user that it is OK to do so.

<table summary="" id="GUID-95A89253-7B8C-43A6-BE90-0C7B90FA237F__TABLE_AF79DB8A57A949DFB2D9C364E4503AD1"><tbody><tr><td><b>Code Region: Reload from Central</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>ReloadLatestWithMessage</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Tell user what we're doing</span><span>
    </span><span>TaskDialog</span><span> td </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Alert"</span><span>);</span><span>
    td</span><span>.</span><span>MainInstruction</span><span> </span><span>=</span><span> </span><span>"Application 'Automatic element creator' needs to reload changes from central in order to proceed."</span><span>;</span><span>
    td</span><span>.</span><span>MainContent</span><span> </span><span>=</span><span> </span><span>"This will update your local with all changes currently in the central model.  This operation "</span><span> </span><span>+</span><span>
                        </span><span>"may take some time depending on the number of changes available on the central."</span><span>;</span><span>
    td</span><span>.</span><span>CommonButtons</span><span> </span><span>=</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>Ok</span><span> </span><span>|</span><span> </span><span>TaskDialogCommonButtons</span><span>.</span><span>Cancel</span><span>;</span><span>

    </span><span>TaskDialogResult</span><span> result </span><span>=</span><span> td</span><span>.</span><span>Show</span><span>();</span><span>

    </span><span>if</span><span> </span><span>(</span><span>result </span><span>==</span><span> </span><span>TaskDialogResult</span><span>.</span><span>Ok</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// There are no currently customizable user options for ReloadLatest.</span><span>
        doc</span><span>.</span><span>ReloadLatest</span><span>(</span><span>new</span><span> </span><span>ReloadLatestOptions</span><span>());</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Proceeding..."</span><span>,</span><span> </span><span>"Reload operation completed, proceeding with updates."</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Canceled."</span><span>,</span><span> </span><span>"Reload operation canceled, so changes will not be made.  Return to this command later when ready to reload."</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Synchronizing with Central Model

The method Document.SynchronizeWithCentral() reloads any changes from the central model so that the current session is up to date and then saves local changes back to central. A save to central is performed even if no changes were made.

When using SynchronizeWithCentral(), options can be specified for accessing the central model as well as synchronizing with it. The main option for accessing the central is to determine how the call should behave if the central model is locked. Since the synchronization requires a temporary lock on the central model, it cannot be performed if the model is already locked. The default behavior is to wait and repeatedly try to lock the central model in order to proceed with the synchronization. This behavior can be overridden using the TransactWithCentralOptions parameter of the SynchronizeWithCentral() method.

The SynchronizeWithCentralOptions parameter of the method is used to set options for the actual synchronization, such as whether elements or worksets owned by the current user should be relinquished during synchronization.

In the following example, an attempt is made to synchronize with a central model. If the central model is locked, it will immediately give up.

<table summary="" id="GUID-95A89253-7B8C-43A6-BE90-0C7B90FA237F__TABLE_79B7EEDC12AB4851ACA186D695869D4F"><tbody><tr><td><b>Code Region: Synchronize with Central</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SyncWithoutRelinquishing</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Set options for accessing central model</span><span>
    </span><span>TransactWithCentralOptions</span><span> transOpts </span><span>=</span><span> </span><span>new</span><span> </span><span>TransactWithCentralOptions</span><span>();</span><span>
    </span><span>SynchLockCallback</span><span> transCallBack </span><span>=</span><span> </span><span>new</span><span> </span><span>SynchLockCallback</span><span>();</span><span>
    </span><span>// Override default behavior of waiting to try again if the central model is locked</span><span>
    transOpts</span><span>.</span><span>SetLockCallback</span><span>(</span><span>transCallBack</span><span>);</span><span>

    </span><span>// Set options for synchronizing with central</span><span>
    </span><span>SynchronizeWithCentralOptions</span><span> syncOpts </span><span>=</span><span> </span><span>new</span><span> </span><span>SynchronizeWithCentralOptions</span><span>();</span><span>
    </span><span>// Sync without relinquishing any checked out elements or worksets</span><span>
    </span><span>RelinquishOptions</span><span> relinquishOpts </span><span>=</span><span> </span><span>new</span><span> </span><span>RelinquishOptions</span><span>(</span><span>false</span><span>);</span><span>
    syncOpts</span><span>.</span><span>SetRelinquishOptions</span><span>(</span><span>relinquishOpts</span><span>);</span><span>
    </span><span>// Do not automatically save local model after sync</span><span>
    syncOpts</span><span>.</span><span>SaveLocalAfter</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    syncOpts</span><span>.</span><span>Comment</span><span> </span><span>=</span><span> </span><span>"Changes to Workset1"</span><span>;</span><span>

    </span><span>try</span><span>
    </span><span>{</span><span>
        doc</span><span>.</span><span>SynchronizeWithCentral</span><span>(</span><span>transOpts</span><span>,</span><span> syncOpts</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>catch</span><span> </span><span>(</span><span>Exception</span><span> e</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Synchronize Failed"</span><span>,</span><span> e</span><span>.</span><span>Message</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span><span>

</span><span>class</span><span> </span><span>SynchLockCallback</span><span> </span><span>:</span><span> </span><span>ICentralLockedCallback</span><span>
</span><span>{</span><span>
    </span><span>// If unable to lock central, give up rather than waiting</span><span>
    </span><span>public</span><span> </span><span>bool</span><span> </span><span>ShouldWaitForLockAvailability</span><span>()</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> </span><span>false</span><span>;</span><span>
    </span><span>}</span><span>

</span><span>}</span></code></pre></td></tr></tbody></table>

In the next example, the user is given a message prior to synching, and is given options on whether to relinquish all elements when synchronizing, or keep worksets checked out.

<table summary="" id="GUID-95A89253-7B8C-43A6-BE90-0C7B90FA237F__TABLE_BD4FEF23BDD9450B8518FEEE643E8305"><tbody><tr><td><b>Code Region: Synchronize with Central With Message</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>void</span><span> </span><span>SynchWithCentralWithMessage</span><span>(</span><span>Document</span><span> doc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Checkout workset (for use with "keep checked out worksets" option later)</span><span>
    </span><span>FilteredWorksetCollector</span><span> fwc </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredWorksetCollector</span><span>(</span><span>doc</span><span>);</span><span>
    fwc</span><span>.</span><span>OfKind</span><span>(</span><span>WorksetKind</span><span>.</span><span>UserWorkset</span><span>);</span><span>
    </span><span>Workset</span><span> workset1 </span><span>=</span><span> fwc</span><span>.</span><span>First</span><span>&lt;</span><span>Workset</span><span>&gt;(</span><span>ws </span><span>=&gt;</span><span> ws</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Workset1"</span><span>);</span><span>

    </span><span>WorksharingUtils</span><span>.</span><span>CheckoutWorksets</span><span>(</span><span>doc</span><span>,</span><span> </span><span>new</span><span> </span><span>WorksetId</span><span>[]</span><span> </span><span>{</span><span> workset1</span><span>.</span><span>Id</span><span> </span><span>});</span><span>

    </span><span>// Make a change</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Add Level"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>
        </span><span>Level</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> </span><span>100</span><span>);</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>

    </span><span>// Tell user what we're doing</span><span>
    </span><span>TaskDialog</span><span> td </span><span>=</span><span> </span><span>new</span><span> </span><span>TaskDialog</span><span>(</span><span>"Alert"</span><span>);</span><span>
    td</span><span>.</span><span>MainInstruction</span><span> </span><span>=</span><span> </span><span>"Application 'Automatic element creator' has made changes and is prepared to synchronize with central."</span><span>;</span><span>
    td</span><span>.</span><span>MainContent</span><span> </span><span>=</span><span> </span><span>"This will update central with all changes currently made in the project by the application or by the user.  This operation "</span><span> </span><span>+</span><span>
                        </span><span>"may take some time depending on the number of changes made by the app and by the user."</span><span>;</span><span>

    td</span><span>.</span><span>AddCommandLink</span><span>(</span><span>TaskDialogCommandLinkId</span><span>.</span><span>CommandLink1</span><span>,</span><span> </span><span>"Do not synchronize at this time."</span><span>);</span><span>
    td</span><span>.</span><span>AddCommandLink</span><span>(</span><span>TaskDialogCommandLinkId</span><span>.</span><span>CommandLink2</span><span>,</span><span> </span><span>"Synchronize and relinquish all elements."</span><span>);</span><span>
    td</span><span>.</span><span>AddCommandLink</span><span>(</span><span>TaskDialogCommandLinkId</span><span>.</span><span>CommandLink3</span><span>,</span><span> </span><span>"Synchronize but keep checked out worksets."</span><span>);</span><span>
    td</span><span>.</span><span>DefaultButton</span><span> </span><span>=</span><span> </span><span>TaskDialogResult</span><span>.</span><span>CommandLink1</span><span>;</span><span>

    </span><span>TaskDialogResult</span><span> result </span><span>=</span><span> td</span><span>.</span><span>Show</span><span>();</span><span>

    </span><span>switch</span><span> </span><span>(</span><span>result</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>case</span><span> </span><span>TaskDialogResult</span><span>.</span><span>CommandLink1</span><span>:</span><span>
        </span><span>default</span><span>:</span><span>
            </span><span>{</span><span>
                </span><span>// Do not synch.  Nothing to do.</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>case</span><span> </span><span>TaskDialogResult</span><span>.</span><span>CommandLink2</span><span>:</span><span>
        </span><span>case</span><span> </span><span>TaskDialogResult</span><span>.</span><span>CommandLink3</span><span>:</span><span>
            </span><span>{</span><span>
                </span><span>// Prepare to synch</span><span>
                </span><span>// TransactWithCentralOptions has to do with the behavior related to locked or busy central models.</span><span>
                </span><span>// We'll use the default behavior.</span><span>
                </span><span>TransactWithCentralOptions</span><span> twcOpts </span><span>=</span><span> </span><span>new</span><span> </span><span>TransactWithCentralOptions</span><span>();</span><span>

                </span><span>// Setup synch-with-central options (add a comment about our change)</span><span>
                </span><span>SynchronizeWithCentralOptions</span><span> swcOpts </span><span>=</span><span> </span><span>new</span><span> </span><span>SynchronizeWithCentralOptions</span><span>();</span><span>
                swcOpts</span><span>.</span><span>Comment</span><span> </span><span>=</span><span> </span><span>"Synchronized by 'Automatic element creator' with user acceptance."</span><span>;</span><span>

                </span><span>if</span><span> </span><span>(</span><span>result </span><span>==</span><span> </span><span>TaskDialogResult</span><span>.</span><span>CommandLink3</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>// Setup relinquish options to keep user worksets checked out</span><span>
                    </span><span>RelinquishOptions</span><span> rOptions </span><span>=</span><span> </span><span>new</span><span> </span><span>RelinquishOptions</span><span>(</span><span>true</span><span>);</span><span>
                    rOptions</span><span>.</span><span>UserWorksets</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
                    swcOpts</span><span>.</span><span>SetRelinquishOptions</span><span>(</span><span>rOptions</span><span>);</span><span>
                </span><span>}</span><span>

                doc</span><span>.</span><span>SynchronizeWithCentral</span><span>(</span><span>twcOpts</span><span>,</span><span> swcOpts</span><span>);</span><span>

                </span><span>break</span><span>;</span><span>
            </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Create New Local Model

The WorksharingUtils.CreateNewLocal() method copies a central model to a new local file. This method does not open the new file. For an example of creating a new local model and opening it, see [Opening a Workshared Document](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Worksharing_Opening_a_Workshared_Document_html)
