---
created: 2026-01-28T20:43:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | General Properties | Autodesk

> ## Excerpt
> The following properties are common to each Element created using Revit.

---
The following properties are common to each Element created using Revit.

### ElementId

Every element in an active document has a unique identifier represented by the ElementId storage type. ElementId objects are project wide. It is a unique number that is never changed in the element model, which allows it to be stored externally to retrieve the element when needed.

In the Revit Platform API, you can create an ElementId directly, and then associate a unique integer value to the new ElementId. The new ElementId value is 0 by default.

<table summary="" id="GUID-BC19ED01-4A0E-48A4-A7F1-4CAFD0A950F6__TABLE_07CCE2108B0F48CAADA10468D09D9A34"><tbody><tr><td><b>Code Region 5-3: Setting ElementId</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>SetElementId</span><span>(</span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the id of the element</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> selectedId </span><span>=</span><span> element</span><span>.</span><span>Id</span><span>;</span><span>
    </span><span>int</span><span> idInteger </span><span>=</span><span> selectedId</span><span>.</span><span>IntegerValue</span><span>;</span><span>

    </span><span>// create a new id and set the value</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> id </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>(</span><span>idInteger</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

ElementId has the following uses:

-   Use ElementId to retrieve a specific element from Revit. From the Revit Application class, gain access to the active document, and then get the specified element using the Document.GetElement(ElementId) method.

<table summary="" id="GUID-BC19ED01-4A0E-48A4-A7F1-4CAFD0A950F6__TABLE_814B259DBFC046E79FF7C02BBFB19C0B"><tbody><tr><td><b>Code Region 5-4: Using ElementId</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>UsingElementId</span><span>(</span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the id of the element</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> selectedId </span><span>=</span><span> element</span><span>.</span><span>Id</span><span>;</span><span>
    </span><span>int</span><span> idInteger </span><span>=</span><span> selectedId</span><span>.</span><span>IntegerValue</span><span>;</span><span>

    </span><span>// create a new id and set the value</span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> id </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span>(</span><span>idInteger</span><span>);</span><span>

    </span><span>// Get the element </span><span>
    </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Element</span><span> first </span><span>=</span><span> element</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

If the ID number does not exist in the project, the element you retrieve is null.

-   Use ElementId to check whether two Elements in one project are equal or not. It is not recommended to use the Object.Equal() method.
    
    ### UniqueId
    

Every element has a UniqueId, represented by the String storage type. The UniqueId corresponds to the ElementId. However, unlike ElementId, UniqueId functions like a GUID (Globally Unique Identifier), which is unique across separate Revit projects. UniqueId can help you to track elements when you export Revit project files to other formats.

<table summary="" id="GUID-BC19ED01-4A0E-48A4-A7F1-4CAFD0A950F6__TABLE_BAADEF17FA0A4A06AC7BE10ADFCE6AC6"><tbody><tr><td><b>Code Region 5-5: UniqueId</b></td></tr><tr><td><p><code>string uniqueId = element.UniqueId;</code></p></td></tr></tbody></table>

Note: The ElementId is only unique in the current project. It is not unique across separate Revit projects. UniqueId is always unique across separate projects.

### Location

The location of an object is important in the building modeling process. In Revit, some objects have a point location. For example a table has a point location. Other objects have a line location, representing a location curve or no location at all. A wall is an element that has a line location.

The Revit Platform API provides the Location class and location functionality for most elements. For example, it has the Move() and Rotate() methods to translate and rotate the elements. However, the Location class has no property from which you can get information such as a coordinate. In this situation, downcast the Location object to its subclass-like LocationPoint or LocationCurve-for more detailed location information and control using object derivatives.

Retrieving an element's physical location in a project is useful when you get the geometry of an object. The following rules apply when you retrieve a location:

-   Wall, Beam, and Brace are curve-driven using LocationCurve.
-   Room, RoomTag, SpotDimension, Group, FamilyInstances that are not curve-driven, and all In-Place-FamilyInstances use LocationPoint.

In the Revit Platform API, curve-driven means that the geometry or location of an element is determined by one or more associated curves. Almost all analytical model elements are curve-driven - linear and area loads, walls, framing elements, and so on.

Other Elements cannot retrieve a LocationCurve or LocationPoint. They return Location with no information.

**Table 12: Elements Location Information**

<table summary="" id="GUID-BC19ED01-4A0E-48A4-A7F1-4CAFD0A950F6__TABLE_DC8EA66CC4DB40A7B1BE68D11B0D57ED"><tbody><tr><td><b>Location Information</b></td><td><b>Elements</b></td></tr><tr><td>LocationCurve</td><td>Wall, Beam, Brace, Structural Truss, LineLoad(without host)</td></tr><tr><td>LocationPoint</td><td>Room, RoomTag, SpotDimension, Group, Column, Mass</td></tr><tr><td>Only Location</td><td>Level, Floor, some Tags, BeamSystem, Rebar, Reinforcement, PointLoad, AreaLoad(without Host), Span Direction(IndependentTag)</td></tr><tr><td>No Location</td><td>View, LineLoad(with host), AreaLoad(with Host), BoundaryCondition</td></tr></tbody></table>

Note: There are other Elements without Location information. For example a LineLoad (with host) or an AreaLoad (with host) have no Location.

Some FamilyInstance LocationPoints, such as all in-place-FamilyInstances and masses, are specified to point (0, 0, 0) when they are created. The LocationPoint coordinate is changed if you transform or move the instance.

To change a Group-s LocationPoint, do one of the following:

-   Drag the Group origin in the Revit UI to change the LocationPoint coordinate. In this situation, the Group LocationPoint is changed while the Group-s location is not changed.
-   Move the Group using the ElementTransformUtils.MoveElement() method to change the LocationPoint. This changes both the Group location and the LocationPoint.

For more information about LocationCurve and LocationPoint, see [Moving Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Moving_Elements_html).

### Level

Levels are finite horizontal planes that act as a reference for level-hosted or level-based elements, such as roofs, floors, and ceilings. The Revit Platform API provides a Level class to represent level lines in Revit. Get the Level object to which the element is assigned using the API if the element is level-based.

<table summary="" id="GUID-BC19ED01-4A0E-48A4-A7F1-4CAFD0A950F6__TABLE_874419C0D7FB47C3933E8117BBA29AB7"><tbody><tr><td><b>Code Region 5-6: Assigning Level</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>AssignLevel</span><span>(</span><span>Element</span><span> element</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the level object to which the element is assigned.</span><span>
    </span><span>if</span><span> </span><span>(</span><span>element</span><span>.</span><span>LevelId</span><span>.</span><span>Equals</span><span>(</span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"The element isn't based on a level."</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>Level</span><span> level </span><span>=</span><span> element</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>element</span><span>.</span><span>LevelId</span><span>)</span><span> </span><span>as</span><span> </span><span>Level</span><span>;</span><span>

        </span><span>// Format the prompt information(Name and elevation)</span><span>
        </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"The element is based on a level."</span><span>;</span><span>
        prompt </span><span>+=</span><span> </span><span>"\nThe level name is:  "</span><span> </span><span>+</span><span> level</span><span>.</span><span>Name</span><span>;</span><span>
        prompt </span><span>+=</span><span> </span><span>"\nThe level elevation is:  "</span><span> </span><span>+</span><span> level</span><span>.</span><span>Elevation</span><span>;</span><span>

        </span><span>// Show the information to the user.</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>prompt</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

A number of elements, such as a column, use a level as a basic reference. When you get the column level, the level you retrieve is the Base Level.

Note: Get the Beam or Brace level using the Reference Level parameter. From the Level property, you only get null instead of the reference level information.

Level is the most commonly used element in Revit. In the Revit Platform API, retrieve all levels using a Level class filter.

For more Level details, see [Datum and Information Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_html).

### Parameter

Every element has a set of parameters that users can view and edit in Revit. The parameters are visible in the Element Properties dialog box (select any element and click the Properties button next to the type selector). For example, the following image shows Room parameters.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-78903670-DCD6-473B-AA90-45A0AA31B65D-low.png)**Figure 25: Room parameters**

In the Revit Platform API, each Element object has a Parameters property, which is a collection of all the properties attached to the Element. You can change the property values in the collection. For example, you can get the area of a room from the room object parameters; additionally, you can set the room number using the room object parameters. The Parameter is another way to provide access to property information not exposed in the element object.

In general, every element parameter has an associated parameter ID. Parameter IDs are represented by the ElementId class. For user-created parameters, the IDs correspond to real elements in the document. However, most parameters are built-in and their IDs are constants stored in ElementIds.

Parameter is a generic form of data storage in elements. In the Revit Platform API, it is best to use the built-in parameter ID to get the parameter. Revit has a large number of built-in parameters available using the BuiltInParameter enumerated type.

For more details, see [Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_html).
