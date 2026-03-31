---
created: 2026-01-28T20:48:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Applying_Filters_html
author: 
---

# Help | Applying Filters | Autodesk

> ## Excerpt
> Filters can be applied to a FilteredElementCollector using ElementFilters. An ElementFilter is a class that examines an element to see if it meets a certain criteria. The ElementFilter base class has three derived classes that divide element filters into three categories.

---
Filters can be applied to a FilteredElementCollector using ElementFilters. An ElementFilter is a class that examines an element to see if it meets a certain criteria. The ElementFilter base class has three derived classes that divide element filters into three categories.

-   _**ElementQuickFilter**_ - Quick filters operate only on the ElementRecord, a low-memory class which has a limited interface to read element properties. Elements which are rejected by a quick filter will not be expanded in memory.
-   _**ElementSlowFilter**_ - Slow filters require that the Element be obtained and expanded in memory first. Thus it is preferable to couple slow filters with at least one ElementQuickFilter, which should minimize the number of Elements that are expanded in order to evaluate against the criteria set by this filter.
-   _**ElementLogicalFilter**_ - Logical filters combine two or more filters logically. The component filters may be reordered by Revit to cause the quickest acting filters to be evaluated first.

Most filters may be inverted using an overload constructor that takes a Boolean argument indicating to invert the filter so that elements that would normally be accepted by the filter will be rejected, and elements that would normally be rejected will be accepted. Filters that cannot be inverted are noted in their corresponding sections below.

There is a set of predefined filters available for common uses. Many of these built-in filters provide the basis for the FilteredElementCollector shortcut methods mentioned in the FilteredElementCollector section above. The next three sections provide more information on the built-in filters.

Once a filter is created, it needs to be applied to the FilteredElementCollector. The generic method WherePasses() is used to apply a single ElementFilter to the FilteredElementCollector.

Filters can also be applied using a number of shortcut methods provided by FilteredElementCollector. Some apply a specific filter without further input, such as WhereElementIsCurveDriven(), while others apply a specific filter with a simple piece of input, such as the OfCategory() method which takes a BuiltInCategory as a parameter. And lastly there are methods such as UnionWith() that join filters together. All of these methods return the same collector allowing filters to be easily chained together.

### Quick filters

Quick filters operate only on the ElementRecord, a low-memory class which has a limited interface to read element properties. Elements which are rejected by a quick filter will not be expanded in memory. The following table summarizes the built-in quick filters, and some examples follow for a few of the filters.

**Table 13: Built-in Quick Filters**

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_699DFD12B41C4EB9A0136ABFC83E1321"><tbody><tr><td><b>Built-in Filter</b></td><td><b>What it passes</b></td><td><b>Shortcut Method(s)</b></td></tr><tr><td>BoundingBoxContainsPointFilter</td><td>Elements which have a bounding box that contains a given point</td><td>None</td></tr><tr><td>BoundingBoxIntersectsFilter</td><td>Elements which have a bounding box which intersects a given outline</td><td>None</td></tr><tr><td>BoundingBoxIsInsideFilter</td><td>Elements which have a bounding box inside a given outline</td><td>None</td></tr><tr><td>ElementCategoryFilter</td><td>Elements matching the input category id</td><td>OfCategoryId()</td></tr><tr><td>ElementClassFilter</td><td>Elements matching the input runtime class (or derived classes)</td><td>OfClass()</td></tr><tr><td>ElementDesignOptionFilter</td><td>Elements in a particular design option</td><td>ContainedInDesignOption()</td></tr><tr><td>ElementIdSetFilter</td><td>Elements whose ElementIds are included in a collection</td></tr><tr><td>ElementIsCurveDrivenFilter</td><td>Elements which are curve driven</td><td>WhereElementIsCurveDriven()</td></tr><tr><td>ElementIsElementTypeFilter</td><td>Elements which are "Element types"</td><td>WhereElementIsElementType() WhereElementIsNotElementType()</td></tr><tr><td>ElementMulticategoryFilter</td><td>Elements matching any of a given set of categories</td><td>None</td></tr><tr><td>ElementMulticlassFilter</td><td>Elements matching a given set of classes (or derived classes)</td><td>None</td></tr><tr><td>ElementOwnerViewFilter</td><td>Elements which are view-specific</td><td>OwnedByView() WhereElementIsViewIndependent()</td></tr><tr><td>ElementStructuralTypeFilter</td><td>Elements matching a given structural type</td><td>None</td></tr><tr><td>ExclusionFilter</td><td>All elements except the element ids input to the filter</td><td>Excluding()</td></tr><tr><td>FamilySymbolFilter</td><td>Symbols of a particular family</td><td></td></tr><tr><td>VisibleInViewFilter</td><td>Elements that are most likely visible in the given view</td><td></td></tr></tbody></table>

