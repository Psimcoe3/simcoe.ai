---
created: 2026-01-28T20:58:34 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_FamilyInstances_html
author: 
---

# Help | FamilyInstances | Autodesk

> ## Excerpt
> FamilyInstance objects include Beams, Braces, Columns, Furniture, Massing, and more. The FamilyInstance object provides more detailed properties so that the family instance type and appearance in the project can be changed.

---
FamilyInstance objects include Beams, Braces, Columns, Furniture, Massing, and more. The FamilyInstance object provides more detailed properties so that the family instance type and appearance in the project can be changed.

Location-related properties show the physical and geometric characteristics of FamilyInstance objects, such as orientation, rotation and location.

#### Orientation

The face orientation or hand orientation can be changed for some FamilyInstance objects. For example, a door can face the outside or the inside of a room or wall and it can be placed with the handle on the left side or the right side. The following table compares door, window, and desk family instances.

**Table 29: Compare Family Instances**

<table summary="" id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__TABLE_371C55EC78FA4B73AB166155DE3B21DF"><tbody><tr><td><b>Boolean Property</b></td><td><b>Door</b></td><td><b>Window (Fixed: 36"w × 72"h)</b></td><td><b>Desk</b></td></tr><tr><td>CanFlipFacing</td><td>True</td><td>True</td><td>False</td></tr><tr><td>CanFlipHand</td><td>True</td><td>False</td><td>False</td></tr></tbody></table>

If CanFlipFacing or CanFlipHand is true, you can call the flipFacing() or flipHand() methods respectively. These methods can change the facing orientation or hand orientation respectively. Otherwise, the methods do nothing and return False.

When changing orientation, remember that some types of windows can change both hand orientation and facing orientation, such as a Casement 3x3 with Trim family.

There are four different facing orientation and hand orientation combinations for doors. See the following picture for the combinations and the corresponding Boolean values are in the following table.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-AC8B1DB7-860B-46D3-A0BD-DBF120980580-low.png)**Figure 44: Doors with different Facing and Hand Orientations**

**Table 30: Different Instances of the Same Type**

<table summary="" id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__TABLE_53EE227C6EAD4D4E8E1EC76AD87D8D6E"><tbody><tr><td><b>Boolean Property</b></td><td><b>Door 1</b></td><td><b>Door 2</b></td><td><b>Door 3</b></td><td><b>Door 4</b></td></tr><tr><td>FacingFlipped</td><td>False</td><td>True</td><td>False</td><td>True</td></tr><tr><td>HandFlipped</td><td>False</td><td>True</td><td>True</td><td>False</td></tr></tbody></table>

#### Orientation - Work Plane

The work plane orientation for a FamilyInstance can be changed, as well. If CanFlipWorkPlane is true, you can set the IsWorkPlaneFlipped property. Attempting to set this property for a FamilyInstance that does not allow the work plane to be flipped will result in an exception.

#### Rotation - Mirrored

The Mirrored property indicates whether the FamilyInstance object has been mirrored.

**Table 31: Door Mirrored Property**

<table summary="" id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__TABLE_836BD5C4044E42CC828DE4947CEE0260"><tbody><tr><td><b>Boolean Property</b></td><td><b>Door 1</b></td><td><b>Door 2</b></td><td><b>Door 3</b></td><td><b>Door 4</b></td></tr><tr><td>Mirrored</td><td>False</td><td>False</td><td>True</td><td>True</td></tr></tbody></table>

In the previous door example, the Mirrored property for Door 1 and Door 2 is False, while for both Door 3 and Door 4 it is True. This is because when you create a door in the Revit project, the default result is either Door 1 or Door 2. To create a door like Door 3 or Door 4, you must flip the Door 1 and Door 2 hand orientation respectively. The flip operation is like a mirror transformation, which is why the Door 3 and Door 4 Mirrored property is True.

For more information about using the Mirror() method in Revit, refer to the [Editing Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_html) chapter.

