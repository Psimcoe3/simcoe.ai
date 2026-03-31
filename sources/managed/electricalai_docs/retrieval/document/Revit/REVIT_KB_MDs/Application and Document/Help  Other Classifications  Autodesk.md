---
created: 2026-01-28T20:43:31 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Other Classifications | Autodesk

> ## Excerpt
> Elements can be classified by Category, Family, Symbol and Instance.

---
Elements can be classified by Category, Family, Symbol and Instance.

There are some relationships between the classifications. For example:

-   You can distinguish different kinds of FamilyInstances by the category. Items such as structural columns are in the Structural Columns category, beams and braces are in the Structural Framing category, and so on.
-   You can differentiate structural FamilyInstance Elements by their symbol.
    
    ### Category
    

The Element.Category property represents the category or subcategory to which an Element belongs. It is used to identify the Element type. For example, anything in the walls Category is considered a wall. Other categories include doors and rooms.

Categories are the most general class. The Document.Settings.Categories property is a map that contains all Category objects in the document and is subdivided into the following:

-   Model Categories - Model Categories include beams, columns, doors, windows, and walls.
-   Annotation Categories. Annotation Categories include dimensions, grids, levels, and textnotes.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-4C0CA7CF-C5CF-4042-B99D-AE185F64D17F-low.png)**Figure 20: Categories**

Note: The following guidelines apply to categories:

-   In general, the following rules apply to categories:
    -   Each family object belongs to a category
    -   Non-family objects, like materials and views, do not belong to a category
    -   There are exceptions such as ProjectInfo, which belongs to the Project Information category.
-   An element and its corresponding symbols are usually in the same category. For example, a basic wall and its wall type Generic - 8" are all in the Walls category.
-   The same type of Elements can be in different categories. For example, SpotDimensions has the SpotDimensionType, but it can belong to two different categories: Spot Elevations and Spot Coordinates.
-   Different Elements can be in the same category because of their similarity or for architectural reasons. ModelLine and DetailLine are in the Lines category.

To gain access to the categories you may access all categories from the document's Settings class (for example, to insert a new category set), or if you only need access to a category object associated with a built-in category, you may access the category object directly from the static overloaded GetCategory() method of the Category class.

To access categories:

-   Get an entire map of Categories from the document properties: Document.Settings.Categories returns a CategoryNameMap containing a map of all Revit categories indexed by their name. `Category.IsVisibleInUI` returns true if the category is visible to the user in lists of categories in the Revit user interface (dialogs such as Visibility Graphics or View Filters)
-   Get a specific built-in category by calling the appropriate overload of the static method Category.GetCategory().
-   Get a specific category or subcategory by its ElementId by calling the corresponding overload of the static method Category.GetCategory().

<table summary="" id="GUID-5D2ED5AF-7D4F-49BE-85E8-68CB49BD8178__TABLE_8F0B43132FB64B63880CFD0EB41FCFA4"><tbody><tr><td><b>Code Region 5-1: Getting categories from document settings</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetCategories</span><span>(</span><span>Document</span><span> document</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>// Get settings of current document</span><span>
    </span><span>Settings</span><span> documentSettings </span><span>=</span><span> document</span><span>.</span><span>Settings</span><span>;</span><span>

    </span><span>// Get all categories of current document</span><span>
    </span><span>Categories</span><span> groups </span><span>=</span><span> documentSettings</span><span>.</span><span>Categories</span><span>;</span><span>

    </span><span>// Show the number of all the categories to the user</span><span>
    </span><span>String</span><span> prompt </span><span>=</span><span> </span><span>"Number of all categories in current Revit document:"</span><span> </span><span>+</span><span> groups</span><span>.</span><span>Size</span><span>;</span><span> 

    </span><span>// get Floor category according to OST_Floors and show its name</span><span>
    </span><span>Category</span><span> floorCategory </span><span>=</span><span> groups</span><span>.</span><span>get_Item</span><span>(</span><span>BuiltInCategory</span><span>.</span><span>OST_Floors</span><span>);</span><span>
    prompt </span><span>+=</span><span> floorCategory</span><span>.</span><span>Name</span><span>;</span><span>

    </span><span>// Give the user some information</span><span>
    </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span> prompt</span><span>);</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Category is used in the following manner:

-   Category is used to classify elements. The element category determines certain behaviors. For example, all elements in the same category can be included in the same schedule.
-   Elements have parameters based on their categories.
-   Categories are also used for controlling visibility and graphical appearance in Revit.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-FD2C68CC-B442-4A39-B507-8965B15B1DCF-low.png)

**Figure 21: Visibility by Category**

An element's category is determined by the Category ID.

-   Category IDs are represented by the ElementId class.
-   Imported Category IDs correspond to elements in the document.
-   Most categories are built-in and their IDs are constants stored in ElementIds.
-   Each built-in category ID has a corresponding value in the BuiltInCategory Enumeration. They can be converted to corresponding BuiltInCategory enumerated types. `LabelUtils.GetLabelFor(BuiltInCategory)` returns the string name of the given BuiltInCategory in the current Revit language.
-   If the category is not built-in, the ID is converted to a null value.

