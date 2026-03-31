


<!-- ===== BEGIN: Help  Discipline-Specific Functionality  Autodesk.md ===== -->

---
created: 2026-01-28T21:07:38 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Discipline-Specific Functionality | Autodesk

> ## Excerpt
> 

---
### Was this information helpful?

-   Yes
-   No


<!-- ===== END: Help  Discipline-Specific Functionality  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Architecture  Autodesk.md ===== -->

---
created: 2026-01-28T21:07:44 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Architecture_html
author: 
---

# Help | Architecture | Autodesk

> ## Excerpt
> This chapter covers API functionality that is specific to the architectural features of Revit:

---
This chapter covers API functionality that is specific to the architectural features of Revit:

-   Functionality related to rooms (Element.Room, RoomTag, etc.)


<!-- ===== END: Help  Architecture  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Rooms  Autodesk.md ===== -->

---
created: 2026-01-28T21:07:48 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Architecture_Rooms_html
author: 
---

# Help | Rooms | Autodesk

> ## Excerpt
> The following sections cover information about the room class, its parameters, and how to use the room class in the API.

---
The following sections cover information about the room class, its parameters, and how to use the room class in the API.

### Room, Area, and Tags

The Room class is used to represent rooms and elements such as room schedule and area plans. The properties and create function for different rooms, areas, and their corresponding tags in the API are listed in the following table:

**Table 55: Room, Area, and Tags relationship**

<table summary="" id="GUID-296B8B21-776F-4CA5-9541-4C9AC4FB1BD7__TABLE_3A75F9E14A7F403DA194E37757BAF07E"><tbody><tr><td><b>Element</b></td><td><b>Class</b></td><td><b>Category</b></td><td><b>Boundary</b></td><td><b>Location</b></td><td><b>Can Create</b></td></tr><tr><td>Room in Plan View</td><td>Room</td><td>OST_Rooms</td><td>Has if in an enclosed region</td><td>LocationPoint</td><td>NewRoom() except for NewRoom(Phase)</td></tr><tr><td>Room in Schedule View</td><td>Room</td><td>OST_Rooms</td><td>Null</td><td>Null</td><td>NewRoom(Phase)</td></tr><tr><td>Area</td><td>Room</td><td>OST_Areas</td><td>Always has</td><td>LocationPoint</td><td>No</td></tr><tr><td>Room Tag</td><td>RoomTag</td><td>OST_RoomTags</td><td></td><td>LocationPoint</td><td>Creation.Document.NewRoomTag()</td></tr><tr><td>Area Tag</td><td>FamilySymbol</td><td>OST_AreaTags</td><td></td><td>LocationPoint</td><td>No</td></tr></tbody></table>

Note: Room.Name is the combination of the room name and room number. For example, for a room whose number is 2 and whose name is "Upstairs Bedroom", Room.Name returns "Upstairs Bedroom 2". Use the ROOM\_NAME BuiltInParameter to get the room name.

Note: As an Annotation Element, the specific view is available using RoomTag.View. Never try to set the RoomTag.Name property because the name is automatically assigned; otherwise an exception is thrown.

### Creating a room

The following code illustrates the simplest way to create a room at a certain point in a specific level:

<table summary="" id="GUID-296B8B21-776F-4CA5-9541-4C9AC4FB1BD7__TABLE_688507D3BC0946D088B0F8A785E390FB"><tbody><tr><td><b>Code Region 28-1: Creating a room</b></td></tr><tr><td><pre><code><span>Room</span><span> </span><span>CreateRoom</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Level</span><span> level</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// Create a UV structure which determines the room location</span><span>
        UV roomLocation </span><span>=</span><span> </span><span>new</span><span> UV</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>

        </span><span>// Create a new room</span><span>
        </span><span>Room</span><span> room </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewRoom</span><span>(</span><span>level</span><span>,</span><span> roomLocation</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> room</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create a new room failed."</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> room</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Rooms can be created in a room schedule then inserted into a plan circuit.

-   The Document.NewRoom(Phase) method is used to create a new room, not associated with any specific location, and insert it into an existing schedule. Make sure the room schedule exists or create a room schedule in the specified phase before you make the call.
-   The Document.NewRoom(Room room, PlanCircuit circuit) method is used to create a room from a room in a schedule and a PlanCircuit.
    -   The input room must exist only in the room schedule, meaning that it does not display in any plan view.
    -   After invoking the method, a model room with the same name and number is created in the view where the PlanCircuit is located.

For more details about PlanCircuit, see Plan Topology below.

The following code illustrates the entire process:

<table summary="" id="GUID-296B8B21-776F-4CA5-9541-4C9AC4FB1BD7__TABLE_FC79A3F7D4D1444BBB53D8FE708C1DE2"><tbody><tr><td><b>Code Region 28-2: Creating and inserting a room into a plan circuit</b></td></tr><tr><td><pre><code><span>Room</span><span> </span><span>InsertNewRoomInPlanCircuit</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Level</span><span> level</span><span>,</span><span> </span><span>Phase</span><span> newConstructionPhase</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// create room using Phase</span><span>
    </span><span>Room</span><span> newScheduleRoom </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewRoom</span><span>(</span><span>newConstructionPhase</span><span>);</span><span>

    </span><span>// set the Room Number and Name</span><span>
    </span><span>string</span><span> newRoomNumber </span><span>=</span><span> </span><span>"101"</span><span>;</span><span>
    </span><span>string</span><span> newRoomName </span><span>=</span><span> </span><span>"Class Room 1"</span><span>;</span><span>
    newScheduleRoom</span><span>.</span><span>Name</span><span> </span><span>=</span><span> newRoomName</span><span>;</span><span>
    newScheduleRoom</span><span>.</span><span>Number</span><span> </span><span>=</span><span> newRoomNumber</span><span>;</span><span>

    </span><span>// Get a PlanCircuit</span><span>
    </span><span>PlanCircuit</span><span> planCircuit </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>// first get the plan topology for given level</span><span>
    </span><span>PlanTopology</span><span> planTopology </span><span>=</span><span> document</span><span>.</span><span>get_PlanTopology</span><span>(</span><span>level</span><span>);</span><span>

    </span><span>// Iterate circuits in this plan topology</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>PlanCircuit</span><span> circuit </span><span>in</span><span> planTopology</span><span>.</span><span>Circuits</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// get the first circuit we find</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> circuit</span><span>)</span><span>
        </span><span>{</span><span>
            planCircuit </span><span>=</span><span> circuit</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>Room</span><span> newRoom2 </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> planCircuit</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Create Room"</span><span>))</span><span>
        </span><span>{</span><span>
            </span><span>if</span><span> </span><span>(</span><span>transaction</span><span>.</span><span>Start</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Started</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// The input room must exist only in the room schedule, </span><span>
                </span><span>// meaning that it does not display in any plan view.</span><span>
                newRoom2 </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewRoom</span><span>(</span><span>newScheduleRoom</span><span>,</span><span> planCircuit</span><span>);</span><span>
                </span><span>// a model room with the same name and number is created in the </span><span>
                </span><span>// view where the PlanCircuit is located</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> newRoom2</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>// Give the user some information</span><span>
                    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Room placed in Plan Circuit successfully."</span><span>);</span><span>
                </span><span>}</span><span>
                transaction</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> newRoom2</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Once a room has been created and added to a location, it can be removed from the location (but still remains in available in the project) by using the Room.Unplace() method. It can then be placed in a new location.

### Room Boundary

Rooms have boundaries that create an enclosed region where the room is located.

-   Boundaries include the following elements:
    -   Walls
    -   Model lines
    -   Columns
    -   Roofs

#### Retrieving Room Boundaries

The boundary around a room is obtained from the base class method SpatialElement.GetBoundarySegments(). The method returns null when the room is not in an enclosed region or only exists in the schedule. Each room may have several regions, each of which have several segments hence the data is returned in the form of a list of BoundarySegment lists.

The following figure shows a room boundary selected in the Revit UI:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-E020193E-68FA-485C-A682-970439B603CA-low.png)**Figure 138: Room boundary**

The size of the segment list depends on the enclosed region topology. Each BoundarySegment list makes a circuit or a continuous line in which one segment joins the next. The following pictures provide several examples. In the following pictures, all walls are Room-Bounding and the model lines category is OST\_AreaSeparationLines. If an element is not Room-Bounding, it is excluded from the elements to make the boundary.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-C8247A40-AC00-4EF1-BBE9-66D4CA925FCA-low.png)**Figure 139: Rooms 1, 2, 3, 4**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-C8B9B186-ECE0-4077-B70A-3CCDC7E6F0A9-low.png)**Figure 140: Room 5, 6**

The following table provides the Room.GetBoundarySegments().Size results for the previous rooms:

**Table 56: Room.GetBoundarySegments().Size**

<table summary="" id="GUID-296B8B21-776F-4CA5-9541-4C9AC4FB1BD7__TABLE_9C4867FF72DB4355964D1183E0F511C1"><tbody><tr><td><b>Room</b></td><td><b>Room.GetBoundarySegments().Size</b></td></tr><tr><td>Room 1<p>Room 2</p><p>Room 3</p></td><td>1</td></tr><tr><td>Room 4</td><td>2</td></tr><tr><td>Room 5<p>Room 6</p></td><td>3</td></tr></tbody></table>

Note: Walls joined by model lines are considered continuous line segments. Single model lines are ignored.

After getting `IList<IList<BoundarySegment>>` , get the BoundarySegment by iterating the list.

#### BoundarySegment

The segments that make the region are represented by the BoundarySegment class; its ElementId property returns the id of the corresponding element with the following conditions:

-   For a ModelCurve element, the category must be BuiltInCategory.OST\_AreaSeparationLines meaning that it represents a Room Separator.
-   For other elements such as wall, column, and roof, if the element is a room boundary, the Room Bounding parameter (BuiltInParameter.WALL\_ATTR\_ROOM\_BOUNDING) must be true as in the following picture.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-F762B108-6A38-490C-8C31-6536BD47C294-low.png)**Figure 141: Room Bounding property**

<table summary="" id="GUID-296B8B21-776F-4CA5-9541-4C9AC4FB1BD7__TABLE_1AB2B76C083C4432A13D135957D26A78"><tbody><tr><td><b>Code Region 28-3: Setting room bounding</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>SetRoomBounding</span><span>(</span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
 </span><span>Parameter</span><span> parameter </span><span>=</span><span> wall</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>WallAttrRoomBounding</span><span>);</span><span>
    parameter</span><span>.</span><span>Set</span><span>(</span><span>1</span><span>);</span><span>   </span><span>//set "Room Bounding" to true</span><span>
    parameter</span><span>.</span><span>Set</span><span>(</span><span>0</span><span>);</span><span>   </span><span>//set "Room Bounding" to false</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Notice how the roof forms the BoundarySegment for a room in the following pictures. The first picture shows Level 3 in the elevation view. The room is created in the Level 3 floor view. The latter two pictures show the boundary of the room and the house in 3D view.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-B1B62BD3-BA8F-4E97-8339-2D0332B60B8D-low.png)**Figure 142: Room created in level 3 view**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-CD7125F1-550D-43EE-AAE0-C713A68E4F0C-low.png)**Figure 143: Room boundary formed by** roof

The area boundary can only be a ModelCurve with the category Area Boundary (BuiltInCategory.OST\_AreaSchemeLines) while the boundary of the displayed room can be walls and other elements.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-43500822-B45E-44BC-811A-B2968583A253-low.png)**Figure 144: Wall end edge**

If the BoundarySegment corresponds to the curve between the room separation and wall as the previous picture shows:

-   The Element property returns null
-   The Curve is not null.

#### Boundary and Transaction

When you call Room.GetBoundarySegments() after creating an Element using the API such as a wall, the wall can change the room boundary. You must make sure the data is updated.

The following illustrations show how the room changes after a wall is created using the Revit Platform API.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-ED28E6B5-4AD6-436F-860E-0928BF5E3093-low.png)**Figure 145: Added wall changes the room boundary**

To update the room boundary data, use the transaction mechanism in the following code:

<table summary="" id="GUID-296B8B21-776F-4CA5-9541-4C9AC4FB1BD7__TABLE_3EE0B931892A494099FC8367E84A1609"><tbody><tr><td><b>Code Region 28-4: Using a transaction to update room boundary</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>UpdateRoomBoundary</span><span>(</span><span>UIApplication</span><span> application</span><span>,</span><span> </span><span>Room</span><span> room</span><span>,</span><span> </span><span>Level</span><span> level</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Document</span><span> document </span><span>=</span><span> application</span><span>.</span><span>ActiveUIDocument</span><span>.</span><span>Document</span><span>;</span><span>

    </span><span>//Get the size before creating a wall</span><span>
    </span><span>int</span><span> size </span><span>=</span><span> room</span><span>.</span><span>GetBoundarySegments</span><span>(</span><span>new</span><span> </span><span>SpatialElementBoundaryOptions</span><span>()).</span><span>First</span><span>().</span><span>Count</span><span>;</span><span>
    </span><span>string</span><span> message </span><span>=</span><span> </span><span>"Room boundary size before wall: "</span><span> </span><span>+</span><span> size</span><span>;</span><span>

    </span><span>//Prepare a line</span><span>
    XYZ startPos </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(-</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    XYZ endPos </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Line</span><span> line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>startPos</span><span>,</span><span> endPos</span><span>);</span><span>

    </span><span>//Create a new wall and enclose the creating into a single transaction</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Create Wall"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>transaction</span><span>.</span><span>Start</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Started</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>Wall</span><span> wall </span><span>=</span><span> </span><span>Wall</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> line</span><span>,</span><span> level</span><span>.</span><span>Id</span><span>,</span><span> </span><span>false</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> wall</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>TransactionStatus</span><span>.</span><span>Committed</span><span> </span><span>==</span><span> transaction</span><span>.</span><span>Commit</span><span>())</span><span>
                </span><span>{</span><span>
                    </span><span>//Get the new size</span><span>
                    size </span><span>=</span><span> room</span><span>.</span><span>GetBoundarySegments</span><span>(</span><span>new</span><span> </span><span>SpatialElementBoundaryOptions</span><span>()).</span><span>First</span><span>().</span><span>Count</span><span>;</span><span>
                    message </span><span>+=</span><span> </span><span>"\nRoom boundary size after wall: "</span><span> </span><span>+</span><span> size</span><span>;</span><span>
                    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> message</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span>
            </span><span>{</span><span>
                transaction</span><span>.</span><span>RollBack</span><span>();</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

For more details, see [Transactions](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_html).

### Plan Topology

The level plan that rooms lie in have a topology made by elements such as walls and room separators. The PlanTopology and PlanCircuit classes are used to present the level topology.

-   Get the PlanTopology object from the Document object using the Level. In each plan view, there is one PlanTopology corresponding to every phase.
-   The same condition applies to BoundarySegment, except room separators and Elements whose Room Bounding parameter is true can be a side (boundary) in the PlanCircuit.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-F3DEA4DB-6737-4FCE-92D2-71887B180850-low.png)**Figure 146: Room and Plan Topology diagram**

The PlanCircuit.SideNum property returns the circuit side number, while SpatialElement.GetBoundarySegments() returns an `IList<IList<Autodesk.Revit.DB.BoundarySegment>>` , whose Count is different from the circuit side number.

-   SpatialElement.GetBoundarySegments() recognizes the bottom wall as two walls if there is a branch on the wall.
-   PlanCircuit.SideNum always sees the bottom wall in the picture as one regardless of the number of branches.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-A0516A39-7DA6-4836-872D-7F6B8CCE9AC6-low.png)**Figure 147: Compare room boundary with PlanCircuit**

**Table 57: Compare Room Boundary with PlanCircuit**

|  |  |  |
| --- | --- | --- |
| Circuit | Circuit.SideNum | `IList<IList<Autodesk.Revit.DB.BoundarySegment>>.Count` for Room |
| Circuit 1 | 3 | 3 (Room1) |
| Circuit 2 | 4 +2 = 6 | 4 +3 = 7 (Room2) |
| Circuit 3 | 3 +2 = 5 | 3 +3 = 6 (Room3) |
| Circuit 4 | 3 | 3 (Room4) |
| Circuit 5 | 3 | 3 (Room5) |

### Room and FamilyInstance

Doors and Windows are special family instances related to Room. Only doors are discussed here since the only difference is that windows have no handle to flip.

The following characteristics apply to doors:

-   Door elements can exist without a room.
-   In the API (and only in the API), a Door element has two additional properties that refer to the regions on the two opposite sides of a door: ToRoom and FromRoom
-   If the region is a room, the property's value would be a Room element.
-   If the region is not a room, the property will return null. Both properties may be null at the same time.
-   The region on the side into which a door opens, will be ToRoom. The room on the other side will be FromRoom.
-   Both properties get dynamically updated whenever the corresponding regions change.

In the following pictures, five doors are inserted into walls without flipping the facing. The table lists the FromRoom, ToRoom, and Room properties for each door. The Room property belongs to all Family Instances.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-23DF1ADB-3B88-489B-9FA6-2FA4B976C81E-low.png)**Figure 148: Door 1**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-DC31973C-8DD6-4FD2-A2A7-5CCD23C09D96-low.png)**Figure 149: Door 2**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4A8FCCCC-163D-4DA2-8E23-4697EF0D4FB7-low.png)**Figure 150: Door 3**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-AE717BBD-B64C-4114-8359-7C4BF49B1151-low.png)**Figure 151: Door 4**

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-A10FBA3A-E29D-4E15-A48B-727AF19103DB-low.png)**Figure 152: Door 5**

**Table 58: Door Properties**

<table summary="" id="GUID-296B8B21-776F-4CA5-9541-4C9AC4FB1BD7__TABLE_03F9594B2C7B461795D0E26AFA269340"><tbody><tr><td><b>Door</b></td><td><b>FromRoom</b></td><td><b>ToRoom</b></td><td><b>Room</b></td></tr><tr><td>Door 1</td><td>null</td><td>null</td><td>null</td></tr><tr><td>Door 2</td><td>Room 1</td><td>null</td><td>null</td></tr><tr><td>Door 3</td><td>Room 3</td><td>Room 2</td><td>Room 2</td></tr><tr><td>Door 4</td><td>Room 4</td><td>null</td><td>null</td></tr><tr><td>Door 5</td><td>null</td><td>Room 6</td><td>Room 6</td></tr></tbody></table>

All family instances have the Room property, which is the room where an instance is located in the last project phase. Windows and doors face into a room. Change the room by flipping the door or window facing, or by calling FamilyInstance.FlipFromToRoom(). For other kinds of instances, such as beams and columns, the Room is the room that has the same boundary as the instance.

The following code illustrates how to get the Room from the family instance. It is necessary to check if the result is null or not.

<table summary="" id="GUID-296B8B21-776F-4CA5-9541-4C9AC4FB1BD7__TABLE_B527281679094DA792C75BDF548381E8"><tbody><tr><td><b>Code Region 28-5: Getting a room from the family instance</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetRoomInfo</span><span>(</span><span>FamilyInstance</span><span> familyInstance</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Room</span><span> room </span><span>=</span><span> familyInstance</span><span>.</span><span>Room</span><span>;</span><span>
        room </span><span>=</span><span> familyInstance</span><span>.</span><span>FromRoom</span><span>;</span><span>  </span><span>//for door and window family only</span><span>
        room </span><span>=</span><span> familyInstance</span><span>.</span><span>ToRoom</span><span>;</span><span>    </span><span>//for door and window family only</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> room</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>//use the room...</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Other Room Properties

The Room class has several other properties you can use to get information about the object. Rooms have these read-only dimension properties:

-   Area
-   Perimeter
-   UnboundedHeight
-   Volume
-   ClosedShell

This example displays the dimension information for a selected room. Note that the volume calculations setting must be enabled, or the room volume is returned as 0.

<table summary="" id="GUID-296B8B21-776F-4CA5-9541-4C9AC4FB1BD7__TABLE_73F54C983FE64483B3ECE04CA88B2D54"><tbody><tr><td><b>Code Region 28-6: Getting a room's dimensions</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetRoomDimensions</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>Room</span><span> room</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>String</span><span> roominfo </span><span>=</span><span> </span><span>"Room dimensions:\n"</span><span>;</span><span>
    </span><span>// turn on volume calculations:</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> t </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Turn on volume calculation"</span><span>))</span><span>
    </span><span>{</span><span>
        t</span><span>.</span><span>Start</span><span>();</span><span>
        </span><span>AreaVolumeSettings</span><span> settings </span><span>=</span><span> </span><span>AreaVolumeSettings</span><span>.</span><span>GetAreaVolumeSettings</span><span>(</span><span>doc</span><span>);</span><span>
        settings</span><span>.</span><span>ComputeVolumes</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        t</span><span>.</span><span>Commit</span><span>();</span><span>
    </span><span>}</span><span>

    roominfo </span><span>+=</span><span> </span><span>"Vol: "</span><span> </span><span>+</span><span> room</span><span>.</span><span>Volume</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
    roominfo </span><span>+=</span><span> </span><span>"Area: "</span><span> </span><span>+</span><span> room</span><span>.</span><span>Area</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
    roominfo </span><span>+=</span><span> </span><span>"Perimeter: "</span><span> </span><span>+</span><span> room</span><span>.</span><span>Perimeter</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
    roominfo </span><span>+=</span><span> </span><span>"Unbounded height: "</span><span> </span><span>+</span><span> room</span><span>.</span><span>UnboundedHeight</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>roominfo</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The ClosedShell property for a Room (or Space) is the geometry formed by the boundaries of the open space of the room (walls, floors, ceilings, roofs, and boundary lines). This property is useful if you need to check for intersection with other physical element in the model with the room, for example, to see if part or all of the element is located in the room. For an example, see the RoofsRooms sample application, included with the Revit SDK, where ClosedShell is used to check whether a room is vertically unbounded.

In addition, you can get or set the base offset and limit offset for rooms with these properties:

-   BaseOffset
-   LimitOffset

You can get or set the level that defines the upper limit of the room with the UpperLimit property.


<!-- ===== END: Help  Rooms  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Civil Alignments API  Autodesk.md ===== -->

---
created: 2026-01-28T21:07:53 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Civil_html
author: 
---

# Help | Civil Alignments API | Autodesk

> ## Excerpt
> Revit provides support for Civil Alignments and their associated annotations. Alignments are imported from InfraWorks as a part of the workflow to
transfer Civil Structures. The API supports read of alignment properties and geometric information, along with read/write and create of associated
annotations. All new classes for the Alignments API are exposed through a different assembly in the Revit installation, located at Addins\CivilAlignments
\Autodesk.CivilAlignments.DBApplication.dll

---
Revit provides support for Civil Alignments and their associated annotations. Alignments are imported from InfraWorks as a part of the workflow to transfer Civil Structures. The API supports read of alignment properties and geometric information, along with read/write and create of associated annotations. All new classes for the Alignments API are exposed through a different assembly in the Revit installation, located at Addins\\CivilAlignments \\Autodesk.CivilAlignments.DBApplication.dll

`Autodesk.Revit.DB.Infrastructure.Alignment` represents an alignment and can be used to find alignments in a document, and to query a particular alignment's properties and to analyze alignment geometry. This object is not an Element, but the underlying Element can be obtained from this object if needed.

`Autodesk.Revit.DB.Infrastructure.AlignmentStationLabel` represents an alignment station label annotation and can be used to find such labels in a document as well as to create and modify such labels. This object is not an Element, but the underlying Element (which is a SpotDimension instance) can be obtained from this object if needed.

-   Autodesk.Revit.DB.Infrastructure.AlignmentStationLabelOptions
-   Autodesk.Revit.DB.Infrastructure.AlignmentStationLabelSetOptions provide options for creating a single alignment label or for creating a set of alignment labels.


<!-- ===== END: Help  Civil Alignments API  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  MEP Engineering  Autodesk.md ===== -->

---
created: 2026-01-28T21:07:58 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_html
author: 
---

# Help | MEP Engineering | Autodesk

> ## Excerpt
> 

---
-   [Help Home](https://help.autodesk.com/view/RVT/2023/ENU/)

[![](https://help.autodesk.com/view/RVT/2023/ENU/images/product-title.png)](https://help.autodesk.com/view/RVT/2023/ENU/)

-   What's New in Revit
-   Revit 2023 Release Notes
-   Get Started
-   Have You Tried
-   Cloud Models
-   Model the Design
-   Architectural Design
-   Structural Engineering
-   MEP Engineering
-   Document and Present the Design
-   Analyze the Design
-   Collaborate with Others
-   Customize Revit
-   Dynamo for Revit
-   Revit and Revit LT Installation
-   Autodesk Installation
-   Revit Developer's Guide
    -   [Revit API Developers Guide](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_html)
        -   [Introduction](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_html)
        -   [Basic Interaction with Revit Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_html)
        -   [Revit Geometric Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_html)
        -   [Discipline-Specific Functionality](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_html)
            -   [Architecture](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Architecture_html)
            -   [Civil Alignments API](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Civil_html)
            -   [MEP Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_html)
                -   [MEP Element Creation](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Element_Creation_html)
                -   [MEP Systems](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Systems_html)
                -   [Connectors](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Connectors_html)
                -   [MEP Fabrication Detailing](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Fabrication_Detailing_html)
                -   [Family Creation](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Family_Creation_html)
                -   [Mechanical Settings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Mechanical_Settings_html)
                -   [Electrical Analysis for Preliminary Design](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Electrical_Analysis_for_Preliminary_Design_html)
                -   [Electrical Settings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Electrical_Settings_html)
                -   [Routing Preferences](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Routing_Preferences_html)
            -   [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html)
            -   [Site](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Site_html)
        -   [Advanced Topics](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_html)
        -   [Appendices](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_html)
        -   [FAQ](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_FAQ_html)
-   Troubleshoot

To support MEP engineering features of the Revit software, the API provides read and write access to HVAC and Piping data in a Revit model including:

-   Traversing ducts, pipes, fittings, and connectors in a system
-   Adding, removing, and changing ducts, pipes, and other equipment
-   Getting and setting system properties
-   Determining if the system is well-connected
-   Access to Mechanical Settings
-   Managing Routing Preferences

### Was this information helpful?

-   Yes
-   No


<!-- ===== END: Help  MEP Engineering  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  MEP Element Creation  Autodesk.md ===== -->

---
created: 2026-01-28T21:08:03 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Element_Creation_html
author: 
---

# Help | MEP Element Creation | Autodesk

> ## Excerpt
> MEP Elements can be created using the Revit API.

---
MEP Elements can be created using the Revit API.

Many elements related to duct, pipe and electrical systems can be created using the following methods available in the Autodesk.Revit.Creation.Document class:

-   NewFlexDuct
-   NewFlexPipe
-   NewMechanicalSystem
-   NewPipingSystem
-   NewCrossFitting
-   NewElbowFitting
-   NewTakeoffFitting
-   NewTeeFitting
-   NewTransitionFitting
-   NewUnionFitting

Other MEP elements, such as pipes, can only be created using the static Create() method of its corresponding class. Some MEP elements, such as ducts, can be created by a static method of the corresponding class (i.e. Duct) or by a method of the Autodesk.Revit.Creation.Document class. For these elements, the static Create() method is preferred.

-   Duct
-   FlexDuct
-   Pipe
-   FlexPipe
-   PipingSystem
-   Wire


<!-- ===== END: Help  MEP Element Creation  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Create Pipes and Ducts  Autodesk.md ===== -->

---
created: 2026-01-28T21:08:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Element_Creation_Create_Pipes_and_Ducts_html
author: 
---

# Help | Create Pipes and Ducts | Autodesk

> ## Excerpt
> There are 3 ways to create new ducts, flex ducts, pipes and flex pipes. They can be created between two points, between two connectors, or between a point and a connector.

---
There are 3 ways to create new ducts, flex ducts, pipes and flex pipes. They can be created between two points, between two connectors, or between a point and a connector.

The following code creates a new pipe between two points using the Pipe.Create() method. New flex pipes, ducts and flex ducts can all be created similarly.

<table summary="" id="GUID-0B91BAE8-59FD-4D4B-84E6-53B6A21DE00A__TABLE_629FE6ABDA5B4E2AB6D5B0C751A762BE"><tbody><tr><td><b>Code Region: Creating a new Pipe using static Create() method</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Pipe</span><span> </span><span>CreateNewPipe</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>ElementId</span><span> systemTypeId</span><span>,</span><span> </span><span>ElementId</span><span> levelId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// find a pipe type</span><span>

    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>PipeType</span><span>));</span><span>
    </span><span>PipeType</span><span> pipeType </span><span>=</span><span> collector</span><span>.</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>PipeType</span><span>;</span><span>

    </span><span>Pipe</span><span> pipe </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> pipeType</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// create pipe between 2 points</span><span>
        XYZ p1 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
        XYZ p2 </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>

        pipe </span><span>=</span><span> </span><span>Pipe</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> systemTypeId</span><span>,</span><span> pipeType</span><span>.</span><span>Id</span><span>,</span><span> levelId</span><span>,</span><span> p1</span><span>,</span><span> p2</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> pipe</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The code region below demonstrates how to create a FlexPipe using the static FlexPipe.Create() method. Pipes, ducts and flex ducts can all be created between two points similarly.

<table summary="" id="GUID-0B91BAE8-59FD-4D4B-84E6-53B6A21DE00A__TABLE_F0DB25A497FD4C038875DAFA6DEDBB62"><tbody><tr><td><b>Code Region: Creating a new FlexPipe using static Create() method</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>FlexPipe</span><span> </span><span>CreateFlexPipe</span><span>(</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Level</span><span> level</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// find a pipe type</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FlexPipeType</span><span>));</span><span>
    </span><span>ElementId</span><span> pipeTypeId </span><span>=</span><span> collector</span><span>.</span><span>FirstElementId</span><span>();</span><span>

    </span><span>// find a pipe system type</span><span>
    </span><span>FilteredElementCollector</span><span> sysCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    sysCollector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>PipingSystemType</span><span>));</span><span>
    </span><span>ElementId</span><span> pipeSysTypeId </span><span>=</span><span> sysCollector</span><span>.</span><span>FirstElementId</span><span>();</span><span>

    </span><span>FlexPipe</span><span> pipe </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>pipeTypeId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span> </span><span>&amp;&amp;</span><span> pipeSysTypeId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// create flex pipe with 3 points</span><span>
        </span><span>List</span><span>&lt;</span><span>XYZ</span><span>&gt;</span><span> points </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>XYZ</span><span>&gt;();</span><span>
        points</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span>
        points</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>10</span><span>,</span><span> </span><span>0</span><span>));</span><span>
        points</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>10</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span>

        pipe </span><span>=</span><span> </span><span>FlexPipe</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> pipeSysTypeId</span><span>,</span><span> pipeTypeId</span><span>,</span><span> level</span><span>.</span><span>Id</span><span>,</span><span> points</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> pipe</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

