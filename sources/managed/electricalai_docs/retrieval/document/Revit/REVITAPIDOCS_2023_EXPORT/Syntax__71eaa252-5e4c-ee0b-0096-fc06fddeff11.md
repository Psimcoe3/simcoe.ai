[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewDisplayBackgroundImageFlags Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

A collection of bit flags that control how the background image is positioned in relation to the crop region (or the view boundary).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public enum ViewDisplayBackgroundImageFlags ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ViewDisplayBackgroundImageFlags ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ViewDisplayBackgroundImageFlags ``` |

# Members

| Member name | Description |
| --- | --- |
| None | The image is displayed pixel-to-pixel |
| FitToScreen | The image is stretched in both directions |
| FixedAspectRatio | The image is stretched but the ratio of its height to width is preserved. |
| UseTiling | The pixels of the background are filled by tiling of the image. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)