#### Rotation - CanRotate and rotate()

The family instance Boolean CanRotate property is used to test whether the family instance can be rotated 180 degrees. This depends on the family to which the instance belongs. For example, in the following picture, the CanRotate properties for Window 1 (Casement 3×3 with Trim: 36"×72") and Door 1 (Double-Glass 2: 72"×82") are true, while Window 2 (Fixed: 36"w × 72"h) is false.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-8E93FD79-81F8-4B3D-B09F-9C9A4A1A556C-low.png)**Figure 45: Changes after rotate()**

If CanRotate is true, you can call the family instance rotate() method, which flips the family instance by 180 degrees. Otherwise, the method does nothing and returns False. The previous picture also shows the Window 1 and Door 1 states after executing the rotate() method.

Recall from the [Rotating elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_Rotating_elements_html) section earlier in this document, that family instances (and other elements) can be rotated a user-specified angle usingElementTransformUtils.RotateElement() and ElementTransformUtils.RotateElements().

#### Location

The Location property determines the physical location of an instance in a project. An instance can have a point location or a line location.

The following characteristics apply to Location:

-   A point location is a LocationPoint class object - A footing, a door, or a table has a point location
    
-   A line location is a LocationCurve class object - A beam has a line location.
    
-   They are both subclasses of the Location class.
    

For more information about Location, refer to [Editing Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_html).

### Host and HostFace

Host and HostFace are both FamilyInstance properties.

#### Host

A FamilyInstance object has a Host property that returns its hosting element.

Some FamilyInstance objects do not have host elements, such as Tables and other furniture, so the Host property returns nothing because no host elements are created. However, other objects, such as doors and windows, must have host elements. In this case the Host property returns a wall Element in which the window or the door is located. See the following picture.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-837ECA51-19DE-4B19-A304-A5C26F24EBD0-low.png)**Figure 46: Doors and windows hosted in a wall**

HostFace The HostFace property gets the reference to the host face of the family instance, or if the instance is placed on a work plane, the reference to the geometry face underlying the work plane. This property will return a null reference if the work plane is not referencing other geometry, or if the instance is not hosted on a face or work plane.

### Subcomponent and Supercomponent

The FamilyInstance.GetSubComponentIds() method returns the ElementIds of family instances loaded into that family. When an instance of 'Table-Dining Round w Chairs.rfa' is placed in a project, the ElementIds of the set of chairs are returned by the GetSubComponentIds() method.

The SuperComponent property returns the family instance's parent component. In 'Table-Dining Round w Chairs.rfa', the family instance supercomponent for each nested chair is the instance of 'Table-Dining Round w Chairs.rfa'.

<table summary="" id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__TABLE_5421C731BF84459E860D8DA820244CCA"><tbody><tr><td><b>Code Region 12-1: Getting SubComponents and SuperComponent from FamilyInstance</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetSubAndSuperComponents</span><span>(</span><span>FamilyInstance</span><span> familyInstance</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> subElemSet </span><span>=</span><span> familyInstance</span><span>.</span><span>GetSubComponentIds</span><span>();</span><span>
    </span><span>if</span><span> </span><span>(</span><span>subElemSet </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>string</span><span> subElems </span><span>=</span><span> </span><span>""</span><span>;</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>ElementId</span><span> ee </span><span>in</span><span> subElemSet</span><span>)</span><span>
        </span><span>{</span><span>
            </span><span>FamilyInstance</span><span> f </span><span>=</span><span> familyInstance</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>ee</span><span>)</span><span> </span><span>as</span><span> </span><span>FamilyInstance</span><span>;</span><span>
            subElems </span><span>=</span><span> subElems </span><span>+</span><span> f</span><span>.</span><span>Name</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
        </span><span>}</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"Subcomponent count = "</span><span> </span><span>+</span><span> subElemSet</span><span>.</span><span>Count</span><span> </span><span>+</span><span> </span><span>"\n"</span><span> </span><span>+</span><span> subElems</span><span>);</span><span>
    </span><span>}</span><span>
    </span><span>FamilyInstance</span><span> </span><span>super</span><span> </span><span>=</span><span> familyInstance</span><span>.</span><span>SuperComponent</span><span> </span><span>as</span><span> </span><span>FamilyInstance</span><span>;</span><span>
    </span><span>if</span><span> </span><span>(</span><span>super</span><span> </span><span>!=</span><span> </span><span>null</span><span>)</span><span>
    </span><span>{</span><span>
        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>"SUPER component: "</span><span> </span><span>+</span><span> </span><span>super</span><span>.</span><span>Name</span><span>);</span><span>
    </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Geometry

