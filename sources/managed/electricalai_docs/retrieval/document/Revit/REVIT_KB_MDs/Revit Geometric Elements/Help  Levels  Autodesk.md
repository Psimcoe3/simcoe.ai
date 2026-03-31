---
created: 2026-01-28T21:00:00 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_Levels_html
author: 
---

# Help | Levels | Autodesk

> ## Excerpt
> A level is a finite horizontal plane that acts as a reference for level-hosted elements, such as walls, roofs, floors, and ceilings.

---
A level is a finite horizontal plane that acts as a reference for level-hosted elements, such as walls, roofs, floors, and ceilings.

In the Revit Platform API, the Level class is derived from the DatumPlane class, which is derived from the Element class. The inherited Name property is used to retrieve the user-visible level name beside the level bubble in the Revit UI. To retrieve all levels in a project, use an ElementClassFilter with the Level class.

## Elevation

The Level class has the following properties:

-   The Elevation property is used to retrieve or change the elevation above or below ground level.
-   The ProjectElevation property is used to retrieve the elevation relative to the project origin regardless of the Elevation Base parameter value.
-   The Elevation Base value is a Level type parameter.
    -   Its BuiltInParameter is LEVEL\_RELATIVE\_BASE\_TYPE.
    -   Its StorageType is Integer
    -   0 corresponds to Project and 1 corresponds to Shared.

The following code sample illustrates how to retrieve all levels in a project using a Level class filter.

<table summary="" id="GUID-AA1B1CD4-3988-4F90-9C19-CE0DC1EC2039__TABLE_B0CB7899667846E8B42DA126C2134E9F"><tbody><tr><td><b>Code Region 15-1: Retrieving all Levels</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>Getinfo_Level</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>StringBuilder</span><span> levelInformation </span><span>=</span><span> </span><span>new</span><span> </span><span>StringBuilder</span><span>();</span><span>
        </span><span>int</span><span> levelNumber </span><span>=</span><span> </span><span>0</span><span>;</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Level</span><span>)).</span><span>ToElements</span><span>();</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> e </span><span>in</span><span> collection</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>Level</span><span> level </span><span>=</span><span> e </span><span>as</span><span> </span><span>Level</span><span>;</span><span>

                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> level</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>// keep track of number of levels</span><span>
                        levelNumber</span><span>++;</span><span>

                        </span><span>//get the name of the level</span><span>
                        levelInformation</span><span>.</span><span>Append</span><span>(</span><span>"\nLevel Name: "</span><span> </span><span>+</span><span> level</span><span>.</span><span>Name</span><span>);</span><span>

                        </span><span>//get the elevation of the level</span><span>
                        levelInformation</span><span>.</span><span>Append</span><span>(</span><span>"\n\tElevation: "</span><span> </span><span>+</span><span> level</span><span>.</span><span>Elevation</span><span>);</span><span>

                        </span><span>// get the project elevation of the level</span><span>
                        levelInformation</span><span>.</span><span>Append</span><span>(</span><span>"\n\tProject Elevation: "</span><span> </span><span>+</span><span> level</span><span>.</span><span>ProjectElevation</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>//number of total levels in current document</span><span>
        levelInformation</span><span>.</span><span>Append</span><span>(</span><span>"\n\n There are "</span><span> </span><span>+</span><span> levelNumber </span><span>+</span><span> </span><span>" levels in the document!"</span><span>);</span><span>

        </span><span>//show the level information in the messagebox</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>levelInformation</span><span>.</span><span>ToString</span><span>());</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Creating a Level

Using the Level command, you can define a vertical height or story within a building and you can create a level for each existing story or other building references. Levels must be added in a section or elevation view. Additionally, you can create a new level using the Revit Platform API.

The following code sample illustrates how to create a new level.

<table summary="" id="GUID-AA1B1CD4-3988-4F90-9C19-CE0DC1EC2039__TABLE_5B1F57D7695E4CDFB78261D5F533C977"><tbody><tr><td><b>Code Region 15-2: Creating a new Level</b></td></tr><tr><td><pre><code><span>Level</span><span> </span><span>CreateLevel</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// The elevation to apply to the new level</span><span>
    </span><span>double</span><span> elevation </span><span>=</span><span> </span><span>20.0</span><span>;</span><span> 

    </span><span>// Begin to create a level</span><span>
    </span><span>Level</span><span> level </span><span>=</span><span> </span><span>Level</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> elevation</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> level</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create a new level failed."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Change the level name</span><span>
    level</span><span>.</span><span>Name</span><span> </span><span>=</span><span> </span><span>"New level"</span><span>;</span><span>

    </span><span>return</span><span> level</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: After creating a new level, Revit does not create the associated plan view for this level. If necessary, you can create it yourself.

## Finding levels based on elevation

You can find levels based on their elevation with a `FilteredElementCollector`. You can also use one of these static methods which return the id of the Level which is closest to the specified elevation. The level can be at, above, or below the target elevation. If there is more than one Level at the same distance from the elevation, the Level with the lowest id will be returned

-   Level.GetNearestLevelId(Document document, double elevation)
-   Level.GetNearestLevelId(Document document, double elevation, out double offset)
