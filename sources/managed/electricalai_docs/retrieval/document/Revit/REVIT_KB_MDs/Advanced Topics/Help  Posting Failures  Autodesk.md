---
created: 2026-01-28T21:18:28 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Failure_Posting_and_Handling_Posting_Failures_html
author: 
---

# Help | Posting Failures | Autodesk

> ## Excerpt
> To use the failure posting mechanism to report problems, the following steps are required:

---
To use the failure posting mechanism to report problems, the following steps are required:

1.  New failures not already defined in Revit must be defined and registered in the FailureDefinitionRegistry during the OnStartup() call of the ExternalApplication.
2.  Find the failure definition id, either from the BuiltInFailures classes or from the pre-registered custom failures using the class related to FailureDefinition.
3.  Post the failure to the document that has a problem using the classes related to FailureMessage to set options and details related to the failure.
    
    ### Defining and registering a failure
    

Each possible failure in Revit must be defined and registered during Revit application startup by creating a FailureDefinition object that contains some persistent information about the failure such as identity, severity, basic description, types of resolution and default resolution.

The following example creates two new failures, a warning and an error, that can be used for walls that are too tall. In this example, they are used in conjunction with an Updater that will do the failure posting (in a subsequent code sample in this chapter). The FailureDefinitionIds are saved in the Updater class since they will be required when posting failures. The sections following explain the FailureDefinition.CreateFailureDefinition() method parameters in more detail.

<table summary="" id="GUID-8AE4ADAF-82AB-4AC1-81A2-7A8DD9346055__TABLE_A909459E77B3435CBD87D86E1D7F66BD"><tbody><tr><td><b>Code Region 26-1: Defining and registering a failure</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>PostWallFailure</span><span>()</span><span>
</span><span>{</span><span>
    </span><span>WallWarnUpdater</span><span> wallUpdater </span><span>=</span><span> </span><span>new</span><span> </span><span>WallWarnUpdater</span><span>(</span><span>new</span><span> </span><span>AddInId</span><span>(</span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"F0F045A5-06E8-4C89-837D-8A8F85484953"</span><span>)));</span><span>
    </span><span>UpdaterRegistry</span><span>.</span><span>RegisterUpdater</span><span>(</span><span>wallUpdater</span><span>);</span><span>
    </span><span>ElementClassFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>Wall</span><span>));</span><span>
    </span><span>UpdaterRegistry</span><span>.</span><span>AddTrigger</span><span>(</span><span>wallUpdater</span><span>.</span><span>GetUpdaterId</span><span>(),</span><span> filter</span><span>,</span><span> </span><span>Element</span><span>.</span><span>GetChangeTypeGeometry</span><span>());</span><span>

    </span><span>// define a new failure id for a warning about walls</span><span>
    </span><span>FailureDefinitionId</span><span> warnId </span><span>=</span><span> </span><span>new</span><span> </span><span>FailureDefinitionId</span><span>(</span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"FB4F5AF3-42BB-4371-B559-FB1648D5B4D1"</span><span>));</span><span>

    </span><span>// register the new warning using FailureDefinition</span><span>
    </span><span>FailureDefinition</span><span> failDef </span><span>=</span><span> </span><span>FailureDefinition</span><span>.</span><span>CreateFailureDefinition</span><span>(</span><span>warnId</span><span>,</span><span> </span><span>FailureSeverity</span><span>.</span><span>Warning</span><span>,</span><span> </span><span>"Wall is too big (&gt;100'). Performance problems may result."</span><span>);</span><span>

    </span><span>FailureDefinitionId</span><span> failId </span><span>=</span><span> </span><span>new</span><span> </span><span>FailureDefinitionId</span><span>(</span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"691E5825-93DC-4f5c-9290-8072A4B631BC"</span><span>));</span><span>

    </span><span>FailureDefinition</span><span> failDefError </span><span>=</span><span> </span><span>FailureDefinition</span><span>.</span><span>CreateFailureDefinition</span><span>(</span><span>failId</span><span>,</span><span> </span><span>FailureSeverity</span><span>.</span><span>Error</span><span>,</span><span> </span><span>"Wall is WAY too big (&gt;200'). Performance problems may result."</span><span>);</span><span>
    </span><span>// save ids for later reference</span><span>
    wallUpdater</span><span>.</span><span>WarnId</span><span> </span><span>=</span><span> warnId</span><span>;</span><span>
    wallUpdater</span><span>.</span><span>FailureId</span><span> </span><span>=</span><span> failId</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

#### FailureDefinitionId

A unique FailureDefinitionId must be used as a key to register the FailureDefinition. Each unique FailureDefinitionId should be created using a GUID generation tool. Later, the FailureDefinitionId can be used to look up a FailureDefinition in FailureDefinitionRegistry, and to create and post FailureMessages.

