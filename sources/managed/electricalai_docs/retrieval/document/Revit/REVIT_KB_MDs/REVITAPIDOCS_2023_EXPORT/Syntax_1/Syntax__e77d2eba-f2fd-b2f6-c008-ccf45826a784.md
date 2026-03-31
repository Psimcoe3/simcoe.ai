[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValid Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Checks for errors or inconsistencies in the data in this CompoundStructure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsValid( 	Document doc, 	out IDictionary<int, CompoundStructureError> errMap, 	out IDictionary<int, int> twoLayerErrorsMap ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValid ( _ 	doc As Document, _ 	<OutAttribute> ByRef errMap As IDictionary(Of Integer, CompoundStructureError), _ 	<OutAttribute> ByRef twoLayerErrorsMap As IDictionary(Of Integer, Integer) _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValid( 	Document^ doc,  	[OutAttribute] IDictionary<int, CompoundStructureError>^% errMap,  	[OutAttribute] IDictionary<int, int>^% twoLayerErrorsMap ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Access to the document in which the CompoundStructure will be used.

errMap
:   Type:  System.Collections.Generic IDictionary   Int32  ,  [CompoundStructureError](8e8457e0-84c4-ccb1-114c-fa25a6d37fed.htm)   %    
     This map will associate each problematic layer index to a value in CompoundStructureError. General structure errors are reported as associated to layer index -1.

twoLayerErrorsMap
:   Type:  System.Collections.Generic IDictionary   Int32  ,  Int32   %    
     The map is associated to a check run only for vertically Compound Structures. Essentially the Compound Structure is sliced at representative heights. It looks at the region from exterior to interior, and requires that the assigned layer indices do not decrease. If they do, an entry is generated for this map. The first entry is the last valid layer index encountered. The second entry is a region id whose assigned layer index is too small: it should be at least as large as the first entry.

#### Return Value

True if the compound structure is valid for the document, false otherwise.

# Remarks

This check is run before the CompoundStructure may be assigned to a particular ElementType.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)