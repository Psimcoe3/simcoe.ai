[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCategoryOverrides Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Gets graphic overrides for a category in view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public OverrideGraphicSettings GetCategoryOverrides( 	ElementId categoryId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCategoryOverrides ( _ 	categoryId As ElementId _ ) As OverrideGraphicSettings ``` |

 

| Visual C++ |
| --- |
| ``` public: OverrideGraphicSettings^ GetCategoryOverrides( 	ElementId^ categoryId ) ``` |

#### Parameters

categoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Category to be checked.

#### Return Value

Object representing all graphic overrides of the category categoryId in view. A default OverrideGraphicSettings object will be returned if it not previously been set for this view.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The view type does not support Visibility/Graphics Overriddes. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)