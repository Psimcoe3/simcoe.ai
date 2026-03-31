---
created: 2026-01-28T21:18:32 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Failure_Posting_and_Handling_Handling_Failures_html
author: 
---

# Help | Handling Failures | Autodesk

> ## Excerpt
> Normally posted failures are processed by Revit's standard failure resolution UI at the end of a transaction (specifically when Transaction.Commit() or Transaction.Rollback() are invoked). The user is presented information and options to deal with the failures.

---
Normally posted failures are processed by Revit's standard failure resolution UI at the end of a transaction (specifically when Transaction.Commit() or Transaction.Rollback() are invoked). The user is presented information and options to deal with the failures.

If an operation (or set of operations) on the document requires some special treatment from a Revit add-in for certain errors, failure handling can be customized to carry out this resolution. Custom failure handling can be supplied:

-   For a given transaction using the interface IFailuresPreprocessor.
-   For all possible errors using the FailuresProcessing event.

Finally, the API offers the ability to completely replace the standard failure processing user interface using the interface IFailuresProcessor. Although the first two methods for handling failures should be sufficient in most cases, this last option can be used in special cases, such as to provide a better failure processing UI or when an application is used as a front-end on top of Revit.

### Overview of Failure Processing

It is important to remember there are many things happening between the call to Transaction.Commit() and the actual processing of failures. Auto-join, overlap checks, group checks and workset editability checks are just to name a few. These checks and changes may make some failures disappear or, more likely, can post new failures. Therefore, conclusions cannot be drawn about the state of failures to be processed when Transaction.Commit() is called. To process failures correctly, it is necessary to hook up to the actual failures processing mechanism.

When failures processing begins, all changes to a document that are supposed to be made in the transaction are made, and all failures are posted. Therefore, no uncontrolled changes to a document are allowed during failures processing. There is a limited ability to resolve failures via the restricted interface provided by FailuresAccessor. If this has happened, all end of transaction checks and failures processing have to be repeated. So there may be a few failure resolution cycles at the end of one transaction.

Each cycle of failures processing includes 3 steps:

1.  Preprocessing of failures (FailuresPreprocessor)
2.  Broadcasting of failures processing event (FailuresProcessing event)
3.  Final processing (FailuresProcessor)

Each of these 3 steps can control what happens next by returning different FailureProcessingResults. The options are:

-   _**Continue**_ - has no impact on execution flow. If FailuresProcessor returns "Continue" with unresolved failures, Revit will instead act as if "ProceedWithRollBack" was returned.
-   _**ProceedWithCommit**_ - interrupts failures processing and immediately triggers another loop of end-of-transaction checks followed by another failures processing. Should be returned after an attempt to resolve failures. Can easily lead to an infinite loop if returned without any successful failure resolution. Cannot be returned if transaction is already being rolled back and will be treated as "ProceedWithRollBack" in this case.
-   _**ProceedWithRollback**_ - continues execution of failure processing, but forces transaction to be rolled back, even if it was originally requested to commit. If before ProceedWithRollBack is returned FailureHandlingOptions are set to clear errors after rollback, no further error processing will take place, all failures will be deleted and transaction is rolled back silently. Otherwise default failure processing will continue, failures may be delivered to the user, but transaction is guaranteed to be rolled back.
-   _**WaitForUserInput**_ - Can be returned only by FailuresProcessor if it is waiting for an external event (typically user input) to complete failures processing.

Depending on the severity of failures posted in the transaction and whether the transaction is being committed or rolled back, each of these 3 steps may have certain options to resolve errors. All information about failures posted in a document, information about ability to perform certain operations to resolve failures and API to perform such operations are provided via the FailuresAccessor class. The Document can be used to obtain additional information, but it cannot be changed other than via FailuresAccessor.

### FailuresAccessor