After creating a pipe, you might want to change the diameter. The Diameter property of Pipe is read-only. To change the diameter, get the RBS\_PIPE\_DIAMETER\_PARAM built-in parameter.

<table summary="" id="GUID-0B91BAE8-59FD-4D4B-84E6-53B6A21DE00A__TABLE_FEBF3895FB4F4222B6C2BB56524CDDBE"><tbody><tr><td><b>Code Region: Changing pipe diameter</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ChangePipeSize</span><span>(</span><span>Pipe</span><span> pipe</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>Parameter</span><span> parameter </span><span>=</span><span> pipe</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>RbsPipeDiameterParam</span><span>);</span><span>

        </span><span>string</span><span> message </span><span>=</span><span> </span><span>"Pipe diameter: "</span><span> </span><span>+</span><span> parameter</span><span>.</span><span>AsValueString</span><span>();</span><span>

        parameter</span><span>.</span><span>Set</span><span>(</span><span>0.5</span><span>);</span><span> </span><span>// set to 6"</span><span>

        </span><span>// Regenerate the docucment before trying to read a parameter that has been edited</span><span>
        pipe</span><span>.</span><span>Document</span><span>.</span><span>Regenerate</span><span>();</span><span>

        message </span><span>+=</span><span> </span><span>"\nPipe diameter after set: "</span><span> </span><span>+</span><span> parameter</span><span>.</span><span>AsValueString</span><span>();</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> message</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Another common way to create a new duct or pipe is between two existing connectors, as the following example demonstrates. In this example, it is assumed that 2 elements with connectors have been selected in Revit, one being a piece of mechanical equipment and the other a duct fitting with a connector that lines up with the SupplyAir connector on the equipment.