Sometimes the geometry of a FamilyInstance object is modified by joins, cuts, coping, extensions, or other post-processing that occurs in Revit. The FamilyInstance.HasModifiedGeometry() method identifies if the geometry of this FamilyInstance has been modified from the automatically generated default. The GetOriginalGeometry() method will return the original geometry of the instance prior to any modifications that may have occurred. To get the current geometry of the instance, use the Geometry property inherited from the Element class.

### Spatial Element Calculation Points

The FamilyInstance has several members for reading the information about spatial calculation point(s) directly from the family instance. The HasSpatialElementCalculationPoint property identifies if this instance has a single SpatialElementCalculationPoint used as the search point for Revit to identify if the instance is inside a room or space. If true, the GetSpatialElementCalculationPoint() method will return the location of the calculation point for this instance as an XYZ point.

The HasSpatialElementFromToCalculationPoints property identifies if this instance has a pair of SpatialElementCalculationPoints used as the search points for Revit to identify if the instance lies between up to two rooms or spaces. The points determine which room or space is considered the "from" and which is considered the "to" for a family instance which connects two rooms or spaces, such as a door or window. When this property is true, the GetSpatialElementFromToCalculationPoints() method returns the locations for the calculation points for this instance as a list of XYZ points.

### Other Properties

The properties in this section are specific to the architectural and structural engineering features of Revit. They are covered thoroughly in their respective chapters.

#### Room Information

FamilyInstance properties include Room, FromRoom, and ToRoom. For more information about Room, refer to [Architecture](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Architecture_html).

#### Space Information

FamilyInstance has a Space property for identifying the space that holds an instance in MEP.

#### Structural Analytical Model

The GetAnalyticalModel() method retrieves the family instance structural analytical model.

For more information about AnalyticalModel refer to [Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html).

### Creating FamilyInstance Objects

Typically a FamilyInstance object is created using one of the twelve overload methods of Autodesk.Revit.Creation.Document called NewFamilyInstance(). The choice of which overload to use depends not only on the category of the instance, but also other characteristics of the placement like whether it should be hosted, placed relative to a reference level, or placed directly on a particular face. The details are included in Table 32 - Options for creating instance with NewFamilyInstance() below.

Some FamilyInstance objects require more than one location to be created. In these cases, it is more appropriate to use the more detailed creation method provided by this object (see Table 33 - Options for creating instances with other methods below). If the instance is not created, an exception is thrown. The type/symbol used must be loaded into the project before the method is called.

All overloads for NewFamilyInstance() check to ensure that the input FamilySymbol is active (FamilySymbol.IsActive). If the input FamilySymbol is inactive, the method will throw an ArgumentException. Symbols that are not used in the document may be deactivated to conserve memory and regeneration time. When the symbol is inactive, its geometry is empty and cannot be accessed. In order to access the geometry of a symbol that is not active in the document, the symbol should first be activated by calling FamilySymbol.Activate().

**Table 32 - Options for creating instance with NewFamilyInstance()**

| Category | NewFamilyInstance() parameters | Comments |
| --- | --- | --- |
| Air Terminals
Boundary Conditions

Casework

Communication Devices

Data Devices

Electrical Equipment

Electrical Fixtures

Entourage

Fire Alarm Devices