A FailuresAccessor object is passed to each of failure processing steps as an argument and is the only available interface to fetch information about failures in a document. While reading from a document during failure processing is allowed, the only way to modify a document during failure resolution is via methods provided by this class. After returning from failure processing, the instance of the class is deactivated and cannot be used any longer.

#### Information Available from FailuresAccessor

The FailuresAccessor object offers some generic information such as:

-   Document for which failures are being processed or preprocessed
-   Highest severity of failures posted in the document
-   Transaction name and failure handling options for transaction being finished
-   Whether transaction was requested to be committed or rolled back.

The FailuresAccessor object also offers information about specific failures via the GetFailuresMessages() method.

#### Options to resolve failures

The FailuresAccessor object provides a few ways to resolve failures:

-   Failure messages with a severity of Warning can be deleted with the DeleteWarning() or DeleteAllWarnings() methods.
-   ResolveFailure() or ResolveFailures() methods can be used to resolve one or more failures using the last failure resolution type set for each failure.
-   DeleteElements() can resolve failures by deleting elements related to the failure.
-   Or delete all failure messages and replace them with one "generic" failure using the ReplaceFailures() method.
    
    ### IFailuresPreprocessor
    

The IFailuresPreprocessor interface can be used to provide custom failure handling for a specific transaction only. IFailuresPreprocessor is an interface that may be used to perform a preprocessing step to either filter out anticipated transaction failures or to post new failures. Failures can be "filtered out" by:

-   silently removing warnings that are known to be posted for the transaction and are deemed as irrelevant for the user in the context of a particular transaction
-   silently resolving certain failures that are known to be posted for the transaction and that should always be resolved in a context of a given transaction
-   silently aborting the transaction in cases where "imperfect" transactions should not be committed or aborting the transaction is preferable over user interaction for a given workflow.

The IFailuresPreprocessor interface gets control first during the failure resolution process. It is nearly equivalent to checking and resolving failures before finishing a transaction, except that IFailuresPreprocessor gets control at the right time, after all failures guaranteed to be posted and/or after all irrelevant ones are deleted.

There may be only one IFailuresPreprocessor per transaction and there is no default failure preprocessor. If one is not attached to the transaction (via the failure handling options), this first step of failure resolution is simply omitted.