<table summary="" id="GUID-0B91BAE8-59FD-4D4B-84E6-53B6A21DE00A__TABLE_82FB37180A8B4D1BB713AB2CE9F8F78F"><tbody><tr><td><b>Code Region: Adding a duct between two connectors</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Duct</span><span> </span><span>CreateDuctBetweenConnectors</span><span>(</span><span>UIDocument</span><span> uiDocument</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// prior to running this example</span><span>
    </span><span>// select some mechanical equipment with a supply air connector</span><span>
    </span><span>// and an elbow duct fitting with a connector in line with that connector</span><span>
    </span><span>ElementId</span><span> levelId </span><span>=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>;</span><span>
    </span><span>Connector</span><span> connector1 </span><span>=</span><span> </span><span>null</span><span>,</span><span> connector2 </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>ConnectorSetIterator</span><span> csi </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uiDocument</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>
    </span><span>Document</span><span> document </span><span>=</span><span> uiDocument</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>// First find the selected equipment and get the correct connector</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Element</span><span> e </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>e </span><span>is</span><span> </span><span>FamilyInstance</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>FamilyInstance</span><span> </span><span>fi</span><span> </span><span>=</span><span> e </span><span>as</span><span> </span><span>FamilyInstance</span><span>;</span><span>
            </span><span>Family</span><span> family </span><span>=</span><span> </span><span>fi</span><span>.</span><span>Symbol</span><span>.</span><span>Family</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>family</span><span>.</span><span>FamilyCategory</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Mechanical Equipment"</span><span>)</span><span>
            </span><span>{</span><span>
                csi </span><span>=</span><span> </span><span>fi</span><span>.</span><span>MEPModel</span><span>.</span><span>ConnectorManager</span><span>.</span><span>Connectors</span><span>.</span><span>ForwardIterator</span><span>();</span><span>
                </span><span>while</span><span> </span><span>(</span><span>csi</span><span>.</span><span>MoveNext</span><span>())</span><span>
                </span><span>{</span><span>
                    </span><span>Connector</span><span> conn </span><span>=</span><span> csi</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>Connector</span><span>;</span><span>
                    </span><span>if</span><span> </span><span>(</span><span>conn</span><span>.</span><span>Direction</span><span> </span><span>==</span><span> </span><span>FlowDirectionType</span><span>.</span><span>Out</span><span> </span><span>&amp;&amp;</span><span> 
                        conn</span><span>.</span><span>DuctSystemType</span><span> </span><span>==</span><span> </span><span>DuctSystemType</span><span>.</span><span>SupplyAir</span><span>)</span><span>
                    </span><span>{</span><span>
                        connector1 </span><span>=</span><span> conn</span><span>;</span><span>
                        levelId </span><span>=</span><span> family</span><span>.</span><span>LevelId</span><span>;</span><span>
                        </span><span>break</span><span>;</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>// next find the second selected item to connect to</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Element</span><span> e </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>e </span><span>is</span><span> </span><span>FamilyInstance</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>FamilyInstance</span><span> </span><span>fi</span><span> </span><span>=</span><span> e </span><span>as</span><span> </span><span>FamilyInstance</span><span>;</span><span>
            </span><span>Family</span><span> family </span><span>=</span><span> </span><span>fi</span><span>.</span><span>Symbol</span><span>.</span><span>Family</span><span>;</span><span>
            </span><span>if</span><span> </span><span>(</span><span>family</span><span>.</span><span>FamilyCategory</span><span>.</span><span>Name</span><span> </span><span>!=</span><span> </span><span>"Mechanical Equipment"</span><span>)</span><span>
            </span><span>{</span><span>
                csi </span><span>=</span><span> </span><span>fi</span><span>.</span><span>MEPModel</span><span>.</span><span>ConnectorManager</span><span>.</span><span>Connectors</span><span>.</span><span>ForwardIterator</span><span>();</span><span>
                </span><span>while</span><span> </span><span>(</span><span>csi</span><span>.</span><span>MoveNext</span><span>())</span><span>
                </span><span>{</span><span>
                    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> connector2</span><span>)</span><span>
                    </span><span>{</span><span>
                        </span><span>Connector</span><span> conn </span><span>=</span><span> csi</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>Connector</span><span>;</span><span>

                        </span><span>// make sure to choose the connector in line with the first connector</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>Math</span><span>.</span><span>Abs</span><span>(</span><span>conn</span><span>.</span><span>Origin</span><span>.</span><span>Y </span><span>-</span><span> connector1</span><span>.</span><span>Origin</span><span>.</span><span>Y</span><span>)</span><span> </span><span>&lt;</span><span> </span><span>0.001</span><span>)</span><span>
                        </span><span>{</span><span>
                            connector2 </span><span>=</span><span> conn</span><span>;</span><span>
                            </span><span>break</span><span>;</span><span>
                        </span><span>}</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>Duct</span><span> duct </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> connector1 </span><span>&amp;&amp;</span><span> </span><span>null</span><span> </span><span>!=</span><span> connector2 </span><span>&amp;&amp;</span><span> levelId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// find a duct type</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>uiDocument</span><span>.</span><span>Document</span><span>);</span><span>
        collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>DuctType</span><span>));</span><span>

        </span><span>// Use Linq query to make sure it is one of the rectangular duct types</span><span>
        </span><span>var</span><span> query </span><span>=</span><span> </span><span>from</span><span> element </span><span>in</span><span> collector
                    </span><span>where</span><span> element</span><span>.</span><span>Name</span><span>.</span><span>Contains</span><span>(</span><span>"Mitered Elbows"</span><span>)</span><span> </span><span>==</span><span> </span><span>true</span><span>
                    </span><span>select</span><span> element</span><span>;</span><span>

        </span><span>// use extension methods to get first duct type</span><span>
        </span><span>DuctType</span><span> ductType </span><span>=</span><span> collector</span><span>.</span><span>Cast</span><span>&lt;</span><span>DuctType</span><span>&gt;().</span><span>First</span><span>&lt;</span><span>DuctType</span><span>&gt;();</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> ductType</span><span>)</span><span>
        </span><span>{</span><span>
            duct </span><span>=</span><span> </span><span>Duct</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> ductType</span><span>.</span><span>Id</span><span>,</span><span> levelId</span><span>,</span><span> connector1</span><span>,</span><span> connector2</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> duct</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Lining and Insulation

Pipe and duct insulation and lining can be added as separate objects associated with ducts and pipes. The ids of insulation elements associated with a duct or pipe can be retrieved using the static method InsulationLiningBase.GetInsulationIds() while the ids of lining elements can be retreived using the static method InsulationLiningBase.GetLiningIds().

To create new insulations associated with a given duct, pipe, fitting, accessory, or content use the corresponding static method: DuctInsulation.Create() or PipeInsulation.Create(). DuctLining.Create() can be used to create a new instance of a lining applied to the inside of a given duct, fitting or accessory.


<!-- ===== END: Help  Create Pipes and Ducts  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Creating Wires  Autodesk.md ===== -->

---
created: 2026-01-28T21:08:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Element_Creation_Creating_Wires_html
author: 
---

# Help | Creating Wires | Autodesk

> ## Excerpt
> New electrical wires can be created using the Revit API.

---
New electrical wires can be created using the Revit API.

The static Wire.Create() allows for new wires to be created in the document. The Create() method requires the id of the view in which the newly created wire will be visible. It must be the id of a floor plan or reflected ceiling plan view. The WiringType for the wire can be either Arc, for wiring that is concealed within walls, ceilings, or floors, or Chamfer, for wiring that is exposed.

The location of the wire is specified by a list of XYZ points defining the vertices of the wire, and optionally a start and/or end connector. The endpoint connectors can be null, however, if the start connector is specified, the connector's origin will be added to the wire's vertices as the start point. Likewise, if the end connector is specified, the connector's origin will be added to the wire's vertices as the end point. The static method Wire.AreVertexPointsValid() will check a list of XYZ points and start and end connectors to ensure they are suitable for a wire.

The shape of the wire is determined by it's wiring type and the total number of points supplied via the vertex points and endpoint connectors. If the wiring type is WiringType.Arc:

-   If there are 2 total points supplied, the wire is a straight-line wire.
-   If there are 3 total points supplied, the wire is a circular arc wire.
-   If there are 4 or more points, the wire is a spline wire.

If the wiring type is WiringType.Chamfer, a polyline wire will be created connecting all the points.

The following example creates a new straight-line wire in the active view with no connectors specified.

<table summary="" id="GUID-E529A8B2-2104-44F4-8C94-95109EFE35AA__TABLE_5421C731BF84459E860D8DA820244CCA"><tbody><tr><td><b>Code Region: Creating a new wire</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>Wire</span><span> </span><span>CreateWire</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Wire</span><span> wire </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>IList</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> wireTypes </span><span>=</span><span> collector</span><span>.</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Wire</span><span>).</span><span>WhereElementIsElementType</span><span>().</span><span>ToElements</span><span>();</span><span>
    </span><span>WireType</span><span> wireType </span><span>=</span><span> wireTypes</span><span>.</span><span>First</span><span>()</span><span> </span><span>as</span><span> </span><span>WireType</span><span>;</span><span>

    </span><span>if</span><span> </span><span>(</span><span>wireType </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>IList</span><span>&lt;</span><span>XYZ</span><span>&gt;</span><span> wireVertices </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>XYZ</span><span>&gt;();</span><span>
        wireVertices</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span>
        wireVertices</span><span>.</span><span>Add</span><span>(</span><span>new</span><span> XYZ</span><span>(</span><span>2</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>));</span><span>

        wire </span><span>=</span><span> </span><span>Wire</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> wireType</span><span>.</span><span>Id</span><span>,</span><span> document</span><span>.</span><span>ActiveView</span><span>.</span><span>Id</span><span>,</span><span> </span><span>WiringType</span><span>.</span><span>Arc</span><span>,</span><span> wireVertices</span><span>,</span><span> </span><span>null</span><span>,</span><span> </span><span>null</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> wire</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Connectors

To connect a wire to elements after creation, call Wire.ConnectTo(), passing in a start and end connector. If the wire is already connected when this method is used, the old connection will be disconnected and the wire will be connected to the new target.

### Vertices

Once a wire is created, vertices can be retrieved using the Wire.GetVertex() method. This method takes an index of the requested vertex which should be between 0 and Wire.NumberOfVertices (which includes the start and end points of the wire).

Use Wire.AppendVertex() to add a vertex to the end of the list, or Wire.InsertVertex() to add a vertex at a specific point in the list. The Wire.IsVertexPointValid() method checks if the given vertex point can be added to this wire. IsVertexPointValid() will return false if the point cannot be added because there is already a vertex at this position on the view plane (within tolerance). Note that a vertex cannot be inserted before the start vertex if the start vertex already connects to an element. Similarly, a vertex cannot be appended to the end of the list if the end point is already connected to an element.

Wire.RemoveVertex() will remove a vertex from the list. If the wire vertex is already connected to an element, this method will fail to remove the vertex. In order to remove this vertex, it should be disconnected first, then removed, and then reconnected (if required).


<!-- ===== END: Help  Creating Wires  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Placeholders  Autodesk.md ===== -->

---
created: 2026-01-28T21:08:19 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Element_Creation_Placeholders_html
author: 
---

# Help | Placeholders | Autodesk

> ## Excerpt
> The Revit API provides the ability to put placeholder elements into a system when the exact design of the layout is not yet know. Using placeholder ducts and pipes can allow for a well-connected system while the design is still unknown, and then which can then be elaborated in the final design at a later stage.

---
### Placeholder ducts and pipes

The Revit API provides the ability to put placeholder elements into a system when the exact design of the layout is not yet know. Using placeholder ducts and pipes can allow for a well-connected system while the design is still unknown, and then which can then be elaborated in the final design at a later stage.

The two static methods Duct.CreatePlaceholder() and Pipe.CreatePlaceholder() create placeholder elements. The IsPlaceholder property of Duct and Pipe indicates whether they are a placeholder element or not.

When ready to create actual ducts and pipes from the placeholders, use the MechanicalUtils.ConvertDuctPlaceholders() and PlumbingUtils.ConvertPipePlaceholders() methods to convert a set of placeholder elements to ducts and pipes. Once conversion succeeds, the placeholder elements are deleted. The new duct, pipe and fitting elements are created and connections are established.


<!-- ===== END: Help  Placeholders  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Creating Systems  Autodesk.md ===== -->

---
created: 2026-01-28T21:08:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Element_Creation_Creating_Systems_html
author: 
---

# Help | Creating Systems | Autodesk

> ## Excerpt
> Create electrical, mechanical and piping systems.

---
Create electrical, mechanical and piping systems.

MechanicalSystem and PipingSystem have static overloaded Create() methods to create new mechanical or piping systems. This is the preferred method for creating new MEP Systems. The simplest Create() overload for both classes creates a new system in a given document with a given type Id (which should be the Id for a DuctSystemType for a MechanicalSystem or the Id of a PipeSystemType for a PipingSystem. Both classes have a second Create() overload that also takes a name for the system. Once created, elements can be added to the system using the MEPSystem.Add() method.

MechanicalSystem and PipingSystem can also be created from the Creation.Document class using NewMechanicalSystem() and NewPipingSystem(). NewPipingSystem() and NewMechanicalSystem() both take a Connector that is the base equipment connector, such as a hot water heater for a piping system, or a fan for a mechanical system. They also take a ConnectorSet of connectors that will be added to the system, such as faucets on sinks in a piping system. The last piece of information required to create a new system is either a PipeSystemType for NewPipingSystem() or a DuctSystemType for NewMechanicalSystem().

Electrical systems can be created using the ElectricalSystem.Create method, which has two overloads. One creates a new ElectricalSystem element from an unused Connector. The other creates a new ElectricalSystem element from a set of electrical components. Both overloads require an ElectricalSystemType.

In the following sample, a new SupplyAir duct system is created from a selected piece of mechanical equipment (such as a fan) and all selected Air Terminals.

<table summary="" id="GUID-A3BD9AE5-8A17-4976-B47D-2A969EE6F58E__TABLE_B73A4F64958E4B84A9F29925ED840E45"><tbody><tr><td><b>Code Region: Creating a new mechanical system</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateSystem</span><span>(</span><span>UIDocument</span><span> uiDocument</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// create a connector set for new mechanical system</span><span>
    </span><span>ConnectorSet</span><span> connectorSet </span><span>=</span><span> </span><span>new</span><span> </span><span>ConnectorSet</span><span>();</span><span>
    </span><span>// Base equipment connector</span><span>
    </span><span>Connector</span><span> baseConnector </span><span>=</span><span> </span><span>null</span><span>;</span><span>

    </span><span>// Select a Parallel Fan Powered VAV and some Supply Diffusers</span><span>
    </span><span>// prior to running this example</span><span>
    </span><span>ConnectorSetIterator</span><span> csi </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> selectedIds </span><span>=</span><span> uiDocument</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>();</span><span>
    </span><span>Document</span><span> document </span><span>=</span><span> uiDocument</span><span>.</span><span>Document</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> selectedIds</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Element</span><span> e </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>e </span><span>is</span><span> </span><span>FamilyInstance</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>FamilyInstance</span><span> </span><span>fi</span><span> </span><span>=</span><span> e </span><span>as</span><span> </span><span>FamilyInstance</span><span>;</span><span>
            </span><span>Family</span><span> family </span><span>=</span><span> </span><span>fi</span><span>.</span><span>Symbol</span><span>.</span><span>Family</span><span>;</span><span>
            </span><span>// Assume the selected Mechanical Equipment is the base equipment for new system</span><span>
            </span><span>if</span><span> </span><span>(</span><span>family</span><span>.</span><span>FamilyCategory</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Mechanical Equipment"</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>//Find the "Out" and "SupplyAir" connector on the base equipment</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> </span><span>fi</span><span>.</span><span>MEPModel</span><span>)</span><span>
                </span><span>{</span><span>
                    csi </span><span>=</span><span> </span><span>fi</span><span>.</span><span>MEPModel</span><span>.</span><span>ConnectorManager</span><span>.</span><span>Connectors</span><span>.</span><span>ForwardIterator</span><span>();</span><span>
                    </span><span>while</span><span> </span><span>(</span><span>csi</span><span>.</span><span>MoveNext</span><span>())</span><span>
                    </span><span>{</span><span>
                        </span><span>Connector</span><span> conn </span><span>=</span><span> csi</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>Connector</span><span>;</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>conn</span><span>.</span><span>Direction</span><span> </span><span>==</span><span> </span><span>FlowDirectionType</span><span>.</span><span>Out</span><span> </span><span>&amp;&amp;</span><span> conn</span><span>.</span><span>DuctSystemType</span><span> </span><span>==</span><span> </span><span>DuctSystemType</span><span>.</span><span>SupplyAir</span><span>)</span><span>
                        </span><span>{</span><span>
                            baseConnector </span><span>=</span><span> conn</span><span>;</span><span>
                            </span><span>break</span><span>;</span><span>
                        </span><span>}</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span> </span><span>if</span><span> </span><span>(</span><span>family</span><span>.</span><span>FamilyCategory</span><span>.</span><span>Name</span><span> </span><span>==</span><span> </span><span>"Air Terminals"</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>// add selected Air Terminals to connector set for new mechanical system</span><span>
                csi </span><span>=</span><span> </span><span>fi</span><span>.</span><span>MEPModel</span><span>.</span><span>ConnectorManager</span><span>.</span><span>Connectors</span><span>.</span><span>ForwardIterator</span><span>();</span><span>
                csi</span><span>.</span><span>MoveNext</span><span>();</span><span>
                connectorSet</span><span>.</span><span>Insert</span><span>(</span><span>csi</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>Connector</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>MechanicalSystem</span><span> mechanicalSys </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> baseConnector </span><span>&amp;&amp;</span><span> connectorSet</span><span>.</span><span>Size</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// create a new SupplyAir mechanical system</span><span>
        mechanicalSys </span><span>=</span><span> uiDocument</span><span>.</span><span>Document</span><span>.</span><span>Create</span><span>.</span><span>NewMechanicalSystem</span><span>(</span><span>baseConnector</span><span>,</span><span> connectorSet</span><span>,</span><span> </span><span>DuctSystemType</span><span>.</span><span>SupplyAir</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Creating Systems  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  MEP Systems  Autodesk.md ===== -->

---
created: 2026-01-28T21:08:28 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Systems_html
author: 
---

# Help | MEP Systems | Autodesk

> ## Excerpt
> MEPSystem is the base class for electrical, mechanical and piping systems in Revit MEP.

---
MEPSystem is the base class for electrical, mechanical and piping systems in Revit MEP.

ElectricalSystem, MechanicalSystem and PipingSystem all derive from the MEPSystem class. The base class has some common functionality across system types, such as adding elements to the system or finding the base panel or equipment of the system. A few methods in the base class only apply to HVAC and plumbing systems, such as the DivideSystem() method which divides the physical networks in the system and creates a new system for each network.

The derived classes have additional methods and properties specific to the system type.

## MEPSection

The MEPSystem class has a SectionsCount property which returns the number of sections for the system. An MEPSection object can be obtained using either the GetSectionByIndex() method or the GetSectionByNumber() method. Although these methods are in the base MEPSystem class, the MEPSection class represents duct and pipe sections and is mainly for pressure loss calculation. It is a series of connected elements (segments - ducts or pipes, fittings, terminals and accessories) which can be obtained from the GetElementIds() method. All section members should have same flow analysis properties: Flow, Size, Velocity, Friction and Roughness.

The segment length, pressure drop and loss coefficient for each element in the section can vary, so methods are available in MEPSection to get these values given a specific element id for an element in the section. The coefficient for ducts is the loss coefficient. For pipes this is the same as the friction factor.

## Calculations

Some properties of MEP systems are calculated by Revit. Both MechanicalSystem and PipingSystem have an IsWellConnected property which indicates if the system is well connected or not. If the system is not well connected, parameters which need to be calculated are invalid.

For mechanical and piping systems, some values are calculated based on properties of the sections of the system. The MEPSystem.GetCriticalPathSectionNumbers() method returns a list of the critical path section numbers in order of the direction of flow and PressureLossOfCriticalPath() gets the total pressure loss of the sections in the critical path.

The GetFlow() and GetStaticPressure() methods available from MechanicalSystem and PipingSystem get the flow and static pressure for the system.

PipingSystem has additional calculated properties: GetFixtureUnits() and GetVolume()

Note: Due to the way these calculated properties are handled internally by Revit, they do not support dynamic model update. However, other system properties that are not calculated do support dynamic model update.


<!-- ===== END: Help  MEP Systems  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Connectors  Autodesk.md ===== -->

---
created: 2026-01-28T21:08:32 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Connectors_html
author: 
---

# Help | Connectors | Autodesk

> ## Excerpt
> Connectors are associated with a domain - ducts, piping or electrical - which is obtained from the Domain property of a Connector. Connectors are present on mechanical equipment as well as on ducts and pipes.

---
Connectors are associated with a domain - ducts, piping or electrical - which is obtained from the Domain property of a Connector. Connectors are present on mechanical equipment as well as on ducts and pipes.

To traverse a system, you can examine connectors on the base equipment of the system and determine what is attached to the connector by checking the IsConnected property and then the AllRefs property. When looking for a physical connection, it is important to check the ConnectionType of the connector. There are both physical and logical connectors in Revit, but only the physical connectors are visible in the application. The following imagine shows the two types of physical connectors - end connections and curve connectors.

## Connector Creation

Several static methods exist to create connectors. They require a reference to a planar face that will host the connector and, optionally, an edge of that planar face that defines the connector location.

These connectors are created in the family document, and their data is exposed on elements in a project via FamilyInstance.MEPModel.ConnectorManager.

-   CreateCableTrayConnector
-   CreateConduitConnector
-   CreateDuctConnector
-   CreateElectricalConnector
-   CreatePipeConnector

Connectors on MEPCurve and FabricationPart are created by default when a new MEPCurve element is created and cannot be rehosted. Their data are accessed via MEPCurve.ConnectorManager or FabricationPart.ConnectorManager.

## Connector Modification

The `ConnectorElement.ChangeHostReference` method changes the connector host reference by allowing you to specify a reference to a different plane reference, and optionally to an edge. If only a plane reference is specified, the connector position will be able to subsequently move along the plane. If an edge is also specified, then the connector location is fixed in place.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-BBDF045B-E39B-4A5A-9D87-8AFCA7E1F5F3-low.png)**Figure 167: Physical connectors**

The following sample shows how to determine the owner of a connector, and what, if anything it attaches to, along with the connection type.

<table summary="" id="GUID-A41D6151-06A8-4BCB-84B1-6B0338ACC6EA__TABLE_E9824E5167E64B28B657C8145321BEE4"><tbody><tr><td><b>Code Region 30-5: Determine what is attached to a connector</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetElementAtConnector</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Connector</span><span> connector</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>MEPSystem</span><span> mepSystem </span><span>=</span><span> connector</span><span>.</span><span>MEPSystem</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> mepSystem</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>string</span><span> message </span><span>=</span><span> </span><span>"Connector is owned by: "</span><span> </span><span>+</span><span> connector</span><span>.</span><span>Owner</span><span>.</span><span>Name</span><span>;</span><span>

        </span><span>if</span><span> </span><span>(</span><span>connector</span><span>.</span><span>IsConnected</span><span> </span><span>==</span><span> </span><span>true</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ConnectorSet</span><span> connectorSet </span><span>=</span><span> connector</span><span>.</span><span>AllRefs</span><span>;</span><span>
            </span><span>ConnectorSetIterator</span><span> csi </span><span>=</span><span> connectorSet</span><span>.</span><span>ForwardIterator</span><span>();</span><span>
            </span><span>while</span><span> </span><span>(</span><span>csi</span><span>.</span><span>MoveNext</span><span>())</span><span>
            </span><span>{</span><span>
                </span><span>Connector</span><span> connected </span><span>=</span><span> csi</span><span>.</span><span>Current</span><span> </span><span>as</span><span> </span><span>Connector</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> connected</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>// look for physical connections</span><span>
                    </span><span>if</span><span> </span><span>(</span><span>connected</span><span>.</span><span>ConnectorType</span><span> </span><span>==</span><span> </span><span>ConnectorType</span><span>.</span><span>End</span><span> </span><span>||</span><span>
                        connected</span><span>.</span><span>ConnectorType</span><span> </span><span>==</span><span> </span><span>ConnectorType</span><span>.</span><span>Curve</span><span> </span><span>||</span><span>
                        connected</span><span>.</span><span>ConnectorType</span><span> </span><span>==</span><span> </span><span>ConnectorType</span><span>.</span><span>Physical</span><span>)</span><span>
                    </span><span>{</span><span>
                        message </span><span>+=</span><span> </span><span>"\nConnector is connected to: "</span><span> </span><span>+</span><span> connected</span><span>.</span><span>Owner</span><span>.</span><span>Name</span><span>;</span><span>
                        message </span><span>+=</span><span> </span><span>"\nConnection type is: "</span><span> </span><span>+</span><span> connected</span><span>.</span><span>ConnectorType</span><span>;</span><span>
                    </span><span>}</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
            message </span><span>+=</span><span> </span><span>"\nConnector is not connected to anything."</span><span>;</span><span>
        </span><span>}</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> message</span><span>);</span><span>            
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following dialog box is the result of running this code example on the connector from a piece of plumbing equipment.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-938B934C-71EB-42CE-8B02-FE2392B5CC3F-low.png)**Figure 168: Connector Information**


<!-- ===== END: Help  Connectors  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  MEP Fabrication Detailing  Autodesk.md ===== -->

---
created: 2026-01-28T21:08:36 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_MEP_Fabrication_Detailing_html
author: 
---

# Help | MEP Fabrication Detailing | Autodesk

> ## Excerpt
> Several Revit API classes work together to provide the ability to add fabrication components to a Revit document.

---
Several Revit API classes work together to provide the ability to add fabrication components to a Revit document.

## Fabrication detailing classes

Before you can place fabrication parts in an MEP model, you must specify a fabrication configuration and load fabrication services into the model. There are a number of classes in the Revit API to facilitate this process including:

-   **FabricationConfiguration** - Contains information about the fabrication configuration settings used by the project.
-   **FabricationConfigurationInfo** - Contains information about the properties of a FabricationConfiguration.
-   **ConfigurationReloadInfo** - Contains results from reloading a FabricationConfiguration.
-   **ConnectionValidationInfo** - Contains connection-related warnings generated by reloading a FabricationConfiguration.
-   **FabricationService** - Part of the fabrication configuration and defines what FabricationServiceButtons can be used.
-   **FabricationServiceButton** - Defines what items to use for different size-based conditions.
-   **FabricationPart** - Represents a fabrication component in Revit.
-   **FabricationPartType** - Defines the type of a FabricationPart.
-   **FabricationRodInfo** - Gives support rod information for a FabricationPart.
-   **FabricationHostedInfo** - Contains hosting information for a FabricationPart and provides the ability to disconnect from the host.
-   **FabricationConnectorInfo** - Contains information about the connectors of a FabricationPart.
-   **FabricationUtils** - General utility methods in the Autodesk Revit product for fabrication.
-   **FabricationDimensionDefinition** - Contains information about a fabrication dimension.

The primary classes involved in MEP Fabrication are covered in more detail below. Sample code can be found in the Revit SDK in the FabricationPartLayout sample.

## Fabrication configuration

Using the FabricationConfiguration class, users can get and set the fabrication configuration settings for the document. They can also load and unload services, reload the fabrication configuration, get loaded services, get fabrication specifications, get material and insulation information from the configuration, and get connector information.

There is only one fabrication configuration for the document and you can get it using the static FabricationConfiguration.GetFabricationConfiguration() method. To change the configuration, call the overloaded SetConfiguration() method, passing in a FabricationConfigurationInfo object which contains the information about the FabricationConfiguration. One overload of the SetConfiguration() method will set the configuration with the global profile, and one takes a profile name and sets the configuration with that specific profile. (The FabricationConfiguration.GetProfile() method returns the name of the current profile in use and the FabricationConfigurationInfo.GetProfiles() method returns all profile names associated with the configuration.)

The ReloadConfiguration() method reloads the fabrication configuration from its source fabrication configuration. This must be done prior to loading fabrication services.

Use the GetAllLoadedServices() method to get all loaded services or GetAllUsedServices() to get only used fabrication services. A service is in use if any fabrication part in the service is created by the user. Both methods return a list of FabricationService objects.

LoadServices() and UnloadServices() can be used to load and unload a list of fabrication services, respectively.

The FabricationConfiguration class also has methods to get configuration data abbreviations. The GetMaterialAbbreviation() returns the abbreviation of the material or the insulation or the double wall material. GetSpecificationAbbreviation() returns the specification abbreviation for the given specification and GetInsulationSpecificationAbbreviation() will return the abbreviation for the given insulation specification.

## Fabrication services

Fabrication services are part of the fabrication configuration and define what fabrication service buttons can be used. The PaletteCount property returns the number of palettes in the service. Using the index of the palettes, you can call GetPaletteName() to get the name of the palette. The method GetButtonCount() will return the number of buttons in a specified palette and the actual buttons can be retrieved by calling GetButton() with a specified palette index and button index.

### Fabrication service button

The FabricationServiceButton class contains information about a fabrication button. A fabrication service button defines an item that can be used to define a FabricationPart, possibly subject to a list of size-based specific conditions. Fabrication service buttons are part of a fabrication service.

## Fabrication parts

Using the FabricationPart class, users can create, place, move and align fabrication parts in a Revit model. Users can also get or set the dimensions of the fabrication part, and get the fabrication hosted information and support rod information.

The overloaded static FabricationPart.Create() method creates a new fabrication part based on a fabrication service button. The overloaded static CreateHanger() method creates a hanger on another fabrication part. The static AlignPartByConnectors() method will move and align a fabrication part by one of its connectors to align with another connector.

FabricationParts can also be created from design elements using the DesignToFabricationConverter class. The Convert() method will convert a set of MEP design elements into fabrication parts. Successfully created FabricationParts can be obtained using the GetConvertedFabricationParts() methods. If the Convert() method indicates a partial failure, the GetPartialConvertFailureResults() method will return a list of possible failures. For partial failure types (e.g. InvalidConnections) there is a corresponding method of the DesignToFabricationConverter class to retrieve a list of the ElementIds of the FabricationParts with that error type (e.g. GetConvertedFabricationPartsWithInvalidConnections()).

Methods also exist to get and set the value of the fabrication dimension, to get the host element information and to get the fabrication rod information. `FabricationPart.GetInsulationLiningGeometry()` returns any insulation or liner geometry for a fabrication part. If there is no insulation or liner applied the return value will be null.

### Connections and position

FabricationPart has a number of methods to attach to connectors or to change the position of the FabricationPart. The static StretchAndFit() method supports the operation to stretch the fabrication part from the specified connector and fit to the target routing end. The routing end is indicated as a FabricationPartRouteEnd object, which can be obtained from the static FabricationPartRouteEnd.CreateFromConnector() or FabricationPartRouteEnd.CreateFromCenterline() methods. If the StretchAndFit() method fails, it will return a FabricationPartFitResult enumeration that provides more details on the failure.

Other methods to modify the FabricationPart include Reposition(), RotateConnectedPartByConnector() and PlaceAsTap().

### Product lists

Some FabricationPart elements, such as purchased duct and pipe fittings, have a "product list". The product list entries represent a catalog of available sizes for the selected part. The ProductListEntry property specifies the product list entry of the FabricationPart. If the IsProductList() method returns false, the ProductListEntry will be -1.

To get the list of product entries for the FabricationPart, use the GetProductListEntryCount() and GetProductListEntryName() methods. Prior to changing the ProductListEntry for the FabricationPart, call IsProductListEntryCompatibleSize() to check to see if this part can be changed to the specified product list entry without altering any connected dimensions.

### Exporting fabrication job files

FabricationPart.SaveAsFabricationJob() writes a fabrication job to disk in the MAJ file format. The exported file will contain the fabrication parts included in the input. It takes an options class, FabricationSaveJobOptions, allowing for the possibility of including holes in fabrication parts where branches meet the main straight.

### Load and unload of one-off fabrication parts from loose item files

Autodesk.Revit.DB.FabricationItemFile contains information about one-off items that can be loaded into a fabrication configuration.

Autodesk.Revit.DB.FabricationItemFolder may contain nested FabricationItemFolders and a list of FabricationItemFiles.

The members:

-   FabricationConfiguration.LoadItemFiles()
-   FabricationConfiguration.UnloadItemFiles()
-   FabricationConfiguration.GetAllLoadedItemFiles()
-   FabricationConfiguration.GetAllUsedItemFiles()
-   FabricationConfiguration.CanUnloadItemFiles()
-   FabricationConfiguration.AreItemFilesLoaded()
-   FabricationConfiguration.GetItemFolders()

allow control over the loading and unloading of item files into the configuration.

FabricationPart.Create(Document, FabricationItemFile, ElementId) creates a FabricationPart from an item file.

### Version history of parts

Autodesk.Revit.DB.FabricationVersionInfo gives the information about differerent versions of fabrication data, including the reason why the data was changed.

FabricationPart.GetVersionHistory() returns a list of FabricationVersionInfo classes that describe the history of the changes made to the part. The most recent changes are first in the list.

### Part swap out information

Autodesk.Revit.DB.ReloadSwapOutInfo gives information about a part that was swapped out during reload.

The members:

-   ConfigurationReloadInfo.OutOfDatePartCount
-   ConfigurationReloadInfo.GetOutOfDatePartStatus()

identify the parts that had newer versions found during a reload and which Revit attempted to swap out.

### Centerline length

FabricationPart.CenterlineLength returns the length of the fabrication part's centerline.


<!-- ===== END: Help  MEP Fabrication Detailing  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Family Creation  Autodesk.md ===== -->

---
created: 2026-01-28T21:08:40 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Family_Creation_html
author: 
---

# Help | Family Creation | Autodesk

> ## Excerpt
> When creating mechanical equipment in a Revit family document, you will need to add connectors to allow the equipment to connect to a system. Duct, electrical and pipe connectors can all be added similarly, using a reference plane where the connector will be placed and a system type for the connector.

---
When creating mechanical equipment in a Revit family document, you will need to add connectors to allow the equipment to connect to a system. Duct, electrical and pipe connectors can all be added similarly, using a reference plane where the connector will be placed and a system type for the connector.

The overloaded static methods provided by the ConnectorElement class are:

-   CreateCableTrayConnector
-   CreateConduitConnector
-   CreateDuctConnector
-   CreateElectricalConnector
-   CreatePipeConnector

Each of the methods above has a second overload that takes an additional Edge parameter that allows creation of connector elements centered on internal loops of a given face. The following code demonstrates how to add two pipe connectors to faces on an extrusion and set some properties on them.

<table summary="" id="GUID-81E296BE-A292-4979-B57E-730683178E6C__TABLE_D944BABE67A4400DB87E2D09E5772F32"><tbody><tr><td><b>Code Region 30-6: Adding a pipe connector</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreatePipeConnectors</span><span>(</span><span>UIDocument</span><span> uiDocument</span><span>,</span><span> </span><span>Extrusion</span><span> extrusion</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// get the faces of the extrusion</span><span>
        </span><span>Options</span><span> geoOptions </span><span>=</span><span> uiDocument</span><span>.</span><span>Document</span><span>.</span><span>Application</span><span>.</span><span>Create</span><span>.</span><span>NewGeometryOptions</span><span>();</span><span>
        geoOptions</span><span>.</span><span>View</span><span> </span><span>=</span><span> uiDocument</span><span>.</span><span>Document</span><span>.</span><span>ActiveView</span><span>;</span><span>
        geoOptions</span><span>.</span><span>ComputeReferences</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>

        </span><span>List</span><span>&lt;</span><span>PlanarFace</span><span>&gt;</span><span> planarFaces </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>PlanarFace</span><span>&gt;();</span><span>
        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>GeometryElement</span><span> geoElement </span><span>=</span><span> extrusion</span><span>.</span><span>get_Geometry</span><span>(</span><span>geoOptions</span><span>);</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>GeometryObject</span><span> geoObject </span><span>in</span><span> geoElement</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>Solid</span><span> geoSolid </span><span>=</span><span> geoObject </span><span>as</span><span> </span><span>Solid</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> geoSolid</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>foreach</span><span> </span><span>(</span><span>Face</span><span> geoFace </span><span>in</span><span> geoSolid</span><span>.</span><span>Faces</span><span>)</span><span>
                        </span><span>{</span><span>
                                </span><span>if</span><span> </span><span>(</span><span>geoFace </span><span>is</span><span> </span><span>PlanarFace</span><span>)</span><span>
                                </span><span>{</span><span>
                                        planarFaces</span><span>.</span><span>Add</span><span>(</span><span>geoFace </span><span>as</span><span> </span><span>PlanarFace</span><span>);</span><span>
                                </span><span>}</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>if</span><span> </span><span>(</span><span>planarFaces</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>1</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>// Create the Supply Hydronic pipe connector</span><span>
                </span><span>ConnectorElement</span><span> connSupply </span><span>=</span><span> </span><span>ConnectorElement</span><span>.</span><span>CreatePipeConnector</span><span>(</span><span>uiDocument</span><span>.</span><span>Document</span><span>,</span><span>
                                                                                   </span><span>PipeSystemType</span><span>.</span><span>SupplyHydronic</span><span>,</span><span>
                                                                                   planarFaces</span><span>[</span><span>0</span><span>].</span><span>Reference</span><span>);</span><span>
                </span><span>Parameter</span><span> param </span><span>=</span><span> connSupply</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>ConnectorRadius</span><span>);</span><span>
                param</span><span>.</span><span>Set</span><span>(</span><span>1.0</span><span>);</span><span> </span><span>// 1' radius</span><span>
                param </span><span>=</span><span> connSupply</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>RbsPipeFlowDirectionParam</span><span>);</span><span>
                param</span><span>.</span><span>Set</span><span>(</span><span>2</span><span>);</span><span>

                </span><span>// Create the Return Hydronic pipe connector</span><span>
                </span><span>ConnectorElement</span><span> connReturn </span><span>=</span><span>  </span><span>ConnectorElement</span><span>.</span><span>CreatePipeConnector</span><span>(</span><span>uiDocument</span><span>.</span><span>Document</span><span>,</span><span>
                                                                                    </span><span>PipeSystemType</span><span>.</span><span>ReturnHydronic</span><span>,</span><span>
                                                                                    planarFaces</span><span>[</span><span>1</span><span>].</span><span>Reference</span><span>);</span><span>
                param </span><span>=</span><span> connReturn</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>ConnectorRadius</span><span>);</span><span>
                param</span><span>.</span><span>Set</span><span>(</span><span>0.5</span><span>);</span><span> </span><span>// 6" radius</span><span>
                param </span><span>=</span><span> connReturn</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>RbsPipeFlowDirectionParam</span><span>);</span><span>
                param</span><span>.</span><span>Set</span><span>(</span><span>1</span><span>);</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The following illustrates the result of running this example using in a new family document created using a Mechanical Equipment template and passing in an extrusion 2'×2'×1'. Note that the connectors are placed at the centroid of the planar faces.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-9971E21F-AE7B-4FF3-9251-A91C6DEAA663-low.png)**Figure 169: Two connectors created on an extrusion**


<!-- ===== END: Help  Family Creation  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Mechanical Settings  Autodesk.md ===== -->

---
created: 2026-01-28T21:08:45 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Mechanical_Settings_html
author: 
---

# Help | Mechanical Settings | Autodesk

> ## Excerpt
> Many of the settings available on the Manage tab under MEP Settings - Mechanical Settings are also available through the Revit API.

---
Many of the settings available on the Manage tab under MEP Settings - Mechanical Settings are also available through the Revit API.

### Pipe Settings

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/MechPipeSettings.png)

**Pipe Settings**

The PipeSettings class provides access to the settings shown above, such as Pipe Size Suffix and Pipe Connector Tolerance. There is one PipeSettings object per document and it is accessible through the static method PipeSettings.GetPipeSettings().

#### Fitting Angles

Fitting angle usage settings for pipes are available from the following property and methods of the PipeSettings class:

-   PipeSettings.FittingAngleUsage
-   PipeSettings.GetSpecificFittingAngles()
-   PipeSettings.GetSpecificFittingAngleStatus()
-   PipeSettings.SetSpecificFittingAngleStatus()

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/MechPipeAngleSettings.png)

**Pipe Fitting Angles**

#### Segments and Sizes

The settings available in the UI under Pipe Settings - Segments and Sizes are available as well.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/MechPipeSizesSettings.png)

**Segments and Sizes**

This information is available through the Segment and MEPSize classes. A Segment represents a length of MEPCurve that contains a material and set of available sizes. The pipe sizes are represented by the MEPSize class. The Segments available can be found using a filter. The following example demonstrates how to get some of the information in the dialog above.

<table summary="" id="GUID-B9C38F9B-A11B-4369-B879-0A641A3E725F__TABLE_263A8421D9FB45E78F60EB85C3483449"><tbody><tr><td><b>Code Region: Traversing Pipe Sizes in Pipe Settings</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>PipeSizes</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> collectorPipeType </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collectorPipeType</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Segment</span><span>));</span><span>

    </span><span>IEnumerable</span><span>&lt;</span><span>Segment</span><span>&gt;</span><span> segments </span><span>=</span><span> collectorPipeType</span><span>.</span><span>ToElements</span><span>().</span><span>Cast</span><span>&lt;</span><span>Segment</span><span>&gt;();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Segment</span><span> segment </span><span>in</span><span> segments</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>StringBuilder</span><span> strPipeInfo </span><span>=</span><span> </span><span>new</span><span> </span><span>StringBuilder</span><span>();</span><span>
        strPipeInfo</span><span>.</span><span>AppendLine</span><span>(</span><span>"Segment: "</span><span> </span><span>+</span><span> segment</span><span>.</span><span>Name</span><span>);</span><span>

        strPipeInfo</span><span>.</span><span>AppendLine</span><span>(</span><span>"Roughness: "</span><span> </span><span>+</span><span> segment</span><span>.</span><span>Roughness</span><span>);</span><span>

        strPipeInfo</span><span>.</span><span>AppendLine</span><span>(</span><span>"Pipe Sizes:"</span><span>);</span><span>
        </span><span>double</span><span> dLengthFac </span><span>=</span><span> </span><span>304.8</span><span>;</span><span>  </span><span>// used to convert stored units from ft to mm for display</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>MEPSize</span><span> size </span><span>in</span><span> segment</span><span>.</span><span>GetSizes</span><span>())</span><span>
        </span><span>{</span><span>
            strPipeInfo</span><span>.</span><span>AppendLine</span><span>(</span><span>string</span><span>.</span><span>Format</span><span>(</span><span>"Nominal: {0:F3}, ID: {1:F3}, OD: {2:F3}"</span><span>,</span><span>
                                        size</span><span>.</span><span>NominalDiameter</span><span> </span><span>*</span><span> dLengthFac</span><span>,</span><span> size</span><span>.</span><span>InnerDiameter</span><span> </span><span>*</span><span> dLengthFac</span><span>,</span><span> size</span><span>.</span><span>OuterDiameter</span><span> </span><span>*</span><span> dLengthFac</span><span>));</span><span>
        </span><span>}</span><span>

        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"PipeSetting Data"</span><span>,</span><span> strPipeInfo</span><span>.</span><span>ToString</span><span>());</span><span>
        </span><span>break</span><span>;</span><span>                  
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/PipeSettingsExample.jpg)

**Output of previous example**

To add new sizes to the list, use the Segment.AddSize() method. Use Segment.RemoveSize() to remove a size by nominal diameter.

#### Slopes

The PipeSettings class also provides access to the slope values available in the UI under Pipe Settings - Slopes. Use GetPipeSlopes() to retreive a list of slope values. PipeSettings.SetPipeSlopes() provides the ability to set all the slope values at once, while PipeSettings.AddPipeSlope() adds a single pipe slope. Revit stores the slope value as a percentage (0-100).

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/MechPipeSlopeSettings.png)

**Pipe Slope Values**

### Duct Settings

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/MechDuctSettings.png)

**Duct Settings**

The DuctSettings class provides access to the settings shown above, such as Duct Fitting Annotation Size and Air Density. There is one DuctSettings object per document and it is accessible through the static method DuctSettings.GetDuctSettings().

#### Duct Fitting Angles

Fitting angle usage settings for ducts are available from the following property and methods of the DuctSettings class:

-   DuctSettings.FittingAngleUsage
-   DuctSettings.GetSpecificFittingAngles()
-   DuctSettings.GetSpecificFittingAngleStatus()
-   DuctSettings.SetSpecificFittingAngleStatus()

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/MechDuctAngleSettings.png)

**Duct Fitting Angles**

### MEP Hidden Line Settings

The `MEPHiddenLineSettings` class represents the settings of the mechanical hidden line display (e.g. ducts and pipes). It can be obtained from the static method: `MEPHiddenLineSettings.GetMEPHiddenLineSettings(Document)` It offers the following properties:

-   MEPHiddenLineSettings.DrawHiddenLine
-   MEPHiddenLineSettings.LineStyle
-   MEPHiddenLineSettings.InsideGap
-   MEPHiddenLineSettings.OutsideGap
-   MEPHiddenLineSettings.SingleLineGap


<!-- ===== END: Help  Mechanical Settings  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Electrical Analysis for Preliminary Design  Autodesk.md ===== -->

