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