<table summary="" id="GUID-52A45CC1-3BB4-48B4-BFC7-F6F8666C2AA4__TABLE_02F7FD0C66BF48ADAC64D7C8D87D43A4"><tbody><tr><td><b>Code Region 26-3: Handling failures from IFailuresPreprocessor</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>SwallowTransactionWarning</span><span> </span><span>:</span><span> </span><span>IExternalCommand</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> </span><span>Execute</span><span>(</span><span>ExternalCommandData</span><span> commandData</span><span>,</span><span> </span><span>ref</span><span> </span><span>string</span><span> message</span><span>,</span><span> </span><span>ElementSet</span><span> elements</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app </span><span>=</span><span>
                        commandData</span><span>.</span><span>Application</span><span>.</span><span>Application</span><span>;</span><span>
                </span><span>Document</span><span> doc </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>
                </span><span>UIDocument</span><span> uidoc </span><span>=</span><span> commandData</span><span>.</span><span>Application</span><span>.</span><span>ActiveUIDocument</span><span>;</span><span>

                </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
                </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> elementCollection </span><span>=</span><span>
                        collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Level</span><span>)).</span><span>ToElements</span><span>();</span><span>
                </span><span>Level</span><span> level </span><span>=</span><span> elementCollection</span><span>.</span><span>Cast</span><span>&lt;</span><span>Level</span><span>&gt;().</span><span>ElementAt</span><span>&lt;</span><span>Level</span><span>&gt;(</span><span>0</span><span>);</span><span>

                </span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>);</span><span>
                t</span><span>.</span><span>Start</span><span>(</span><span>"room"</span><span>);</span><span>
                </span><span>FailureHandlingOptions</span><span> failOpt </span><span>=</span><span> t</span><span>.</span><span>GetFailureHandlingOptions</span><span>();</span><span>
                failOpt</span><span>.</span><span>SetFailuresPreprocessor</span><span>(</span><span>new</span><span> </span><span>RoomWarningSwallower</span><span>());</span><span>
                t</span><span>.</span><span>SetFailureHandlingOptions</span><span>(</span><span>failOpt</span><span>);</span><span>

                doc</span><span>.</span><span>Create</span><span>.</span><span>NewRoom</span><span>(</span><span>level</span><span>,</span><span> </span><span>new</span><span> UV</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span>
                t</span><span>.</span><span>Commit</span><span>();</span><span>

                </span><span>return</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span><span>
</span><span>public</span><span> </span><span>class</span><span> </span><span>RoomWarningSwallower</span><span> </span><span>:</span><span> </span><span>IFailuresPreprocessor</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>FailureProcessingResult</span><span> </span><span>PreprocessFailures</span><span>(</span><span>FailuresAccessor</span><span> failuresAccessor</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>IList</span><span>&lt;</span><span>FailureMessageAccessor</span><span>&gt;</span><span> failList </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>FailureMessageAccessor</span><span>&gt;();</span><span>
                </span><span>// Inside event handler, get all warnings</span><span>
                failList </span><span>=</span><span> failuresAccessor</span><span>.</span><span>GetFailureMessages</span><span>();</span><span>        
                </span><span>foreach</span><span> </span><span>(</span><span>FailureMessageAccessor</span><span> failure </span><span>in</span><span> failList</span><span>)</span><span>
                </span><span>{</span><span> 
                        </span><span>// check FailureDefinitionIds against ones that you want to dismiss,</span><span>
                        </span><span>FailureDefinitionId</span><span> failID </span><span>=</span><span> failure</span><span>.</span><span>GetFailureDefinitionId</span><span>();</span><span>
                        </span><span>// prevent Revit from showing Unenclosed room warnings</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>failID </span><span>==</span><span> </span><span>BuiltInFailures</span><span>.</span><span>RoomFailures</span><span>.</span><span>RoomNotEnclosed</span><span>)</span><span>
                        </span><span>{</span><span>
                                failuresAccessor</span><span>.</span><span>DeleteWarning</span><span>(</span><span>failure</span><span>);</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>

                </span><span>return</span><span> </span><span>FailureProcessingResult</span><span>.</span><span>Continue</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### FailuresProcessing Event

The FailuresProcessing event is most suitable for applications that want to provide custom failure handling without a user interface, either for the entire session or for many unrelated transactions. Some use cases for handling failures via this event are:

-   automatic removal of certain warnings and/or automatic resolving of certain errors based on office standards (or other criteria)
-   custom logging of failures

The FailuresProcessing event is raised after IFailuresPreprocessor (if any) has finished. It can have any number of handlers, and all of them will be invoked. Since event handlers have no way to return a value, the SetProcessingResult() on the event argument should be used to communicate status. Only Continue, ProceedWithRollback or ProceedWithCommit can be set.

The following example shows an event handler for the FailuresProcessing event.

<table summary="" id="GUID-52A45CC1-3BB4-48B4-BFC7-F6F8666C2AA4__TABLE_B81CB6C364F64D78936118530C4EF8F2"><tbody><tr><td><b>Code Region 26-4: Handling the FailuresProcessing Event</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>CheckWarnings</span><span>(</span><span>object</span><span> sender</span><span>,</span><span> </span><span>FailuresProcessingEventArgs</span><span> e</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>FailuresAccessor</span><span> fa </span><span>=</span><span> e</span><span>.</span><span>GetFailuresAccessor</span><span>();</span><span>
        </span><span>IList</span><span>&lt;</span><span>FailureMessageAccessor</span><span>&gt;</span><span> failList </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>FailureMessageAccessor</span><span>&gt;();</span><span>
        failList </span><span>=</span><span> fa</span><span>.</span><span>GetFailureMessages</span><span>();</span><span> </span><span>// Inside event handler, get all warnings</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>FailureMessageAccessor</span><span> failure </span><span>in</span><span> failList</span><span>)</span><span>
        </span><span>{</span><span> 
                </span><span>// check FailureDefinitionIds against ones that you want to dismiss,</span><span>
                </span><span>FailureDefinitionId</span><span> failID </span><span>=</span><span> failure</span><span>.</span><span>GetFailureDefinitionId</span><span>();</span><span>
                </span><span>// prevent Revit from showing Unenclosed room warnings</span><span>
                </span><span>if</span><span> </span><span>(</span><span>failID </span><span>==</span><span> </span><span>BuiltInFailures</span><span>.</span><span>RoomFailures</span><span>.</span><span>RoomNotEnclosed</span><span>)</span><span>
                </span><span>{</span><span>
                        fa</span><span>.</span><span>DeleteWarning</span><span>(</span><span>failure</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### FailuresProcessor

The IFailuresProcessor interface gets control last, after the FailuresProcessing event is processed. There is only one active IFailuresProcessor in a Revit session. To register a failures processor, derive a class from IFailuresProcessor and register it using the Application.RegisterFailuresProcessor() method. If there is previously registered failures processor, it is discarded. If a Revit add-in opts to register a failures processor for Revit that processor will become the default error handler for all Revit errors for the session and the standard Revit error dialog will not appear. If no failures processors are set, there is a default one in the Revit UI that invokes all regular Revit error dialogs. FailuresProcessor should only be overridden to replace the existing Revit failure UI with a custom failure resolution handler, which can be interactive or have no user interface.

If the RegisterFailuresProcessor() method is passed NULL, any transaction that has any failures is silently aborted (unless failures are resolved by first two steps of failures processing).

The IFailuresProcessor.ProcessFailures() method is allowed to return WaitForUserInput, which leaves the transaction pending. It is expected that in this case, FailuresProcessor leaves some UI on the screen that will eventually commit or rollback a pending transaction - otherwise the pending state will last indefinitely, essentially freezing the document.

The following example of implementing the IFailuresProcessor checks for a failure, deletes the failing elements and sets an appropriate message for the user.

<table summary="" id="GUID-52A45CC1-3BB4-48B4-BFC7-F6F8666C2AA4__TABLE_0C94C835C36D4E2C9FE8AA01C8DED3B3"><tbody><tr><td><b>Code Region 26-5: IFailuresProcessor</b></td></tr><tr><td><pre><code><span>[</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>Transaction</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Attributes</span><span>.</span><span>TransactionMode</span><span>.</span><span>Manual</span><span>)]</span><span>   
</span><span>public</span><span> </span><span>class</span><span> </span><span>MyFailuresUI</span><span> </span><span>:</span><span> </span><span>IExternalApplication</span><span>
</span><span>{</span><span>
        </span><span>static</span><span> </span><span>AddInId</span><span> m_appId </span><span>=</span><span> </span><span>new</span><span> </span><span>AddInId</span><span>(</span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"9F179363-B349-4541-823F-A2DDB2B86AF3"</span><span>));</span><span>
        </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> </span><span>OnStartup</span><span>(</span><span>UIControlledApplication</span><span> uiControlledApplication</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>IFailuresProcessor</span><span> myFailUI </span><span>=</span><span> </span><span>new</span><span> </span><span>FailUI</span><span>();</span><span>
                </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span>.</span><span>RegisterFailuresProcessor</span><span>(</span><span>myFailUI</span><span>);</span><span>
                </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>Result</span><span> </span><span>OnShutdown</span><span>(</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>class</span><span> </span><span>FailUI</span><span> </span><span>:</span><span> </span><span>IFailuresProcessor</span><span>
        </span><span>{</span><span>
                </span><span>public</span><span> </span><span>void</span><span> </span><span>Dismiss</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>// This method is being called in case of exception or document destruction to </span><span>
                        </span><span>// dismiss any possible pending failure UI that may have left on the screen</span><span>
                </span><span>}</span><span>

                </span><span>public</span><span> </span><span>FailureProcessingResult</span><span> </span><span>ProcessFailures</span><span>(</span><span>FailuresAccessor</span><span> failuresAccessor</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>IList</span><span>&lt;</span><span>FailureResolutionType</span><span>&gt;</span><span> resolutionTypeList </span><span>=</span><span>
                                </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>FailureResolutionType</span><span>&gt;();</span><span> 
                        </span><span>IList</span><span>&lt;</span><span>FailureMessageAccessor</span><span>&gt;</span><span> failList </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>FailureMessageAccessor</span><span>&gt;();</span><span>
                        </span><span>// Inside event handler, get all warnings</span><span>
                        failList </span><span>=</span><span> failuresAccessor</span><span>.</span><span>GetFailureMessages</span><span>();</span><span> 
                        </span><span>string</span><span> errorString </span><span>=</span><span> </span><span>""</span><span>;</span><span>
                        </span><span>bool</span><span> hasFailures </span><span>=</span><span> </span><span>false</span><span>;</span><span>
                        </span><span>foreach</span><span> </span><span>(</span><span>FailureMessageAccessor</span><span> failure </span><span>in</span><span> failList</span><span>)</span><span>
                        </span><span>{</span><span>

                                </span><span>// check how many resolutions types were attempted to try to prevent</span><span>
                                </span><span>// entering infinite loop</span><span>
                                resolutionTypeList </span><span>=</span><span> 
                                        failuresAccessor</span><span>.</span><span>GetAttemptedResolutionTypes</span><span>(</span><span>failure</span><span>);</span><span>
                                </span><span>if</span><span> </span><span>(</span><span>resolutionTypeList</span><span>.</span><span>Count</span><span> </span><span>&gt;=</span><span> </span><span>3</span><span>)</span><span>
                                </span><span>{</span><span>
                                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> </span><span>"Cannot resolve failures - transaction will be rolled back."</span><span>);</span><span>
                                        </span><span>return</span><span> </span><span>FailureProcessingResult</span><span>.</span><span>ProceedWithRollBack</span><span>;</span><span>
                                </span><span>}</span><span>

                                errorString </span><span>+=</span><span> </span><span>"IDs "</span><span>;</span><span>
                                </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> failure</span><span>.</span><span>GetFailingElementIds</span><span>())</span><span>
                                </span><span>{</span><span>
                                        errorString </span><span>+=</span><span> id </span><span>+</span><span> </span><span>", "</span><span>;</span><span>
                                        hasFailures </span><span>=</span><span> </span><span>true</span><span>;</span><span>
                                </span><span>}</span><span>
                                errorString </span><span>+=</span><span> </span><span>"\nWill be deleted because: "</span><span> </span><span>+</span><span> failure</span><span>.</span><span>GetDescriptionText</span><span>()</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
                                failuresAccessor</span><span>.</span><span>DeleteElements</span><span>(</span><span>
                                                        failure</span><span>.</span><span>GetFailingElementIds</span><span>()</span><span> </span><span>as</span><span> </span><span>IList</span><span>&lt;</span><span>ElementId</span><span>&gt;);</span><span>
                        </span><span>}</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>hasFailures</span><span>)</span><span>
                        </span><span>{</span><span>
                                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Error"</span><span>,</span><span> errorString</span><span>);</span><span>
                                </span><span>return</span><span> </span><span>FailureProcessingResult</span><span>.</span><span>ProceedWithCommit</span><span>;</span><span>
                        </span><span>}</span><span>

                        </span><span>return</span><span> </span><span>FailureProcessingResult</span><span>.</span><span>Continue</span><span>;</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