---
created: 2026-01-28T21:08:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Electrical_Analysis_for_Preliminary_Design_html
author: 
---

# Help | Electrical Analysis for Preliminary Design | Autodesk

> ## Excerpt
> Electrical engineers can estimate the building load throughout the distribution system without placing physical electrical families in the model, enabling conceptual analysis and planning.

---
Electrical engineers can estimate the building load throughout the distribution system without placing physical electrical families in the model, enabling conceptual analysis and planning.

## Overview

-   Create area-based load boundary lines based on one or more lines and a specified level using `CurveElement.CreateAreaBasedLoadBoundaryLine` or `CurveElement.CreateAreaBasedLoadBoundaryLines`
-   For a given level and phase, check if there are any empty plan circuits that do not have electrical load areas with `ElectricalLoadAreaData.HasCircuitsWithoutElectricalLoadAreas`
    -   If this returns true, create electrical load areas on all the empty plan circuits of the given level using `ElectricalLoadAreaData.CreateElectricalLoadAreas`
-   Because electrical load areas are special kind of `SpatialElement`, you can find all existing and any newly created ones using a `FilteredElementCollector`
-   Finally, create Area Based Loads by creating a Zone with `Zone.CreateAreaBasedLoad` and a `AreaBasedLoadData` then add the Electrical Load Area to the AreaBasedLoadData. Note that one Load Area can be included by more than one Area Based Loads - for example Area Based Load 1 can include Load Area X and Area Based Load 2 can also include Load Area X.

```
public void CreateAreaBasedElectricalLoads(Document doc, List<Curve> lines, Level level, Phase phase)
{
    IEnumerable<SpatialElement> electricalLoadAreas;
    using (Transaction transaction = new Transaction(doc, "Create Electrical Load Areas"))
    {
        transaction.Start();
        //Create Area Based Load Boundary Lines.
        CurveElement.CreateAreaBasedLoadBoundaryLines(doc, lines, level.Id);

        if (ElectricalLoadAreaData.HasCircuitsWithoutElectricalLoadAreas(doc, level.Id, phase.Id))
        {
            //Create Electrical Load Areas.
            ISet<ElementId> createdElectricalLoadAreaIds = ElectricalLoadAreaData.CreateElectricalLoadAreas(doc, level.Id, phase.Id);
        }

        electricalLoadAreas = new FilteredElementCollector(doc)
                .OfClass(typeof(SpatialElement))
                .WherePasses(new ElementLevelFilter(level.Id))
                .WherePasses(new ElementPhaseStatusFilter(phase.Id, ElementOnPhaseStatus.None))
                .Cast<SpatialElement>()
                .Where(x => x.SpatialElementType == SpatialElementType.ElectricalLoadArea);

        transaction.Commit();
    }

    using (Transaction transaction = new Transaction(doc, "Create Area Based Loads"))
    {
        transaction.Start();

        //Create Area Based Load on each Load Area.
        foreach (SpatialElement electricalLoadArea in electricalLoadAreas)
        {
            Zone areaBasedLoad = Zone.CreateAreaBasedLoad(doc, "AreaBasedLoad1", level.Id, phase.Id);
            AreaBasedLoadData areaBasedLoadData = areaBasedLoad.GetDomainData() as AreaBasedLoadData;
            areaBasedLoadData.AddElectricalLoadArea(electricalLoadArea.Id);
            areaBasedLoadData.Voltage = UnitUtils.ConvertToInternalUnits(100, UnitTypeId.Volts);
        }
        transaction.Commit();
    }
}
```

## Defining Electrical Analytical Loads

When defining loads, you can define area-based loads and equipment loads.

Area-based loads let you define a closed region and indicate power requirements based on power/area density. For example, lighting in 2nd floor office spaces is 2w/ft2, while lighting in conference rooms is 3w/ft2, and general power across the entire floor is 3.5 w/ft2.

An Area Based Load is composed by one or more Electrical Load Areas. One Electrical Load Area can be included by more than one Area Based Loads. Geometrically, an Electrical Load Area is a minimized enclosed region surrounded by area-based load boundary lines. In the Revit API, Electrical Load Area elements are represented as SpatialElement objects with their property SpatialElementType = ElectricalLoadArea. The SpatialElement.GetSpatialElementDomainData() method gets the SpatialElementDomainData for a given spatial element, and then down-casts it as ElectricalLoadAreaData to GetAreaBasedLoadIds() of it.

The Electrical Load Area elements can be created by `CreateElectricalLoadAreas()`. This function creates electrical load areas on all the empty plan circuits of the given level.

Equipment loads allow you to capture load requirements associated with major equipment components, such as elevators, chillers, or any other component beyond the general power density-based loads.

Equipment load elements can be created by ElectricalAnalyticalNode.Create() with the parameter ElectricalAnalyticalNodeType as EquipmentLoad. The `AnalyticalEquipmentLoadData` class provides access to this data.

When defining the distribution system, you can create Electrical Analytical Equipment (busses, transformers, transfer switches, and power sources), and interconnect these components. You can then associate area and equipment loads with the distribution system components to sum load throughout the distribution system.

## Electrical Analytical Nodes

The ElectricalAnalyticalNode class represents an electrical analytical node under the Analytical Power Distribution in the System Browser. The type of this node can be any of the value of the ElectricalAnalyticalNodeType enum:

-   Power Source
-   Bus
-   Transformer
-   Transfer Switch
-   Equipment Load

The static method ElectricalAnalyticalNode.Create is used to create these nodes.


<!-- ===== END: Help  Electrical Analysis for Preliminary Design  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Electrical Settings  Autodesk.md ===== -->

---
created: 2026-01-28T21:08:54 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Electrical_Settings_html
author: 
---

# Help | Electrical Settings | Autodesk

> ## Excerpt
> Some of the settings available on the Manage tab under MEP Settings - Electrical Settings are also available through the Revit API.

---
Some of the settings available on the Manage tab under MEP Settings - Electrical Settings are also available through the Revit API.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ElectricalSettings.png)

## Electrical Settings

The ElectricalSetting class provides access to different electrical settings, such as fitting angles, wire types, and voltage types. There is one ElectricalSetting object per document and it is accessible through the static method ElectricalSetting.GetElectricalSettings().

### General Settings

The following general settings are available as properties of the ElectricalSetting class:

-   CircuitSequence - Accesses the circuit sequence numbering schema
-   CircuitNamePhaseA - Accesses the circuit naming by phase (Phase A Label).
-   CircuitNamePhaseB - Accesses the circuit naming by phase (Phase B Label).
-   CircuitNamePhaseC - Accesses the circuit naming by phase (Phase C Label).
    
    ### Fitting Angles
    

Fitting angle settings for cable trays and conduits are available from the following methods of the ElectricalSetting class:

-   GetSpecificFittingAngles()
-   GetSpecificFittingAngleStatus()
-   SetSpecificFittingAngleStatus()

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/ElectricalAnglesSettings.png)

**Fitting Angles**

### Other Electrical Settings

Properties of the ElectricalSetting class provide access to:

-   Distribution System Types
-   Voltage Types
-   Wire Conduit Types
-   Wire Material Types
-   Wire Types

Methods also are available to add or remove from the project distribution system types, voltate types, wire material types and wire types.

## Circuit Naming

`Autodesk.Revit.DB.Electrical.CircuitNamingScheme` represents a scheme used for electrical circuit naming. Significant methods on this class allow schemes to be created and allowing access to the list of combined parameters associated with the scheme:

-   CircuitNamingScheme.Create()
-   CircuitNamingScheme.GetCombinedParameters()
-   CircuitNamingScheme.SetCombinedParameters()

`Autodesk.Revit.DB.Electrical.CircuitNamingSchemeSettings` represents the circuit naming scheme settings object in a project document. Members on this class include:

-   CircuitNamingSchemeSettings.GetCircuitNamingSchemeSettings()
-   CircuitNamingSchemeSettings.CircuitNamingSchemeId


<!-- ===== END: Help  Electrical Settings  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Routing Preferences  Autodesk.md ===== -->

---
created: 2026-01-28T21:09:00 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Routing_Preferences_html
author: 
---

# Help | Routing Preferences | Autodesk

> ## Excerpt
> Routing prefences are accessible through the RoutingPreferenceManager class. An instance of this class is available from a property of the MEPCurveType class. Currently, only PipeType and DuctType support routing preferences.

---
Routing prefences are accessible through the RoutingPreferenceManager class. An instance of this class is available from a property of the MEPCurveType class. Currently, only PipeType and DuctType support routing preferences.

The RoutingPreferenceManager manages all rules for selecting segment types and sizes as well as fitting types based on user selection criteria. The RoutingPreferenceRule class manages one segment or fitting preference and instances of this class can be added to the RoutingPreferenceManager. Each routing preference rule is grouped according to what type of routing item in manages. The type is represented by the RoutingPreferenceRuleGroupType and includes these options:

<table summary="" id="GUID-A3B0E633-3EE8-455C-A97D-E5FB4BD4219F__TABLE_8CCB5A531EBD4B9EBB54FF5E33FB6D59"><tbody><tr><td><b>Member name</b></td><td><b>Description</b></td></tr><tr><td>Undefined</td><td>Undefined group type (default initial value)</td></tr><tr><td>Segments</td><td>Segment types (e.g. pipe stocks)</td></tr><tr><td>Elbows</td><td>Elbow types</td></tr><tr><td>Junctions</td><td>Junction types (e.g. takeoff, tee, wye, tap)</td></tr><tr><td>Crosses</td><td>Cross types</td></tr><tr><td>Transitions</td><td>Transition types (Note that the multi-shape transitions may have their own groups)</td></tr><tr><td>Unions</td><td>Union types that connect two segments together</td></tr><tr><td>MechanicalJoints</td><td>Mechanical joint types that connect fitting to fitting, segment to fitting, or segment to segment</td></tr><tr><td>TransitionsRectangularToRound</td><td>Multi-shape transition from the rectangular profile to the round profile</td></tr><tr><td>TransitionsRectangularToOval</td><td>Multi-shape transition from the rectangular profile to the oval profile</td></tr><tr><td>TransitionsOvalToRound</td><td>Multi-shape transition from the oval profile to the round profile</td></tr></tbody></table>

Each routing preference rule can have one or more selection criteria, represented by the RoutingCriterionBase class, and the derived type PrimarySizeCriterion. PrimarySizeCriterion selects fittings and segments based on minimum and maximum size constraints.

The RoutingConditions class holds a collection of RoutingCondition instances. The RoutingCondition class represents routing information that is used as input when determining if a routing criterion, such as minimum or maximum diameter, is met. The RoutingPreferencesManager.GetMEPPartId() method gets a fitting or segment id based on a RoutingPreferenceRuleGroupType and RoutingConditions.

The following example gets all the pipe types in the document, gets the routing preference manager for each one, then gets the sizes for each segment based on the rules in the routing preference manager.

<table summary="" id="GUID-A3B0E633-3EE8-455C-A97D-E5FB4BD4219F__TABLE_D7312BF9EF464B64995AE941B2BC71EC"><tbody><tr><td><b>Code Region: Using Routing Preferences</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>List</span><span>&lt;double&gt;</span><span> </span><span>GetAvailablePipeSegmentSizesFromDocument</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>System</span><span>.</span><span>Collections</span><span>.</span><span>Generic</span><span>.</span><span>HashSet</span><span>&lt;double&gt;</span><span> sizes </span><span>=</span><span> </span><span>new</span><span> </span><span>HashSet</span><span>&lt;double&gt;</span><span>();</span><span>

    </span><span>FilteredElementCollector</span><span> collectorPipeType </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collectorPipeType</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>PipeType</span><span>));</span><span>

    </span><span>IEnumerable</span><span>&lt;</span><span>PipeType</span><span>&gt;</span><span> pipeTypes </span><span>=</span><span> collectorPipeType</span><span>.</span><span>ToElements</span><span>().</span><span>Cast</span><span>&lt;</span><span>PipeType</span><span>&gt;();</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>PipeType</span><span> pipeType </span><span>in</span><span> pipeTypes</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>RoutingPreferenceManager</span><span> rpm </span><span>=</span><span> pipeType</span><span>.</span><span>RoutingPreferenceManager</span><span>;</span><span>

        </span><span>int</span><span> segmentCount </span><span>=</span><span> rpm</span><span>.</span><span>GetNumberOfRules</span><span>(</span><span>RoutingPreferenceRuleGroupType</span><span>.</span><span>Segments</span><span>);</span><span>
        </span><span>for</span><span> </span><span>(</span><span>int</span><span> index </span><span>=</span><span> </span><span>0</span><span>;</span><span> index </span><span>!=</span><span> segmentCount</span><span>;</span><span> </span><span>++</span><span>index</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>RoutingPreferenceRule</span><span> segmentRule </span><span>=</span><span> rpm</span><span>.</span><span>GetRule</span><span>(</span><span>RoutingPreferenceRuleGroupType</span><span>.</span><span>Segments</span><span>,</span><span> index</span><span>);</span><span>
            </span><span>Segment</span><span> segment </span><span>=</span><span> document</span><span>.</span><span>GetElement</span><span>(</span><span>segmentRule</span><span>.</span><span>MEPPartId</span><span>)</span><span> </span><span>as</span><span> </span><span>Segment</span><span>;</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>MEPSize</span><span> size </span><span>in</span><span> segment</span><span>.</span><span>GetSizes</span><span>())</span><span>
            </span><span>{</span><span>
                sizes</span><span>.</span><span>Add</span><span>(</span><span>size</span><span>.</span><span>NominalDiameter</span><span>);</span><span>  </span><span>//Use a hash-set to remove duplicate sizes among Segments and PipeTypes.</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>List</span><span>&lt;double&gt;</span><span> sizesSorted </span><span>=</span><span> sizes</span><span>.</span><span>ToList</span><span>();</span><span>
    sizesSorted</span><span>.</span><span>Sort</span><span>();</span><span>
    </span><span>return</span><span> sizesSorted</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Routing Preferences  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Structural Engineering  Autodesk.md ===== -->

---
created: 2026-01-28T21:09:04 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html
author: 
---

# Help | Structural Engineering | Autodesk

> ## Excerpt
> The following sections describe API features that only pertain to the structural engineering features of Revit:

---
The following sections describe API features that only pertain to the structural engineering features of Revit:

-   Structural Model Elements - Discusses specific Elements and their properties that only relate to the structural engineering features of Revit.
-   AnalyticalModel - Discusses analytical model-related classes such as AnalyticalModel, RigidLink, and AnalyticalModelSupport.
-   AnalyticalLink - Discusses creating new analytical links between analytical beams and columns.
-   Loads - Discusses Load Settings and three kinds of Loads.
-   Your Analysis Link - Provides suggestions for API users who want to link Revit to certain Structural Analysis applications.

This chapter contains some advanced topics. If you are not familiar with the Revit Platform API, read the basic sections first, such as [Getting Started](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_html), [Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html), [Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_html), and so on.


<!-- ===== END: Help  Structural Engineering  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Structural Model Elements  Autodesk.md ===== -->

---
created: 2026-01-28T21:09:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_html
author: 
---

# Help | Structural Model Elements | Autodesk

> ## Excerpt
> Structural Model Elements are, literally, elements that support a structure such as columns, rebar, trusses, and so on. The following section describe how to manipulate these elements.

---
Structural Model Elements are, literally, elements that support a structure such as columns, rebar, trusses, and so on. The following section describe how to manipulate these elements.

The model elements included in this section are specific to the structural engineering features of Revit. For more information about other structural element classes, see the corresponding parts in [Walls, Floors, Ceilings, Roofs and Openings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_html) and [Family](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_Family_html) Instances.

**Pages in this section**

-   [Structural Columns, Beams and Braces](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Structural_Columns_Beams_and_Braces_html)
-   [Trusses](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Trusses_html)
-   [Reinforcement](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_html)
-   [Boundary Conditions](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Boundary_Conditions_html)
-   [Slabs](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Slabs_html)

**Parent page:** [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html)


<!-- ===== END: Help  Structural Model Elements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Structural Columns, Beams and Braces  Autodesk.md ===== -->

---
created: 2026-01-28T21:09:14 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Structural_Columns_Beams_and_Braces_html
author: 
---

# Help | Structural Columns, Beams and Braces | Autodesk

> ## Excerpt
> Structural column, beam, and brace elements are all represented by the FamilyInstance class. They are distinguished by the StructuralType property.

---
Structural column, beam, and brace elements are all represented by the FamilyInstance class. They are distinguished by the StructuralType property.

<table summary="" id="GUID-396E80E1-6E5D-4D10-9DE8-06A6AFCCEA36__TABLE_1B1A460E99DF46CB919556B2D14BC4F1"><tbody><tr><td><b>Code Region 29-1: Distinguishing between column, beam and brace</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetStructuralType</span><span>(</span><span>FamilyInstance</span><span> familyInstance</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>string</span><span> message </span><span>=</span><span> </span><span>""</span><span>;</span><span>
    </span><span>switch</span><span> </span><span>(</span><span>familyInstance</span><span>.</span><span>StructuralType</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>case</span><span> </span><span>StructuralType</span><span>.</span><span>Beam</span><span>:</span><span>
            message </span><span>=</span><span> </span><span>"FamilyInstance is a beam."</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>case</span><span> </span><span>StructuralType</span><span>.</span><span>Brace</span><span>:</span><span>
            message </span><span>=</span><span> </span><span>"FamilyInstance is a brace."</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>case</span><span> </span><span>StructuralType</span><span>.</span><span>Column</span><span>:</span><span>
            message </span><span>=</span><span> </span><span>"FamilyInstance is a column."</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>case</span><span> </span><span>StructuralType</span><span>.</span><span>Footing</span><span>:</span><span>
            message </span><span>=</span><span> </span><span>"FamilyInstance is a footing."</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>default</span><span>:</span><span>
            message </span><span>=</span><span> </span><span>"FamilyInstance is non-structural or unknown framing."</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>message</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

You can filter out FamilySymbol objects corresponding to structural columns, beams, and braces by using categories. The category for structural beams and braces is BuiltInCategory.OST\_StructuralFraming. The category for structural columns is BuiltInCategory.OST\_StructuralColumns.

<table summary="" id="GUID-396E80E1-6E5D-4D10-9DE8-06A6AFCCEA36__TABLE_FD81547DF68B4F1D9A2410E37BCB8AF1"><tbody><tr><td><b>Code Region 29-2: Using BuiltInCategory.OST_StructuralFraming</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetBeamAndColumnSymbols</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>List</span><span>&lt;</span><span>FamilySymbol</span><span>&gt;</span><span> columnTypes </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>FamilySymbol</span><span>&gt;();</span><span>
    </span><span>List</span><span>&lt;</span><span>FamilySymbol</span><span>&gt;</span><span> framingTypes </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>FamilySymbol</span><span>&gt;();</span><span>
    </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> elements </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Family</span><span>)).</span><span>ToElements</span><span>();</span><span>

    </span><span>foreach</span><span>(</span><span>Element</span><span> element </span><span>in</span><span> elements</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Family</span><span> family </span><span>=</span><span> element </span><span>as</span><span> </span><span>Family</span><span>;</span><span>
        </span><span>Category</span><span> category </span><span>=</span><span> family</span><span>.</span><span>FamilyCategory</span><span>;</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> category</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ISet</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> familySymbolIds </span><span>=</span><span> family</span><span>.</span><span>GetFamilySymbolIds</span><span>();</span><span>
            </span><span>if</span><span> </span><span>((</span><span>int</span><span>)</span><span>BuiltInCategory</span><span>.</span><span>OST_StructuralColumns </span><span>==</span><span> category</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> familySymbolIds</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>FamilySymbol</span><span> symbol </span><span>=</span><span> family</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>)</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
                    columnTypes</span><span>.</span><span>Add</span><span>(</span><span>symbol</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span> </span><span>if</span><span> </span><span>((</span><span>int</span><span>)</span><span>BuiltInCategory</span><span>.</span><span>OST_StructuralFraming </span><span>==</span><span> category</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> familySymbolIds</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>FamilySymbol</span><span> symbol </span><span>=</span><span> family</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>)</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
                    framingTypes</span><span>.</span><span>Add</span><span>(</span><span>symbol</span><span>);</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>string</span><span> message </span><span>=</span><span> </span><span>"Column Types: "</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>FamilySymbol</span><span> familySymbol </span><span>in</span><span> columnTypes</span><span>)</span><span>
    </span><span>{</span><span>
        message </span><span>+=</span><span> </span><span>"\n"</span><span> </span><span>+</span><span> familySymbol</span><span>.</span><span>Name</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>message</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

You can get and set beam setback properties with the FamilyInstance.ExtensionUtility property. If this property returns null, the beam setback can't be modified.

## BeamSystem

BeamSystem provides full access and edit ability to beam systems. You can get and set all of its properties, such as BeamSystemType, BeamType, Direction, and Level. BeamSystem.Direction is not limited to one line of edges. It can be set to any XYZ coordinate on the same plane with the BeamSystem.

Note: You cannot change the StructuralBeam AnalyticalModel after the Elevation property is changed in the UI or by the API. In the following picture the analytical model lines stay in the original location after BeamSystem Elevation is changed to 10 feet.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-95C4AA28-3733-4A65-A75B-0DA398063722-low.png)**Figure 156: Change BeamSystem elevation**


<!-- ===== END: Help  Structural Columns, Beams and Braces  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Trusses  Autodesk.md ===== -->

---
created: 2026-01-28T21:09:18 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Trusses_html
author: 
---

# Help | Trusses | Autodesk

> ## Excerpt
> The Truss class represents all types of trusses in Revit. The TrussType property indicates the type of truss.

---
## Truss

The Truss class represents all types of trusses in Revit. The TrussType property indicates the type of truss.

<table summary="" id="GUID-B255F988-71FD-4687-B105-28DF77869B85__TABLE_7E6CBE88EA35497E997B0C47FFC40112"><tbody><tr><td><b>Code Region 29-7: Creating a truss over two columns</b></td></tr><tr><td><pre><code><span>Truss</span><span> </span><span>CreateTruss</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> column1</span><span>,</span><span> </span><span>FamilyInstance</span><span> column2</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Truss</span><span> truss </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>using</span><span> </span><span>(</span><span>Transaction</span><span> transaction </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>document</span><span>,</span><span> </span><span>"Add Truss"</span><span>))</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>transaction</span><span>.</span><span>Start</span><span>()</span><span> </span><span>==</span><span> </span><span>TransactionStatus</span><span>.</span><span>Started</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>//sketchPlane</span><span>
            XYZ origin </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            XYZ xDirection </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            XYZ yDirection </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>1</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            XYZ zDirection </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>0</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>1</span><span>);</span><span>
            </span><span>Plane</span><span> plane </span><span>=</span><span> </span><span>Plane</span><span>.</span><span>Create</span><span>(</span><span>new</span><span> </span><span>Frame</span><span>(</span><span>origin</span><span>,</span><span> xDirection</span><span>,</span><span> yDirection</span><span>,</span><span> zDirection</span><span>));</span><span>
            </span><span>SketchPlane</span><span> sketchPlane </span><span>=</span><span> </span><span>SketchPlane</span><span>.</span><span>Create</span><span> </span><span>(</span><span>document</span><span>,</span><span> plane</span><span>);</span><span>

            </span><span>//new base Line - use line that spans two selected columns</span><span>
            </span><span>AnalyticalMember</span><span> frame1 </span><span>=</span><span> </span><span>(</span><span>AnalyticalMember</span><span>)</span><span>document</span><span>.</span><span>GetElement</span><span>(</span><span>AnalyticalToPhysicalAssociationManager</span><span>.</span><span>GetAnalyticalToPhysicalAssociationManager</span><span>(</span><span>document</span><span>).</span><span>GetAssociatedElementId</span><span>(</span><span>column1</span><span>.</span><span>Id</span><span>));</span><span>
            XYZ centerPoint1 </span><span>=</span><span> </span><span>(</span><span>frame1</span><span>.</span><span>GetCurve</span><span>()</span><span> </span><span>as</span><span> </span><span>Line</span><span>).</span><span>GetEndPoint</span><span>(</span><span>0</span><span>);</span><span>

            </span><span>AnalyticalMember</span><span> frame2 </span><span>=</span><span> </span><span>(</span><span>AnalyticalMember</span><span>)</span><span>document</span><span>.</span><span>GetElement</span><span>(</span><span>AnalyticalToPhysicalAssociationManager</span><span>.</span><span>GetAnalyticalToPhysicalAssociationManager</span><span>(</span><span>document</span><span>).</span><span>GetAssociatedElementId</span><span>(</span><span>column2</span><span>.</span><span>Id</span><span>));</span><span>
            XYZ centerPoint2 </span><span>=</span><span> </span><span>(</span><span>frame2</span><span>.</span><span>GetCurve</span><span>()</span><span> </span><span>as</span><span> </span><span>Line</span><span>).</span><span>GetEndPoint</span><span>(</span><span>0</span><span>);</span><span>

            XYZ startPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>centerPoint1</span><span>.</span><span>X</span><span>,</span><span> centerPoint1</span><span>.</span><span>Y</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            XYZ endPoint </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>centerPoint2</span><span>.</span><span>X</span><span>,</span><span> centerPoint2</span><span>.</span><span>Y</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Line</span><span> baseLine </span><span>=</span><span> </span><span>null</span><span>;</span><span>

            </span><span>try</span><span>
            </span><span>{</span><span>
                baseLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>startPoint</span><span>,</span><span> endPoint</span><span>);</span><span>
            </span><span>}</span><span>
            </span><span>catch</span><span> </span><span>(</span><span>System</span><span>.</span><span>ArgumentException</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Selected columns are too close to create truss."</span><span>);</span><span>
            </span><span>}</span><span>

            </span><span>// use the active view for where the truss's tag will be placed; View used in</span><span>
            </span><span>// NewTruss should be plan or elevation view parallel to the truss's base line </span><span>
            </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>View</span><span> view </span><span>=</span><span> document</span><span>.</span><span>ActiveView</span><span>;</span><span>

            </span><span>// Get a truss type for the truss</span><span>
            </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
            collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FamilySymbol</span><span>));</span><span>
            collector</span><span>.</span><span>OfCategory</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Truss</span><span>);</span><span>

            </span><span>TrussType</span><span> trussType </span><span>=</span><span> collector</span><span>.</span><span>FirstElement</span><span>()</span><span> </span><span>as</span><span> </span><span>TrussType</span><span>;</span><span>

            </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> trussType</span><span>)</span><span>
            </span><span>{</span><span>
                truss </span><span>=</span><span> </span><span>Truss</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> trussType</span><span>.</span><span>Id</span><span>,</span><span> sketchPlane</span><span>.</span><span>Id</span><span>,</span><span> baseLine</span><span>);</span><span>
                transaction</span><span>.</span><span>Commit</span><span>();</span><span>
            </span><span>}</span><span>
            </span><span>else</span><span>
            </span><span>{</span><span>
                transaction</span><span>.</span><span>RollBack</span><span>();</span><span>
                </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"No truss types found in document."</span><span>);</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> truss</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Trusses  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Reinforcement  Autodesk.md ===== -->

