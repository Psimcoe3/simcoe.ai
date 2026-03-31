---
created: 2026-01-28T21:19:04 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Performance_Adviser_html
author: 
---

# Help | Performance Adviser | Autodesk

> ## Excerpt
> The performance adviser feature of the Revit API is designed to analyze a document and flag for the user any elements and/or settings that may cause performance degradation. The Performance Adviser command executes a set of rules and displays their result in a standard review warnings dialog.

---
The performance adviser feature of the Revit API is designed to analyze a document and flag for the user any elements and/or settings that may cause performance degradation. The Performance Adviser command executes a set of rules and displays their result in a standard review warnings dialog.

The API for performance adviser consists of 2 classes:

-   **PerformanceAdviser** - an application-wide object that has a dual role as a registry of rules to run in order to detect potential performance problems and an engine to execute them
-   **IPerformanceAdviserRule** - an interface that allows you to define new rules for the Performance Adviser
    
    ### Performance Adviser
    

PerformanceAdviser is used to add or delete rules to be checked, enable and disable rules, get information about rules in the list, and to execute some or all rules in the list. Applications that create new rules are expected to use AddRule() to register the new rule during application startup and DeleteRule() to deregister it during application shutdown. ExecuteAllRules() will execute all rules in the list on a given document, while ExecuteRules() can be used to execute selected rules in a document. Both methods will return a list of failure messages explaining performance problems detected in the document.

The following example demonstrates looping through all performance adviser rules and executing all the rules for a document.

