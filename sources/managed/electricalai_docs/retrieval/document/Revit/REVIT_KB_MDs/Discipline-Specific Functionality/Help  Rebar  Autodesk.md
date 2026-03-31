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
