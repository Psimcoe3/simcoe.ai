---
created: 2026-01-28T21:19:30 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Place_and_Locations_Project_Position_html
author: 
---

# Help | Project Position | Autodesk

> ## Excerpt
> Project position is an object that represents a geographical offset and rotation. It is usually used by the ProjectLocation object to get and set geographical information. The following figure shows the results after changing the ProjectLocation geographical rotation and the coordinates for the same point. However, you cannot see the result of changing the ProjectLocation geographical offset directly.

---
Project position is an object that represents a geographical offset and rotation. It is usually used by the ProjectLocation object to get and set geographical information. The following figure shows the results after changing the ProjectLocation geographical rotation and the coordinates for the same point. However, you cannot see the result of changing the ProjectLocation geographical offset directly.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-7242FF42-B873-48EC-8D6C-208675848D2D-low.png)**Figure 125: Point coordinates**

Note: East indicates that the Location is rotated counterclockwise; West indicates that the location is rotated clockwise. If the Angle value is between 180 and 360 degrees, Revit transforms it automatically. For example, if you select East and type 200 degrees for Angle, Revit transforms it to West 160 degrees.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-C784E377-BFF8-4CCE-B5A8-77310071FCD3-low.png)**Figure 126: Geographical offset and rotation sketch map**

The following sample code illustrates how to retrieve the ProjectLocation object.

<table summary="" id="GUID-A1B6B145-132D-47EF-8B2E-DB1659CB6A0A__TABLE_73FFF89973034B8AA41420D93CAE0CDF"><tbody><tr><td><b>Code Region 21-1: Retrieving the ProjectLocation object</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ShowActiveProjectLocationUsage</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the project location handle </span><span>
    </span><span>ProjectLocation</span><span> projectLocation </span><span>=</span><span> document</span><span>.</span><span>ActiveProjectLocation</span><span>;</span><span>

    </span><span>// Show the information of current project location</span><span>
    XYZ origin </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>ProjectPosition</span><span> position </span><span>=</span><span> projectLocation</span><span>.</span><span>GetProjectPosition</span><span>(</span><span>origin</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> position</span><span>)</span><span>
    </span><span>{</span><span>
            </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"No project position in origin point."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Format the prompt string to show the message.</span><span>
    </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"Current project location information:\n"</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t"</span><span> </span><span>+</span><span> </span><span>"Origin point position:"</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t\t"</span><span> </span><span>+</span><span> </span><span>"Angle: "</span><span> </span><span>+</span><span> position</span><span>.</span><span>Angle</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t\t"</span><span> </span><span>+</span><span> </span><span>"East to West offset: "</span><span> </span><span>+</span><span> position</span><span>.</span><span>EastWest</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t\t"</span><span> </span><span>+</span><span> </span><span>"Elevation: "</span><span> </span><span>+</span><span> position</span><span>.</span><span>Elevation</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t\t"</span><span> </span><span>+</span><span> </span><span>"North to South offset: "</span><span> </span><span>+</span><span> position</span><span>.</span><span>NorthSouth</span><span>;</span><span>

    </span><span>// Angles are in radians when coming from Revit API, so we </span><span>
    </span><span>// convert to degrees for display</span><span>
    </span><span>const</span><span> </span><span>double</span><span> angleRatio </span><span>=</span><span> </span><span>Math</span><span>.</span><span>PI </span><span>/</span><span> </span><span>180</span><span>;</span><span>        </span><span>// angle conversion factor</span><span>

    </span><span>SiteLocation</span><span> site </span><span>=</span><span> projectLocation</span><span>.</span><span>GetSiteLocation</span><span>();</span><span>
    </span><span>string</span><span> degreeSymbol </span><span>=</span><span> </span><span>((</span><span>char</span><span>)</span><span>176</span><span>).</span><span>ToString</span><span>();</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t"</span><span> </span><span>+</span><span> </span><span>"Site location:"</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t\t"</span><span> </span><span>+</span><span> </span><span>"Latitude: "</span><span> </span><span>+</span><span> site</span><span>.</span><span>Latitude</span><span> </span><span>/</span><span> angleRatio </span><span>+</span><span> degreeSymbol</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t\t"</span><span> </span><span>+</span><span> </span><span>"Longitude: "</span><span> </span><span>+</span><span> site</span><span>.</span><span>Longitude</span><span> </span><span>/</span><span> angleRatio </span><span>+</span><span> degreeSymbol</span><span>;</span><span>
    prompt </span><span>+=</span><span> </span><span>"\n\t\t"</span><span> </span><span>+</span><span> </span><span>"TimeZone: "</span><span> </span><span>+</span><span> site</span><span>.</span><span>TimeZone</span><span>;</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> prompt</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: There is only one active project location at a time. To see the result after changing the ProjectLocation geographical offset and rotation, change the Orientation property from Project North to True North in the plan view Properties pane.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-57E4EC63-4A77-4C7C-91B3-770F3ADDBE6D-low.png)**Figure 128: Project is rotated 30 degrees from Project North to True North**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-57C77B88-C8F7-4207-9A4F-3728182159F3-low.png)**Figure 129: Project location information**