---
created: 2026-01-28T21:09:23 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_html
author: 
---

# Help | Reinforcement | Autodesk

> ## Excerpt
> The Revit API provides classes to manage reinforcement, such as rebar or fabric sheets, in valid hosts such as concrete columns, beams, walls, foundations, and structural floors.

---
The Revit API provides classes to manage reinforcement, such as rebar or fabric sheets, in valid hosts such as concrete columns, beams, walls, foundations, and structural floors.

**Pages in this section**

-   [Rebar](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Rebar_html)
-   [Rebar Couplers](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Rebar_Couplers_html)
-   [Area and Path Reinforcement](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Area_and_Path_Reinforcement_html)
-   [Fabric Reinforcement](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Fabric_Reinforcement_html)
-   [Rebar Containers](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Rebar_Containers_html)
-   [Reinforcement Settings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Reinforcement_Settings_html)
-   [Reinforcement Rounding](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Reinforcement_Rounding_html)
-   [Annotation](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Annotation_html)

**Parent page:** [Structural Model Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_html)


<!-- ===== END: Help  Reinforcement  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Rebar  Autodesk.md ===== -->

---
created: 2026-01-28T21:09:28 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Rebar_html
author: 
---

# Help | Rebar | Autodesk

> ## Excerpt
> The Rebar class represents rebar used to reinforce suitable elements, such as concrete beams, columns, slabs or foundations.

---
The Rebar class represents rebar used to reinforce suitable elements, such as concrete beams, columns, slabs or foundations.

## Shape Driven and Free Form Rebar

There are two kind of rebar – Shape Driven and Free Form. The Shape Driven Rebar is a Rebar the is driven by a shape. The Free Form rebar is driven by curves. Free Form Rebar can be constructed in two ways: from curves (and it will not have constraint) and the second option with a server that will allow the rebar to have constraints. The server will also allow the API user the possibility to implement how the rebar curves are calculated based on the constraints. This allows API developers to create their own kind of Rebar.

### Distribution Path

RebarHandlePositionData.GetDistributionPath() gets the distribution path currently stored in the rebar.

For a free form rebar set the distance between two consecutive bars may be different if it is calculated between different points on bars. The distribution path is an array of curves with the property that based on these curves the set was calculated to respect the layout rule and number of bars or spacing.

## Creating rebar

Free Form rebar can be created with the Rebar.CreateFreeForm method. Shape Driven rebar objects can be created using these static Rebar methods. The method `RebarHostData.IsReferenceContainedByAValidHost()` identifies if an element that contains the given reference can host reinforcement.

<table summary="" id="GUID-91C5087B-2E92-4276-878B-68FA8491D238__TABLE_ADE284ED5FB34C0BB90041821A89E1AA"><tbody><tr><td><b>Name</b></td><td><b>Description</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>Rebar</span><span> </span><span>Rebar</span><span>.</span><span>CreateFromCurves</span><span>(</span><span>
        </span><span>Document</span><span> doc</span><span>,</span><span>
        </span><span>RebarStyle</span><span> style</span><span>,</span><span>
        </span><span>RebarBarType</span><span> rebarType</span><span>,</span><span>
        </span><span>RebarHookType</span><span> startHook</span><span>,</span><span>
        </span><span>RebarHookType</span><span> endHook</span><span>,</span><span>
        </span><span>Element</span><span> host</span><span>,</span><span>
        XYZ norm</span><span>,</span><span>
        </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> curves</span><span>,</span><span>
        </span><span>RebarHookOrientation</span><span> startHookOrient</span><span>,</span><span>
        </span><span>RebarHookOrientation</span><span> endHookOrient</span><span>,</span><span>
        </span><span>bool</span><span> useExistingShapeIfPossible</span><span>,</span><span>
        </span><span>bool</span><span> createNewShape
</span><span>);</span></code></pre></td><td>Creates a new instance of a Rebar element within the project. All curves must belong to the plane defined by the normal and origin.</td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>Rebar</span><span> </span><span>Rebar</span><span>.</span><span>CreateFromRebarShape</span><span>(</span><span>
        </span><span>Document</span><span> doc</span><span>,</span><span>
        </span><span>RebarShape</span><span> rebarShape</span><span>,</span><span>
        </span><span>RebarBarType</span><span> rebarType</span><span>,</span><span>
        </span><span>Element</span><span> host</span><span>,</span><span>
        XYZ origin</span><span>,</span><span>
        XYZ xVec</span><span>,</span><span>
        XYZ yVec
</span><span>);</span></code></pre></td><td>Creates a new Rebar, as an instance of a RebarShape. The instance will have the default shape parameters from the RebarShape, and its location is based on the bounding box of the shape in the shape definition. Hooks are removed from the shape before computing its bounding box. If appropriate hooks can be found in the document, they will be assigned arbitrarily.</td></tr><tr><td><pre><code><span>public</span><span> </span><span>static</span><span> </span><span>Rebar</span><span> </span><span>Rebar</span><span>.</span><span>CreateFromCurvesAndShape</span><span>(</span><span>
        </span><span>Document</span><span> doc</span><span>,</span><span>
        </span><span>RebarShape</span><span> rebarShape</span><span>,</span><span>
        </span><span>RebarBarType</span><span> rebarType</span><span>,</span><span>
        </span><span>RebarHookType</span><span> startHook</span><span>,</span><span>
        </span><span>RebarHookType</span><span> endHook</span><span>,</span><span>  
        </span><span>Element</span><span> host</span><span>,</span><span>
        XYZ norm</span><span>,</span><span>
        </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> curves</span><span>,</span><span>
        </span><span>RebarHookOrientation</span><span> startHookOrient</span><span>,</span><span>
        </span><span>RebarHookOrientation</span><span> endHookOrient
</span><span>);</span></code></pre></td><td>Creates a new instance of a Rebar element within the project. The instance will have the default shape parameters from the RebarShape. All curves must belong to the plane defined by the normal and origin.</td></tr></tbody></table>

The first version creates rebar from an array of curves describing the rebar, while the second creates a Rebar object based on a RebarShape and position. The third version creates rebar from an array of curves and based on a RebarShape.

When using the CreateFromCurves() or CreateFromCurvesAndShape() method, the parameters RebarBarType and RebarHookType are available in the RebarBarTypes and RebarHookTypes properties of the Document.

The following code illustrates how to create Rebar with a specific layout.

<table summary="" id="GUID-91C5087B-2E92-4276-878B-68FA8491D238__TABLE_EC06CBA3959B462CA66E36650440B29F"><tbody><tr><td><b>Creating rebar with a specific layout</b></td></tr><tr><td><pre><code><span>Rebar</span><span> </span><span>CreateRebar</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> column</span><span>,</span><span> </span><span>RebarBarType</span><span> barType</span><span>,</span><span> </span><span>RebarHookType</span><span> hookType</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Define the rebar geometry information - Line rebar</span><span>
    </span><span>LocationPoint</span><span> location </span><span>=</span><span> column</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationPoint</span><span>;</span><span>
    XYZ origin </span><span>=</span><span> location</span><span>.</span><span>Point</span><span>;</span><span>
    XYZ normal </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>// create rebar 9' long</span><span>
    XYZ rebarLineEnd </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>origin</span><span>.</span><span>X</span><span>,</span><span> origin</span><span>.</span><span>Y</span><span>,</span><span> origin</span><span>.</span><span>Z </span><span>+</span><span> </span><span>9</span><span>);</span><span>
    </span><span>Line</span><span> rebarLine </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>origin</span><span>,</span><span> rebarLineEnd</span><span>);</span><span>

    </span><span>// Create the line rebar</span><span>
    </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> curves </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;();</span><span>
    curves</span><span>.</span><span>Add</span><span>(</span><span>rebarLine</span><span>);</span><span>

    </span><span>Rebar</span><span> rebar </span><span>=</span><span> </span><span>Rebar</span><span>.</span><span>CreateFromCurves</span><span>(</span><span>document</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Structure</span><span>.</span><span>RebarStyle</span><span>.</span><span>Standard</span><span>,</span><span> barType</span><span>,</span><span> hookType</span><span>,</span><span> hookType</span><span>,</span><span> column</span><span>,</span><span> origin</span><span>,</span><span> curves</span><span>,</span><span> </span><span>RebarHookOrientation</span><span>.</span><span>Right</span><span>,</span><span> </span><span>RebarHookOrientation</span><span>.</span><span>Left</span><span>,</span><span> </span><span>true</span><span>,</span><span> </span><span>true</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> rebar</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// set specific layout for new rebar as fixed number, with 10 bars, distribution path length of 1.5'</span><span>
        </span><span>// with bars of the bar set on the same side of the rebar plane as indicated by normal</span><span>
        </span><span>// and both first and last bar in the set are shown</span><span>
        rebar</span><span>.</span><span>GetShapeDrivenAccessor</span><span>().</span><span>SetLayoutAsFixedNumber</span><span>(</span><span>10</span><span>,</span><span> </span><span>1.5</span><span>,</span><span> </span><span>true</span><span>,</span><span> </span><span>true</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> rebar</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: For more examples of creating rebar elements, see the Reinforcement and NewRebar sample applications included with the Revit SDK.

The following table lists the integer value for the Parameter REBAR\_ELEM\_LAYOUT\_RULE:

**Rebar Layout Rule**

<table summary="" id="GUID-91C5087B-2E92-4276-878B-68FA8491D238__TABLE_5AA90202B3B6445091B4CE95DBA649D9"><tbody><tr><td><b>Value</b></td><td><b>0</b></td><td><b>1</b></td><td><b>2</b></td><td><b>3</b></td><td><b>4</b></td></tr><tr><td>Description</td><td>Single</td><td>Fixed Number</td><td>Maximum Spacing</td><td>Number with Spacing</td><td>Minimum Clear Spacing</td></tr></tbody></table>

Rebar.GetShapeDrivenAccessor().ScaleToBox() takes the shape and scales it to fit the box defined by an origin and two vectors that define the edges of a rectangle.

Clear cover is associated with individual faces of valid rebar hosts. You can access the cover settings of a host through the Autodesk.Revit.Elements.RebarHostData object. A simpler, less powerful mechanism for accessing the same settings is provided through parameters.

Cover is defined by a named offset distance, modeled as an element Autodesk.Revit.DB.Structure.RebarCoverType.

## Copying / Propagating Rebar to a new host

Methods in the `RebarPropagation` class allow rebar to be copied from one host element to a different host element with similar geometry. It copies the source rebars, aligns them to the destination face based on their alignment with the source face, and adapts them to destination host. The propagation is done based on a destination host element where the new rebar will be hosted or a destination face.

## Moving individual rebar in a Rebar Set

The methods `Rebar.MoveBarInSet()`, `Rebar.GetBarIndexFromReference()`, `Rebar.GetMovedBarTransform()`, and `Rebar.ResetMovedBarTransform()` allow an application to move an individual bar and to read and reset the transform of the individual bar in a Rebar Set.

## Removing individual bars from a Rebar Set

`Rebar.SetBarIncluded(bool, int)` allows you to designate that the bar at a given index will be included or excluded. Setting `Rebar.IncludeFirstBar(bool)` and `Rebar.IncludeLastBar(bool)` are equivalent to removing the bar at the first or last position index.

`Rebar.DoesBarExistAtPosition(int)` can be used to find if the bar at any position index is included or excluded.

## Numbering

Rebar is one of the categories of elements whose numbering can be controlled via the Revit API. The NumberingSchema and NumberingSchemaType classes can be used to define how rebar elements are to be organized for the purpose of numbering/tagging them. Each NumberingSchema controls numbering of elements of one particular kind. Instances of NumberingSchema are also elements and there is always only one of each type in every Revit document. Available types of all built-in numbering schemas are enumerated in NumberingSchemaTypes class.

Elements (e.g. Rebar) belonging to a particular schema (e.g. NumberingSchemaTypes.StructuralNumberingSchemas.Rebar) are organized and numbered in sequences. A sequence is a collection of elements that share the same numbering partition as defined by their respective values of the Partition parameter (NUMBER\_PARTITION\_PARAM). A numbering sequence must contain at least one element. In other words, a sequence is established once there is at least one element of which the partition parameter has a value that differs from other elements (in the same numbering schema). If the last element is removed (deleted or moved to a different sequence) then the empty sequence ceases to exist.

Elements get assigned to sequences either upon their creation (based on the then current numbering partition value), by explicitly modifying the Partition parameter of an element, or by using the AssignElementsToSequence() method. The AssignElementsToSequence() method is preferred over explicitly changing the Partition parameter, because the method applies changes to sequences and element numbers immediately, while changed parameters only go into effect after the current transaction is closed.

In addition to directly or indirectly changing the Partition parameter of elements, numbering sequences can be reorganized by using methods of the NumberingSchema class. The MoveSequence() method moves all elements of an existing sequence to a new sequence that does not exist yet in the schema, thus effectively renaming the Partition parameter on all the affected elements. The AppendSequence() method removes all elements from one sequence and appends them to elements of another existing sequence while applying the matching policy. The method MergeSequences() takes elements of all specified sequences and moves them all into a newly created sequence. All the merged elements will be renumbered and matched as needed based on the matching algorithm.

The sample below uses the MoveSequence() method to swap numbers for Rebar in two numbering sequences.

| Code Region: Swap numbers |
| --- |
| 
```
/// <summary>
/// This method uses multiple moving operations to swap numbers
/// for Rebars in two numbering sequences. The sequences are
/// identified by the names of two numbering partitions.
/// </summary>
/// <param name="document">Document to modify</param>
/// <param name="part1">Name of the partition of one numbering sequence</param>
/// <param name="part2">Name of the partition of another numbering sequence</param>
private void SwapNumberingSequences(Document document, string part1, string part2)
{
    // Obtain a schema object for a particular kind of elements 
    NumberingSchema schema = NumberingSchema.GetNumberingSchema(document,NumberingSchemaTypes.StructuralNumberingSchemas.Rebar);

    using (Transaction transaction = new Transaction(document))
    {
        // Changes to numbering sequences must be made inside a transaction
        transaction.Start("Swap Numbering Sequences");

        // We will use a temporary partition for the swap operation,
        // for the move operation only works if the target partition 
        // does not exist yet in the same numbering schema.
        // (We assume this TEMPORARY partition does not exist.)
        string tempPartition = "TEMPORARY";

        // Step 1
        // First we move all elements from one sequence into 
        // a partition we know does not exist. This action will
        // create the temporary partition and remove the original
        // one (part1).
        schema.MoveSequence(part1, tempPartition);

        // Step 2
        // With the sequence in partition 'part1' removed
        // we can now move elements from the second sequence to it.
        // This action will re-create a sequence in partition 'part1'
        // and remove the sequence in partition 'part2'
        schema.MoveSequence(part2, part1);

        // Step 3
        // Finally, we can move elements 'parked' in the temporary
        // sequence to partition 'part2', for that partition was
        // removed in the previous step and thus can now be created
        // again. The temporary partition will be automatically 
        // removed upon completing this step.
        schema.MoveSequence(tempPartition, part2);

        transaction.Commit();
    }
}
```

 |

Elements in different sequences are numbered independently, meaning that there may be elements with the same number in two sequences even though the elements are different. Likewise, there may be perfectly identical elements in two or more sequences bearing different numbers. However, within each one numbering sequence any two identical elements will always have the same number, while different elements will never have the same number within a numbering sequence.

Enumerable elements are always numbered automatically upon their creation. Each new element will get an incrementally higher number. However, new elements that match existing elements within the same sequence will get the same number assigned. Elements will keep their assigned numbers as long as it is possible. This means, for example, that if some previously created rebar elements get deleted, all remaining elements (within the same numbering sequence) will keep their numbers, which may result in gaps in the respective numbering sequence. Gaps can be removed by invoking RemoveGaps() for sequences in which gaps are not desired.

The following example consolidates the numbers on Rebar elements by removing any remaining gaps in numbering sequences and setting the start number of each sequence so numbers in sequences do not overlap.

| Code Region: Consolidate Rebar numbers |
| --- |
| 
```
private void ConsolidateRebarNumbers(Document document)
{
    // Obtain a schema object for a particular kind of elements 
    NumberingSchema schema = NumberingSchema.GetNumberingSchema(document,NumberingSchemaTypes.StructuralNumberingSchemas.Rebar);

    // Collect the names of partitions of all the numbering sequences currently contained in the schema
    IList<string> sequences = schema.GetNumberingSequences();

    using (Transaction transaction = new Transaction(document))
    {
        // Changes to numbers must be made inside a transaction
        transaction.Start("Consolidate Rebar Numbers");

        // First we make sure numbers in all sequences are consecutive
        // by removing possible gaps in numbers. Note: RemoveGaps does
        // nothing for a sequence where there are no gaps present.

        // We also want to find what the maximum range of numbers is
        // of all the sequences (the one the widest span of used numbers)
        int maxRange = 0;

        foreach (string name in sequences)
        {
            schema.RemoveGaps(name);

            // Here we use First() from the Linq extension.
            // There is always at least one range in every sequence,
            // and after gaps are closed there is exactly one range.
            IntegerRange range = schema.GetNumbers(name).First();  
            int rangeSpan = 1 + (range.High - range.Low);
            if (rangeSpan > maxRange)
            {
                maxRange = rangeSpan;
            }
        }

        // Next we give sequences different start numbers
        // starting with 100 and then stepping by at least
        // the maximum range we found in the previous step
        int startNumber = 100;

        // We round the range up to the closest 100
        int step = 100 * (int)((maxRange + 99) / 100.0);

        foreach (string name in sequences)
        {
            schema.ShiftNumbers(name, startNumber);
            startNumber += step;
        }

        transaction.Commit();
    }
}
```

 |

Numbers are stored as values of a numbering parameter on each numbered element. The Id of the parameter is obtained by querying the NumberingSchema.NumberingParameterId property. The value of the number can be obtained by querying the parameter for the respective numbered element. The value is read-only and thus cannot be set; it is always computed based on relations of elements across numbering partitions and the matching policy within the numbering sequence of each element.

Even though numbers are always assigned automatically to all elements of a schema, the method ChangeNumber() gives the programmer a way to explicitly overwrite a specific number as long as the new number is unique in the numbering sequence. The caller specifies a number to be changed and a new value that is to be applied, providing the value does not exist yet in the same numbering sequence.

## Distribution type

The Rebar.DistributionType property can be used to modify the type of a rebar set. Rebar sets can be Uniform or VaryingLength, For a uniform distribution type: all bars parameters are the same as the first bar in set. For a varying length distribution type: bars parameters can vary(primarily in length) taking in consideration the constraints of the first bar in set.

The Rebar.GetParameterValueAtIndex() method gets the parameter value for a bar at the specified index. Accepts only values between 0 and NumberOfBarPositions-1. If the DistributionType is Uniform then the returned ParameterValue is the same no matter the index. If the DistributionType is VaryingLength then the returned ParameterValue is evaluated at the given index.

## Bar Type Diameter

The options classBarTypeDiameterOptions allows creation of a new set of diameter values for a RebarBarType. It can be used when copying the diameter information as a bulk of data from one RebarBarType to another.

The diameter options can be set for a RebarBarType with RebarBarType.SetBarTypeDiameters() which sets all input diameters from the input BarTypeDiameterOptions in the current RebarBarType.

## Constraints

The RebarConstraint class represents a constraint on a handle of a rebar element.

For Shape Driven Rebar Constraints, Each handle on a rebar is defined by a plane, and can be constrained along the direction perpendicular to the plane. Rebar constraints work by locking the handle planes to planar references, or 'targets.'

For Free Form Rebar Constraints, each handle of the Rebar can be constrained to multiple host faces or to the face cover

The RebarConstraintsManager provides information about the constraints (RebarConstraints) acting on the shape handles (RebarConstrainedHandles) of a Rebar element. It can also be used to modify the constraints.

## Geometry

The methods `Rebar.GetTransformedCenterlineCurves()` and `RebarInSystem.GetTransformedCenterlineCurves()` return the centerline curves for a given bar, where the geometry of the curves are in the actual transformed position. The `BarPositionTransform` (representing the relative position of any individual bar in the set - a translation along the distribution path)and `MovedBarTransform` (representing the movement of the bar relative to its default position along the distribution path) will be applied to the returned curves.

## Freeform Rebar

The properties: `RebarFreeFormAccessor.RebarStyle` and `RebarFreeFormAccessor.StirrupTieAttachmentType` provide read and write access to the corresponding properties of freeform rebar elements.

The method: `RebarFreeFormAccessor.SetReportedShape()` changes the rebar shape of a freeform rebar that is currently using the `RebarWorkInstructions.Straight` option to the provided rebar shape.

## Rebar conversion

The methods `AreaReinforcement.ConvertRebarInSystemToRebars()` and `PathReinforcement.ConvertRebarInSystemToRebars()` convert all of the RebarInSystem elements owned by the input element into equivalent Rebar elements.


<!-- ===== END: Help  Rebar  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Rebar Couplers  Autodesk.md ===== -->

---
created: 2026-01-28T21:09:32 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Rebar_Couplers_html
author: 
---

# Help | Rebar Couplers | Autodesk

> ## Excerpt
> Rebar couplers are used to connect adjacent rebar.

---
Rebar couplers are used to connect adjacent rebar.

## Creating couplers

Couplers can connect two adjacent rebar or cap the end of a single rebar. Couplers are represented by the RebarCoupler class. The static Create() method can be used to create new couplers.

The following example creates a coupler to connect two adjacent single rebar bars. The Create() method needs the ElementId of a coupler type and the RebarReinforcementData for the two rebars to connect.

<table summary="" id="GUID-F9EA1C58-86D1-4085-9FDC-57D15E895A99__TABLE_0CDC6E31685E4EB2BDE96CA3BBAC7072"><tbody><tr><td><b>Code Region: Creating a rebar coupler</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>RebarCoupler</span><span> </span><span>CreateCoupler</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>List</span><span>&lt;</span><span>Rebar</span><span>&gt;</span><span> bars</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>RebarCoupler</span><span> coupler </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>// if we have at least 2 bars, create a coupler between them</span><span>
    </span><span>if</span><span> </span><span>(</span><span>bars</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>1</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// get a type id for the Coupler</span><span>
        </span><span>ElementId</span><span> defaultTypeId </span><span>=</span><span> doc</span><span>.</span><span>GetDefaultFamilyTypeId</span><span>(</span><span>new</span><span> </span><span>ElementId</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Coupler</span><span>));</span><span>

        </span><span>if</span><span> </span><span>(</span><span>defaultTypeId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// Specify the rebar and ends to couple</span><span>
            </span><span>RebarReinforcementData</span><span> rebarData1 </span><span>=</span><span> </span><span>RebarReinforcementData</span><span>.</span><span>Create</span><span>(</span><span>bars</span><span>[</span><span>0</span><span>].</span><span>Id</span><span>,</span><span> </span><span>0</span><span>);</span><span>
            </span><span>RebarReinforcementData</span><span> rebarData2 </span><span>=</span><span> </span><span>RebarReinforcementData</span><span>.</span><span>Create</span><span>(</span><span>bars</span><span>[</span><span>1</span><span>].</span><span>Id</span><span>,</span><span> </span><span>1</span><span>);</span><span>

            </span><span>RebarCouplerError</span><span> error</span><span>;</span><span>
            coupler </span><span>=</span><span> </span><span>RebarCoupler</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> defaultTypeId</span><span>,</span><span> rebarData1</span><span>,</span><span> rebarData2</span><span>,</span><span> </span><span>out</span><span> error</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>error </span><span>!=</span><span> </span><span>RebarCouplerError</span><span>.</span><span>ValidationSuccessfuly</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Create Coupler failed: "</span><span> </span><span>+</span><span> error</span><span>.</span><span>ToString</span><span>());</span><span>
            </span><span>}</span><span>

            </span><span>// Use a coupler to cap the other end of the first bar</span><span>
            </span><span>RebarReinforcementData</span><span> rebarData </span><span>=</span><span> </span><span>RebarReinforcementData</span><span>.</span><span>Create</span><span>(</span><span>bars</span><span>[</span><span>0</span><span>].</span><span>Id</span><span>,</span><span> </span><span>1</span><span>);</span><span>
            </span><span>RebarCoupler</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> defaultTypeId</span><span>,</span><span> rebarData</span><span>,</span><span> </span><span>null</span><span>,</span><span> </span><span>out</span><span> error</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>error </span><span>!=</span><span> </span><span>RebarCouplerError</span><span>.</span><span>ValidationSuccessfuly</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> </span><span>"Create Coupler failed: "</span><span> </span><span>+</span><span> error</span><span>.</span><span>ToString</span><span>());</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>return</span><span> coupler</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

If the coupler cannot be created, a RebarCouplerError enum will be returned. Some reasons the creation may fail include bars not touching, different layouts between the rebar sets, or the bars may be the wrong diameter for the coupler.

The CouplerLinkTwoBars() method will return true if the coupler connects two rebars, or false it if only caps one rebar.

The Rebar class has a GetCouplerId() method to get the id of the a coupler attached to either end of the rebar.

## Coupler location and Angle

To get the location point or points (in the case of a rebar set), call the GetPointsForPlacement() method, which returns a list of XYZ points indicating where the coupler (or couplers) are placed. The GetCouplerPositionTransform() method will return a transform representing the relative position of the coupler at a specified index in the set. The index should be between 0 and the coupler quantity - 1. GetCouplerQuantity() will return the quantity of couplers in the set.

`RebarCoupler.RotationAngle` identifies the rotation angle of the coupler around its axis.

## Numbering

RebarCoupler is one of the categories of elements whose numbering can be controlled via the Revit API. The NumberingSchema and NumberingSchemaType classes can be used to define how coupler elements are to be organized for the purpose of numbering/tagging them. Each NumberingSchema controls numbering of elements of one particular kind. Instances of NumberingSchema are also elements and there is always only one of each type in every Revit document. Available types of all built-in numbering schemas are enumerated in NumberingSchemaTypes class.

Elements (e.g.RebarCoupler) belonging to a particular schema (e.g. NumberingSchemaTypes.StructuralNumberingSchemas.RebarCoupler) are organized and numbered in sequences. A sequence is a collection of elements that share the same numbering partition as defined by their respective values of the Partition parameter (NUMBER\_PARTITION\_PARAM). A numbering sequence must contain at least one element. In other words, a sequence is established once there is at least one element of which the partition parameter has a value that differs from other elements (in the same numbering schema). If the last element is removed (deleted or moved to a different sequence) then the empty sequence ceases to exist.

## End Treatments

The end treatment for a rebar bar comes from the coupler attached to it. The end treatment type for both ends of the coupler is specified by the coupler family type.

The overloaded EndTreatmentType.Create() method can be used to create a new EndTreatmentType with or without a string to specify the end treatment name. The CreateDefaultEndTreatmentType() method creates a new EndTreatmentType with a default name.

To access the end treatment type for a RebarCoupler, use the BuiltInParameters COUPLER\_MAIN\_ENDTREATMENT to set End Treatment 1 and COUPLER\_COUPLED\_ENDTREATMENT to set End Treatment 2 for the FamilySymbol representing the rebar coupler type. The example below creates a new EndTreatmentType and assigns it to End Treatment 1 for the coupler type. An existing EndTreatmentType can also be used.

<table summary="" id="GUID-F9EA1C58-86D1-4085-9FDC-57D15E895A99__TABLE_E034F3BCBEF24BFDA60468978F34529C"><tbody><tr><td><b>Code Region: Change EndTreatmentType for RebarCoupler</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>NewEndTreatmentForCouplerType</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>ElementId</span><span> couplerTypeId</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>EndTreatmentType</span><span> treatmentType </span><span>=</span><span> </span><span>EndTreatmentType</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Custom"</span><span>);</span><span>
    </span><span>FamilySymbol</span><span> couplerType </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>couplerTypeId</span><span>)</span><span> </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
    </span><span>Parameter</span><span> param </span><span>=</span><span> couplerType</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>CouplerMainEndtreatment</span><span>);</span><span>
    param</span><span>.</span><span>Set</span><span>(</span><span>treatmentType</span><span>.</span><span>Id</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

An end treatment can be defined in a RebarShape to define the shapes that have specific treatments at the ends. The end treatment in the RebarShape is used for shape recognition. The user defines the shapes according to their specifications and when a coupler is placed on a bar, it automatically searches for the right RebarShape, if the ReinforcementSettings.RebarShapeDefinesEndTreatments property is set to true. Note that this property can only be set before any rebar or reinforcement are added to the document.

<table summary="" id="GUID-F9EA1C58-86D1-4085-9FDC-57D15E895A99__TABLE_5413E9B0976C4798A18E9976D908CBBA"><tbody><tr><td><b>Code Region: Set and EndTreatmentType for a RebarShape</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>bool</span><span> </span><span>SetEndTreatmentType</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>RebarShape</span><span> rebarShape</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>bool</span><span> </span><span>set</span><span> </span><span>=</span><span> </span><span>false</span><span>;</span><span>
    </span><span>// check if end treatments are defined by rebar shape</span><span>
    </span><span>ReinforcementSettings</span><span> settings </span><span>=</span><span> </span><span>ReinforcementSettings</span><span>.</span><span>GetReinforcementSettings</span><span>(</span><span>doc</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>settings</span><span>.</span><span>RebarShapeDefinesEndTreatments</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>EndTreatmentType</span><span> treatmentType </span><span>=</span><span> </span><span>EndTreatmentType</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Flame Cut"</span><span>);</span><span>
        rebarShape</span><span>.</span><span>SetEndTreatmentTypeId</span><span>(</span><span>treatmentType</span><span>.</span><span>Id</span><span>,</span><span> </span><span>0</span><span>);</span><span>

        </span><span>ElementId</span><span> treatmentTypeId </span><span>=</span><span> </span><span>EndTreatmentType</span><span>.</span><span>CreateDefaultEndTreatmentType</span><span>(</span><span>doc</span><span>);</span><span>
        rebarShape</span><span>.</span><span>SetEndTreatmentTypeId</span><span>(</span><span>treatmentTypeId</span><span>,</span><span> </span><span>1</span><span>);</span><span>

        </span><span>set</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
    </span><span>}</span><span>
    </span><span>else</span><span>
    </span><span>{</span><span>
        </span><span>try</span><span>
        </span><span>{</span><span>
            </span><span>// can only be changed if document contains no rebars, area reinforcement or path reinforcement</span><span>
            settings</span><span>.</span><span>RebarShapeDefinesEndTreatments</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>catch</span><span> </span><span>(</span><span>Exception</span><span> e</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>// cannot change the settings value</span><span>
            </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> e</span><span>.</span><span>Message</span><span>);</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>return</span><span> </span><span>set</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The RebarShape class has methods to determine if it has end treatments, and methods to get and set the EndTreatmentType for both ends of the RebarShape.

Note that Rebar Couplers can’t be placed on Area, Path, or Rebar Container.

<table summary="" id="GUID-F9EA1C58-86D1-4085-9FDC-57D15E895A99__TABLE_54FC83994F7B45ED9A5589F8C2E226D3"><tbody><tr><td><b>Code Region: Get end treatments for Rebar</b></td></tr><tr><td><pre><code><span>private</span><span> </span><span>void</span><span> </span><span>ListEndTreatments</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>List</span><span>&lt;</span><span>Rebar</span><span>&gt;</span><span> bars</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>StringBuilder</span><span> info </span><span>=</span><span> </span><span>new</span><span> </span><span>StringBuilder</span><span>();</span><span>
    </span><span>for</span><span> </span><span>(</span><span>int</span><span> n </span><span>=</span><span> </span><span>0</span><span>;</span><span> n </span><span>&lt;</span><span> bars</span><span>.</span><span>Count</span><span>;</span><span> n</span><span>++)</span><span>
    </span><span>{</span><span>
        </span><span>// get end treatment for both ends of bar</span><span>
        </span><span>for</span><span> </span><span>(</span><span>int</span><span> i </span><span>=</span><span> </span><span>0</span><span>;</span><span> i </span><span>&lt;</span><span> </span><span>2</span><span>;</span><span> i</span><span>++)</span><span>
        </span><span>{</span><span>
            </span><span>ElementId</span><span> treatmentTypeId </span><span>=</span><span> bars</span><span>[</span><span>n</span><span>].</span><span>GetEndTreatmentTypeId</span><span>(</span><span>i</span><span>);</span><span>
            </span><span>if</span><span> </span><span>(</span><span>treatmentTypeId </span><span>!=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>EndTreatmentType</span><span> treatmentType </span><span>=</span><span> doc</span><span>.</span><span>GetElement</span><span>(</span><span>treatmentTypeId</span><span>)</span><span> </span><span>as</span><span> </span><span>EndTreatmentType</span><span>;</span><span>
                info</span><span>.</span><span>AppendLine</span><span>(</span><span>string</span><span>.</span><span>Format</span><span>(</span><span>"End treatment for bar {0} end {1}: {2}"</span><span>,</span><span> n</span><span>,</span><span> i</span><span>,</span><span> treatmentType</span><span>.</span><span>EndTreatment</span><span>));</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> info</span><span>.</span><span>ToString</span><span>());</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Rebar Couplers  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Area and Path Reinforcement  Autodesk.md ===== -->

---
created: 2026-01-28T21:09:36 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Area_and_Path_Reinforcement_html
author: 
---

# Help | Area and Path Reinforcement | Autodesk

> ## Excerpt
> The Revit API provides classes representing area and path reinforcement in the structural features of Revit.

---
The Revit API provides classes representing area and path reinforcement in the structural features of Revit.

Find the AreaReinforcementCurves for AreaReinforcement by calling the GetBoundaryCurveIds() method which returns an IList of ElementIds that represent AreaReinforcementCurves.

While the AreaReinforcement.GetBoundaryCurveIds() method returns a set of ElementIds representing AreaReinforcementCurves, which have a property that returns a Curve, the PathReinforcement.GetCurveElementIds() method returns a collection of ElementIds that represent ModelCurves. There is no way to flip the PathReinforcement except by on creation using the PathReinforcement.Create() method. PathReinforcment can only be created using an array of curves.

For more details about retrieving an Element's Geometry, refer to [Geometry](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_html).

Note: Project-wide settings related to area and path reinforcement are accessible from the [ReinforcementSettings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Reinforcement_Settings_html "Several settings regarding reinforcement in the model are controlled at the document level and are accessed through the ReinfocementSettings class for the document.") class.

The API provides access to the layers of Area Reinforcement elements and allows the individual lines exposed through those layers to be moved and removed.

The overloaded AreaReinforcement.Create() method provides two ways to create new AreaReinforcement: based on a host boundary or from an array of curves. The Major Direction of the area reinforcement can be set when creating a new AreaReinforcement using either of the overloaded Create() methods, but the AreaReinforcment.Direction property is read-only.

<table summary="" id="GUID-8AD6CFC8-A065-4108-B700-E523575169C3__TABLE_D2975572CF144E9582C227C448096E39"><tbody><tr><td><b>Creating area reinforcement</b></td></tr><tr><td><pre><code><span>AreaReinforcement</span><span> </span><span>CreateAreaReinforcementInWall</span><span>(</span><span>Wall</span><span> wall</span><span>,</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get the wall analytical profile whose curves will define the boundary of the the area reinforcement </span><span>
     </span><span>AnalyticalPanel</span><span> analytical </span><span>=</span><span> </span><span>(</span><span>AnalyticalPanel</span><span>)</span><span>document</span><span>.</span><span>GetElement</span><span>(</span><span>AnalyticalToPhysicalAssociationManager</span><span>.</span><span>GetAnalyticalToPhysicalAssociationManager</span><span>(</span><span>document</span><span>)</span><span>
</span><span>.</span><span>GetAssociatedElementId</span><span>(</span><span>wall</span><span>.</span><span>Id</span><span>));</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> analytical</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Can't get AnalyticalModel from the selected wall"</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> curves </span><span>=</span><span> analytical</span><span>.</span><span>GetOuterContour</span><span>().</span><span>Cast</span><span>&lt;</span><span>Curve</span><span>&gt;().</span><span>ToList</span><span>();</span><span>

    </span><span>//define the Major Direction of AreaReinforcement,</span><span>
    </span><span>//we get direction of first Line on the Wall as the Major Direction</span><span>
    </span><span>Line</span><span> firstLine </span><span>=</span><span> </span><span>(</span><span>Line</span><span>)(</span><span>curves</span><span>[</span><span>0</span><span>]);</span><span>
    XYZ majorDirection </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>
        firstLine</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>X </span><span>-</span><span> firstLine</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>X</span><span>,</span><span>
        firstLine</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Y </span><span>-</span><span> firstLine</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Y</span><span>,</span><span>
        firstLine</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Z </span><span>-</span><span> firstLine</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Z</span><span>);</span><span>

    </span><span>// Obtain the default types</span><span>
    </span><span>ElementId</span><span> defaultRebarBarTypeId </span><span>=</span><span> document</span><span>.</span><span>GetDefaultElementTypeId</span><span>(</span><span>ElementTypeGroup</span><span>.</span><span>RebarBarType</span><span>);</span><span>
    </span><span>ElementId</span><span> defaultAreaReinforcementTypeId </span><span>=</span><span> document</span><span>.</span><span>GetDefaultElementTypeId</span><span>(</span><span>ElementTypeGroup</span><span>.</span><span>AreaReinforcementType</span><span>);</span><span>
    </span><span>ElementId</span><span> defaultHookTypeId </span><span>=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>;</span><span>

    </span><span>// Create the area reinforcement</span><span>
    </span><span>AreaReinforcement</span><span> rein </span><span>=</span><span> </span><span>AreaReinforcement</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> wall</span><span>,</span><span> curves</span><span>,</span><span> majorDirection</span><span>,</span><span> defaultAreaReinforcementTypeId</span><span>,</span><span> defaultRebarBarTypeId</span><span>,</span><span> defaultHookTypeId</span><span>);</span><span>

    </span><span>return</span><span> rein</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Creating path reinforcement

The overloaded static method PathReinforcement.Create() method provides two ways to create path reinforcement. Both create path reinforcement in a host object from an array of curves, but one will use the default rebar shape while the other takes a Rebar Shape id as a parameter. The example below uses the default rebar shape.

<table summary="" id="GUID-8AD6CFC8-A065-4108-B700-E523575169C3__TABLE_03C405B4DCD042B88DB2270995530831"><tbody><tr><td><b>Creating path reinforcement</b></td></tr><tr><td><pre><code><span>PathReinforcement</span><span> </span><span>CreatePathReinforcement</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Wall</span><span> wall</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create a geometry line in the selected wall as the path</span><span>
    </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> curves </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;();</span><span>
    </span><span>LocationCurve</span><span> location </span><span>=</span><span> wall</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
    XYZ start </span><span>=</span><span> location</span><span>.</span><span>Curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>);</span><span>
    XYZ </span><span>end</span><span> </span><span>=</span><span> location</span><span>.</span><span>Curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>);</span><span>
    curves</span><span>.</span><span>Add</span><span>(</span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>start</span><span>,</span><span> </span><span>end</span><span>));</span><span>

    </span><span>// Obtain the default types</span><span>
    </span><span>ElementId</span><span> defaultRebarBarTypeId </span><span>=</span><span> document</span><span>.</span><span>GetDefaultElementTypeId</span><span>(</span><span>ElementTypeGroup</span><span>.</span><span>RebarBarType</span><span>);</span><span>
    </span><span>ElementId</span><span> defaultPathReinforcementTypeId </span><span>=</span><span> document</span><span>.</span><span>GetDefaultElementTypeId</span><span>(</span><span>ElementTypeGroup</span><span>.</span><span>PathReinforcementType</span><span>);</span><span>
    </span><span>ElementId</span><span> defaultHookTypeId </span><span>=</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>;</span><span>

    </span><span>// Begin to create the path reinforcement</span><span>
    </span><span>PathReinforcement</span><span> rein </span><span>=</span><span> </span><span>PathReinforcement</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> wall</span><span>,</span><span> curves</span><span>,</span><span> </span><span>true</span><span>,</span><span> defaultPathReinforcementTypeId</span><span>,</span><span> defaultRebarBarTypeId</span><span>,</span><span> defaultHookTypeId</span><span>,</span><span> defaultHookTypeId</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> rein</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Create path reinforcement failed."</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Give the user some information</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Create path reinforcement succeed."</span><span>);</span><span>

    </span><span>return</span><span> rein</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

