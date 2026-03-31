[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InCanvasControlData Constructor (String, XYZ)

---



|  |
| --- |
| [InCanvasControlData Class](5fdf010d-7dbb-332d-4704-8e067f2338dc.htm)   [See Also](#seeAlsoToggle) |

Constructs an InCanvasControlData with specific values assigned.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public InCanvasControlData( 	string imagePath, 	XYZ position ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	imagePath As String, _ 	position As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: InCanvasControlData( 	String^ imagePath,  	XYZ^ position ) ``` |

#### Parameters

imagePath
:   Type:  System String    
     File path with the image to be used. This must be an absolute path to a location on disk.

position
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The position to be used.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The file format specified by imagePath is an unsupported format - only \*.bmp files are supported. -or- The file path specified by imagePath is not absolute. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | The file specified by imagePath doesn't exist. |

# See Also

[InCanvasControlData Class](5fdf010d-7dbb-332d-4704-8e067f2338dc.htm)

[InCanvasControlData Overload](995d0129-b6ab-4640-f476-7fdfde9ee7d8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)