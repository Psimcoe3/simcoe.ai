[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### View Property

---



|  |
| --- |
| [Options Class](aa41fc13-9f81-836c-4271-82568ba5d7e8.htm)   [See Also](#seeAlsoToggle) |

The view used for geometry extraction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public View View { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property View As View 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property View^ View { 	View^ get (); 	void set (View^ value); } ``` |

# Remarks

If a view-specific version of an element exists, it will be extracted in the retrieval of geometry. Also, the detail level of the geometry will be taken from the view's detail level.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when setting this property with a    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when setting this property, if DetailLevel is already set. When DetailLevel is set view-specific geometry can't be extracted. |

# See Also

[Options Class](aa41fc13-9f81-836c-4271-82568ba5d7e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)