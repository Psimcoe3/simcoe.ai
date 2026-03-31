[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### KeyScheduleParameterName Property

---



|  |
| --- |
| [ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)   [See Also](#seeAlsoToggle) |

In a key schedule, the name of the parameter for choosing one of the keys.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public string KeyScheduleParameterName { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property KeyScheduleParameterName As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ KeyScheduleParameterName { 	String^ get (); 	void set (String^ value); } ``` |

#### Field Value

The name of the key schedule parameter.

# Remarks

When a key schedule is created, elements of the schedule's category receive a new parameter for choosing one of the keys defined in the key schedule. This is the name of that parameter.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This ViewSchedule is not key schedule. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | When setting this property: The document containing this ViewSchedule is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- When setting this property: The document containing this ViewSchedule is being loaded, or is in the midst of another sensitive process. -or- When setting this property: This ViewSchedule is an internal element, such as a component of a loaded family or a group type. -or- When setting this property: The document containing this ViewSchedule is in Group Edit Mode, Sketch Edit Mode, or Paste Mode, and the element is not a member of the group, sketch, or clipboard. -or- When setting this property: This ViewSchedule is a member of a group or sketch, and the document is not currently editing the group or sketch. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | When setting this property: The document containing this ViewSchedule has no open transaction. |

# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)