When specifying the rebar shape id for a new PathReinforcement, if there are no rebar shapes in the project or you are not initially concerned with the rebar shape, you can use the static PathReinforcement method GetOrCreateDefaultRebarShape() to obtain a valid rebar shape for use with PathReinforcement. If you would like to check whether an existing rebar shape is valid for use with path reinforcement, you can call the static method PathReinforcement.IsValidRebarShapeId().

New shape types may be queried, or assigned to the path reinforcement by using the PathReinforcement properties PrimaryBarShapeId and AlternatingBarShapeId. The static method IsValidRebarShapeId() can be used to determine if you have a valid shape before attempting to set the shape id on a path reinforcement object. Note that before attempting to set alternating bars, the alternating bars parameter must be enabled in the Path Reinforcement by setting PATH\_REIN\_ALTERNATING BuiltInParameter to true.

The orientation of the primary and alternating bars may also be queried, or set through the properties PrimaryBarOrientation and AlternatingBarOrientation which take a value from the ReinforcementBarOrientation enumeration. You may check whether an orientation is valid for a particular path reinforcement object by calling the class method IsValidPrimaryBarOrientation() or IsValidAlternatingBarOrientation().

You may query the state of the alternating layer by calling the IsAlternatingLayerEnabled() method. The alternating layer is controlled via the built in parameter PATH\_REIN\_ALTERNATING on the path reinforcing element.

The API provides access to move, include, or remove individual bars for RebarInSystem elements that are owned by PathReinforcement.


<!-- ===== END: Help  Area and Path Reinforcement  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Fabric Reinforcement  Autodesk.md ===== -->

---
created: 2026-01-28T21:09:40 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Fabric_Reinforcement_html
author: 
---

# Help | Fabric Reinforcement | Autodesk

> ## Excerpt
> Fabric reinforcement is a layer of fabric sheets made of welded fabric wire and hosted in concrete slabs or walls.

---
Fabric reinforcement is a layer of fabric sheets made of welded fabric wire and hosted in concrete slabs or walls.

Fabric sheets are typically created in a pattern which results in welded wire sheets overlapping each other to provide continuity of load transfer from one sheet to the next. Sheets may be in one or more layers within a concrete element.

Fabric Sheets are typically specified by a grid spacing and a wire size for each direction. For example: 6x6 - W2.9/W2.9 in US Imperial units (or 152x152-MW18.7/MW18.7 in SI units) would be interpreted as a grid of wires at 6" on center with a wire area of 2.9 hundredths of an inch squared (0.029 sq-in).

In the Revit API, these sheets are represented by the FabricSheet class and they are defined by a FabricSheetType class which controls the number and spacing of wires in each direction, either by a pattern or custom definition. FabricSheetType reference wires as FabricWireItems that are associated with a FabricWireType.

## Fabric Area

The FabricArea class is a container for fabric sheets. When created, fabric sheets are automatically generated for the FabricArea based on the FabricSheetType referenced on creation. The FabricArea class has an overloaded Create() method to create a FabricArea based either on the host boundary or from an array of curves. FabricArea must be hosted by a structural floor, wall, foundation slab or a part created from a structural layer of one of these types.

The example below demonstrates how to create a new FabricArea and get a list of the resulting FabricSheets.

| Code Region: Create a fabric area |
| --- |
| 
```
private FabricArea CreateNewFabricArea(Document document, Element wall)
{
    FabricArea system = null;

    // create default types if they aren't already in the model
    ElementId fabricAreaTypeId = FabricAreaType.CreateDefaultFabricAreaType(document);
    ElementId fabricSheetTypeId = FabricSheetType.CreateDefaultFabricSheetType(document);

    system = FabricArea.Create(document, wall, new XYZ(1, 0, 0), fabricAreaTypeId, fabricSheetTypeId);
    // call regenerate to generate fabric sheets in fabric area
    document.Regenerate();

    // get the list of elementIds for the sheets automatically generated in the fabric area
    IList<ElementId> sheetIds = system.GetFabricSheetElementIds();

    TaskDialog.Show("Revit", string.Format("{0} fabric sheets created", sheetIds.Count));

    return system;
}
```

 |

## Creating fabric sheets

Fabric sheets can be hosted by a container (represented by the FabricArea class), or can exist as single fabric sheets. Single fabric sheets are hosted elements and must be hosted by a structural floor, structural wall, structural foundation slab, or a part created from a structural layer of one of these types. Bent fabric sheets can also be hosted in structural beams, columns and braces.

The FabricSheet class provides an overloaded static Create() method for creating new single fabric sheets in the model. One overload of FabricSheet.Create() creates a flat fabric sheet and requires a reference to the document in which the fabric sheet will be created, a reference to the host element which will host the fabric sheet and the ElementId of the fabric sheet type to create.

Another overload of FabricSheet.Create() can be used to create bent fabric sheets, which is not possible in the Revit user interface. It requires the same input as above, plus a CurveLoop that defines the bending path. This bending path is a profile that defines the bending shape of the fabric sheet. Fabric wires have an allowable bend radiuses so you may provide this CurveLoop profile with or without fillets. In other words, if a U shaped profile is desired, only 3 lines must be specified and the fabric sheet created will be created with the appropriate bend radii at the corners. If the provided profile has no hard corners, (I.e., the curve has a tangent at each point, except the end) no fillets will be created in the final fabric sheet.

The provided CurveLoop is intended to define the centerline of the bent wire. You may specify whether the bend is in the major wires or the minor wires with the BentFabricBendDirection property of the FabricSheet. You may also specify the location of straight wires with respect to bent wires with the BentFabricStraightWiresLocation property.

## Fabric sheet type

A FabricSheet is associated with a FabricSheetType, which is used in the generation of wires for the sheet in the major and minor directions. The FabricSheetLayoutPattern for the wires in a FabricSheetType can be defined as:

-   ActualSpacing - spacing of rebars is fixed
-   FixedNumber - spacing of rebars is adjustable, but the number of bars is constant
-   MaximumSpacing - number of rebars depends on length of rebar set with a maximum spacing constraint specified
-   NumberWithSpacing - spacing and number of rebars are fixed
-   QuantitativeSpacing - multiple groups of wires with a specific spacing and diameter For the first 4 options, FabricSheetType has methods to set the layout pattern with given information for either the minor or major direction, such as SetMajorLayoutAsFixedNumber() or SetMinorAsActualSpacing(). The layout pattern can be retrieved with the properties MajorLayoutPattern and MinorLayoutPattern.

QuantitativeSpacing is for custom patterns. Use SetLayoutAsCustomPattern() to set the major and minor layout patterns to QuantitativeSpacing. If the layout pattern for the FabricSheetType is custom, the MajorDirectionWireType, MinorDirectionWireType, MajorSpacing and MinorSpacing properties do not apply. The SetLayoutAsCustomPattern() method has parameters for the start overlaps for the major and minor directions (both end overhangs are read only and computed internally), as well as a list of FabricWireItems for each direction.

| Code Region: Fabric sheet with custom wire pattern |
| --- |
| 
```
private FabricSheet CreateCustomFabricSheet(Document document, Element wall)
{
    if (FabricSheet.IsValidHost(wall) == false)
        return null;

    // Create a new type for custom FabricSheet
    ElementId fabricSheetTypeId = FabricSheetType.CreateDefaultFabricSheetType(document);
    FabricSheetType fst = document.GetElement(fabricSheetTypeId) as FabricSheetType;

    // Create some fabric wire types
    ElementId idWireType1 = FabricWireType.CreateDefaultFabricWireType(document);
    FabricWireType wireType1 = document.GetElement(idWireType1) as FabricWireType;
    wireType1.WireDiameter = 3.5 / 12.0;

    ElementId idWireType2 = FabricWireType.CreateDefaultFabricWireType(document);
    FabricWireType wireType2 = document.GetElement(idWireType1) as FabricWireType;
    wireType2.WireDiameter = 2.0 / 12.0;

    // Create the wires for the custom pattern
    IList<FabricWireItem> majorWires = new List<FabricWireItem>();
    IList<FabricWireItem> minorWires = new List<FabricWireItem>();
    FabricWireItem item = FabricWireItem.Create(2.0 / 12.0, 1, idWireType1, 0);
    majorWires.Add(item);
    majorWires.Add(item);
    item = FabricWireItem.Create(1.5 / 12.0, 10.0 / 12.0, idWireType2, 0);
    majorWires.Add(item);

    item = FabricWireItem.Create(3.0 / 12.0, 1, idWireType2, 0);
    minorWires.Add(item);
    item = FabricWireItem.Create(3.0 / 12.0, 10.0 / 12.0, idWireType2, 0);
    minorWires.Add(item);

    fst.SetLayoutAsCustomPattern(6.0 / 12.0, 4.0 / 12.0, minorWires, majorWires);

    FabricSheet sheet = FabricSheet.Create(document, wall, fabricSheetTypeId);
    // Regeneration is required before setting any property to object that was created in the same transaction.
    document.Regenerate();

    AnalyticalMember member = (AnalyticalMember)document.GetElement(AnalyticalToPhysicalAssociationManager.GetAnalyticalToPhysicalAssociationManager(document)
    .GetAssociatedElementId(wall.Id));
    sheet.PlaceInHost(wall, member.GetTransform());

    // Give the user some information
    TaskDialog.Show("Revit", string.Format("Flat Fabric Sheet ID='{0}' created successfully.", sheet.Id.IntegerValue));

    return sheet;   
}
```

 |

## Single fabric sheets

When fabric sheets are created, they are not yet placed in their host. You must call the method FabricSheet.PlaceInHost() and pass in the host element as well as a transform which describes the final position of the fabric sheet. The element passed for the host must support hosting fabric sheets. Note that only bent fabric sheets can be hosted in beams, columns or braces, while both bent and flat fabric sheets can be hosted in structural floors, walls and foundation slabs, or parts created from a structural layer of one of these types.

