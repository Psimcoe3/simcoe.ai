[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddSize Method

---



|  |
| --- |
| [DuctSizeSettings Class](68c1d227-424d-36da-0e5a-3f3e51e7f939.htm)   [See Also](#seeAlsoToggle) |

Inserts a new MEPSize in to the duct size settings. The duct shape determines the location of the new size in the size table.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void AddSize( 	DuctShape shape, 	MEPSize sizeInfo ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddSize ( _ 	shape As DuctShape, _ 	sizeInfo As MEPSize _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddSize( 	DuctShape shape,  	MEPSize^ sizeInfo ) ``` |

#### Parameters

shape
:   Type:  [Autodesk.Revit.DB.Mechanical DuctShape](3b512e73-a626-b0a0-42b7-a8bd0f6e2ca9.htm)    
     The shape of duct.

sizeInfo
:   Type:  [Autodesk.Revit.DB MEPSize](475cd9a4-e87a-6f9f-7e75-c079ac004166.htm)    
     The new MEPSize to be added.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Throws if there is no size set determined by the duct shape or there is already the same size in the size set determined by the duct shape. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Throws if the function is called during iterating the size set. |

# See Also

[DuctSizeSettings Class](68c1d227-424d-36da-0e5a-3f3e51e7f939.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)