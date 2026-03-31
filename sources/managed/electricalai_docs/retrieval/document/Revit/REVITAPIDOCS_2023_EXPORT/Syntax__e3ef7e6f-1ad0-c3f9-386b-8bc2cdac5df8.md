[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ImageRowHeight Property

---



|  |
| --- |
| [ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)   [See Also](#seeAlsoToggle) |

Defines the image row height in the schedule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public double ImageRowHeight { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ImageRowHeight As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ImageRowHeight { 	double get (); 	void set (double value); } ``` |

#### Field Value

The row height for any rows containing images in the schedule. The value is 0.0 by default if not customized.

# Remarks

If there is at least one image field in the schedule, then setting this property will force all rows containing images to be resized to the indicated height value (when viewed as a ScheduleSheetInstance on a ViewSheet). Setting this property will have no effect if HasImageField returns false.

This height will be maintained until the user or application restores the original image sizes (in API:  [RestoreImageSize](e9c47953-6070-46ac-5d24-cef0a9cd5b51.htm)  ).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for imageRowHeight must be greater than 0 and no more than 30000 feet. |

# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)