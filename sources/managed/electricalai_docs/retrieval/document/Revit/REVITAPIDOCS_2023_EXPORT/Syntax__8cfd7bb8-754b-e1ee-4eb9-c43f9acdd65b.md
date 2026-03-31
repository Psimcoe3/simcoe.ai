[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SharesSettings Property

---



|  |
| --- |
| [SunAndShadowSettings Class](d616614b-a2ed-b0d0-4f11-f0a0b54a22e5.htm)   [See Also](#seeAlsoToggle) |

Identifies whether settings are shared globally.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool SharesSettings { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SharesSettings As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool SharesSettings { 	bool get (); 	void set (bool value); } ``` |

# Remarks

Identifies whether the per-view SunAndShadowSettings element shares global settings. Global settings are a special case that allows multiple views to be associated together in order that a change in one view affects that same change in other views. There cannot be multiple such groups, and a SunAndShadowSettings element is either a global setting or not.

# See Also

[SunAndShadowSettings Class](d616614b-a2ed-b0d0-4f11-f0a0b54a22e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)