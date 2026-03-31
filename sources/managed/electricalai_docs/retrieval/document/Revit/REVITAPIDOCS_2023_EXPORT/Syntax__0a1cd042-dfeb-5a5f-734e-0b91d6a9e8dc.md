[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetHookOffsetLength Method

---



|  |
| --- |
| [RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)   [See Also](#seeAlsoToggle) |

Identifies the hook offset length for a hook type

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public double GetHookOffsetLength( 	ElementId hookId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetHookOffsetLength ( _ 	hookId As ElementId _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetHookOffsetLength( 	ElementId^ hookId ) ``` |

#### Parameters

hookId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     id of the hook type

#### Return Value

The hook offset length for a hook type

# Remarks

If the AutoCalcHookLengths property is turned off, the default hook offset length will be returned

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | the rebar hook type id hookId is not valid -or- the hook specified by id hookId doesn't have valid offset length -or- The element hookId does not exist in the document containing this RebarBarType -or- the hook specified by id hookId doesn't have valid default offset length |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document containing this RebarBarType is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The element is a member of a loaded family. -or- The element is a member of a group type that is not being edited. -or- hookId is a member of a loaded family. -or- hookId is a member of a group type that is not being edited. |

# See Also

[RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)