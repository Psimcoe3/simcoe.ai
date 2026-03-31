[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsSameAs Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Compare this fabrication part with the part passed and checks the pattern dimensions and options. A list of fields that can be ignored in the comparison check can be specified.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool IsSameAs( 	FabricationPart part, 	IList<FabricationPartCompareType> ignoreFields ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsSameAs ( _ 	part As FabricationPart, _ 	ignoreFields As IList(Of FabricationPartCompareType) _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsSameAs( 	FabricationPart^ part,  	IList<FabricationPartCompareType>^ ignoreFields ) ``` |

#### Parameters

part
:   Type:  [Autodesk.Revit.DB FabricationPart](c9b86162-c105-696a-a919-49a7a7938cc4.htm)    
     The part to compare this part with.

ignoreFields
:   Type:  System.Collections.Generic IList   [FabricationPartCompareType](af08ec0a-ab0d-2ba4-c6cd-f11c236a6e4d.htm)    
     Array of types of data to ignore from the comparison check.

#### Return Value

Returns true if the fabrication parts are the same.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)