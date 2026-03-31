---
created: 2026-01-28T21:10:17 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Loads_html
author: 
---

# Help | Loads | Autodesk

> ## Excerpt
> The following sections identify load settings and discuss load limitation guidelines.

---
The following sections identify load settings and discuss load limitation guidelines.

### Load Settings

All functionality on the Setting dialog box Load Cases and Load Combinations tabs can be accessed by the API.

The following properties are available from the corresponding LoadCase BuiltInParameter:

**Table 60 Load Case Properties and Parameters**

<table summary="" id="GUID-642E5AFE-C4B0-42B9-9098-1B21C65913B8__TABLE_C3AE1FFD6C9642D781FC08B1F62074EC"><tbody><tr><td><b>Property</b></td><td><b>BuiltInParameter</b></td></tr><tr><td>Case Number</td><td>LOAD_CASE _NUMBER</td></tr><tr><td>Nature</td><td>LOAD_CASE_NATURE</td></tr><tr><td>Category</td><td>LOAD_CASE_CATEGORY</td></tr></tbody></table>

The LOAD\_CASE\_CATEGORY parameter returns an ElementId. The following table identifies the mapping between Category and ElementId Value.

**Table 61: Load Case Category**

<table summary="" id="GUID-642E5AFE-C4B0-42B9-9098-1B21C65913B8__TABLE_A967E9A4BF38411FA2C9CEE4E27038A5"><tbody><tr><td><b>Load Case Category</b></td><td><b>BuiltInCategory</b></td></tr><tr><td>Dead Loads</td><td>OST_LoadCasesDead</td></tr><tr><td>Live Loads</td><td>OST_LoadCasesLive</td></tr><tr><td>Wind Loads</td><td>OST_LoadCasesWind</td></tr><tr><td>Snow Loads</td><td>OST_LoadCasesSnow</td></tr><tr><td>Roof Live Loads</td><td>OST_LoadCasesRoofLive</td></tr><tr><td>Accidental Loads</td><td>OST_LoadCasesAccidental</td></tr><tr><td>Temperature Loads</td><td>OST_LoadCasesTemperature</td></tr><tr><td>Seismic Loads</td><td>OST_LoadCasesSeismic</td></tr></tbody></table>

#### Creating loads and load combinations

The following classes have one or more static Create() methods to create corresponding classes:

-   LoadUsage
-   LoadNature
-   LoadCase
-   LoadCombination.
-   PointLoad
-   LineLoad
-   AreaLoad

Point, area, and line loads can be created with or without a host element. Each of these classes has a `isValidHostId` method that indicates if a specific element can host that type of load.

Because they are all Element subclasses, they can be deleted using Document.Delete().

Load Combinations are created via the static method LoadCombination.Create() which has two overloads. The first takes only a reference to the document in which you want to create the load combination and the string for the name of the new combination. The second takes these arguments plus the LoadCombinationType and LoadCombinationState. The LoadCombinationType can be either Combination, for a straight load combination, or Envelope, for an envelope of the effects of several load cases or combinations.

The LoadCombinationState can be either Serviceability or Ultimate. Use Serviceability if the load combination represents a service load level on the structure. This is typically used in design or checking of member deflections or other serviceability criteria such as Allowable Stress Design methodologies. Use Ultimate if the load combination represents an ultimate load state or a factored load state on the structure typically used in Load Resistance Factor Design methodologies.

After a LoadCombination is created, you will need to fill it with LoadComponents which comprise the load combination and their factors. LoadComponents are added to the LoadCombination by calling LoadCombination.SetComponents() with a list of the components as shown in this code snippet below.

Note: Make sure that the list of components does not refer to itself.

The following example demonstrates how to create a Load Combination and how to find or create Load Cases and Load Natures to use to set the components of the Load Combination.

