---
created: 2026-01-28T20:58:39 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_Code_Samples_html
author: 
---

# Help | Code Samples | Autodesk

> ## Excerpt
> Code samples for working with Family Instances.

---
Code samples for working with Family Instances.

Review the following code samples for more information about working with Family Instances. Please note that in the NewFamilyInstance() method, a StructuralType argument is required to specify the type of the family instance to be created. Here are some examples:

**Table 34: The value of StructuralType argument in the NewFamilyInstance() method**

<table summary="" id="GUID-A452F78B-7B95-4493-899D-8A09D009F5C5__TABLE_4B2C9E355A404441B3E452343BAC24F3"><tbody><tr><td><b>Type of Family Instance</b></td><td><b>Value of StructuralType</b></td></tr><tr><td>Doors, tables, etc.</td><td>NonStructural</td></tr><tr><td>Beams</td><td>Beam</td></tr><tr><td>Braces</td><td>Brace</td></tr><tr><td>Columns</td><td>Column</td></tr><tr><td>Footings</td><td>Footing</td></tr></tbody></table>

### Create Tables

The following function demonstrates how to load a family of Tables into a Revit project and create instances from all symbols in this family.

The LoadFamily() method returns false if the specified family was previously loaded. Therefore, in the following case, do not load the family, Table-Dining Round w Chairs.rfa, before this function is called. In this example, the tables are created at Level 1 by default.

<table summary="" id="GUID-A452F78B-7B95-4493-899D-8A09D009F5C5__TABLE_CCCB052A20BB4FDF905FD5EEB09854F5"><tbody><tr><td><b>Code Region 12-3: Creating tables</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>CreateTables</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>String</span><span> fileName </span><span>=</span><span> </span><span>@</span><span>"C:\ProgramData\Autodesk\RVT 2014\Libraries\US Imperial\Furniture\Tables\Table-Dining Round w Chairs.rfa"</span><span>;</span><span>

    </span><span>// try to load family</span><span>
    </span><span>Family</span><span> family </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(!</span><span>document</span><span>.</span><span>LoadFamily</span><span>(</span><span>fileName</span><span>,</span><span> </span><span>out</span><span> family</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Unable to load "</span><span> </span><span>+</span><span> fileName</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Loop through table symbols and add a new table for each</span><span>
    </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> familySymbolIds </span><span>=</span><span> family</span><span>.</span><span>GetFamilySymbolIds</span><span>();</span><span>
    </span><span>double</span><span> x </span><span>=</span><span> </span><span>0.0</span><span>,</span><span> y </span><span>=</span><span> </span><span>0.0</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> familySymbolIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>FamilySymbol</span><span> symbol </span><span>=</span><span> family</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>)</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
        XYZ location </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>x</span><span>,</span><span> y</span><span>,</span><span> </span><span>10.0</span><span>);</span><span>

        </span><span>FamilyInstance</span><span> instance </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewFamilyInstance</span><span>(</span><span>location</span><span>,</span><span> symbol</span><span>,</span><span> </span><span>StructuralType</span><span>.</span><span>NonStructural</span><span>);</span><span>
        x </span><span>+=</span><span> </span><span>10.0</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The result of loading the Tables family and placing one instance of each FamilySymbol:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-5FE17FC0-A248-47AE-A08A-1BBA3156193B-low.png)**Figure 47: Load family and create tables in the Revit project**

### Create a Beam

In this sample, a family symbol is loaded instead of a family, because loading a single FamilySymbol is faster than loading a Family that contains many FamilySymbols.

<table summary="" id="GUID-A452F78B-7B95-4493-899D-8A09D009F5C5__TABLE_0F194E1AB6F9406183FDBBB0C07DAE48"><tbody><tr><td><b>Code Region 12-4: Creating a beam</b></td></tr><tr><td><pre><code><span>FamilyInstance</span><span> </span><span>CreateBeam</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>View</span><span> view</span><span>)</span><span>
</span><span>{</span><span>

    </span><span>// get the given view's level for beam creation</span><span>
    </span><span>Level</span><span> level </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>view</span><span>.</span><span>LevelId</span><span>)</span><span> </span><span>as</span><span> </span><span>Level</span><span>;</span><span>

    </span><span>// get a family symbol</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FamilySymbol</span><span>)).</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_StructuralFraming</span><span>);</span><span>

    </span><span>FamilySymbol</span><span> gotSymbol </span><span>=</span><span> collector</span><span>.</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>

    </span><span>// create new beam 10' long starting at origin</span><span>
    XYZ startPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ endPoint </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>

    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Curve</span><span> beamLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>startPoint</span><span>,</span><span> endPoint</span><span>);</span><span>

    </span><span>// create a new beam</span><span>
    </span><span>FamilyInstance</span><span> instance </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewFamilyInstance</span><span>(</span><span>beamLine</span><span>,</span><span> gotSymbol</span><span>,</span><span> level</span><span>,</span><span> </span><span>StructuralType</span><span>.</span><span>Beam</span><span>);</span><span>

    </span><span>return</span><span> instance</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Create Doors

Create a long wall about 180' in length and select it before running this sample. The host object must support inserting instances; otherwise the NewFamilyInstance() method will fail. If a host element is not provided for an instance that must be created in a host, or the instance cannot be inserted into the specified host element, the method NewFamilyInstance() does nothing.