<table summary="" id="GUID-5D2ED5AF-7D4F-49BE-85E8-68CB49BD8178__TABLE_BB8156D2B13340B8A39BD2CC3F794499"><tbody><tr><td><b>Code Region 5-2: Getting element category</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetElementCategory</span><span>(</span><span>UIDocument</span><span> uidoc</span><span>)</span><span>
</span><span>{</span><span>
    </span><span>Element</span><span> selectedElement </span><span>=</span><span> </span><span>null</span><span>;</span><span>
    </span><span>foreach</span><span> </span><span>(</span><span>ElementId</span><span> id </span><span>in</span><span> uidoc</span><span>.</span><span>Selection</span><span>.</span><span>GetElementIds</span><span>())</span><span>
    </span><span>{</span><span>
        selectedElement </span><span>=</span><span> uidoc</span><span>.</span><span>Document</span><span>.</span><span>GetElement</span><span>(</span><span>id</span><span>);</span><span>
        </span><span>break</span><span>;</span><span>  </span><span>// just get one selected element</span><span>
    </span><span>}</span><span>

    </span><span>// Get the category instance from the Category property</span><span>
    </span><span>Category</span><span> category </span><span>=</span><span> selectedElement</span><span>.</span><span>Category</span><span>;</span><span>

    </span><span>BuiltInCategory</span><span> enumCategory </span><span>=</span><span> </span><span>(</span><span>BuiltInCategory</span><span>)</span><span>category</span><span>.</span><span>Id</span><span>.</span><span>IntegerValue</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

Note: To avoid Globalization problems when using Category.Name, BuiltInCategory is a better choice. Category.Name can be different in different languages.

### Family

Families are classes of Elements within a category. Families can group Elements by the following:

-   A common set of parameters (properties).
-   Identical use.
-   Similar graphical representation.

Most families are component Family files, meaning that you can load them into your project or create them from Family templates. You determine the property set and the Family graphical representation.

Another family type is the system Family. System Families are not available for loading or creating. Revit predefines the system Family properties and graphical representation; they include walls, dimensions, roofs, floors (or slabs), and levels.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-428BCB2F-3741-4F05-A51A-9D5A9A03813D-low.png)**Figure 22: Families**

In addition to functioning as an Element class, Family is also a template used to generate new items that belong to the Family.

#### Family in the Revit Platform API

In the Revit Platform API, both the Family class and FamilyInstance belong to the Component Family. Other Elements include System Family.

Families in the Revit Platform API are represented by three objects:

-   Family
-   FamilySymbol
-   FamilyInstance.

Each object plays a significant role in the Family structure.

The Family object has the following characteristics:

-   Represents an entire family such as a beam.
-   Represents the entire family file on a disk.
-   Contains a number of FamilySymbols.

The FamilySymbol object represents a specific set of family settings in the Family such as the Type, Concrete-Rectangular Beam: 16×32.

The FamilyInstance object is a FamilySymbol instance representing a single instance in the Revit project. For example, the FamilyInstance can be a single instance of a 16×32 Concrete-Rectangular Beam in the project.

Note: Remember that the FamilyInstance exists in FamilyInstance Elements, Datum Elements, and Annotation Elements.

Consequently, the following rules apply:

-   Each FamilyInstance has one FamilySymbol.
-   Each FamilySymbol belongs to one Family.
-   Each Family contains one or more FamilySymbols.

For more detailed information, see [Family Instances](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_html).

### ElementType

In the Revit Platform API, Symbols are usually non-visible elements used to define instances. Symbols are called Types in the user interface.

-   A type can be a specific size in a family, such as a 1730 × 2032 door, or an 8×4×1/2 angle.
-   A type can be a style, such as default linear or default angular style for dimensions.

Symbols represent Elements that contain shared data for a set of similar elements. In some cases, Symbols represent building components that you can get from a warehouse, such as doors or windows, and can be placed many times in the same building. In other cases, Symbols contain host object parameters or other elements. For example, a WallType Symbol contains the thickness, number of layers, material for each layer, and other properties for a particular wall type.

FamilySymbol is a symbol in the API. It is also called Family Type in the Revit user interface. FamilySymbol is a class of elements in a family with the exact same values for all properties. For example, all 32×78 six-panel doors belong to one type, while all 24×80 six-panel doors belong to another type. Like a Family, a FamilySymbol is also a template. The FamilySymbol object is derived from the ElementType object and the Element object.

### Instance

Instances are items with specific locations in the building (model instances) or on a drawing sheet (annotation instances). Instance represents transformed identical copies of an ElementType. For example, if a building contains 20 windows of a particular type, there is one ElementType with 20 Instances. Instances are called Components in the user interface.

Note: For FamilyInstance, the Symbol property can be used instead of the GetTypeId() method to get the corresponding FamilySymbol. It is convenient and safe since you do not need to do a type conversion.
