[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AlignmentStationLabel Class

---



|  |
| --- |
| [Members](c1e852d4-7674-3c96-1330-c4feb39a3a72.htm)   [See Also](#seeAlsoToggle) |

Represents an object which provides access to a specialized Revit annotation element used for labeling  [Alignment](6594712d-3b22-9b08-ab4c-782df88f36d1.htm)  stations.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public class AlignmentStationLabel ``` |

 

| Visual Basic |
| --- |
| ``` Public Class AlignmentStationLabel ``` |

 

| Visual C++ |
| --- |
| ``` public ref class AlignmentStationLabel ``` |

# Remarks

The element is a  [SpotDimension](f3c633ac-1595-cb8d-5c1b-66eb3eefb433.htm)  . The element's category is  [OST\_AlignmentStationLabels](ba1c5b30-242f-5fdc-8ea9-ec3b61e6e722.htm)  or, if in a set of labels,  [OST\_AlignmentStationLabelSets](ba1c5b30-242f-5fdc-8ea9-ec3b61e6e722.htm)  . The element's type is a  [SpotDimensionType](06ffc197-308a-a350-6dd7-6f812e175bb6.htm)  with  [DimensionStyleType](130b0264-615d-610e-38e0-4ce2a8e2aecd.htm)  equal to  [AlignmentStationLabel](130b0264-615d-610e-38e0-4ce2a8e2aecd.htm)  . The element's  [Origin](df8b9dc6-9d36-ac2b-04cf-816d88f039b8.htm)  is a point on the tessellated representation of an alignment. To get the precise point on the alignment's curve, use  [GetPointAtStation(Double)](1b4cc73b-dc00-0439-5480-fd7979b1e106.htm)  with input obtained from  [Station](1558579e-cdee-03ca-58b1-5630fe0fa0c1.htm)  .

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB.Infrastructure AlignmentStationLabel

# See Also

[AlignmentStationLabel Members](c1e852d4-7674-3c96-1330-c4feb39a3a72.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)