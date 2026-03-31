[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UnhideElements Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Sets the elements to be shown in the given view if they are currently hidden.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void UnhideElements( 	ICollection<ElementId> elementIdSet ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub UnhideElements ( _ 	elementIdSet As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void UnhideElements( 	ICollection<ElementId^>^ elementIdSet ) ``` |

#### Parameters

elementIdSet
:   Type:  [System.Collections.Generic ICollection](http://msdn2.microsoft.com/en-us/library/92t2ye13)   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     A set of ElementIds to be unhidden.

# Remarks

This change is permanent until the elements are hidden again. All elements in the set must be currently hidden. An application can check this with  [IsHidden(View)](2c3d4123-fded-cd5f-ed0d-12b1e1a3ce42.htm)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when argument is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the set of elements to be unhidden is empty or one of the elements can not be unhidden. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when document regeneration failed. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)