Note: The FamilySymbolFilter cannot be inverted.

Note: The bounding box filters exclude all objects derived from View and objects derived from ElementType.

The following example creates an outline in the document and then uses a BoundingBoxIntersectsFilter to find the elements in the document with a bounding box that intersects that outline. It then shows how to use an inverted filter to find all walls whose bounding box do not intersect the given outline. Note that the use of the OfClass() method applies an ElementClassFilter to the collection as well.

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_186443DF4DA745609A975C68D0E5FD0B"><tbody><tr><td><b>Code Region 6-2: BoundingBoxIntersectsFilter example</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>IntersectsFilterSample</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use BoundingBoxIntersects filter to find elements with a bounding box that intersects the given Outline in the document.</span><span>

        </span><span>// Create a Outline, uses a minimum and maximum XYZ point to initialize the outline. </span><span>
        </span><span>Outline</span><span> myOutLn </span><span>=</span><span> </span><span>new</span><span> </span><span>Outline</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>),</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>100</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>100</span><span>));</span><span>

        </span><span>// Create a BoundingBoxIntersects filter with this Outline</span><span>
        </span><span>BoundingBoxIntersectsFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>BoundingBoxIntersectsFilter</span><span>(</span><span>myOutLn</span><span>);</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>// This filter excludes all objects derived from View and objects derived from ElementType</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> elements </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>).</span><span>ToElements</span><span>();</span><span>

        </span><span>// Find all walls which don't intersect with BoundingBox: use an inverted filter to match elements</span><span>
        </span><span>// Use shortcut command OfClass() to find walls only</span><span>
        </span><span>BoundingBoxIntersectsFilter</span><span> invertFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>BoundingBoxIntersectsFilter</span><span>(</span><span>myOutLn</span><span>,</span><span> </span><span>true</span><span>);</span><span>
        collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> notIntersectWalls </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Wall</span><span>)).</span><span>WherePasses</span><span>(</span><span>invertFilter</span><span>).</span><span>ToElements</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The next example uses an exclusion filter to find all walls that are not currently selected in the document.

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_02814077FD664BF89F63FFB6803DF358"><tbody><tr><td><b>Code Region 6-3: Creating an exclusion filter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>FindNotSelectedWalls</span><span>(</span><span>UIDocument</span><span> uiDocument</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Find all walls that are not currently selected, </span><span>
        </span><span>// Get all element ids which are current selected by users, exclude these ids when filtering</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uiDocument</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>

        </span><span>// Use the selection to instantiate an exclusion filter</span><span>
        </span><span>ExclusionFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ExclusionFilter</span><span>(</span><span>selectedIds</span><span>);</span><span>
        </span><span>// For the sake of simplicity we do not test here whether the selection is empty or not,</span><span>
        </span><span>// but in production code a proper validation would have to be done to avoid an argument</span><span>
        </span><span>// exception from the filter's consructor.</span><span>

        </span><span>// Apply the filter to the elements in the active document,</span><span>
        </span><span>// Use shortcut method OfClass() to find Walls only</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>uiDocument</span><span>.</span><span>Document</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> walls </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>).</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Wall</span><span>)).</span><span>ToElements</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: The ElementClassFilter will match elements whose class is an exact match to the input class, or elements whose class is derived from the input class. The following example uses an ElementClassFilter to get all loads in the document.

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_EACB2C1A610A4E4CB771DD4758CC68ED"><tbody><tr><td><b>Code Region 6-4: Using an ElementClassFilter to get loads</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MakeLoadFilter</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use ElementClassFilter to find all loads in the document</span><span>
        </span><span>// Using typeof(LoadBase) will yield all AreaLoad, LineLoad and PointLoad</span><span>
        </span><span>ElementClassFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>LoadBase</span><span>));</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> allLoads </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>).</span><span>ToElements</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

