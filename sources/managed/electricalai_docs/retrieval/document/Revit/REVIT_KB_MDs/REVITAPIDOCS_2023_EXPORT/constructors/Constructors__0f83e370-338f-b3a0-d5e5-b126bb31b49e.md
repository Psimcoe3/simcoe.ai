[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ImageExportOptions Members

---



|  |
| --- |
| [ImageExportOptions Class](c2e823a1-6eb0-2bf3-f07b-ed46d8f7b70a.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [ImageExportOptions](c2e823a1-6eb0-2bf3-f07b-ed46d8f7b70a.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [ImageExportOptions](fa14ebd5-72be-c63f-fa9e-a84e33cd5567.htm) | Constructs a new instance of the options class used to produce images. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](514d82df-3b74-9696-fb98-1c4a8f3887cd.htm) | Releases all resources used by the  [ImageExportOptions](c2e823a1-6eb0-2bf3-f07b-ed46d8f7b70a.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method Static member | [GetFileName](0f5a2275-9fcb-2d85-2ccc-0190dbb21b9b.htm) | Gets the file name that will be produced when exporting a view to an image. |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetViewsAndSheets](b5e34c47-572e-8901-4b37-6ad86153a67f.htm) | Gets a list of views and sheets to be exported. Used only when ExportRange is SetOfViews. |
| Public method Static member | [IsValidFileName](f3618687-c964-60cc-a6a1-2ccd1f192ba9.htm) | Verify if File name is valid |
| Public method Static member | [IsValidForSaveToProjectAsImage](5c064e7c-4fc6-035f-7c35-3e6a735e552f.htm) | Verify if ImageExportOptions object is valid for calling saveToProjectAsImage |
| Public method | [SetViewsAndSheets](f9ac839c-2722-2249-1be8-5033601b948f.htm) | Sets a list of views and sheets to be exported. Used only when ExportRange is SetOfViews. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ExportRange](10472c5c-13f5-abf1-ee1d-751094b0a7cb.htm) | The export range defining which view(s) will be exported. |
| Public property | [FilePath](f771e862-4b30-98aa-63a7-af382b1d6d72.htm) | The file name and path for the exported file. |
| Public property | [FitDirection](37d97820-8b1e-8987-d210-78f594aa76da.htm) | The fit direction. Used only if ZoomType is FitToPage. |
| Public property | [HLRandWFViewsFileType](43d9d802-42bd-b161-a249-a133be427d28.htm) | File type for exported HLR and wireframe views. |
| Public property | [ImageResolution](4dd2bc52-4ece-d7e8-cb96-c2ebc645fb5d.htm) | The image resolution in dots per inch. |
| Public property | [IsValidObject](795ceab7-beda-8a76-58d5-d1f1fbf3910e.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [PixelSize](558f150d-0b11-26cc-0516-19af55eea2a4.htm) | The pixel size of an image in one direction. Used only if ZoomType is FitToPage. |
| Public property | [ShadowViewsFileType](0bc687d3-64d3-0e0e-8095-f51cea1634ee.htm) | The file type for exported shadow views. |
| Public property | [ShouldCreateWebSite](e7f6b59a-2846-8036-8ff6-718e9d83062b.htm) | Whether or not to create a web site with a page for each export. Used only when ExportRange is SetOfViews. |
| Public property | [ViewName](d264fa66-1a71-be0e-e203-ba497bccc61d.htm) | The name of the view to be created. |
| Public property | [Zoom](6ab4f8bb-3abb-8c49-eefd-642e9d57a262.htm) | The value for Zoom (as a percentage). Used only when ZoomType is Zoom. |
| Public property | [ZoomType](a3e468fa-4a19-bb8a-1029-8ab47806975c.htm) | The zoom type, which defines how the image size is determined. |

# See Also

[ImageExportOptions Class](c2e823a1-6eb0-2bf3-f07b-ed46d8f7b70a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)