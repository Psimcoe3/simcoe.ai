[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### City Class

---



|  |
| --- |
| [Members](8f9a8aca-067a-1e06-0946-e5092634a254.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

An object that contains geographical location information for a known city.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class City : APIObject ``` |

 

| Visual Basic |
| --- |
| ``` Public Class City _ 	Inherits APIObject ``` |

 

| Visual C++ |
| --- |
| ``` public ref class City : public APIObject ``` |

# Remarks

This object contains longitude, latitude, time zone information for a city already known by Revit. Currently Revit does not the ability to add cities to the existing list. The list of known cities can be retrieved using the Cities property on the application object.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
double angleRatio = Math.PI / 180;   // ratio of Angle

// Get the Latitude information
double latiude = city.Latitude / angleRatio;
String latiudeInfo = "Latitude:      " + latiude.ToString();

// Get the Longitude information
double longitude = city.Longitude / angleRatio;
String longitudeInfo = "Longitude:   " + longitude.ToString();

// Get the TimeZone information
String timeZoneInfo = "TimeZone:   " + city.TimeZone.ToString();

// Set the information text box.
string cityInfo = latiudeInfo + "\n" + longitudeInfo
                            + "\n" + timeZoneInfo;
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Dim angleRatio As Double = Math.PI / 180
' ratio of Angle
' Get the Latitude information
Dim latiude As Double = city.Latitude / angleRatio
Dim latiudeInfo As [String] = "Latitude:      " & latiude.ToString()

' Get the Longitude information
Dim longitude As Double = city.Longitude / angleRatio
Dim longitudeInfo As [String] = "Longitude:   " & longitude.ToString()

' Get the TimeZone information
Dim timeZoneInfo As [String] = "TimeZone:   " & city.TimeZone.ToString()

' Set the information text box.
Dim cityInfo As String = latiudeInfo & vbLf & longitudeInfo & vbLf & timeZoneInfo
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB City

# See Also

[City Members](8f9a8aca-067a-1e06-0946-e5092634a254.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)