There is a small subset of Element subclasses in the API which are not supported by the element class filter. These types exist in the API, but not in Revit's native object model, which means that this filter doesn't support them. In order to use a class filter to find elements of these types, it is necessary to use a higher level class and then process the results further to find elements matching only the subtype.

Note: Dedicated filters exist for some of these types.

The following types are affected by this restriction:

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_B749B356451E43F892FA804E108867EB"><tbody><tr><td><b>Type</b></td><td><b>Dedicated Filter</b></td></tr><tr><td>Subclasses of Autodesk.Revit.DB.Material</td><td>None</td></tr><tr><td>Subclasses of Autodesk.Revit.DB.CurveElement</td><td>CurveElementFilter</td></tr><tr><td>Subclasses of Autodesk.Revit.DB.ConnectorElement</td><td>None</td></tr><tr><td>Subclasses of Autodesk.Revit.DB.HostedSweep</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Architecture.Room</td><td>RoomFilter</td></tr><tr><td>Autodesk.Revit.DB.Mechanical.Space</td><td>SpaceFilter</td></tr><tr><td>Autodesk.Revit.DB.Area</td><td>AreaFilter</td></tr><tr><td>Autodesk.Revit.DB.Architecture.RoomTag</td><td>RoomTagFilter</td></tr><tr><td>Autodesk.Revit.DB.Mechanical.SpaceTag</td><td>SpaceTagFilter</td></tr><tr><td>Autodesk.Revit.DB.AreaTag</td><td>AreaTagFilter</td></tr><tr><td>Autodesk.Revit.DB.CombinableElement</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Mullion</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Panel</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.AnnotationSymbol</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Structure.AreaReinforcementType</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Structure.PathReinforcementType</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.AnnotationSymbolType</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Architecture.RoomTagType</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Mechanical.SpaceTagType</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.AreaTagType</td><td>None</td></tr><tr><td>Autodesk.Revit.DB.Structure.TrussType</td><td>None</td></tr></tbody></table>

### Slow Filters

Slow filters require that the Element be obtained and expanded in memory first. Thus it is preferable to couple slow filters with at least one ElementQuickFilter, which should minimize the number of Elements that are expanded in order to evaluate against the criteria set by this filter. The following table summarizes the built-in slow filters, while a few examples follow to provide an in-depth look at some of the filters.

**Table 14: Built-in Slow Filters**

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_89C43C4C3BBF4001A3430D2B3088713F"><tbody><tr><td><b>Built-in Filter</b></td><td><b>What it passes</b></td><td><b>Shortcut Method(s)</b></td></tr><tr><td>AreaFilter</td><td>Areas</td><td>None</td></tr><tr><td>AreaTagFilter</td><td>Area tags</td><td>None</td></tr><tr><td>CurveElementFilter</td><td>CurveElements</td><td>None</td></tr><tr><td>ElementLevelFilter</td><td>Elements associated with a given level id</td><td>None</td></tr><tr><td>ElementParameterFilter</td><td>Elements passing one or more parameter filter rules</td><td>None</td></tr><tr><td>ElementPhaseStatusFilter</td><td>Elements with a given phase status on a given phase</td><td>None</td></tr><tr><td>FamilyInstanceFilter</td><td>Instances of a particular family instance</td><td>None</td></tr><tr><td>FamilyStructuralMaterialTypeFilter</td><td>Family elements of given structural material type</td><td>None</td></tr><tr><td>PrimaryDesignOptionMemberFilter</td><td>Elements owned by any primary design option</td><td>None</td></tr><tr><td>RoomFilter</td><td>Rooms</td><td>None</td></tr><tr><td>RoomTagFilter</td><td>Room tags</td><td>None</td></tr><tr><td>SpaceFilter</td><td>Spaces</td><td>None</td></tr><tr><td>SpaceTagFilter</td><td>Space tags</td><td>None</td></tr><tr><td>StructuralInstanceUsageFilter</td><td>FamilyInstances of given structural usage</td><td>None</td></tr><tr><td>StructuralMaterialTypeFilter</td><td>FamilyInstances of given structural material type</td><td>None</td></tr><tr><td>StructuralWallUsageFilter</td><td>Walls of given structural wall usage</td><td>None</td></tr><tr><td><a href="https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Element_Intersection_Filters_html" data-url="https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/files/Revit_API_Developers_Guide/Basic_Interaction_with_Revit_Elements/Filtering/Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Element_Intersection_Filters_html.html">Element Intersection Filters</a></td><td>Elements that intersect the solid geometry of a given element</td><td>None</td></tr><tr><td><a href="https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Element_Intersection_Filters_html" data-url="https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/files/Revit_API_Developers_Guide/Basic_Interaction_with_Revit_Elements/Filtering/Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_Element_Intersection_Filters_html.html">Element Intersection Filters&gt;</a></td><td>Elements that intersect the given solid geometry</td><td>None</td></tr></tbody></table>

