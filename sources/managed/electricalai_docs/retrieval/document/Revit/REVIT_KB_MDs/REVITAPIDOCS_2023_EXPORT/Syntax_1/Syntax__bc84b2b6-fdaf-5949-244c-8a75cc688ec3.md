[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetLinePatternId Method

---



|  |
| --- |
| [Category Class](d390ecf6-e5db-d7c1-d7f2-766c0686e975.htm)   [See Also](#seeAlsoToggle) |

Sets the line pattern id associated with this category for the given graphics style type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetLinePatternId( 	ElementId linePatternId, 	GraphicsStyleType graphicsStyleType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetLinePatternId ( _ 	linePatternId As ElementId, _ 	graphicsStyleType As GraphicsStyleType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetLinePatternId( 	ElementId^ linePatternId,  	GraphicsStyleType graphicsStyleType ) ``` |

#### Parameters

linePatternId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The line pattern id for the graphics style.

graphicsStyleType
:   Type:  [Autodesk.Revit.DB GraphicsStyleType](60a5cce6-2cdc-dd63-e737-f584582ceeca.htm)    
     The type of graphics style.

# Remarks

* The line pattern id will be one of the following:
* A negative value (representing a built-in line pattern); this value can only be obtained via GetLinePatternId
* The id of a LinePatternElement

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Thrown when the input argument "linePatternId" is an illegal id. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when this category does not have stored line pattern id for this graphics style type. |

# See Also

[Category Class](d390ecf6-e5db-d7c1-d7f2-766c0686e975.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)