[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### End Property

---



|  |
| --- |
| [Leader Class](66228564-d8b8-fc81-454c-e175528f7188.htm)   [See Also](#seeAlsoToggle) |

End point of the Leader.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ End { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property End As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ End { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Remarks

The End point is the leader's end that points to the object being annotated.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: A valid point must not be father then 10 miles (approx. 16 km) from the origin. -or- When setting this property: The leader's End point may not be placed at the current position of the Anchor or Elbow point. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The leader is not currently owned by a valid element. A probable reason for that could be if the element has been independently deleted, or the leader has never been properly initialized. |

# See Also

[Leader Class](66228564-d8b8-fc81-454c-e175528f7188.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)