The following slow filters cannot be inverted:

-   RoomFilter
-   RoomTagFilter
-   AreaFilter
-   AreaTagFilter
-   SpaceFilter
-   SpaceTagFilter
-   FamilyInstanceFilter

As mentioned in the quick filters section, some classes do not work with the ElementClassFilter. Some of those classes, such as Room and RoomTag have their own dedicated filters.

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_4AB07B2CE0294AE3ACFEAD5378B7CBAF"><tbody><tr><td><b>Code Region 6-5: Using the Room filter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>MakeRoomFilter</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use a RoomFilter to find all room elements in the document. It is necessary to use the RoomFilter and not an ElementClassFilter or the shortcut method OfClass() because the Room class is not supported by those methods.</span><span>
        </span><span>RoomFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>RoomFilter</span><span>();</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> rooms </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>).</span><span>ToElements</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The ElementParameterFilter is a powerful filter that can find elements based on values of parameters they may have. It can find elements whose parameter values match a specific value or are greater or less than some value. ElementParameterFilter can also be used to find elements that support a specific shared parameter.

The example below uses an ElementParameterFilter to find rooms whose size is more than 100 square feet and rooms with less than 100 square feet.

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_3905C77CB625485CAD0429E99FCE13CA"><tbody><tr><td><b>Code Region 6-6: Using a parameter filter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>FindRooms</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Creates an ElementParameter filter to find rooms whose area is greater than specified value</span><span>
        </span><span>// Create filter by provider and evaluator </span><span>
        </span><span>BuiltInParameter</span><span> areaParam </span><span>=</span><span> </span><span>BuiltInParameter</span><span>.</span><span>ROOM_AREA</span><span>;</span><span>
        </span><span>// provider</span><span>
        </span><span>ParameterValueProvider</span><span> pvp </span><span>=</span><span> </span><span>new</span><span> </span><span>ParameterValueProvider</span><span>(</span><span>new</span><span> </span><span>ElementId</span><span>((</span><span>int</span><span>)</span><span>areaParam</span><span>));</span><span>
        </span><span>// evaluator</span><span>
        </span><span>FilterNumericRuleEvaluator</span><span> fnrv </span><span>=</span><span> </span><span>new</span><span> </span><span>FilterNumericGreater</span><span>();</span><span>
        </span><span>// rule value </span><span>
        </span><span>double</span><span> ruleValue </span><span>=</span><span> </span><span>100.0f</span><span>;</span><span>      </span><span>// filter room whose area is greater than 100 SF</span><span>
        </span><span>// rule</span><span>
        </span><span>FilterRule</span><span> fRule </span><span>=</span><span> </span><span>new</span><span> </span><span>FilterDoubleRule</span><span>(</span><span>pvp</span><span>,</span><span> fnrv</span><span>,</span><span> ruleValue</span><span>,</span><span> </span><span>1E-6</span><span>);</span><span>

        </span><span>// Create an ElementParameter filter</span><span>
        </span><span>ElementParameterFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementParameterFilter</span><span>(</span><span>fRule</span><span>);</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> rooms </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>).</span><span>ToElements</span><span>();</span><span>

        </span><span>// Find rooms whose area is less than or equal to 100: </span><span>
        </span><span>// Use inverted filter to match elements</span><span>
        </span><span>ElementParameterFilter</span><span> lessOrEqualFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementParameterFilter</span><span>(</span><span>fRule</span><span>,</span><span> </span><span>true</span><span>);</span><span> 
        collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> lessOrEqualFounds </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>lessOrEqualFilter</span><span>).</span><span>ToElements</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following example shows how to use the FamilyStructuralMaterialTypeFilter to find all families whose material type is wood. It also shows how to use an inverted filter to find all families whose material type is not wood.

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_3DD5DAFCBBD842A6BF7F33B4BB528F98"><tbody><tr><td><b>Code Region 6-7: Find all families with wood material</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>FindWoodFamilies</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Use FamilyStructuralMaterialType filter to find families whose material type is Wood</span><span>
        </span><span>FamilyStructuralMaterialTypeFilter</span><span> filter </span><span>=</span><span> </span><span>new</span><span> </span><span>FamilyStructuralMaterialTypeFilter</span><span>(</span><span>StructuralMaterialType</span><span>.</span><span>Wood</span><span>);</span><span>

        </span><span>// Apply the filter to the elements in the active document</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> woodFamiles </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>filter</span><span>).</span><span>ToElements</span><span>();</span><span>

        </span><span>// Find families are not Wood: Use inverted filter to match families</span><span>
        </span><span>FamilyStructuralMaterialTypeFilter</span><span> notWoodFilter </span><span>=</span><span> 
                </span><span>new</span><span> </span><span>FamilyStructuralMaterialTypeFilter</span><span>(</span><span>StructuralMaterialType</span><span>.</span><span>Wood</span><span>,</span><span> </span><span>true</span><span>);</span><span>
        collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> notWoodFamilies </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>notWoodFilter</span><span>).</span><span>ToElements</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The last two slow filters derive from ElementIntersectsFilter which is a base class for filters used to match elements which intersect with geometry. See Code Region: Find Nearby Walls in the section [Geometry Utility Classes](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_Geometry_Utility_Classes_html)for an example of the use of this type of filter.

