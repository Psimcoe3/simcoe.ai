[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Point Property

---



|  |
| --- |
| [ScheduleSheetInstance Class](68db8e46-90de-6b54-3dae-598957d94201.htm)   [See Also](#seeAlsoToggle) |

Location on the sheet where the ScheduleInstance is placed (in sheet coordinates).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public XYZ Point { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Point As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ Point { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: This operation is prohibited for ScheduleInstances associated with revision schedules in titleblocks. |

# See Also

[ScheduleSheetInstance Class](68db8e46-90de-6b54-3dae-598957d94201.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)