[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsTrajectorySegmentationEnabled Property

---



|  |
| --- |
| [Sweep Class](ed383459-badd-2323-4f73-0d94fd76ce0f.htm)   [See Also](#seeAlsoToggle) |

The trajectory segmentation option for the sweep.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsTrajectorySegmentationEnabled { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IsTrajectorySegmentationEnabled As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsTrajectorySegmentationEnabled { 	bool get (); 	void set (bool value); } ``` |

# Remarks

This property is used to retrieve/set the trajectory segmentation state of the sweep. if return is true, means user can control the MaxSegmentAngle, otherwise is disable.

# See Also

[Sweep Class](ed383459-badd-2323-4f73-0d94fd76ce0f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)