[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Parse Method

---



|  |
| --- |
| [ElementId Class](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)   [See Also](#seeAlsoToggle) |

Parse the string representation of the id into a corresponding ElementId.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public static ElementId Parse( 	string idStr ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Parse ( _ 	idStr As String _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ Parse( 	String^ idStr ) ``` |

#### Parameters

idStr
:   Type:  System String    
     The string representation of the id to return.

#### Return Value

ElementId string represented.

# Remarks

If the string represents  [!:Autodesk::Revit::DB::Element::InvalidElementId]  it will be returned.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the string cannot be parsed into an ElementId. |

# See Also

[ElementId Class](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)