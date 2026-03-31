[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.RebarShapeFailures Members

---



|  |
| --- |
| [BuiltInFailures RebarShapeFailures Class](7e0a8c39-c873-730e-6ffd-2fc6d6f71f3e.htm)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

Provides a container of all Revit built-in FailureDefinitionId instances.

The  [BuiltInFailures RebarShapeFailures](7e0a8c39-c873-730e-6ffd-2fc6d6f71f3e.htm)  type exposes the following members.

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property Static member | [CircleMultiPlanarShape](ad509efd-ac26-dc5d-54cd-1cb1c28d69ac.htm) | A circle can't be converted to multiplanar shape. |
| Public property Static member | [CircleUnbounded](d3eeab1b-3e4a-7973-5f2f-ac31e9d1045c.htm) | An unbounded circle can only be used to construct a spiral shape. |
| Public property Static member | [CurveOverconstrained](e83009e5-91d5-49d8-cbdc-c5fbbf45df4a.htm) | Segment is overconstrained. It has at least one parameterized dimension that conflicts with another dimension. |
| Public property Static member | [CurvesCollinear](6f433812-1259-e5ba-1f8c-3556f24e2109.htm) | Collinear segments are not allowed in a Rebar Shape definition. |
| Public property Static member | [CurvesUnlooped](d700b4dc-2bc1-beb4-fa23-ea9bf05518e0.htm) | Segments defining the Rebar Shape must be in a continuous loop. |
| Public property Static member | [CurveUnderconstrained](f1b3d8d6-8d52-bac2-bc0a-cfa6463a3ae0.htm) | Segment is underconstrained. It requires additional parameterized dimensions. |
| Public property Static member | [DefaultParamaterValuesIncorrect](3ca04b0b-1f42-6ad2-5bcd-af1c1dd5e58f.htm) | Default parameters have incorrect values. One reason for failure might be an edge length that is too short (it's smaller than bent radius). |
| Public property Static member | [DepthDimensionNotExisted](fd565083-b1f2-57f0-d476-495a7c4b19d3.htm) | Multi-planar shape's depth dimension has been deleted. Please assign a new one to multi-planar depth. |
| Public property Static member | [DiagonalEdgesAreUnderconstrained](1d84e275-3faf-2ead-358b-bb9d21a7521d.htm) | Shape is underconstrained. Please add additional dimension constraints to the shape's diagonal edges. (Diagonal segments with only one dimension constraint are automatically given a second constraint to lie at an angle of exactly 45 degrees, regardless of how they are drawn. The current shape has more than one such segment in sequence, and the resulting constrained edges are co-linear.) |
| Public property Static member | [DimensionLoose](15fedc66-dd33-375f-0ca9-a957fee2847a.htm) | This dimension cannot be used to parameterize the Rebar Shape. |
| Public property Static member | [DimensionWithCommonLengthUnit](010ac28a-d4d0-b299-a464-7c1fba8c0653.htm) | A shape dimension is labelled with a parameter that uses the Common Length unit. |
| Public property Static member | [DimensionWithoutParameter](d36c8b49-6741-c36f-7b50-90e212a35638.htm) | Dimension has no parameter assigned to it. |
| Public property Static member | [FormulaDrivenDimension](af3c3dc4-6100-2a35-0e00-47c6185650f3.htm) | Dimension can't be driven by a formula parameter. |
| Public property Static member | [HooksAndEndTreatmentAtTheSameEnd](62341bf1-5acd-c5a7-0f00-b9e3d7325513.htm) | Cannot add hooks and end treatments at the same end. |
| Public property Static member | [MultiPlanarDepth](1d2db0fa-9f4b-d00b-2413-ae893ac8ded1.htm) | Multi-planar depth of Rebar Shape can't be too small. |
| Public property Static member | [MultipleArcsMustOverlap](19653fbd-43e2-7d9b-7fc5-9a881bf39dfa.htm) | Multiple arcs are supported only if they are concentric and form a circle with an overlap. |
| Public property Static member | [ParameterValueNotDefined](f88641af-047c-6969-6283-b3b9528937e0.htm) | Parameter assigned to the dimension has no value defined. |
| Public property Static member | [PlanarMultiPlanarShape](5ceb005d-c8a9-045a-00bf-b9ef3059a78a.htm) | The current shape is only bent in a single plane. A multi-planar definition is not required. Please redefine the shape on the top plane only. |
| Public property Static member | [ShapeFailure](4d3eba00-9c8b-cd0d-c33b-3ae2145d1eda.htm) | The displayed Rebar Shape is created using a 'Rebar Bar for Preview'. This bar defines the bend radius displayed in the family. Using this preview bar the drawn shape cannot be completed. |
| Public property Static member | [WrongDepthDimensionLabel](6d8b67fa-22eb-2674-3bc8-9eda54a43b8d.htm) | Multi-planar depth dimension label is already used for one of the planar shape parameters. |

# See Also

[BuiltInFailures RebarShapeFailures Class](7e0a8c39-c873-730e-6ffd-2fc6d6f71f3e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)