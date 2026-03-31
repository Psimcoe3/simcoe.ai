[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReorderRevisionSequence Method

---



|  |
| --- |
| [Revision Class](af882c60-68ae-2e53-5c41-7aa43cfc1df4.htm)   [See Also](#seeAlsoToggle) |

Reorders the sequence of Revisions in the project.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static void ReorderRevisionSequence( 	Document document, 	IList<ElementId> newSequence ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub ReorderRevisionSequence ( _ 	document As Document, _ 	newSequence As IList(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void ReorderRevisionSequence( 	Document^ document,  	IList<ElementId^>^ newSequence ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which the Revision sequence should be reordered.

newSequence
:   Type:  System.Collections.Generic IList   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The new sequence of Revisions.

# Remarks

This method allows the caller to change the sequence of the Revisions within the project by specifying the new sequence. The specified sequence must include every Revision in the project exactly once.

Note that changing the sequence of Revisions can change the SequenceNumber and RevisionNumber of Revisions that have already been issued.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | newSequence does not contain every Revision exactly once. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Revision Class](af882c60-68ae-2e53-5c41-7aa43cfc1df4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)