### Creating and Deleting Project Locations

Create new project locations by duplicating an existing project location using the Duplicate() method. The following code sample illustrates how to create a new project location using the Duplicate() method.

<table summary="" id="GUID-A1B6B145-132D-47EF-8B2E-DB1659CB6A0A__TABLE_27AF2AE0989C472BB31F2D5233A7BE03"><tbody><tr><td><b>Code Region 21-2: Creating a project location</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>ProjectLocation</span><span> </span><span>DuplicateLocation</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>string</span><span> newName</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>ProjectLocation</span><span> currentLocation </span><span>=</span><span> document</span><span>.</span><span>ActiveProjectLocation</span><span>;</span><span>
        </span><span>ProjectLocationSet</span><span> locations </span><span>=</span><span> document</span><span>.</span><span>ProjectLocations</span><span>;</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ProjectLocation</span><span> projectLocation </span><span>in</span><span> locations</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>projectLocation</span><span>.</span><span>Name</span><span> </span><span>==</span><span> newName</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"The name is same as a project location's name, please change one."</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>return</span><span> currentLocation</span><span>.</span><span>Duplicate</span><span>(</span><span>newName</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following code sample illustrates how to delete an existing project location from the current project.

<table summary="" id="GUID-A1B6B145-132D-47EF-8B2E-DB1659CB6A0A__TABLE_3FE6D1C068D6463280D075BA85C12B80"><tbody><tr><td><b>Code Region 21-3: Deleting a project location</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>DeleteLocation</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ProjectLocation</span><span> currentLocation </span><span>=</span><span> document</span><span>.</span><span>ActiveProjectLocation</span><span>;</span><span>
    </span><span>//There must be at least one project location in the project.</span><span>
    </span><span>ProjectLocationSet</span><span> locations </span><span>=</span><span> document</span><span>.</span><span>ProjectLocations</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>1</span><span> </span><span>==</span><span> locations</span><span>.</span><span>Size</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>return</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>string</span><span> name </span><span>=</span><span> </span><span>"location"</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>name </span><span>!=</span><span> currentLocation</span><span>.</span><span>Name</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>ProjectLocation</span><span> projectLocation </span><span>in</span><span> locations</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>projectLocation</span><span>.</span><span>Name</span><span> </span><span>==</span><span> name</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>ICollection</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>&gt;</span><span> elemSet </span><span>=</span><span> document</span><span>.</span><span>Delete</span><span>(</span><span>projectLocation</span><span>.</span><span>Id</span><span>);</span><span>
                </span><span>if</span><span> </span><span>(</span><span>elemSet</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Project Location Deleted!"</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: The following rules apply to deleting a project location:

-   The active project location cannot be deleted because there must be at least one project location in the project.
-   You cannot delete the project location if the ProjectLocationSet class instance is read-only.
