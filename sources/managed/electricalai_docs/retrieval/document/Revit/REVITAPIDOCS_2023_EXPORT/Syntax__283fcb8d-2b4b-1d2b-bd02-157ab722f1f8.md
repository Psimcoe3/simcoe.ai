[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FindMergeableClusters Method

---



|  |
| --- |
| [PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)   [See Also](#seeAlsoToggle) |

Segregates a set of elements into subsets which are valid for merge.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static IList<ICollection<ElementId>> FindMergeableClusters( 	Document doc, 	ICollection<ElementId> partIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function FindMergeableClusters ( _ 	doc As Document, _ 	partIds As ICollection(Of ElementId) _ ) As IList(Of ICollection(Of ElementId)) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<ICollection<ElementId^>^>^ FindMergeableClusters( 	Document^ doc,  	ICollection<ElementId^>^ partIds ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

partIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     A set of element ids.

#### Return Value

An array of clusters such that all the elements in a single cluster are valid for merge. Each cluster will be maximal in that appending any of the other Parts specified as input will result in a collection that is not valid for merge.

# Remarks

Element ids in the input set that do not correspond to Part elements will be ignored, as will element ids corresponding to Part elements that already have associated parts.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)