<table summary="" id="GUID-A452F78B-7B95-4493-899D-8A09D009F5C5__TABLE_5592C01551724E6984533F0AF3B62C54"><tbody><tr><td><b>Code Region 12-5: Creating doors</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>CreateDoorsInWall</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// get wall's level for door creation</span><span>
    </span><span>Level</span><span> level </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>wall</span><span>.</span><span>LevelId</span><span>)</span><span> </span><span>as</span><span> </span><span>Level</span><span>;</span><span>

    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FamilySymbol</span><span>))</span><span>
                                                </span><span>.</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Doors</span><span>)</span><span>
                                                </span><span>.</span><span>ToElements</span><span>();</span><span>
    </span><span>IEnumerator</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> symbolItor </span><span>=</span><span> collection</span><span>.</span><span>GetEnumerator</span><span>();</span><span>

    </span><span>double</span><span> x </span><span>=</span><span> </span><span>0</span><span>,</span><span> y </span><span>=</span><span> </span><span>0</span><span>,</span><span> z </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>while</span><span> </span><span>(</span><span>symbolItor</span><span>.</span><span>MoveNext</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>FamilySymbol</span><span> symbol </span><span>=</span><span> symbolItor</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
        XYZ location </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>x</span><span>,</span><span> y</span><span>,</span><span> z</span><span>);</span><span>
        </span><span>FamilyInstance</span><span> instance </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewFamilyInstance</span><span>(</span><span>location</span><span>,</span><span> symbol</span><span>,</span><span> wall</span><span>,</span><span> level</span><span>,</span><span> </span><span>StructuralType</span><span>.</span><span>NonStructural</span><span>);</span><span>
        x </span><span>+=</span><span> </span><span>10</span><span>;</span><span>
        y </span><span>+=</span><span> </span><span>10</span><span>;</span><span>
        z </span><span>+=</span><span> </span><span>1.5</span><span>;</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The result of the previous code in Revit is shown in the following picture. Notice that if the specified location is not at the specified level, the NewFamilyInstance() method uses the location elevation instead of the level elevation.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-3175405A-CD58-4A39-8DC8-696E76652DBB-low.png)Figure 48: Insert doors into a wall

### Create FamilyInstances Using Reference Directions

Use reference directions to insert an item in a specific direction.

<table summary="" id="GUID-A452F78B-7B95-4493-899D-8A09D009F5C5__TABLE_C986FBDF6F0949709645D46A44A8B99C"><tbody><tr><td><b>Code Region 12-6: Creating FamilyInstances using reference directions</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateWithRefDir</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get a floor to place the beds</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>Floor</span><span> floor </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Floor</span><span>)).</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>Floor</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>floor </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// Find a Bed-Box family</span><span>
        </span><span>Family</span><span> family </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>FilteredElementCollector</span><span> famCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        famCollector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Family</span><span>));</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span> famCollector</span><span>.</span><span>ToElements</span><span>();</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> element </span><span>in</span><span> collection</span><span>)</span><span>
        </span><span>{</span><span>

            </span><span>if</span><span> </span><span>(</span><span>element</span><span>.</span><span>Name</span><span>.</span><span>CompareTo</span><span>(</span><span>"Bed-Box"</span><span>)</span><span> </span><span>==</span><span> </span><span>0</span><span>)</span><span>
            </span><span>{</span><span>
                family </span><span>=</span><span> element </span><span>as</span><span> </span><span>Family</span><span>;</span><span>
                </span><span>break</span><span>;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>if</span><span> </span><span>(</span><span>family </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// Enumerate the beds in the Bed-Box family</span><span>
            </span><span>FilteredElementCollector</span><span> fsCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
            </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> fsCollection </span><span>=</span><span> fsCollector</span><span>.</span><span>WherePasses</span><span>(</span><span>new</span><span> </span><span>FamilySymbolFilter</span><span>(</span><span>family</span><span>.</span><span>Id</span><span>)).</span><span>ToElements</span><span>();</span><span>
            </span><span>IEnumerator</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> symbolItor </span><span>=</span><span> fsCollection</span><span>.</span><span>GetEnumerator</span><span>();</span><span>

            </span><span>int</span><span> x </span><span>=</span><span> </span><span>0</span><span>,</span><span> y </span><span>=</span><span> </span><span>0</span><span>;</span><span>
            </span><span>int</span><span> i </span><span>=</span><span> </span><span>0</span><span>;</span><span>
            </span><span>while</span><span> </span><span>(</span><span>symbolItor</span><span>.</span><span>MoveNext</span><span>())</span><span>
            </span><span>{</span><span>
                </span><span>FamilySymbol</span><span> symbol </span><span>=</span><span> symbolItor</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
                XYZ location </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>x</span><span>,</span><span> y</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                XYZ direction </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>();</span><span>
                </span><span>switch</span><span> </span><span>(</span><span>i </span><span>%</span><span> </span><span>3</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>case</span><span> </span><span>0</span><span>:</span><span>
                        direction </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                        </span><span>break</span><span>;</span><span>
                    </span><span>case</span><span> </span><span>1</span><span>:</span><span>
                        direction </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>1</span><span>);</span><span>
                        </span><span>break</span><span>;</span><span>
                    </span><span>case</span><span> </span><span>2</span><span>:</span><span>
                        direction </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>);</span><span>
                        </span><span>break</span><span>;</span><span>
                </span><span>}</span><span>
                </span><span>FamilyInstance</span><span> instance </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewFamilyInstance</span><span>(</span><span>location</span><span>,</span><span> symbol</span><span>,</span><span> direction</span><span>,</span><span> floor</span><span>,</span><span> </span><span>StructuralType</span><span>.</span><span>NonStructural</span><span>);</span><span>
                x </span><span>+=</span><span> </span><span>10</span><span>;</span><span>
                i</span><span>++;</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The result of the previous code appears in the following picture:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-86B0A1C3-988D-4C4B-BA8E-3C8C9BDEAAE0-low.png)**Figure 49: Create family instances using different reference directions**