<table summary="" id="GUID-642E5AFE-C4B0-42B9-9098-1B21C65913B8__TABLE_74493DE9246F492781C7803EB1678785"><tbody><tr><td><b>Code Region: Creating a new LoadCombination</b></td></tr><tr><td><pre><code><span>LoadCombination</span><span> </span><span>CreateLoadCombinationLoadCaseLoadUsageLoadNatureAndLoadComponent</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create a new load combination</span><span>
    </span><span>LoadCombination</span><span> loadCombination </span><span>=</span><span> </span><span>LoadCombination</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"DL1 + RAIN1"</span><span>,</span><span> </span><span>LoadCombinationType</span><span>.</span><span>Combination</span><span>,</span><span> </span><span>LoadCombinationState</span><span>.</span><span>Ultimate</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>loadCombination </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create new load combination failed."</span><span>);</span><span>

    </span><span>// Get all existing LoadCase</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>LoadCase</span><span>)).</span><span>ToElements</span><span>();</span><span>

    </span><span>// Find LoadCase "DL1"</span><span>
    </span><span>LoadCase</span><span> case1 </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> e </span><span>in</span><span> collection</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>LoadCase</span><span> loadCase </span><span>=</span><span> e </span><span>as</span><span> </span><span>LoadCase</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>loadCase</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"DL1"</span><span>)</span><span>
        </span><span>{</span><span>
            case1 </span><span>=</span><span> loadCase</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// Get all existing LoadNature</span><span>
    collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collection </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>LoadNature</span><span>)).</span><span>ToElements</span><span>();</span><span>

    </span><span>// Find LoadNature "Dead"</span><span>
    </span><span>LoadNature</span><span> nature1 </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> e </span><span>in</span><span> collection</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>LoadNature</span><span> loadNature </span><span>=</span><span> e </span><span>as</span><span> </span><span>LoadNature</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>loadNature</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Dead"</span><span>)</span><span>
        </span><span>{</span><span>
            nature1 </span><span>=</span><span> loadNature</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>// Create LoadNature "Dead" if not exist</span><span>
    </span><span>if</span><span> </span><span>(</span><span>nature1 </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        nature1 </span><span>=</span><span> </span><span>LoadNature</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Dead"</span><span>);</span><span>

    </span><span>// Create LoadCase "DL1" if not exist</span><span>
    </span><span>if</span><span> </span><span>(</span><span>case1 </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        case1 </span><span>=</span><span> </span><span>LoadCase</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"DL1"</span><span>,</span><span> nature1</span><span>.</span><span>Id</span><span>,</span><span> </span><span>LoadCaseCategory</span><span>.</span><span>Dead</span><span>);</span><span>

    </span><span>// Create LoadNature "Rain"</span><span>
    </span><span>LoadNature</span><span> nature2 </span><span>=</span><span> </span><span>LoadNature</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Rain"</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>nature2 </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create new load nature failed."</span><span>);</span><span>

    </span><span>// Create LoadCase "RAIN1"</span><span>
    </span><span>LoadCase</span><span> case2 </span><span>=</span><span> </span><span>LoadCase</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"RAIN1"</span><span>,</span><span> nature2</span><span>.</span><span>Id</span><span>,</span><span> </span><span>LoadCaseCategory</span><span>.</span><span>Snow</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>case1 </span><span>==</span><span> </span><span>null</span><span> </span><span>||</span><span> case2 </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create new load case failed."</span><span>);</span><span>

    </span><span>// Create LoadComponents - they consist of LoadCases or nested LoadCombination and Factors</span><span>
    </span><span>List</span><span>&lt;</span><span>LoadComponent</span><span>&gt;</span><span> components </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>LoadComponent</span><span>&gt;();</span><span>
    components</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> </span><span>LoadComponent</span><span>(</span><span>case1</span><span>.</span><span>Id</span><span>,</span><span> </span><span>2.0</span><span>));</span><span>
    components</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> </span><span>LoadComponent</span><span>(</span><span>case2</span><span>.</span><span>Id</span><span>,</span><span> </span><span>1.5</span><span>));</span><span>

    </span><span>// Add components to combination</span><span>
    loadCombination</span><span>.</span><span>SetComponents</span><span>(</span><span>components</span><span>);</span><span>

    </span><span>// Create LoadUsages</span><span>
    </span><span>LoadUsage</span><span> usage1 </span><span>=</span><span> </span><span>LoadUsage</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Frequent"</span><span>);</span><span>
    </span><span>LoadUsage</span><span> usage2 </span><span>=</span><span> </span><span>LoadUsage</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Rare"</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>usage1 </span><span>==</span><span> </span><span>null</span><span> </span><span>||</span><span> usage2 </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create new load usage failed."</span><span>);</span><span>

    </span><span>// Add load usages to combination</span><span>
    loadCombination</span><span>.</span><span>SetUsageIds</span><span>(</span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>ElementId</span><span>&gt;()</span><span> </span><span>{</span><span>usage1</span><span>.</span><span>Id</span><span>,</span><span> usage2</span><span>.</span><span>Id</span><span>});</span><span>

    </span><span>// Give the user some information</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>string</span><span>.</span><span>Format</span><span>(</span><span>"Load Combination ID='{0}' created successfully."</span><span>,</span><span> loadCombination</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>));</span><span>

    </span><span>return</span><span> loadCombination</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

You may also modify the cases, components, natures, etc by using LoadCombination.GetComponents(), making modifications and then calling LoadCombination.SetComponents() again. LoadUsages for the LoadCombination can be modified by calling LoadCombination.GetUsageIds() to get the list of LoadUsage Ids, modifying the list, and calling SetUsageIds() again. The following code sample demonstrates how to modify an existing LoadCombination.