Furniture

Furniture Systems

Generic Models

Lighting Devices

Lighting Fixtures

Mass

Mechanical Equipment

Nurse Call Devices

Parking

Planting

Plumbing Fixtures

Security Devices

Site

Specialty Equipment

Sprinklers

Structural Connections

Structural Foundations

Structural Stiffeners

Telephone Devices

 | XYZ, FamilySymbol, StructuralType | Creates the instance in an arbitrary location without reference to a level or host element. |
| XYZ, FamilySymbol, Element, StructuralType | If it is to be hosted on a wall, floor or ceiling |
| XYZ, FamilySymbol, XYZ, Element, StructuralType | If it is to be hosted on a wall, floor, or ceiling, and needs to be oriented in a non-default direction |
| XYZ, FamilySymbol, Element, Level, StructuralType | If it is to be hosted on a wall, floor or ceiling and associated to a reference level |
| XYZ, FamilySymbol, Level, StructuralType | If it is to be associated to a reference level |
| Face, XYZ, XYZ, FamilySymbol | If it is face-based and needs to be oriented in a non-default direction |
| Reference, XYZ, XYZ, FamilySymbol | If it is face-based and needs to be oriented in a non-default direction, accepts a reference to a face rather than a Face |
| Face, Line, FamilySymbol | If it is face-based and linear |
| Reference, Line, FamilySymbol | If it is face-based and linear, but accepts a reference to a face, rather than a Face |
| Columns

Structural Columns

 | XYZ, FamilySymbol, Level, StructuralType | Creates the column so that its base lies on the reference level. The column will extend to the next available level in the model, or will extend the default column height if there are no suitable levels above the reference level. |
| Doors

Windows

 | XYZ, FamilySymbol, Element, StructuralType | Doors and windows must be hosted by a wall. Use this method if they can be placed with the default orientation. |
| XYZ, FamilySymbol, XYZ, Element, StructuralType | If the created instance needs to be oriented in a non-default direction |
| XYZ, FamilySymbol, Element, Level, StructuralType | If the instance needs to be associated to a reference level |
| Structural Framing (Beams, Braces) | Curve, FamilySymbol, Level, StructuralType | Creates a level based brace or beam given its curve. This is the recommended method to create Beams and Braces |
| XYZ, FamilySymbol, StructuralType | Creates instance in an arbitrary location<sub id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__GUID-B882C985-E755-421D-8E90-11D3A7A18E08">1</sub> |
| XYZ, FamilySymbol, Element, Level, StructuralType | If it is hosted on an element (floor etc.) and associated to a reference level<sub id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__GUID-C97A8C8D-95F2-409B-BC49-56A6BC147C05">1</sub> |
| XYZ, FamilySymbol, Level, StructuralType | If it is associated to a reference level<sub id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__GUID-67E647D0-AE0D-4DCD-89D0-650BE40053C4">1</sub> |
| XYZ, FamilySymbol, Element, StructuralType | If it is hosted on an element (floor etc.)<sub id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__GUID-4EC2265A-86DF-4E48-BA74-22B54662042C">1</sub> |
| Detail Component | Line, FamilySymbol, View | Applies only to 2D family line based detail symbols |
| Generic Annotations | XYZ, FamilySymbol, View | Applies only to 2D family symbols |

<sub id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__GUID-ACE8C585-6799-491F-8D93-A417B8E8CD1C">1</sub> The structural instance will be of zero-length after creation. Extend it by setting its curve (FamilyInstance.Location as LocationCurve) using LocationCurve.Curve property.

You can simplify your code and improve performance by creating more than one family instance at a time using Document.NewFamilyInstances(). This method has a single parameter, which is a list of FamilyInstanceCreationData objects describing the family instances to create.

