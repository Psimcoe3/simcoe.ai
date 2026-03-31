[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReorderParameters Method

---



|  |
| --- |
| [FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)   [See Also](#seeAlsoToggle) |

Reorders the family parameters by the specified parameters order.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void ReorderParameters( 	IList<FamilyParameter> parameters ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ReorderParameters ( _ 	parameters As IList(Of FamilyParameter) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ReorderParameters( 	IList<FamilyParameter^>^ parameters ) ``` |

#### Parameters

parameters
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [FamilyParameter](6175e974-870e-7fbc-3df7-46105f937a6e.htm)    
     The new parameters order for the family. The contents of this collection should consist of exactly the same parameters returned by the GetParameters() method. This will include invisible parameters; they can be reordered but this will have no effect when viewing the parameters in the Revit UI.

# Remarks

Reordering the parameters only affects visible parameters within the same parameter group.

Parameters that belong to different groups will remain separated, and the groups' order will not be affected.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when argument is    a null reference (  Nothing  in Visual Basic)  or empty. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the input parameters collection does not contain the same parameters as those returned by GetParameters(). |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when this family is a Rebar Shape family which doesn't support parameters reorder. |

# See Also

[FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)