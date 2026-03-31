[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RepeatElements Method

---



|  |
| --- |
| [ComponentRepeater Class](27dbc5bd-40e7-c044-11e6-7053adf92c6f.htm)   [See Also](#seeAlsoToggle) |

Repeats a set of adaptive component hosted on one or more repeating references.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static IList<ComponentRepeater> RepeatElements( 	Document document, 	ICollection<ElementId> elementIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function RepeatElements ( _ 	document As Document, _ 	elementIds As ICollection(Of ElementId) _ ) As IList(Of ComponentRepeater) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<ComponentRepeater^>^ RepeatElements( 	Document^ document,  	ICollection<ElementId^>^ elementIds ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document that contains the elements.

elementIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The set of adaptive components used as an input pattern for the repeating operation.

#### Return Value

One or more component repeater objects representing the result pattern of the repeating operation.

# Remarks

All elements must be adaptive family instances and have no shape handles. At least one placement point must be hosted on a 1D or 2D repeating reference. All other placement points can be hosted on a 0D, 1D or 2D repeating reference, or must be unhosted. Use  [CanElementBeRepeated(Document, ElementId)](85030abd-7476-91fc-a67b-50dd8bcf9697.htm)  to test whether an element meets these conditions.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The document does not allow creation of a component repeater. -or- The given element id set is empty. -or- One or more elements in elementIds do not exist in the document. -or- Not all given elements can be repeated. All elements must be adaptive family instances, have no shape handles, and have at least one placement point hosted on a 1D or 2D repeating reference. The remaining placement points must be either unhosted or hosted on another repeating reference. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[ComponentRepeater Class](27dbc5bd-40e7-c044-11e6-7053adf92c6f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)