<table summary="" id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__TABLE_9699E0DCC4A34998A166B3D7E492F468"><tbody><tr><td><b>Code Region 12-2: Batch creating family instances</b></td></tr><tr><td><pre><code><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> </span><span>BatchCreateColumns</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>Level</span><span> level</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>List</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Creation</span><span>.</span><span>FamilyInstanceCreationData</span><span>&gt;</span><span> fiCreationDatas </span><span>=</span><span> </span><span>new</span><span> </span><span>List</span><span>&lt;</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Creation</span><span>.</span><span>FamilyInstanceCreationData</span><span>&gt;();</span><span>

        </span><span>ICollection</span><span>&lt;</span><span>ElementId</span><span>&gt;</span><span> elementSet </span><span>=</span><span> </span><span>null</span><span>;</span><span>

        </span><span>//Try to get a FamilySymbol</span><span>
        </span><span>FamilySymbol</span><span> familySymbol </span><span>=</span><span> </span><span>null</span><span>;</span><span>
        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span> collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FamilySymbol</span><span>)).</span><span>ToElements</span><span>();</span><span>
        </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> e </span><span>in</span><span> collection</span><span>)</span><span>
        </span><span>{</span><span>
                familySymbol </span><span>=</span><span> e </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> familySymbol</span><span>.</span><span>Category</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>"Structural Columns"</span><span> </span><span>==</span><span> familySymbol</span><span>.</span><span>Category</span><span>.</span><span>Name</span><span>)</span><span>
                        </span><span>{</span><span>
                                </span><span>break</span><span>;</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>

        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> familySymbol</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>//Create 10 FamilyInstanceCreationData items for batch creation </span><span>
                </span><span>for</span><span> </span><span>(</span><span>int</span><span> i </span><span>=</span><span> </span><span>1</span><span>;</span><span> i </span><span>&lt;</span><span> </span><span>11</span><span>;</span><span> i</span><span>++)</span><span>
                </span><span>{</span><span>
                        XYZ location </span><span>=</span><span> </span><span>new</span><span> XYZ</span><span>(</span><span>i </span><span>*</span><span> </span><span>10</span><span>,</span><span> </span><span>100</span><span>,</span><span> </span><span>0</span><span>);</span><span>
                        </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Creation</span><span>.</span><span>FamilyInstanceCreationData</span><span> fiCreationData </span><span>=</span><span> </span><span>new</span><span> </span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>Creation</span><span>.</span><span>FamilyInstanceCreationData</span><span>(</span><span>location</span><span>,</span><span> familySymbol</span><span>,</span><span> level</span><span>,</span><span> 
                                        </span><span>StructuralType</span><span>.</span><span>Column</span><span>);</span><span>
                        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> fiCreationData</span><span>)</span><span>
                        </span><span>{</span><span>
                                fiCreationDatas</span><span>.</span><span>Add</span><span>(</span><span>fiCreationData</span><span>);</span><span>
                        </span><span>}</span><span>
                </span><span>}</span><span>

                </span><span>if</span><span> </span><span>(</span><span>fiCreationDatas</span><span>.</span><span>Count</span><span> </span><span>&gt;</span><span> </span><span>0</span><span>)</span><span>
        </span><span>{</span><span>
                        </span><span>// Create Columns</span><span>
            elementSet </span><span>=</span><span> document</span><span>.</span><span>Create</span><span>.</span><span>NewFamilyInstances2</span><span>(</span><span>fiCreationDatas</span><span>);</span><span>
        </span><span>}</span><span>
                </span><span>else</span><span>
                </span><span>{</span><span>
                </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Batch creation failed."</span><span>);</span><span>
                </span><span>}</span><span>
    </span><span>}</span><span>
        </span><span>else</span><span>
        </span><span>{</span><span>
                </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"No column types found."</span><span>);</span><span>
        </span><span>}</span><span>

        </span><span>return</span><span> elementSet</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Instances of some family types are better created through methods other than Autodesk.Revit.Creation.Document.NewFamilyInstance(). These are listed in the table below.

**Table 33 - Options for creating instances with other methods**

