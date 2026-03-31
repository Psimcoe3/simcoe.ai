[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RevisionCloud Class

---



|  |
| --- |
| [Members](17ea7caf-6857-ef7b-7611-9e6cf9cd2708.htm)   [See Also](#seeAlsoToggle) |

A RevisionCloud is a graphical "cloud" that can be displayed on a view or sheet to indicate where revisions in the model have occurred.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public class RevisionCloud : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RevisionCloud _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RevisionCloud : public Element ``` |

# Remarks

RevisionClouds are view specific and can be created in most graphical views, except 3D. Unlike most Elements, RevisionClouds may be added directly to a ViewSheet. Each RevisionCloud is associated with one Revision.

When a RevisionCloud is visible on a ViewSheet (either because it is directly placed on that ViewSheet or because it is visible in a View placed on the ViewSheet), any revision schedules displayed on the ViewSheet will automatically include the Revision associated with the RevisionCloud.

Note also that when a RevisionCloud is created in a ViewLegend, it is treated as a legend representation of what a RevisionCloud looks like rather than as an actual indication of a change to the model. As a result, RevisionClouds in ViewLegends will not affect the contents of revision schedules.

RevisionClouds are created from a collection of sketched curves. Each curve will have a series of "cloud bumps" drawn along it to form the appearance of a cloud. There is no requirement that the curves form closed loops.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB RevisionCloud

# See Also

[RevisionCloud Members](17ea7caf-6857-ef7b-7611-9e6cf9cd2708.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)