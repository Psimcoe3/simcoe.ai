---
created: 2026-01-28T21:16:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_Implementing_IUpdater_html
author: 
---

# Help | Implementing IUpdater | Autodesk

> ## Excerpt
> The IUpdater interface requires that the following 5 methods to be implemented:

---
The IUpdater interface requires that the following 5 methods to be implemented:

-   GetUpdaterId() - This method should return a globally unique Id for the Updater consisting of the application Id plus a GUID for this Updater. This method is called once during registration of the Updater.
    
-   GetUpdaterName() - This returns a name by which the Updater can be identified to the user, if there is a problem with the Updater at runtime.
    
-   GetAdditionalInformation() - This method should return auxiliary text that Revit will use to inform the end user when the Updater is not loaded.
    
-   GetChangePriority() - This method identifies the nature of the changes the Updater will be performing. It is used to identify the order of execution of updaters. This method is called once during registration of the Updater.
    
-   Execute() - This is the method that Revit will invoke to perform an update. See the next section for more information on the Execute() method.
    

If a document is modified by an Updater, the document will store the unique Id of the updater. If the user later opens the document and the Updater is not present, Revit will warn the user that the 3<sup id="GUID-6D434229-0A2E-41FE-B29D-1BB2E6471F50__GUID-6E5D2283-83A6-4CEF-8A32-F90313B5F84E">rd</sup> party updater which previously edited the document is not available unless the Updater is flagged as optional. By default, updaters are non-optional and optional updaters should be used only when necessary.

The following code is a simple example of implementing the IUpdater interface (to change the WallType for newly added walls) and registering the updater in the OnStartup() method. It demonstrates all the key aspects of creating and using an updater.

<table summary="" id="GUID-6D434229-0A2E-41FE-B29D-1BB2E6471F50__TABLE_CA2261094F954FA8BC31C87B4CA0A70C"><tbody><tr><td><b>Code Region 25-1: Example of implementing IUpdater</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>class</span><span> </span><span>WallUpdaterApplication</span><span> </span><span>:</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>IExternalApplication</span><span>
</span><span>{</span><span>
        </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnStartup</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>// Register wall updater with Revit</span><span>
                </span><span>WallUpdater</span><span> updater </span><span>=</span><span> </span><span>new</span><span> </span><span>WallUpdater</span><span>(</span><span>application</span><span>.</span><span>ActiveAddInId</span><span>);</span><span>
                </span><span>UpdaterRegistry</span><span>.</span><span>RegisterUpdater</span><span>(</span><span>updater</span><span>);</span><span>

                </span><span>// Change Scope = any Wall element</span><span>
                </span><span>ElementClassFilter</span><span> wallFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>Wall</span><span>));</span><span>

                </span><span>// Change type = element addition</span><span>
                </span><span>UpdaterRegistry</span><span>.</span><span>AddTrigger</span><span>(</span><span>updater</span><span>.</span><span>GetUpdaterId</span><span>(),</span><span> wallFilter</span><span>,</span><span> </span><span>Element</span><span>.</span><span>GetChangeTypeElementAddition</span><span>());</span><span>
                </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>Result</span><span> </span><span>OnShutdown</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>UI</span><span>.</span><span>UIControlledApplication</span><span> application</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>WallUpdater</span><span> updater </span><span>=</span><span> </span><span>new</span><span> </span><span>WallUpdater</span><span>(</span><span>application</span><span>.</span><span>ActiveAddInId</span><span>);</span><span>
                </span><span>UpdaterRegistry</span><span>.</span><span>UnregisterUpdater</span><span>(</span><span>updater</span><span>.</span><span>GetUpdaterId</span><span>());</span><span>
                </span><span>return</span><span> </span><span>Result</span><span>.</span><span>Succeeded</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span><span>

</span><span>public</span><span> </span><span>class</span><span> </span><span>WallUpdater</span><span> </span><span>:</span><span> </span><span>IUpdater</span><span>
</span><span>{</span><span>
        </span><span>static</span><span> </span><span>AddInId</span><span> m_appId</span><span>;</span><span>
        </span><span>static</span><span> </span><span>UpdaterId</span><span> m_updaterId</span><span>;</span><span>
        </span><span>WallType</span><span> m_wallType </span><span>=</span><span> </span><span>null</span><span>;</span><span>

        </span><span>// constructor takes the AddInId for the add-in associated with this updater</span><span>
        </span><span>public</span><span> </span><span>WallUpdater</span><span>(</span><span>AddInId</span><span> id</span><span>)</span><span>
        </span><span>{</span><span>
                m_appId </span><span>=</span><span> id</span><span>;</span><span>
                m_updaterId </span><span>=</span><span> </span><span>new</span><span> </span><span>UpdaterId</span><span>(</span><span>m_appId</span><span>,</span><span> </span><span>new</span><span> </span><span>Guid</span><span>(</span><span>"FBFBF6B2-4C06-42d4-97C1-D1B4EB593EFF"</span><span>));</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>void</span><span> </span><span>Execute</span><span>(</span><span>UpdaterData</span><span> data</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>Document</span><span> doc </span><span>=</span><span> data</span><span>.</span><span>GetDocument</span><span>();</span><span>

                </span><span>// Cache the wall type</span><span>
                </span><span>if</span><span> </span><span>(</span><span>m_wallType </span><span>==</span><span> </span><span>null</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
                        collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>WallType</span><span>));</span><span>
                        </span><span>var</span><span> wallTypes </span><span>=</span><span> </span><span>from</span><span> element </span><span>in</span><span> collector
                                                        </span><span>where</span><span>
                                                                element</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Exterior - Brick on CMU"</span><span>
                                                        </span><span>select</span><span> element</span><span>;</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>wallTypes</span><span>.</span><span>Count</span><span>&lt;</span><span>Element</span><span>&gt;()</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
                        </span><span>{</span><span>
                                m_wallType </span><span>=</span><span> wallTypes</span><span>.</span><span>Cast</span><span>&lt;</span><span>WallType</span><span>&gt;().</span><span>ElementAt</span><span>&lt;</span><span>WallType</span><span>&gt;(</span><span>0</span><span>);</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>

                </span><span>if</span><span> </span><span>(</span><span>m_wallType </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>// Change the wall to the cached wall type.</span><span>
                        </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> addedElemId </span><span>in</span><span> data</span><span>.</span><span>GetAddedElementIds</span><span>())</span><span>
                        </span><span>{</span><span>
                                </span><span>Wall</span><span> wall </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>addedElemId</span><span>)</span><span> </span><span>as</span><span> </span><span>Wall</span><span>;</span><span>
                                </span><span>if</span><span> </span><span>(</span><span>wall </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
                                </span><span>{</span><span>
                                        wall</span><span>.</span><span>WallType</span><span> </span><span>=</span><span> m_wallType</span><span>;</span><span>
                                </span><span>}</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>public</span><span> </span><span>string</span><span> </span><span>GetAdditionalInformation</span><span>()</span><span>
        </span><span>{</span><span>
                </span><span>return</span><span> </span><span>"Wall type updater example: updates all newly created walls to a special wall"</span><span>;</span><span>
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
                </span><span>return</span><span> </span><span>"Wall Type Updater"</span><span>;</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
