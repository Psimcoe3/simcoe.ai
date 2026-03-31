[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoutingPreferenceRule Constructor

---



|  |
| --- |
| [RoutingPreferenceRule Class](28dd1a35-5115-c0fb-26e3-7bce14893b89.htm)   [See Also](#seeAlsoToggle) |

Constructs a RoutingPreferenceRule containing a segment or fitting Id (MEPPartId) and description.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public RoutingPreferenceRule( 	ElementId MEPPartId, 	string description ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	MEPPartId As ElementId, _ 	description As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: RoutingPreferenceRule( 	ElementId^ MEPPartId,  	String^ description ) ``` |

#### Parameters

MEPPartId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The Id of the segment or fitting. InvalidElementId may be specified if no MEPPart will be allowed when the conditions satisfy the criteria in this rule.

description
:   Type:  System String    
     The description of the rule.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RoutingPreferenceRule Class](28dd1a35-5115-c0fb-26e3-7bce14893b89.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)