#### Severity

When registering a new failure, a severity is specified, along with the FailureDefinitionId and a text description of the failure that can be displayed to the user. The severity determines what actions are allowed in a document and whether the transaction can be committed at all. The severity options are:

-   _**Warning**_ - Failure that can be ignored by end-user. Failures of this severity do not prevent transactions from being committed. This severity should be used when Revit needs to communicate a problem to the user, but the problem does not prevent the user from continuing to work on the document
-   _**Error**_ - Failure that cannot be ignored. If FailureMeassage of this severity is posted, the current transaction cannot be committed unless the failure is resolved via an appropriate FailureResolution. This severity should be used when work on the document cannot be continued unless the problem is resolved. If the failure has no predefined resolutions available or these resolutions fail to resolve the problem, the transaction must be aborted in order to continue working with the document. It is strongly encouraged to have at least one resolution in each failure of this severity.
-   _**DocumentCorruption**_ - Failure that forces the Transaction to be rolled back as soon as possible due to known corruption to a document. When failure of this severity is posted, reading of information from a document is not allowed. The current transaction must be rolled back first in order to work with the document. This severity is used only if there is known data corruption in the document. This type of failure should generally be avoided unless there is no way to prevent corruption or to recover from it locally.

A fourth severity, None, cannot be specified when defining a new FailureDefinition.

#### Failure Resolutions

When a failure can be resolved, all possible resolutions should be predefined in the FailureDefinition class. This informs Revit what failure resolutions can possibly be used with a given failure. The FailureDefinition contains a full list of resolution types applicable to the failure, including a user-visible caption of the resolution.

The number of resolutions is not limited, however as of the 2011 Revit API, the only exposed failure resolution is DeleteElements. When more than one resolution is specified, unless explicitly changed using the SetDefaultResolutionType() method, the first resolution added becomes the default resolution. The default resolution is used by the Revit failure processing mechanism to resolve failures automatically when applicable. The Revit UI only uses the default resolution, but Revit add-ins, via the Revit API, can use any applicable resolution, and can provide an alternative UI for doing that (as described in the Handling Failures section later in this chapter).

In the case of a failure with a severity of DocumentCorruption, by the time failure resolution could occur, the transaction is already aborted, so there is nothing to resolve. Therefore, FailureResolutions should not be added to API-defined Failures of severity DocumentCorruption.

### Posting a failure

The Document.PostFailure() method is used to notify the document of a problem. Failures will be validated and possibly resolved at the end of the transaction. Warnings posted via this method will not be stored in the document after they are resolved. Failure posting is used to address a state of the document which may change before the end of the transaction or when it makes sense to defer resolution until the end of the transaction. Not all failures encountered by an external command should post a failure. If the failure is unrelated to the document, a task dialog should be used. For example, if the Revit UI is in an invalid state to perform the external command.

To post a failure, create a new FailureMessage using the FailureDefinitionId from when the custom failure was defined, or use a BuiltInFailure provided by the Revit API. Set any additional information in the FailureMessage object, such as failing elements, and then call Document.PostFailure() passing in the new FailureMessage. Note that the document must be modifiable in order to post a failure.

A unique FailureMessageKey returned by PostFailure() can be stored for the lifetime of transaction and used to remove a failure message if it is no longer relevant. If the same FailureMessage is posted two or more times, the same FailureMessageKey is returned. If a posted failure has a severity of DocumentCorruption, an invalid FailureMessageKey is returned. This is because a DocumentCorruption failure cannot be unposted.

The following example shows an IUpdate class (referenced in the "Defining and registering a failure" code region above) that posts a new failure based on information received in the Execute() method.

