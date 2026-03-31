[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Cities Property

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Returns a set of all the known city locations within Revit.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public CitySet Cities { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Cities As CitySet 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property CitySet^ Cities { 	CitySet^ get (); } ``` |

# Remarks

Each city has information about longitude, latitude etc.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Get all Revit support cities
Autodesk.Revit.DB.CitySet cities = application.Cities;

// Set all Revit support cities into an ArrayList
System.Collections.ArrayList cityList = new System.Collections.ArrayList();
foreach (Autodesk.Revit.DB.City city in cities)
{
    cityList.Add(city);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Get all Revit support cities
Dim cities As Autodesk.Revit.DB.CitySet = application.Cities

' Set all Revit support cities into an ArrayList
Dim cityList As New System.Collections.ArrayList()
For Each city As Autodesk.Revit.DB.City In cities
    cityList.Add(city)
Next
```

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)