| Code Region: Creating a bent fabric sheet |
| --- |
| 
```
private FabricSheet CreateBentFabricSheet(Document document, Element column)
{
    if (FabricSheet.IsValidHost(column) == false)
        return null;

    CurveLoop bendingProfile = new CurveLoop();
    Line line1 = Line.CreateBound(new XYZ(2, 0.8, 0), new XYZ(6, 0.8, 0));
    Line line2 = Line.CreateBound(new XYZ(6, -0.8, 0), new XYZ(4, -2, 0));
    Arc arc = Arc.Create(line1.GetEndPoint(1), line2.GetEndPoint(0), new XYZ(7, 0, 0));
    bendingProfile.Append(line1);
    bendingProfile.Append(arc);
    bendingProfile.Append(line2);

    ElementId fabricSheetTypeId = document.GetDefaultElementTypeId(ElementTypeGroup.FabricSheetType);
    FabricSheetType fst = document.GetElement(fabricSheetTypeId) as FabricSheetType;
    fst.SetMajorLayoutAsFixedNumber(12.0, 1.0, 0.8, 4);
    fst.SetMinorLayoutAsMaximumSpacing(10.0, .75, .90, 3.0);

    FabricSheet bentFabricSheet = FabricSheet.Create(document, column.Id, fabricSheetTypeId, bendingProfile);
    // Regeneration is required before setting any property to object that was created in the same transaction.
    document.Regenerate();

    bentFabricSheet.BentFabricBendDirection = BentFabricBendDirection.Major;

    AnalyticalMember amc = (AnalyticalMember)document.GetElement(AnalyticalToPhysicalAssociationManager.GetAnalyticalToPhysicalAssociationManager(document)
        .GetAssociatedElementId(column.Id));
    bentFabricSheet.PlaceInHost(column, amc.GetTransform());

    // Give the user some information
    TaskDialog.Show("Revit", string.Format("Bent Fabric Sheet ID='{0}' created successfully.", bentFabricSheet.Id.IntegerValue));

    return bentFabricSheet;
}
```

 |

## Bent fabric sheets

The IsBent property indicates if the fabric sheet is a bent fabric sheet or not. It is not possible to convert a Fabric Sheet between flat and bent.

You may obtain the curves for a bent sheet or set new curves by calling GetBendProfile() or SetBendProfile() respectively.

| Code Region: Change the bend profile of a fabric sheet |
| --- |
| 
```
private void ModifyBentFabricSheet(Document document, FabricSheet bentFabricSheet)
{
    CurveLoop newBendingProfile = CurveLoop.CreateViaOffset(bentFabricSheet.GetBendProfile(), 0.5, new XYZ(0, 0, -1));
    bentFabricSheet.SetBendProfile(newBendingProfile);

    // Give the user some information
    TaskDialog.Show("Revit", string.Format("Bent Fabric Sheet ID='{0}' modified successfully.", bentFabricSheet.Id.IntegerValue));
}
```

 |

The GetSegmentParameterIdsAndLengths() method will return a dictionary with segment parameter ids as the keys and length as the values. These correspond to segments of a bent fabric sheet (like A, B, C, D etc.), but are not in alphabetical or any other order. (An empty dictionary is returned for flat fabric sheets.) To set the length of a bent fabric sheet segment, use SetSegmentLength().

| Code Region: Get segment ids and lengths |
| --- |
| 
```
private void GetBentFabricSheetData(FabricSheet fabricSheet)
{
    string fabricNumber = fabricSheet.FabricNumber;
    IDictionary<ElementId, double> idsAndLengths = fabricSheet.GetSegmentParameterIdsAndLengths(true);
    StringBuilder displayInfo = new StringBuilder();
    displayInfo.AppendLine(string.Format("Parameter Ids and segment lengths for FabricSheet {0}:", fabricNumber));

    foreach (ElementId key in idsAndLengths.Keys)
    {
        displayInfo.AppendLine(string.Format("Parameter Id: {0}, Length: {1}", key, idsAndLengths[key]));
    }

    TaskDialog.Show("Revit", displayInfo.ToString());
}
```

 |

The FabricNumber property used in the example above, specifies the numerical parameter assigned to the fabric sheet and any sheet of the same type, dimension, material, shape, and partition.


<!-- ===== END: Help  Fabric Reinforcement  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Rebar Containers  Autodesk.md ===== -->

---
created: 2026-01-28T21:09:45 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Rebar_Containers_html
author: 
---

# Help | Rebar Containers | Autodesk

> ## Excerpt
> Rebar Containers are elements which represent an aggregation of rebars in one host. This element can only be created via the API.

---
Rebar Containers are elements which represent an aggregation of rebars in one host. This element can only be created via the API.

The advantages of using the RebarContainer element are:

-   Defining new types of rebar distributions not possible with the Revit user interface
-   Improve rebar performance by combining multiple rebar sets into the definition of a single element
-   The bars don’t react to the host’s geometry modifications

Each RebarContainer contains a collection (empty when first created) of RebarContainerItem objects. RebarContainerItem provides properties and methods similar to that of a Rebar element.

## Creating a new RebarContainer

You may use the static method RebarContainer.Create() which requires the Document in which you want to create a new RebarContainer, the host Element which will host the new RebarContainer and the ElementId of the RebarContainerType which will be assigned to the new RebarContainer.

The following example creates a new rebar container and specifies that any items in the container will be presented as subelements in schedules and tags.

<table summary="" id="GUID-AACF9518-D4B4-401D-933A-E1B7E619AE63__TABLE_0CDC6E31685E4EB2BDE96CA3BBAC7072"><tbody><tr><td><b>Code Region: Creating a rebar container</b></td></tr><tr><td><pre><code><span>RebarContainer</span><span> </span><span>CreateRebarContainer</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> beam</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Create a new rebar container</span><span>
    </span><span>ElementId</span><span> defaultRebarContainerTypeId </span><span>=</span><span> </span><span>RebarContainerType</span><span>.</span><span>CreateDefaultRebarContainerType</span><span>(</span><span>document</span><span>);</span><span>
    </span><span>RebarContainer</span><span> container </span><span>=</span><span> </span><span>RebarContainer</span><span>.</span><span>Create</span><span>(</span><span>document</span><span>,</span><span> beam</span><span>,</span><span> defaultRebarContainerTypeId</span><span>);</span><span>

    </span><span>// Any items for this container should be presented in schedules and tags as separate subelements</span><span>
    container</span><span>.</span><span>PresentItemsAsSubelements</span><span> </span><span>=</span><span> </span><span>true</span><span>;</span><span>

    </span><span>return</span><span> container</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## Filling a RebarContainer

Once you have a new RebarContainer object, you can fill it up with RebarContainerItems by calling one of the following methods on the RebarContainer object:

-   AppendItemFromRebar() - Appends a RebarContainerItem to the collection using properties of the Rebar element used to create it.
-   AppendItemFromCurves() - Appends a RebarContainerItem to the collection from a list of curves using properties from the specified RebarBarType.
-   AppendItemFromRebarShape() - Appends a RebarContainerItem to the collection using properties from the specified RebarBarType and RebarShapeType.
-   AppendItemFromCurvesAndShape() - Appends a RebarContainerItem to the collection from a list of curves using properties from the specified RebarBarType and RebarShapeType. Note that in creating the container items, you will often be required to specify the normal of the plane in which the curves exist. This normal also defines the direction of multiple rebar creation if you set the layout rules to anything other than single. If you set the RebarContainerItem to a FixedNumber layout rule, for instance, those additional bars will be distributed along a line perpendicular to the plane you specify when creating the RebarContainerItem. In this sense the Normal also serves as the direction of distribution for RebarContainerItems with layout rules applied.

## Accessing RebarContainerItems

Use the method RebarContainer.Contains() to query whether the particular RebarContainerItem exists in the RebarContainer.

RebarContainer provides methods to remove individual items, clear all items, get specific items and return the count of RebarContainerItems in the container. The SetItemHiddenStatus() method controls whether specific items in the container are hidden in a specific view or not, and IsItemHidden() identifies if an items is hidden in a view.