<table summary="" id="GUID-471E470E-FD4D-497B-98C7-AC0A97F57D4C__TABLE_D9E9C4F79A25460C9C4ED8B0F49AF588"><tbody><tr><td><b>Code Region: Performance Adviser</b></td></tr><tr><td><pre><code><span>//Get the name of each registered PerformanceRule and then execute all of them.</span><span>
</span><span>public</span><span> </span><span>void</span><span> </span><span>RunAllRules</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>PerformanceAdviserRuleId</span><span> id </span><span>in</span><span> </span><span>PerformanceAdviser</span><span>.</span><span>GetPerformanceAdviser</span><span>().</span><span>GetAllRuleIds</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>string</span><span> ruleName </span><span>=</span><span> </span><span>PerformanceAdviser</span><span>.</span><span>GetPerformanceAdviser</span><span>().</span><span>GetRuleName</span><span>(</span><span>id</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>PerformanceAdviser</span><span>.</span><span>GetPerformanceAdviser</span><span>().</span><span>ExecuteAllRules</span><span>(</span><span>document</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### IPerformanceAdviserRule

Create an instance of the IPerformanceAdviserRule interface to create new rules for the Performance Adviser. Rules can be specific to elements or can be document-wide rules. The following methods need to be implemented:

-   GetName() - a short string naming the rule
-   GetDescription() - a one to two sentence description of the rule
-   InitCheck() -method invoked by performance advisor once in the beginning of the check. If rule checks the document as a whole rather than specific elements, the check should be performed in this method.
-   FinalizeCheck() - method invoked by performance advisor once in the end of the check. Any problematic results found during rule execution can be reported during this message using FailureMessage(s)
-   WillCheckElements() - indicates if rule needs to be executed on idividual elements
-   GetElementFilter() - retrieves a filter to restrict elements to be checked
-   ExecuteElementCheck() - method invoked by performance advisor for each element to be checked

The following excerpt from the PerformanceAdviserControl sample in the Revit API SDK Samples folder demonstrates the implementation of a custom rule used to identify any doors in the document that are face-flipped. (See the sample project for the complete class implementation.)

<table summary="" id="GUID-471E470E-FD4D-497B-98C7-AC0A97F57D4C__TABLE_767B135077F244C49D87F8778175D55E"><tbody><tr><td><b>Code Region: Implementing IPerformanceAdviserRule</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>FlippedDoorCheck</span><span> </span><span>:</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>IPerformanceAdviserRule</span><span>
</span><span>{</span><span>
    </span><span>private</span><span> </span><span>string</span><span> m_name</span><span>;</span><span>
    </span><span>private</span><span> </span><span>string</span><span> m_description</span><span>;</span><span>
    </span><span>private</span><span> </span><span>FailureDefinitionId</span><span> m_doorWarningId</span><span>;</span><span>
    </span><span>private</span><span> </span><span>FailureDefinition</span><span> m_doorWarning</span><span>;</span><span>
    </span><span>private</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> m_FlippedDoors</span><span>;</span><span>
    </span><span>#region Constructor</span><span>
    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Set up rule name, description, and error handling</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>public</span><span> </span><span>FlippedDoorCheck</span><span>()</span><span>
    </span><span>{</span><span>
        m_name </span><span>=</span><span> </span><span>"Flipped Door Check"</span><span>;</span><span>
        m_description </span><span>=</span><span> </span><span>"An API-based rule to search for and return any doors that are face-flipped"</span><span>;</span><span>
        m_doorWarningId </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FailureDefinitionId</span><span>(</span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"25570B8FD4AD42baBD78469ED60FB9A3"</span><span>));</span><span>
        m_doorWarning </span><span>=</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FailureDefinition</span><span>.</span><span>CreateFailureDefinition</span><span>(</span><span>m_doorWarningId</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FailureSeverity</span><span>.</span><span>Warning</span><span>,</span><span> </span><span>"Some doors in this project are face-flipped."</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>#endregion</span><span>

    </span><span>#region IPerformanceAdviserRule implementation</span><span>
    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Does some preliminary work before executing tests on elements.  In this case,</span><span>
    </span><span>/// we instantiate a list of FamilyInstances representing all doors that are flipped.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="document"&gt;The document being checked&lt;/param&gt;</span><span>
    </span><span>public</span><span> </span><span>void</span><span> </span><span>InitCheck</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
    </span><span>{</span><span>
       </span><span>if</span><span> </span><span>(</span><span>m_FlippedDoors </span><span>==</span><span> </span><span>null</span><span>)</span><span>
          m_FlippedDoors </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>&gt;();</span><span>
       </span><span>else</span><span>
          m_FlippedDoors</span><span>.</span><span>Clear</span><span>();</span><span>
       </span><span>return</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// This method does most of the work of the IPerformanceAdviserRule implementation.</span><span>
    </span><span>/// It is called by PerformanceAdviser.</span><span>
    </span><span>/// It examines the element passed to it (which was previously filtered by the filter</span><span>
    </span><span>/// returned by GetElementFilter() (see below)).  After checking to make sure that the</span><span>
    </span><span>/// element is an instance, it checks the FacingFlipped property of the element.</span><span>
    </span><span>///</span><span>
    </span><span>/// If it is flipped, it adds the instance to a list to be used later.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="document"&gt;The active document&lt;/param&gt;</span><span>
    </span><span>/// &lt;param name="element"&gt;The current element being checked&lt;/param&gt;</span><span>
    </span><span>public</span><span> </span><span>void</span><span> </span><span>ExecuteElementCheck</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Element</span><span> element</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>((</span><span>element </span><span>is</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FamilyInstance</span><span>))</span><span>
        </span><span>{</span><span>
             </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FamilyInstance</span><span> doorCurrent </span><span>=</span><span> element </span><span>as</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FamilyInstance</span><span>;</span><span>
             </span><span>if</span><span> </span><span>(</span><span>doorCurrent</span><span>.</span><span>FacingFlipped</span><span>)</span><span>
                 m_FlippedDoors</span><span>.</span><span>Add</span><span>(</span><span>doorCurrent</span><span>.</span><span>Id</span><span>);</span><span>
        </span><span>}</span><span>

    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// This method is called by PerformanceAdviser after all elements in document</span><span>
    </span><span>/// matching the ElementFilter from GetElementFilter() are checked by ExecuteElementCheck().</span><span>
    </span><span>///</span><span>
    </span><span>/// This method checks to see if there are any elements (door instances, in this case) in the</span><span>
    </span><span>/// m_FlippedDoor instance member.  If there are, it iterates through that list and displays</span><span>
    </span><span>/// the instance name and door tag of each item.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="document"&gt;The active document&lt;/param&gt;</span><span>
    </span><span>public</span><span> </span><span>void</span><span> </span><span>FinalizeCheck</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>m_FlippedDoors</span><span>.</span><span>Count</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
            </span><span>System</span><span>.</span><span>Diagnostics</span><span>.</span><span>Debug</span><span>.</span><span>WriteLine</span><span>(</span><span>"No doors were flipped.  Test passed."</span><span>);</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            </span><span>//Pass the element IDs of the flipped doors to the revit failure reporting APIs.</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FailureMessage</span><span> fm </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>FailureMessage</span><span>(</span><span>m_doorWarningId</span><span>);</span><span>
            fm</span><span>.</span><span>SetFailingElements</span><span>(</span><span>m_FlippedDoors</span><span>);</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Transaction</span><span> failureReportingTransaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Failure reporting transaction"</span><span>);</span><span>
            failureReportingTransaction</span><span>.</span><span>Start</span><span>();</span><span>
            document</span><span>.</span><span>PostFailure</span><span>(</span><span>fm</span><span>);</span><span>
            failureReportingTransaction</span><span>.</span><span>Commit</span><span>();</span><span>
            m_FlippedDoors</span><span>.</span><span>Clear</span><span>();</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Gets the description of the rule</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;returns&gt;The rule description&lt;/returns&gt;</span><span>
    </span><span>public</span><span> </span><span>string</span><span> </span><span>GetDescription</span><span>()</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> m_description</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// This method supplies an element filter to reduce the number of elements that PerformanceAdviser</span><span>
    </span><span>/// will pass to GetElementCheck().  In this case, we are filtering for door elements.</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;param name="document"&gt;The document being checked&lt;/param&gt;</span><span>
    </span><span>/// &lt;returns&gt;A door element filter&lt;/returns&gt;</span><span>
    </span><span>public</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementFilter</span><span> </span><span>GetElementFilter</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementCategoryFilter</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>BuiltInCategory</span><span>.</span><span>OST_Doors</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Gets the name of the rule</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;returns&gt;The rule name&lt;/returns&gt;</span><span>
    </span><span>public</span><span> </span><span>string</span><span> </span><span>GetName</span><span>()</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> m_name</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>/// &lt;summary&gt;</span><span>
    </span><span>/// Returns true if this rule will iterate through elements and check them, false otherwise</span><span>
    </span><span>/// &lt;/summary&gt;</span><span>
    </span><span>/// &lt;returns&gt;True&lt;/returns&gt;</span><span>
    </span><span>public</span><span> </span><span>bool</span><span> </span><span>WillCheckElements</span><span>()</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span> </span><span>true</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>#endregion</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