<table summary="" id="GUID-642E5AFE-C4B0-42B9-9098-1B21C65913B8__TABLE_E5871FC0086545969997321B95411984"><tbody><tr><td><b>Code Region: Modify a load combination</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>ModifyLoadCombinationLoadCaseLoadUsageLoadNatureAndLoadComponent</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>LoadCombination</span><span> loadCombination</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Change name of LoadCombination</span><span>
    loadCombination</span><span>.</span><span>Name</span><span> </span><span>=</span><span> </span><span>"DL2 + RAIN1"</span><span>;</span><span>

    </span><span>// Get any LoadCase from combination</span><span>
    </span><span>// Combination can have assigned LoadCase or other (nested) LoadCombination so we need to filter out any LoadCombination</span><span>
    </span><span>LoadCase</span><span> case1 </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>IList</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> caseAndCombinationIds </span><span>=</span><span> loadCombination</span><span>.</span><span>GetCaseAndCombinationIds</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> caseAndCombinationIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Element</span><span> element </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>element </span><span>is</span><span> </span><span>LoadCase</span><span>)</span><span>
        </span><span>{</span><span>
            case1 </span><span>=</span><span> </span><span>(</span><span>LoadCase</span><span>)</span><span>element</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>element </span><span>is</span><span> </span><span>LoadCombination</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>continue</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>if</span><span> </span><span>(</span><span>case1 </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Can't get LoadCase."</span><span>);</span><span>

    </span><span>// Change case name and number</span><span>
    case1</span><span>.</span><span>Name</span><span> </span><span>=</span><span> </span><span>"DL2"</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>LoadCase</span><span>.</span><span>IsNumberUnique</span><span>(</span><span>document</span><span>,</span><span> </span><span>3</span><span>))</span><span>
    </span><span>{</span><span>
        case1</span><span>.</span><span>Number</span><span> </span><span>=</span><span> </span><span>3</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>// Create load nature</span><span>
    </span><span>LoadNature</span><span> liveNature </span><span>=</span><span> </span><span>LoadNature</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Dead nature"</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>liveNature </span><span>==</span><span> </span><span>null</span><span>)</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create new load nature failed."</span><span>);</span><span>

    </span><span>// Change nature category and ID for case</span><span>
    case1</span><span>.</span><span>SubcategoryId</span><span> </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_LoadCasesDead</span><span>);</span><span>
    case1</span><span>.</span><span>NatureId</span><span> </span><span>=</span><span> liveNature</span><span>.</span><span>Id</span><span>;</span><span>

    </span><span>//Change factor for case1</span><span>
    </span><span>IList</span><span>&lt;</span><span>LoadComponent</span><span>&gt;</span><span> components </span><span>=</span><span> loadCombination</span><span>.</span><span>GetComponents</span><span>();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>LoadComponent</span><span> loadComponent </span><span>in</span><span> components</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>loadComponent</span><span>.</span><span>LoadCaseOrCombinationId</span><span> </span><span>==</span><span> case1</span><span>.</span><span>Id</span><span>)</span><span>
        </span><span>{</span><span>
            loadComponent</span><span>.</span><span>Factor</span><span> </span><span>=</span><span> </span><span>3.0</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    loadCombination</span><span>.</span><span>SetComponents</span><span>(</span><span>components</span><span>);</span><span>

    </span><span>// Remove one usage from combination</span><span>
    </span><span>IList</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> usages </span><span>=</span><span> loadCombination</span><span>.</span><span>GetUsageIds</span><span>();</span><span>
    usages</span><span>.</span><span>RemoveAt</span><span>(</span><span>0</span><span>);</span><span>
    loadCombination</span><span>.</span><span>SetUsageIds</span><span>(</span><span>usages</span><span>);</span><span>

    </span><span>// Give the user some information</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>string</span><span>.</span><span>Format</span><span>(</span><span>"Load Combination ID='{0}' modified successfully."</span><span>,</span><span> loadCombination</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>));</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

There is no Duplicate() method in the LoadCase and LoadNature classes. To implement this functionality, you must first create a new LoadCase (or LoadNature) object, and then copy the corresponding properties and parameters from an existing LoadCase (or LoadNature).

The following is a minimum sample code to demonstrate the creation of a point load:

<table summary="" id="GUID-642E5AFE-C4B0-42B9-9098-1B21C65913B8__TABLE_DCD097AAB82D4A7DABE8B6B938F17BF1"><tbody><tr><td><b>Code Region: New PointLoad</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreatePointLoad</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Define the location at which the PointLoad is applied. </span><span>
    XYZ point </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>4</span><span>);</span><span>
    </span><span>// Define the 3d force. </span><span>
    XYZ force </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>-</span><span>1</span><span>);</span><span>
    </span><span>// Define the 3d moment. </span><span>
    XYZ moment </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>

    </span><span>PointLoad</span><span> pointLoad </span><span>=</span><span> </span><span>PointLoad</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> point</span><span>,</span><span> force</span><span>,</span><span> moment</span><span>,</span><span> </span><span>null</span><span>,</span><span> </span><span>null</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