<table summary="" id="GUID-AACF9518-D4B4-401D-933A-E1B7E619AE63__TABLE_D2975572CF144E9582C227C448096E39"><tbody><tr><td><b>Code Region: Adding items to a rebar container</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>AddItemsToRebarContainer</span><span>(</span><span>RebarContainer</span><span> container</span><span>,</span><span> </span><span>FamilyInstance</span><span> beam</span><span>,</span><span> </span><span>RebarBarType</span><span> barType</span><span>,</span><span> </span><span>RebarHookType</span><span> hookType</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Define the rebar geometry information - Line rebar</span><span>
    </span><span>LocationCurve</span><span> location </span><span>=</span><span> beam</span><span>.</span><span>Location</span><span> </span><span>as</span><span> </span><span>LocationCurve</span><span>;</span><span>
    XYZ origin </span><span>=</span><span> location</span><span>.</span><span>Curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>);</span><span>
    </span><span>// create rebar along the length of the beam</span><span>
    XYZ rebarLineEnd </span><span>=</span><span> location</span><span>.</span><span>Curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>);</span><span>
    </span><span>Line</span><span> line </span><span>=</span><span> </span><span>Line</span><span>.</span><span>CreateBound</span><span>(</span><span>origin</span><span>,</span><span> rebarLineEnd</span><span>);</span><span>
    XYZ normal </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>1</span><span>,</span><span> </span><span>0</span><span>,</span><span> </span><span>0</span><span>);</span><span>
    </span><span>Curve</span><span> rebarLine </span><span>=</span><span> line</span><span>.</span><span>CreateOffset</span><span>(</span><span>0.5</span><span>,</span><span> normal</span><span>);</span><span>

    </span><span>// Create the line rebar</span><span>
    </span><span>IList</span><span>&lt;</span><span>Curve</span><span>&gt;</span><span> curves </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Curve</span><span>&gt;();</span><span>
    curves</span><span>.</span><span>Add</span><span>(</span><span>rebarLine</span><span>);</span><span>

    </span><span>RebarContainerItem</span><span> item </span><span>=</span><span> container</span><span>.</span><span>AppendItemFromCurves</span><span>(</span><span>RebarStyle</span><span>.</span><span>Standard</span><span>,</span><span> barType</span><span>,</span><span> hookType</span><span>,</span><span> hookType</span><span>,</span><span> normal</span><span>,</span><span> curves</span><span>,</span><span> </span><span>RebarHookOrientation</span><span>.</span><span>Right</span><span>,</span><span> </span><span>RebarHookOrientation</span><span>.</span><span>Left</span><span>,</span><span> </span><span>true</span><span>,</span><span> </span><span>true</span><span>);</span><span>

    </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> item</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>// set specific layout for new rebar as fixed number, with 10 bars, distribution path length of 1.5'</span><span>
        </span><span>// with bars of the bar set on the same side of the rebar plane as indicated by normal</span><span>
        </span><span>// and both first and last bar in the set are shown</span><span>
        item</span><span>.</span><span>SetLayoutAsFixedNumber</span><span>(</span><span>10</span><span>,</span><span> </span><span>1.5</span><span>,</span><span> </span><span>true</span><span>,</span><span> </span><span>true</span><span>,</span><span> </span><span>true</span><span>);</span><span>
    </span><span>}</span><span>

    </span><span>// Hide the new item in the active view</span><span>
    container</span><span>.</span><span>SetItemHiddenStatus</span><span>(</span><span>container</span><span>.</span><span>Document</span><span>.</span><span>ActiveView</span><span>,</span><span> item</span><span>.</span><span>ItemIndex</span><span>,</span><span> </span><span>true</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## RebarContainerType

Rebar Containers will have types. These types are agnostic to the individual RebarContainerItems contained in them but will afford access to the Container's parameters at the type level. It is a required argument for creation of a new RebarContainer. Obtain a default by calling the static method RebarContainerType.CreateDefaultRebarContainerType() to obtain the ElementId of a RebarContainerType if the desired one does not exist in the database.

## RebarContainer parameters management

Because the RebarContainer may contain several different configurations of individual RebarContainerItems, the overall RebarContainer parameters will be derived from the contained RebarContainerItem members if possible. If the parameter exists on all RebarContainerItems and it is the same across all RebarContainerItems in the RebarContainer then the RebarContainer parameter will show this value. If they are different, or do not exist on all RebarContainerItems in the Container, the parameter will display without value.

To allow you to manage this and specify necessary parameters for the RebarContainer as a whole, you may request the RebarContainerParameterManager from the RebarContainer calling the method GetParametersManager() which will return an object you can use to override the parameters of the RebarContainer. As an example, TotalLength in a RebarContainer with multiple RebarContainerItems with differing lengths, will show an empty parameter for TotalLength. You can call the RebarContainerParametersManager method AddOverride() which has 4 overloads so that you can override the value of any of four value types of parameters (ElementId, Double, Integer, String). Use the method IsRebarContainerParameter() to determine if the parameter is a RebarContainer parameter before attempting to add an override for the parameter.

You can also add a shared parameter as an override to a RebarContainer by calling the method AddSharedParameterAsOverride() and passing in the id of the shared parameter. Check to see that the parameter has not already been added to the RebarContainer before calling this method.

You may remove overrides by calling the method RemoveOverride() or remove all overrides by calling ClearOverrides().

Individual overridden parameters may be set to be modifiable or read only by calling the methods SetOverriddenParameterModifiable() or SetOverriddenParameterReadonly() and query the same with the IsOverriddenParameterModifiable() method.

Lastly, to check if a RebarContainer parameter is overridden, call the method IsParameterOverridden() passing in the ElementId of the parameter in question.

<table summary="" id="GUID-AACF9518-D4B4-401D-933A-E1B7E619AE63__TABLE_3156988F75974323985FCE1D46FE02C5"><tbody><tr><td><b>Code Region: RebarContainer parameters management</b></td></tr><tr><td><pre><code><span>void</span><span> </span><span>ManageParameters</span><span>(</span><span>RebarContainer</span><span> container</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>RebarContainerParameterManager</span><span> paramManager </span><span>=</span><span> container</span><span>.</span><span>GetParametersManager</span><span>();</span><span>

    </span><span>Parameter</span><span> aParam </span><span>=</span><span> container</span><span>.</span><span>LookupParameter</span><span>(</span><span>"A"</span><span>);</span><span>
    </span><span>if</span><span> </span><span>(</span><span>aParam </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        paramManager</span><span>.</span><span>AddOverride</span><span>(</span><span>aParam</span><span>.</span><span>Id</span><span>,</span><span> </span><span>0.4</span><span>);</span><span>
        paramManager</span><span>.</span><span>SetOverriddenParameterModifiable</span><span>(</span><span>aParam</span><span>.</span><span>Id</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

## RebarContainerItems

Rebar container items offer many of the same properties as do Rebar elements. They are a much lighter representation of a modeled rebar and unlike the Rebar class which is derived from Element, RebarContainerItem is derived from the IDisposable Interface.

You may redefine the RebarContainerItem represented by any RebarContainerItem by calling the class methods available on RebarContainerItem objects:

-   SetFromRebar()
-   SetFromCurves()
-   SetFromRebarShape()
-   SetFromCurvesAndShape() These methods mimic the methods which were used on RebarContainer to create the RebarContainerItem in the first place and have identical or nearly identical arguments which can be used to modify any RebarContainerItem in the RebarContainer.

You may query the RebarBarType ID with the class property BarTypeId. In order to apply a different RebarBarType to the RebarContainerItem you must use the SetFrom methods on the RebarContainerItem (i.e. SetFromCurves() or SetFromRebar()).


<!-- ===== END: Help  Rebar Containers  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Reinforcement Settings  Autodesk.md ===== -->

---
created: 2026-01-28T21:09:49 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Reinforcement_Settings_html
author: 
---

# Help | Reinforcement Settings | Autodesk

> ## Excerpt
> Several settings regarding reinforcement in the model are controlled at the document level and are accessed through the ReinfocementSettings class for the document.

---
Several settings regarding reinforcement in the model are controlled at the document level and are accessed through the ReinfocementSettings class for the document.

These settings include reinforcement rounding document level overrides, hosting of rebar elements on path and area reinforcement, as well as tag abbreviations for reinforcement tagging.

Access the document reinforcement settings object by calling the static ReinforcementSettings.GetReinforcementSettings() which takes a reference to the document and returns the corresponding reinforcement settings object.

## Reinforcement rounding overrides

You may access settings for document level reinforcement rounding overrides by using the methods GetRebarRoundingManager() or GetFabricRoundingManager()

## Hosting rebar on area and path reinforcing

The property HostStructuralRebar controls whether Revit will automatically host real rebar on path and area reinforcement. Before setting this property to true, you must verify that there are no path or area reinforcing objects currently in the document by using a FilteredElementCollector.

## Include hooks in rebar shape definition

The RebarShapeDefinesHooks property controls whether rebar shape definitions include hooks in the definition. This maps to the UI property "Include hooks in Rebar Shape definition" setting in Reinforcement Settings. Note that this property may not be changed if the model contains: rebar elements, area or path reinforcing, or rebar containers. Use a FilteredElementCollector to query the model for the existence of any of these elements before attempting to set this property.

## Include end treatments in rebar shape definition

The RebarShapeDefinesEndTreatments property indicates if end treatments are defined by the RebarShape. This property can only be set if there are no rebars, area reinforcements or path reinforcements.

You may access as well as apply new rebar tag abbreviations. Engineers typically specify rebar with certain abbreviations (E.g., NF = near face, E.W. = each way). There are 16 different abbreviation tags stored by the ReinforcementSettings object and are indexed by the enumeration ReinforcementAbbreviationTagType.

Query current abbreviation tags by calling the method GetReinforcementAbbreviationTag() which will return a string value of the current abbreviation corresponding to the tag type passed to the method. You may also retrieve all of the abbreviation tags associated with either path or area reinforcement by calling the method GetReinforcementAbbreviationTags().

Set new abbreviations by calling the method SetReinforcementAbbreviationTag() passing a ReinforcementAbbreviationTagType to specify for which tag type you wish to set the new abbreviation.

## Varying Rebar Set

The NumberVaryingLengthRebarsIndividually property of ReinforcementSettings modifies the way varying length bars are numbered (individually or as a whole). If true, then each bar in a varying rebar set will be assigned a rebar number. Otherwise, the whole rebar set will be assigned a unique rebar number and each bar within the set will be assigned a suffix that is unique within the set.

The ReinforcementSettings.RebarVaryingLengthNumberSuffix property is a unique string identifier used for a bar within a variable length rebar set.


<!-- ===== END: Help  Reinforcement Settings  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Reinforcement Rounding  Autodesk.md ===== -->

---
created: 2026-01-28T21:09:54 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Reinforcement_Rounding_html
author: 
---

# Help | Reinforcement Rounding | Autodesk

> ## Excerpt
> Reinforcement rounding is important for preparation of construction documents. You can use numerical rounding of rebar lengths to simplify organization and annotation when tagging, filtering, or scheduling rebar.

---
Reinforcement rounding is important for preparation of construction documents. You can use numerical rounding of rebar lengths to simplify organization and annotation when tagging, filtering, or scheduling rebar.

Revit enables overriding of three different reinforcement parameters: Fabric Sheet lengths, Rebar total lengths, and Rebar segment lengths. Rebar segment lengths are the individual segments which make up a rebar shape.

The application of Rebar and/or Fabric Sheet rounding is controlled initially at the Document level. If rounding is not enabled at the document level, the rounding for Reinforcement Length (structural unit settings) will be applied to rebar lengths in schedules and tags. If the Document level reinforcement settings are overridden then the rebar settings control rounding for rebars and fabric sheets and may be overridden further at the type and element level.

## Overriding reinforcement rounding settings

The ReinforcementSettings class provides methods to obtain either the fabric or rebar rounding managers by calling GetFabricRoundingManager() or GetRebarRoundingManager() respectively. These rounding managers represent the document level rounding overrides and will control rounding for any types or elements which are not otherwise overridden by accessing the corresponding rounding manager for the type or element in question.

Reinforcement rounding override is enabled by setting the ReinforcementRoundingManager.IsActiveOnElement property to true at the document level. This property must be set to true before attempting to override the reinforcement rounding settings for the document, a type, or an element.

The ReinforcementRoundingManager has two derived classes, FabricRoundingManager and RebarRoundingManager, to handle overrides for these different types of elements. FabricRoundingManager is used for managing reinforcement rounding override settings used by FabricSheetType and FabricSheet elements while RebarRoundingManager is used for managing reinforcement rounding override settings used by RebarBarTypes, Rebar and RebarInSystem elements.

To override reinforcement rounding settings for a rebar type, call Rebar.GetReinforcementRoundingManager() to get a reference to a RebarRoundingManager. Once you have access to the RebarRoundingManager, to override the rounding settings, first set RebarRoundingManager.IsActiveOnElement to true before attempting to set any of the rounding properties.

RebarRoundingManager.TotalLengthRounding is the rounding increment that will be used in rounding. (e.g., 1" means that the actual length will be rounded to an increment of 1") RebarRoundingManager.TotalLengthRoundingMethod takes a RoundingMethod enum which has the following possible values:

-   Nearest - Standard rounding: round to nearest
-   Up - Round up
-   Down - round down

RebarRoundingManager also provides access to the Segment length rounding with properties RebarRoundingManager.SegmentLengthRounding and RebarRoundingManager.SegmentLengthRoundingMethod.

To override reinforcement settings on a fabric sheet type or a fabric sheet element, calling GetReinforcementRoundingManager() on the corresponding class will return a FabricRoundingManager. The FabricRoundingManager class has similar functionality to the RebarRoundingManager for controlling rounding for fabric sheets.

## Querying an element's current reinforcement rounding settings

You may access information about what is currently controlling the reinforcement rounding for any element by querying the following properties: RebarRoundingManager.ApplicableReinforcementRoundingSource (for rebar) or FabricRoundingManager.ApplicableReinforcementRoundingSource (for fabric sheets). You may also query current rounding settings by using the ApplicableTotalLengthRoundingMethod and ApplicableTotalLengthRounding properties, available from both types of rounding managers .


<!-- ===== END: Help  Reinforcement Rounding  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Annotation  Autodesk.md ===== -->

---
created: 2026-01-28T21:09:59 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Reinforcement_Annotation_html
author: 
---

# Help | Annotation | Autodesk

> ## Excerpt
> The MultiReferenceAnnotation can be used to label and dimension Rebar elements, and are labeled in the user interface as "Multi-rebar annotations". The members of this class include:

---
The `MultiReferenceAnnotation` can be used to label and dimension Rebar elements, and are labeled in the user interface as "Multi-rebar annotations". The members of this class include:

-   Create - creates a new MultiReferenceAnnotation based on a document, view, and an instance of the MultiReferenceAnnotationOptions class
-   AreElementsValidForMultiReferenceAnnotation - validates if the input elements match the element category id for the MultiReferenceAnnotationType.
-   is3DViewValidForDimension - Returns True if the view is suitable for placing the MultiReferenceAnnotation
    -   If the DimensionStyle is LinearFixed, it cannot be created in a 3D View.
    -   If the DimensionStyle is Linear, it cannot be created in a 3D View if the view direction is perpendicular to the current work plane normal.
    -   Returns true if the ownerViewId is not a 3D view.

The references of the annoation and placement options are specified in the `MultiReferenceAnnotationOptions` class. Its members include:

-   DimensionLineDirection - The direction vector of the dimension line
-   SetElementsToDimension - The elements referenced by the dimension
-   SetAdditionalReferencesToDimension - Sets the additional references which the dimension will witness. The additional references to dimension cannot come from the same category as the MultiReferenceAnnotationType's reference category.
-   ReferencesDontMatchReferenceCategory - Verifies that all of the references belongs to elements which don't match the reference category required by the MultiReferenceAnnotationType.
-   GetAdditionalReferencesToDimension - Gets the additional references which the dimension will witness

| Code Region: Create MultiReferenceAnnotation |
| --- |
| 
```
public void CreateAnnotation(Document doc)
{
    MultiReferenceAnnotationOptions opt = new MultiReferenceAnnotationOptions(
        new FilteredElementCollector(doc)
        .OfClass(typeof(MultiReferenceAnnotationType))
        .Cast<MultiReferenceAnnotationType>()
        .FirstOrDefault());
    opt.DimensionLineDirection = XYZ.BasisX;
    opt.DimensionPlaneNormal = XYZ.BasisZ;
    opt.DimensionStyleType = DimensionStyleType.Linear;
    opt.SetElementsToDimension(new FilteredElementCollector(doc, doc.ActiveView.Id).OfClass(typeof(Rebar)).ToElementIds());
    using (Transaction t = new Transaction(doc, "MultiReferenceAnnotation"))
    {
        t.Start();
        MultiReferenceAnnotation mra = MultiReferenceAnnotation.Create(doc, doc.ActiveView.Id, opt);
        t.Commit();
    }
}
```

 |


<!-- ===== END: Help  Annotation  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Boundary Conditions  Autodesk.md ===== -->

---
created: 2026-01-28T21:10:03 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Boundary_Conditions_html
author: 
---

# Help | Boundary Conditions | Autodesk

> ## Excerpt
> There are three types of BoundaryConditions:

---
## BoundaryConditions

There are three types of BoundaryConditions:

-   Point
-   Curve
-   Area

The type and pertinent geometry information is retrieved using the following code:

<table summary="" id="GUID-AACCD68F-865F-462A-A11C-A2D70EF13F4B__TABLE_41F84092478B4443ACD16353C6947A88"><tbody><tr><td><b>Code Region 29-9: Getting boundary condition type and geometry</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetInfo_BoundaryConditions</span><span>(</span><span>BoundaryConditions</span><span> boundaryConditions</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>string</span><span> message </span><span>=</span><span> </span><span>"BoundaryConditions : "</span><span>;</span><span>

    boundaryConditions</span><span>.</span><span>GetBoundaryConditionsType</span><span>();</span><span>
    </span><span>switch</span><span> </span><span>(</span><span>boundaryConditions</span><span>.</span><span>GetBoundaryConditionsType</span><span>())</span><span>
    </span><span>{</span><span>
        </span><span>case</span><span> </span><span>BoundaryConditionsType</span><span>.</span><span>Point</span><span>:</span><span>
            XYZ point </span><span>=</span><span> boundaryConditions</span><span>.</span><span>Point</span><span>;</span><span>
            message </span><span>+=</span><span> </span><span>"\nThis BoundaryConditions is a Point Boundary Conditions."</span><span>;</span><span>
            message </span><span>+=</span><span> </span><span>"\nLocation point: ("</span><span> </span><span>+</span><span> point</span><span>.</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                        </span><span>+</span><span> point</span><span>.</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> point</span><span>.</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>case</span><span> </span><span>BoundaryConditionsType</span><span>.</span><span>Line</span><span>:</span><span>
            message </span><span>+=</span><span> </span><span>"\nThis BoundaryConditions is a Line Boundary Conditions."</span><span>;</span><span>
            </span><span>Curve</span><span> curve </span><span>=</span><span> boundaryConditions</span><span>.</span><span>GetCurve</span><span>();</span><span>
            </span><span>// Get curve start point</span><span>
            message </span><span>+=</span><span> </span><span>"\nLocation Line: start point: ("</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                    </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
            </span><span>// Get curve end point</span><span>
            message </span><span>+=</span><span> </span><span>";  end point:("</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                    </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> curve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>case</span><span> </span><span>BoundaryConditionsType</span><span>.</span><span>Area</span><span>:</span><span>
            message </span><span>+=</span><span> </span><span>"\nThis BoundaryConditions is an Area Boundary Conditions."</span><span>;</span><span>
            </span><span>IList</span><span>&lt;</span><span>CurveLoop</span><span>&gt;</span><span> loops </span><span>=</span><span> boundaryConditions</span><span>.</span><span>GetLoops</span><span>();</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>CurveLoop</span><span> curveLoop </span><span>in</span><span> loops</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>foreach</span><span> </span><span>(</span><span>Curve</span><span> areaCurve </span><span>in</span><span> curveLoop</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>// Get curve start point</span><span>
                    message </span><span>+=</span><span> </span><span>"\nCurve start point:("</span><span> </span><span>+</span><span> areaCurve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                            </span><span>+</span><span> areaCurve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> areaCurve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>0</span><span>).</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
                    </span><span>// Get curve end point</span><span>
                    message </span><span>+=</span><span> </span><span>"; Curve end point:("</span><span> </span><span>+</span><span> areaCurve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>X </span><span>+</span><span> </span><span>", "</span><span>
                            </span><span>+</span><span> areaCurve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Y </span><span>+</span><span> </span><span>", "</span><span> </span><span>+</span><span> areaCurve</span><span>.</span><span>GetEndPoint</span><span>(</span><span>1</span><span>).</span><span>Z </span><span>+</span><span> </span><span>")"</span><span>;</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
            </span><span>break</span><span>;</span><span>
        </span><span>default</span><span>:</span><span>
            </span><span>break</span><span>;</span><span>
    </span><span>}</span><span>

    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>message</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Boundary Conditions  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Slabs  Autodesk.md ===== -->

---
created: 2026-01-28T21:10:09 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Structural_Model_Elements_Slabs_html
author: 
---

# Help | Slabs | Autodesk

> ## Excerpt
> Both Slab (Structural Floor) and Slab Foundation are represented by the Floor class and are distinguished by the IsFoundationSlab property.

---
## Slab

Both Slab (Structural Floor) and Slab Foundation are represented by the Floor class and are distinguished by the IsFoundationSlab property.

The Slab Span Directions are represented by the IndependentTag class in the API and are available as follows:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-23AFA5D3-DFA8-48EE-BDC3-EFB37BADCB7D-low.png)**Figure 157: Slab span directions**

When using Floor.Create() to create a Slab, Span Directions are not automatically created. There is also no way to create them directly.

The Slab compound structure layer Structural Deck properties are exposed by the following properties:

-   CompoundStructuralLayer.DeckUsage
-   DeckProfile

The properties are outlined in the following dialog box:

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-F892CB9B-E142-4112-8925-32C543D8A9AA-low.png)**Figure 158: Floor CompoundStructuralLayer properties**


<!-- ===== END: Help  Slabs  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Analytical Model  Autodesk.md ===== -->

---
created: 2026-01-28T21:10:13 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Analytical_Model_html
author: 
---

# Help | Analytical Model | Autodesk

> ## Excerpt
> In structural engineering, an analytical model is the engineering description of a structural physical model. The Analytical Model is an essential part of BIM data and is subject to collaborative workflows within engineering teams and across project teams. The Analytical Model implementation in Revit enables engineers to:

---
In structural engineering, an analytical model is the engineering description of a structural physical model. The Analytical Model is an essential part of BIM data and is subject to collaborative workflows within engineering teams and across project teams. The Analytical Model implementation in Revit enables engineers to:

-   Have freedom of analytical modeling to reflect their individual design decisions with respect to structural elements and buildings/structures seen as whole systems.
-   Analytically represent any types of structure
-   Create consistent Analytical Models enabling structural analysis jobs from Revit models
-   Perform full bi-directional workflow with analysis software and capture model modifications made there
-   Preserve Analytical Model from unexpected changes if needed
-   Create multiple analytical models reflecting diverse analysis types and configurations
-   Replicate the ease of analytical modeling like in dedicated structural analysis software, combined with the power of parametric and collaboration enabling BIM platform.

## AnalyticalElement

AnalyticalElement represents the base class for all analytical objects.

-   Transform GetTransform() - Returns the transform which reflects Analytical Element orientation.
-   AnalyzeAs AnalyzeAs - This represents the Analyze As parameter assigned to Analytical Element.
-   Reference GetReference(AnalyticalModelSelector selector) - Returns a reference to a given curve within the Analytical Element.
-   ElementId MaterialId - Defines the Material Id for the Analytical Element.

## AnalyticalMember

AnalyticalMember represents a linear element in the structural analytical model.

-   AnalyticalMember Create(Document document, Curve curve) - Method which creates a new instance of an Analytical Member within the project
-   AnalyticalStructuralRole StructuralRole - The structural role assigned to the Analytical Member
-   Curve GetCurve() - Returns the curve of the Analytical Member.
-   void SetCurve(Curve curve) - Sets the curve for the Analytical Member. This method disconnects elements from other analytical elements (if the end nodes are in the same position). If the user wants to move the corner, and keep the connection, there are other ways for achieving that like ElementTransformUtils.moveElements.
-   bool IsValidCurve(Curve curve) - Verifies if the curve is valid for an Analytical Member
-   void FlipCurve() - Flips the ends of the Analytical Member
-   StructuralSectionShape StructuralSectionShape - The structural section shape of the Analytical Member (read only)
-   ElementId SectionType - The id of the type from the structural Family assigned to the Analytical Member
-   double CrossSectionRotation - Cross section rotation of the Analytical Member

## AnalyticalPanel

AnalyticalPanel represents a surface in the structural analytical model.

-   AnalyticalPanel Create(Document document, CurveLoop curveLoop) - Method which creates a new instance of an Analytical Panel within the project.
-   CurveLoop GetOuterContour() - Returns the Curve Loop that defines the geometry of the Analytical Surface element
-   bool IsCurveLoopValid(CurveLoop profile) - Checks if curve loop is valid for Analytical Panel
    -   To modify Analytical Panel geometry, users should use SketchEditScope framework.
    -   void StartWithNewSketch(ElementId elementId) - Starts a sketch edit mode for an element which, at this moment, doesn't have a sketch. Another way of editing geometry is SetOuterContour(CurveLoop outerContour) - Sets the Curve Loop that defines the geometry of the Analytical Surface element Like for AnalyticalMember, setting the contour for analytical panel will break the connection with other analytical elements. If the user wants to move the corner, and keep the connection, there are other ways for achieving that like ElementTransformUtils.MoveElements.
-   `ISet<ElementId> GetAnalyticalOpeningsIds()` - Returns the Analytical Openings Ids of the Analytical Panel
-   ElementId SketchId - Sketch associated to this Revit element
-   AnalyticalStructuralRole StructuralRole - Structural role assigned to the Analytical Panel

## AnalyticalOpening

AnalyticalOpening is an element which represents an opening in an Analytical Panel.

-   AnalyticalOpening Create(Document doc, CurveLoop curveLoop, ElementId panelId) - Method which creates a new instance of an Analytical Opening within the project
-   CurveLoop GetOuterContour() - Returns the Curve Loop that defines the geometry of the Analytical Surface element
-   bool IsCurveLoopValidForAnalyticalOpening(CurveLoop loop, Document document, ElementId panelId) - Checks if curve loop is valid for Analytical Opening To modify Analytical Opening geometry, you should use SketchEditScope framework. Another way to modify Analytical Opening geometry is: void SetOuterContour(CurveLoop outerContour) - Sets the Curve Loop that defines the geometry of the Analytical Surface element.
-   ElementId PanelId - ElementId of the host Analytical Panel.
-   ElementId SketchId - Sketch associated to this Revit element

## AnalyticalToPhysicalAssociationManager

AnalyticalToPhysicalAssociationManager manages the associations between analytical and physical elements. In the past solution, the elements itself knew about each other and the user had no control over it (the association could not be modified). With this new approach, the association can be edited. Revit supports 1-1 association and elements cannot be part of multiple associations at the same time.

-   AnalyticalToPhysicalAssociationManager GetAnalyticalToPhysicalAssociationManager(Document doc) Returns the AnalyticalToPhysicalAssociationManager for this document
-   void AddAssociation(ElementId analyticalElementId, ElementId physicalElementId) - Adds a new association between an analytical element and a physical element.
-   void RemoveAssociation(ElementId elementId) - This method will remove the association for the element with the given ElementId.
-   ElementId GetAssociatedElementId(ElementId elementId) - Returns id of the element which is associated with the given ElementId.
-   bool HasAssociation(ElementId id) - Verifies if the element has already defined an association

## AnalyticalNodeData

The AnalyticalNodeData class holds information about connection status of analytical nodes.

-   AnalyticalNodeData GetAnalyticalNodeData(Element element) - Returns AnalyticalNodeData associated with this element, if it exists.
-   AnalyticalNodeConnectionStatus GetConnectionStatus() - Returns the Connections Status for an Analytical Node.

## Loads

-   LineLoad.Create(Document document, ElementId hostElemId, XYZ forceVector1, XYZ momentVector1, LineLoadType symbol)
-   LineLoad.Create(Document document, ElementId hostElemId, int curveIndex, XYZ forceVector1, XYZ momentVector1, Structure.LineLoadType symbol)
-   LineLoad.IsValidHostId(Document doc, ElementId hostElemId)
-   AreaLoad.IsValidHostId(Document doc, ElementId hostElemId)
-   AreaLoad.Create(Document doc, ElementId hostElemId, XYZ forceVector1, AreaLoadType symbol)
-   PointLoad.Create(Document doc, ElementId hostElemId, AnalyticalElementSelector selector, XYZ forceVector, XYZ momentVector, AreaLoadType symbol)
-   PointLoad.IsValidHostId(Document doc, ElementId hostElemId)


<!-- ===== END: Help  Analytical Model  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Loads  Autodesk.md ===== -->

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


<!-- ===== END: Help  Loads  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Analysis Link  Autodesk.md ===== -->

---
created: 2026-01-28T21:10:21 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Analysis_Link_html
author: 
---

# Help | Analysis Link | Autodesk

> ## Excerpt
> With Revit, a structural analytical model is automatically generated as you create the physical model. The analytical model is linked to structural analysis applications, and the physical model is automatically updated from the results through the Revit API. Some third-party software developers already provide bi-directional links to their structural analysis applications. These include the following:

---
With Revit, a structural analytical model is automatically generated as you create the physical model. The analytical model is linked to structural analysis applications, and the physical model is automatically updated from the results through the Revit API. Some third-party software developers already provide bi-directional links to their structural analysis applications. These include the following:

-   ADAPT-Builder Suite from ADAPT Corporation ([www.adaptsoft.com/revitstructure/](http://www.adaptsoft.com/revitstructure/))
-   Fastrak and S-Frame from CSC ([www.cscworld.com](http://www.cscworld.com/))
-   ETABS from CSI ([www.csiberkeley.com/](http://www.csiberkeley.com/))
-   RFEM from Dlubal ([www.dlubal.com/en/download/rfem\_revit\_en.pdf](https://www.dlubal.com/en/download/rfem_revit_en.pdf))
-   Advance Design, VisualDesign, Arche, Effel and SuperSTRESS from GRAITEC ([www.graitec.com/En/revit.asp](http://www.graitec.com/En/revit.asp))
-   Scia Engineer from Nemetschek ([www.scia.net/en/software/product-selection/scia-engineer](https://www.scia.net/en/software/product-selection/scia-engineer))
-   GSA from Oasys Software (Arup) ([www.oasys-software.com/products](http://www.oasys-software.com/products))
-   ProDESK from Prokon Software Consultants ([www.prokon.com/](http://www.prokon.com/))
-   RAM Structural System from Bentley ([www.bentley.com/en/products/product-line/structural-analysis-software/ram-structural-system](https://www.bentley.com/en/products/product-line/structural-analysis-software/ram-structural-system))
-   RISA-3D and RISAFloor from RISA Technologies ([www.risatech.com/partner/revit\_structure.asp](http://www.risatech.com/partner/revit_structure.asp))
-   SOFiSTiK Structural Desktop Suite from SOFiSTiK ([www.sofistik.com](http://www.sofistik.com/))
-   SPACE GASS from SPACE GASS ([www.spacegass.com/revit](http://www.spacegass.com/revit))
-   Robot Structural Analysis Professional from Autodesk ([www.autodesk.com/products/robot-structural-analysis](http://www.autodesk.com/products/robot-structural-analysis))

The key to linking Revit to other analysis applications is to set up the mapping relationship between the objects in different object models. That means the difficulty and level of the integration depends on the similarity between the two object models.

For example, during the product design process, design a table with at least the first two columns in the object mapping in the following table: one for the Revit API and the other for the structural analysis application, shown as follows:

**Table 62: Revit and Analysis Application Object Mapping**

<table summary="" id="GUID-0A4C2D6C-725B-4561-A125-7B341BF05C1F__TABLE_D81C0B850B734CE09B6B55768EBBD590"><tbody><tr><td><b>Revit API</b></td><td><b>Analysis Application</b></td><td><b>Import to Revit</b></td></tr><tr><td>StructuralColumn</td><td>Column</td><td>NewStructuralColumn</td></tr><tr><td>Property:</td><td></td><td></td></tr><tr><td>…</td><td></td><td></td></tr><tr><td>Location</td><td></td><td>Read-only;</td></tr><tr><td>Parameter:</td><td></td><td></td></tr><tr><td>…</td><td></td><td></td></tr><tr><td>Analyze as</td><td></td><td>Editable;</td></tr><tr><td>AnalyticalModel:</td><td></td><td></td></tr><tr><td>…</td><td></td><td></td></tr><tr><td>Profile</td><td></td><td>Read-only;</td></tr><tr><td>RigidLink</td><td></td><td>Read-only;</td></tr><tr><td>…</td><td></td><td></td></tr><tr><td>Material:</td><td></td><td></td></tr><tr><td>…</td><td></td><td></td></tr></tbody></table>


<!-- ===== END: Help  Analysis Link  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Analytical Links  Autodesk.md ===== -->

---
created: 2026-01-28T21:10:25 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Analytical_Links_html
author: 
---

# Help | Analytical Links | Autodesk

> ## Excerpt
> An analytical link is an element connecting 2 separate analytical nodes, which has properties such as fixity state. Analytical links can be created automatically by Revit from analytical beams to analytical columns during modeling based on certain rules. And they can also be created manually, both in the Revit UI and using the Revit API.

---
An analytical link is an element connecting 2 separate analytical nodes, which has properties such as fixity state. Analytical links can be created automatically by Revit from analytical beams to analytical columns during modeling based on certain rules. And they can also be created manually, both in the Revit UI and using the Revit API.

In the Revit API, an analytical link is represented by the AnalyticalLink class. Fixity values are available from its associated AnalyticalLinkType.

The example below demonstrates how to read all of the AnalyticalLinks in the document and displays a TaskDialog summarizing the number of automatically generated and manually created AnalyticalLinks.

<table summary="" id="GUID-1A23FBA5-8781-40F7-8B72-36D58DB7BB7F__TABLE_3FB62346E3AE4F038D6A7FB827D45323"><tbody><tr><td><b>Code Region: Reading AnalyticalLinks</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>ReadAnalyticalLinks</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> collectorAnalyticalLinks </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
    collectorAnalyticalLinks</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>AnalyticalLink</span><span>));</span><span>

    </span><span>IEnumerable</span><span>&lt;</span><span>AnalyticalLink</span><span>&gt;</span><span> alinks </span><span>=</span><span> collectorAnalyticalLinks</span><span>.</span><span>ToElements</span><span>().</span><span>Cast</span><span>&lt;</span><span>AnalyticalLink</span><span>&gt;();</span><span>
    </span><span>int</span><span> nAutoGeneratedLinks </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>int</span><span> nManualLinks </span><span>=</span><span> </span><span>0</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>AnalyticalLink</span><span> alink </span><span>in</span><span> alinks</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>alink</span><span>.</span><span>IsAutoGenerated</span><span>()</span><span> </span><span>==</span><span> </span><span>true</span><span>)</span><span>
            nAutoGeneratedLinks</span><span>++;</span><span>
        </span><span>else</span><span>
            nManualLinks</span><span>++;</span><span>
    </span><span>}</span><span>
    </span><span>string</span><span> msg </span><span>=</span><span> </span><span>"Auto-generated AnalyticalLinks: "</span><span> </span><span>+</span><span> nAutoGeneratedLinks</span><span>;</span><span>
    msg </span><span>+=</span><span> </span><span>"\nManually created AnalyticalLinks: "</span><span> </span><span>+</span><span> nManualLinks</span><span>;</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"AnalyticalLinks"</span><span>,</span><span> msg</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The static method AnalyticalLink.Create() creates a new analytical link. Rather than connecting the two elements directly, the connection is created between two Hubs. The Hub class represents a connection between two or more Autodesk Revit Elements.

The following example creates a new analytical link between two selected FamilyInstance objects. It uses a filter to find all Hubs in the model and then the GetHub() method searches the hubs to find one which references the Id of the AnalyticalElement of each FamilyInstance.

<table summary="" id="GUID-1A23FBA5-8781-40F7-8B72-36D58DB7BB7F__TABLE_227CE4F83929460CBB7531D574369930"><tbody><tr><td><b>Code Region: Creating a new AnalyticalLink</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateLink</span><span>(</span><span>Document</span><span> doc</span><span>,</span><span> </span><span>FamilyInstance</span><span> fi1</span><span>,</span><span> </span><span>FamilyInstance</span><span> fi2</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>FilteredElementCollector</span><span> hubCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
    hubCollector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>Hub</span><span>));</span><span>  </span><span>//Get all hubs</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> allHubs </span><span>=</span><span> hubCollector</span><span>.</span><span>ToElements</span><span>();</span><span>
    </span><span>FilteredElementCollector</span><span> linktypeCollector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>doc</span><span>);</span><span>
    linktypeCollector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>AnalyticalLinkType</span><span>));</span><span>
    </span><span>ElementId</span><span> firstLinkType </span><span>=</span><span> linktypeCollector</span><span>.</span><span>ToElementIds</span><span>().</span><span>First</span><span>();</span><span>  </span><span>//Get the first analytical link type.  </span><span>

    </span><span>// Get hub Ids from two selected family instance items</span><span>
    </span><span>ElementId</span><span> startHubId </span><span>=</span><span> </span><span>GetHub</span><span>(</span><span>AnalyticalToPhysicalAssociationManager</span><span>.</span><span>GetAnalyticalToPhysicalAssociationManager</span><span>(</span><span>doc</span><span>)</span><span>
</span><span>.</span><span>GetAssociatedElementId</span><span>(</span><span>fi1</span><span>.</span><span>Id</span><span>),</span><span> allHubs</span><span>);</span><span> 
    </span><span>ElementId</span><span> endHubId </span><span>=</span><span> </span><span>GetHub</span><span>(</span><span>AnalyticalToPhysicalAssociationManager</span><span>.</span><span>GetAnalyticalToPhysicalAssociationManager</span><span>(</span><span>doc</span><span>)</span><span>
</span><span>.</span><span>GetAssociatedElementId</span><span>(</span><span>fi2</span><span>.</span><span>Id</span><span>),</span><span> allHubs</span><span>);</span><span> 
    </span><span>Transaction</span><span> tran </span><span>=</span><span> </span><span>new</span><span> </span><span>Transaction</span><span>(</span><span>doc</span><span>,</span><span> </span><span>"Create Link"</span><span>);</span><span>
    tran</span><span>.</span><span>Start</span><span>();</span><span>
    </span><span>//Create a link between these two hubs.</span><span>
    </span><span>AnalyticalLink</span><span> createdLink </span><span>=</span><span> </span><span>AnalyticalLink</span><span>.</span><span>Create</span><span>(</span><span>doc</span><span>,</span><span> firstLinkType</span><span>,</span><span> startHubId</span><span>,</span><span> endHubId</span><span>);</span><span>  
    tran</span><span>.</span><span>Commit</span><span>();</span><span>
</span><span>}</span><span>

</span><span>//Get the first Hub on a given AnalyticalElement element</span><span>
</span><span>private</span><span> </span><span>ElementId</span><span> </span><span>GetHub</span><span>(</span><span>ElementId</span><span> hostId</span><span>,</span><span> </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> allHubs</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> ehub </span><span>in</span><span> allHubs</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>Hub</span><span> hub </span><span>=</span><span> ehub </span><span>as</span><span> </span><span>Hub</span><span>;</span><span>
        </span><span>ConnectorManager</span><span> manager </span><span>=</span><span> hub</span><span>.</span><span>GetHubConnectorManager</span><span>();</span><span>
        </span><span>ConnectorSet</span><span> connectors </span><span>=</span><span> manager</span><span>.</span><span>Connectors</span><span>;</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Connector</span><span> connector </span><span>in</span><span> connectors</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>ConnectorSet</span><span> refConnectors </span><span>=</span><span> connector</span><span>.</span><span>AllRefs</span><span>;</span><span>
            </span><span>foreach</span><span> </span><span>(</span><span>Connector</span><span> refConnector </span><span>in</span><span> refConnectors</span><span>)</span><span>
            </span><span>{</span><span>
                </span><span>if</span><span> </span><span>(</span><span>refConnector</span><span>.</span><span>Owner</span><span>.</span><span>Id</span><span> </span><span>==</span><span> hostId</span><span>)</span><span>
                </span><span>{</span><span>
                    </span><span>return</span><span> hub</span><span>.</span><span>Id</span><span>;</span><span>
                </span><span>}</span><span>
            </span><span>}</span><span>
        </span><span>}</span><span>
    </span><span>}</span><span>
    </span><span>return</span><span> </span><span>ElementId</span><span>.</span><span>InvalidElementId</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>


<!-- ===== END: Help  Analytical Links  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Steel Fabrication  Autodesk.md ===== -->

---
created: 2026-01-28T21:10:29 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_Steel_Fabrication_html
author: 
---

# Help | Steel Fabrication | Autodesk

> ## Excerpt
> Autodesk.Revit.DB.Steel.SteelElementProperties attaches steel fabrication information to Revit elements.  Elements which can have fabrication information include:

---
## Linking between Revit elements and steel fabrication elements

Autodesk.Revit.DB.Steel.SteelElementProperties attaches steel fabrication information to Revit elements. Elements which can have fabrication information include:

-   FamilyInstance elements (structural beams and columns)
    
-   StructuralConnectionHandler elements
    
-   Specific steel connection elements (bolts, anchors, plates, etc). These connection elements will be of type Element but with categories related to structural connections, for example:
    
    -   OST\_StructConnectionWelds
    -   OST\_StructConnectionHoles
    -   OST\_StructConnectionShearStuds
    -   OST\_StructConnectionBolts
    -   OST\_StructConnectionAnchors
    -   OST\_StructConnectionPlates
-   Some concrete elements (walls, floors, concrete beams) when they are used as input elements to creation of steel connections.
    

Use SteelElementProperties.GetSteelElementProperties() to obtain the properties if they exist.

The properties contain SteelElementProperties.UniqueID which is the id of the object in fabrication terms, and can be used to determine the Steel Core element corresponding to this Revit element, for use with the Advance Steel API.

You can also look up the id for a Revit element using the static method SteelElementProperties.GetFabricationUniqueID().

For Revit elements which do not currently have a fabrication link, it can be added using: SteelElementProperties.AddFabricationInformationForRevitElements()

If you have a fabrication id, you can lookup the corresponding Revit element using: SteelElementProperties.GetReference(). This may return a reference to an element or a subelement.

## Custom steel connections

StructuralConnectionHandler.CreateGenericConnection() creates a custom StructuralConnectionHandler along with its associated StructuralConnectionHandlerType. Input elements should include structural members and steel connection members, and at least one StructuralConnectionHandler representing the generic connection to replace with the new detailed custom connection.

The methods:

-   StructuralConnectionHandlerType.AddElementsToCustomConnection()
-   StructuralConnectionHandlerType.RemoveMainSubelementsFromCustomConnection()

provide support for adding or removing steel connection elements in a custom connection.

The properties:

-   StructuralConnectionHandler.IsCustom
-   StructuralConnectionHandler.IsDetailed
-   StructuralConnectionHandlerType.IsCustom
-   StructuralConnectionHandlerType.IsDetailed

provide read access to information about the structural connection handler elements.


<!-- ===== END: Help  Steel Fabrication  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Site  Autodesk.md ===== -->

---
created: 2026-01-28T21:10:33 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Site_html
author: 
---

# Help | Site | Autodesk

> ## Excerpt
> The Site API is located in the Autodesk.Revit.DB.Architecture namespace.

---
The Site API is located in the Autodesk.Revit.DB.Architecture namespace.

## Creation

-   TopographySurface.Create(Document doc, IList<XYZ> points, IList<PolymeshFacet> facets) creates a topography surface from a list of triangulation facets.
-   TopographySurface Create(Document, IList<XYZ> points) creates a topography surface from a list of points.

### Validation

TopographySurface.IsValidFaceSet(IList<PolymeshFacet> facets, IList<XYZ> points) checks whether the triangulation data is valid.

### Linked Topography

-   TopographyLinkType represents a site file brought into the current Revit model as a link.
-   TopographyLinkType.Reload() reloads the TopographyLinkType from its current location.

## Editing a TopographySurface

To edit a TopographySurface, create an instance of a TopographyEditScope with the constructor for this class. Then call the TopographyEditScope.Start() method to begin editing and complete the editing operation with TopographyEditScope.Commit().


<!-- ===== END: Help  Site  Autodesk.md ===== -->

---

