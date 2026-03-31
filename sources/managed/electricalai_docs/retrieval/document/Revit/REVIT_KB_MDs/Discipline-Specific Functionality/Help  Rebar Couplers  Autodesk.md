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