<table summary="" id="GUID-8AE4ADAF-82AB-4AC1-81A2-7A8DD9346055__TABLE_86A7525484AB46A4BAD38F3382665A9C"><tbody><tr><td><b>Code Region 26-2: Posting a failure</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>WallWarnUpdater</span><span> </span><span>:</span><span> </span><span>IUpdater</span><span>
</span><span>{</span><span>
    </span><span>static</span><span> </span><span>AddInId</span><span> m_appId</span><span>;</span><span>
    </span><span>UpdaterId</span><span> m_updaterId</span><span>;</span><span>
    </span><span>FailureDefinitionId</span><span> m_failureId </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>FailureDefinitionId</span><span> m_warnId </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>// constructor takes the AddInId for the add-in associated with this updater</span><span>
    </span><span>public</span><span> </span><span>WallWarnUpdater</span><span>(</span><span>AddInId</span><span> id</span><span>)</span><span>
    </span><span>{</span><span>
        m_appId </span><span>=</span><span> id</span><span>;</span><span>
        m_updaterId </span><span>=</span><span> </span><span>new</span><span> </span><span>UpdaterId</span><span>(</span><span>m_appId</span><span>,</span><span> 
            </span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"69797663-7BCB-44f9-B756-E4189FE0DED8"</span><span>));</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>void</span><span> </span><span>Execute</span><span>(</span><span>UpdaterData</span><span> data</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Document</span><span> doc </span><span>=</span><span> data</span><span>.</span><span>GetDocument</span><span>();</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>ApplicationServices</span><span>.</span><span>Application</span><span> app </span><span>=</span><span> doc</span><span>.</span><span>Application</span><span>;</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> data</span><span>.</span><span>GetModifiedElementIds</span><span>())</span><span>
        </span><span>{</span><span>
            </span><span>Wall</span><span> wall </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>)</span><span> </span><span>as</span><span> </span><span>Wall</span><span>;</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Parameter</span><span> p </span><span>=</span><span> wall</span><span>.</span><span>LookupParameter</span><span>(</span><span>"Unconnected Height"</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>p </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>p</span><span>.</span><span>AsDouble</span><span>()</span><span> </span><span>&gt;</span><span> </span><span>200</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>FailureMessage</span><span> failMessage </span><span>=</span><span> </span><span>new</span><span> </span><span>FailureMessage</span><span>(</span><span>FailureId</span><span>);</span><span>
                    failMessage</span><span>.</span><span>SetFailingElement</span><span>(</span><span>id</span><span>);</span><span>
                    doc</span><span>.</span><span>PostFailure</span><span>(</span><span>failMessage</span><span>);</span><span>
                </span><span>}</span><span>
                </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>p</span><span>.</span><span>AsDouble</span><span>()</span><span> </span><span>&gt;</span><span> </span><span>100</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>FailureMessage</span><span> failMessage </span><span>=</span><span> </span><span>new</span><span> </span><span>FailureMessage</span><span>(</span><span>WarnId</span><span>);</span><span>
                    failMessage</span><span>.</span><span>SetFailingElement</span><span>(</span><span>id</span><span>);</span><span>
                    doc</span><span>.</span><span>PostFailure</span><span>(</span><span>failMessage</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>FailureDefinitionId</span><span> </span><span>FailureId</span><span>
    </span><span>{</span><span>
        </span><span>get</span><span> </span><span>{</span><span> </span><span>return</span><span> m_failureId</span><span>;</span><span> </span><span>}</span><span>
        </span><span>set</span><span> </span><span>{</span><span> m_failureId </span><span>=</span><span> value</span><span>;</span><span> </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>FailureDefinitionId</span><span> </span><span>WarnId</span><span>
    </span><span>{</span><span>
        </span><span>get</span><span> </span><span>{</span><span> </span><span>return</span><span> m_warnId</span><span>;</span><span> </span><span>}</span><span>
        </span><span>set</span><span> </span><span>{</span><span> m_warnId </span><span>=</span><span> value</span><span>;</span><span> </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>string</span><span> </span><span>GetAdditionalInformation</span><span>()</span><span> 
    </span><span>{</span><span> 
        </span><span>return</span><span> </span><span>"Give warning and error if wall is too tall"</span><span>;</span><span> 
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>ChangePriority</span><span> </span><span>GetChangePriority</span><span>()</span><span> 
    </span><span>{</span><span> 
        </span><span>return</span><span> </span><span>ChangePriority</span><span>.</span><span>FloorsRoofsStructuralWalls</span><span>;</span><span> 
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>UpdaterId</span><span> </span><span>GetUpdaterId</span><span>()</span><span> 
    </span><span>{</span><span> 
        </span><span>return</span><span> m_updaterId</span><span>;</span><span> 
    </span><span>}</span><span>

    </span><span>public</span><span> </span><span>string</span><span> </span><span>GetUpdaterName</span><span>()</span><span> 
    </span><span>{</span><span> 
        </span><span>return</span><span> </span><span>"Wall Height Check"</span><span>;</span><span> 
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Removal of posted failures

Because there may be multiple changes to a document and multiple regenerations in the same transaction, it is possible that some failures are no longer relevant and they may need to be removed to prevent "false alarms". Specific messages can be un-posted by calling the Document.UnpostFailure() method and passing in the FailureMessageKey obtained when PostFailure() was called. UnpostFailure() will throw an exception if the severity of the failure is DocumentCorruption.

It is also possible to automatically remove all posted failures when a transaction is about to be rolled back (so that the user is not bothered to hit Cancel) by using the Transaction.SetFailureHandlingOptions() method.