### Logical filters

Logical filters combine two or more filters logically. The following table summarizes the built-in logical filters.

**Table 15: Built-in Logical Filters**

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_C27A6B50681A4003AD2212073993E958"><tbody><tr><td><b>Built-in Filter</b></td><td><b>What it passes</b></td><td><b>Shortcut Method(s)</b></td></tr><tr><td>LogicalAndFilter</td><td>Elements that pass 2 or more filters</td><td>WherePasses()- adds one additional filter<p>IntersectWith() - joins two sets of independent filters</p></td></tr><tr><td>LogicalOrFilter</td><td>Elements that pass at least one of 2 or more filters</td><td>UnionWith() - joins two sets of independent filters</td></tr></tbody></table>

In the example below, two quick filters are combined using a logical filter to get all door FamilyInstance elements in the document.

<table summary="" id="GUID-A2686090-69D5-48D3-8DF9-0AC4CC4067A5__TABLE_D3B3A22C953B4E5DA02D0B7956E0C715"><tbody><tr><td><b>Code Region 6-8: Using LogicalAndFilter to find all door instances</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>FindDoors</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Find all door instances in the project by finding all elements that both belong to the door category and are family instances.</span><span>
</span><span>ElementClassFilter</span><span> familyInstanceFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>ElementClassFilter</span><span>(</span><span>typeof</span><span>(</span><span>FamilyInstance</span><span>));</span><span>

</span><span>// Create a category filter for Doors</span><span>
</span><span>ElementCategoryFilter</span><span> doorsCategoryfilter </span><span>=</span><span> 
        </span><span>new</span><span> </span><span>ElementCategoryFilter</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Doors</span><span>);</span><span>

</span><span>// Create a logic And filter for all Door FamilyInstances</span><span>
</span><span>LogicalAndFilter</span><span> doorInstancesFilter </span><span>=</span><span> </span><span>new</span><span> </span><span>LogicalAndFilter</span><span>(</span><span>familyInstanceFilter</span><span>,</span><span> 
        doorsCategoryfilter</span><span>);</span><span>

</span><span>// Apply the filter to the elements in the active document</span><span>
</span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
</span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> doors </span><span>=</span><span> collector</span><span>.</span><span>WherePasses</span><span>(</span><span>doorInstancesFilter</span><span>).</span><span>ToElements</span><span>();</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