<table summary="" id="GUID-C7E4C845-C386-4B7B-BDA1-5D2BE7A5C2D8__TABLE_587C92BF32B044B5846AD0FD32897503"><tbody><tr><td><b>Category</b></td><td><b>Creation method</b></td><td><b>Comments</b></td></tr><tr><td>Air Terminal Tags<p>Area Load Tags</p><p>Area Tags</p><p>Casework Tags</p><p>Ceiling Tags</p><p>Communication Device Tags</p><p>Curtain Panel Tags</p><p>Data Device Tags</p><p>Detail Item Tags</p><p>Door Tags</p><p>Duct Accessory Tags</p><p>Duct Fitting Tags</p><p>Duct Tags</p><p>Electrical Equipment Tags</p><p>Electrical Fixture Tags</p><p>Fire Alarm Device Tags</p><p>Flex Duct Tags</p><p>Flex Pipe Tags</p><p>Floor Tags</p><p>Furniture System Tags</p><p>Furniture Tags</p><p>Generic Model Tags</p><p>Internal Area Load Tags</p><p>Internal Line Load Tags</p><p>Internal Point Load Tags</p><p>Keynote Tags</p><p>Lighting Device Tags</p><p>Lighting Fixture Tags</p><p>Line Load Tags</p><p>Mass Floor Tags</p><p>Mass Tags</p><p>Mechanical Equipment Tags</p><p>Nurse Call Device Tags</p><p>Parking Tags</p><p>Pipe Accessory Tags</p><p>Pipe Fitting Tags</p><p>Pipe Tags</p><p>Planting Tags</p><p>Plumbing Fixture Tags</p><p>Point Load Tags</p><p>Property Line Segment Tags</p><p>Property Tags</p><p>Railing Tags</p><p>Revision Cloud Tags</p><p>Roof Tags</p><p>Room Tags</p><p>Security Device Tags</p><p>Site Tags</p><p>Space Tags</p><p>Specialty Equipment Tags</p><p>Spinkler Tags</p><p>Stair Tags</p><p>Structural Area Reinforcement Tags</p><p>Structural Beam System Tags</p><p>Structural Column Tags</p><p>Structural Connection Tags</p><p>Structural Foundation Tags</p><p>Structural Framing Tags</p><p>Structural Path Reinforcement Tags</p><p>Structural Rebar Tags</p><p>Structural Stiffener Tags</p><p>Structural Truss Tags</p><p>Telephone Device Tags</p><p>Wall Tags</p><p>Window Tags</p><p>Wire Tag</p><p>Zone Tags</p></td><td>IndependentTag.Create(Document, ElementId, Reference, Boolean, TagMode, TagOrientation, XYZ)</td><td>TagMode should be TM_ADDBY_CATEGORY and there should be a related tag family loaded when try to create a tag, otherwise exception will be thrown</td></tr><tr><td>Material Tags</td><td>IndependentTag.Create(Document, ElementId, Reference, Boolean, TagMode, TagOrientation, XYZ)</td><td>TagMode should be TM_ADDBY_MATERIAL and there should be a material tag family loaded, otherwise exception will be thrown</td></tr><tr><td>Multi-Category Tags</td><td>IndependentTag.Create(Document, ElementId, Reference, Boolean, TagMode, TagOrientation, XYZ)</td><td>TagMode should be TM_ADDBY_MULTICATEGORY, and there should be a multi-category tag family loaded, otherwise exception will be thrown</td></tr><tr><td>Title Blocks</td><td>ViewSheet.Create(Document, ElementId)</td><td>The titleblock will be added to the newly created sheet.</td></tr></tbody></table>

Families and family symbols are loaded using the Document.LoadFamily() or Document.LoadFamilySymbol() methods. Some families, such as Beams, have more than one endpoint and are inserted in the same way as a single point instance. Once the linear family instances are inserted, their endpoints can be changed using the Element.Location property. For more information, refer to [Code Samples](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_Code_Samples_html).
