[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarCouplerError Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Error states for the Rebar Coupler

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public enum RebarCouplerError ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration RebarCouplerError ``` |

 

| Visual C++ |
| --- |
| ``` public enum class RebarCouplerError ``` |

# Members

| Member name | Description |
| --- | --- |
| ValidationSuccessfuly | Bars can be coupled |
| IncorrectInputData | Cannot place rebar coupler. |
| DifferentLayout | The rebar sets have different numbers of bars. |
| BarsNotTouching | The selected ends of the bars are too far apart. |
| IncorrectEndTreatmentHook | The coupler cannot be placed at an end that already has a hook. |
| IncorrectEndTreatmentCoupler | The coupler cannot be placed at an end that already has a coupler. |
| BarSegementsAreNotParallel | The selected legs are not aligned. |
| BarSegmentsAreNotOnSameLine | The selected legs are not aligned. |
| InconsistentShape | One of the selected bars has an incorrect shape. |
| InvalidDiameter | The selected coupler type cannot be applied to the selected bar size(s). |
| CurvesOtherThanLine | Cannot place rebar couplers on circular legs. |
| BarSegmentSmallerThanEngagement | The selected leg is shorter than the bar engagement. |
| VaryingDistanceBetweenDistributionsBars | All the bars from the selected sets, which need to be connected, must be separated by the same distance. |
| ArcsHaveDifferentRadii | Cannot place rebar couplers on arcs with different radii. |
| ArcsHaveDifferentCenters | Cannot place rebar couplers on arcs with different centers. |
| ArcToStraightSegment | Cannot connect by coupler a straight segment with an arc segment. |

# See Also

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)