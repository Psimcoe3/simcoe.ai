---
created: 2026-01-28T20:58:56 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Documents_About_family_documents_html
author: 
---

# Help | About family documents | Autodesk

> ## Excerpt
> The Family object represents an entire Revit family. A Family Document is a Document that represents a Family rather than a Revit project.

---
### Family

The Family object represents an entire Revit family. A Family Document is a Document that represents a Family rather than a Revit project.

Using the Family Creation functionality of the Revit API, you can create and edit families and their types. This functionality is particularly useful when you have pre-existing data available from an external system that you want to convert to a Revit family library.

API access to system family editing is not available.

### Categories

As noted in the previous section, the Family.FamilyCategory property indicates the category of the Family such as Columns, Furniture, Structural Framing, or Windows.

The following code can be used to determine the category of the family in an open Revit Family document.

<table summary="" id="GUID-DC143EB8-43CB-48AB-938E-7ADE3A9D2E63__TABLE_B6FD7EC439184ADBA192B4D5489B8B33"><tbody><tr><td><b>Code Region 13-1: Category of open Revit Family Document</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetName</span><span>(</span><span>Document</span><span> familyDoc</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>string</span><span> categoryName </span><span>=</span><span> familyDoc</span><span>.</span><span>OwnerFamily</span><span>.</span><span>FamilyCategory</span><span>.</span><span>Name</span><span>;</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

The FamilyCategory can also be set, allowing the category of a family that is being edited to be changed.

### Parameters

Family parameters can be accessed from the OwnerFamily property of a Family Document as the following example shows.

<table summary="" id="GUID-DC143EB8-43CB-48AB-938E-7ADE3A9D2E63__TABLE_F1CC348A35C04D17A2CFC7F39639E941"><tbody><tr><td><b>Code Region 13-2: Category of open Revit Family Document</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetFamilyDocumentCategory</span><span>(</span><span>Document</span><span> familyDoc</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// get the owner family of the family document.</span><span>
        </span><span>Family</span><span> family </span><span>=</span><span> familyDoc</span><span>.</span><span>OwnerFamily</span><span>;</span><span> 
        </span><span>Parameter</span><span> param </span><span>=</span><span> family</span><span>.</span><span>GetParameter</span><span>(</span><span>ParameterTypeId</span><span>.</span><span>FamilyWorkPlaneBased</span><span>);</span><span>
        </span><span>// this param is a Yes/No parameter in UI, but an integer value in API</span><span>
        </span><span>// 1 for true and 0 for false</span><span>
        </span><span>int</span><span> isTrue </span><span>=</span><span> param</span><span>.</span><span>AsInteger</span><span>();</span><span> 
        </span><span>// param.Set(1); // set value to true.</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Creating a Family Document

The ability to modify Revit Family documents and access family types and parameters is available from the Document class if the Document is a Family document, as determined by the IsFamilyDocument property. To edit an existing family while working in a Project document, use the EditFamily() functions available from the Document class, and then use LoadFamily() to reload the family back into the owner document after editing is complete. To create a new family document use Application.NewFamilyDocument():

<table summary="" id="GUID-DC143EB8-43CB-48AB-938E-7ADE3A9D2E63__TABLE_C37ED16E984740C4A6727147592EB25D"><tbody><tr><td><b>Code Region 13-3: Creating a new Family document</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>CreateFamily</span><span>(</span><span>Application</span><span> application</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>// create a new family document using Generic Model.rft template</span><span>
        </span><span>string</span><span> templateFileName </span><span>=</span><span> </span><span>@</span><span>"C:\Documents and Settings\All Users\Application Data\Autodesk\RST 2011\Imperial Templates\Generic Model.rft"</span><span>;</span><span>

        </span><span>Document</span><span> familyDocument </span><span>=</span><span> application</span><span>.</span><span>NewFamilyDocument</span><span>(</span><span>templateFileName</span><span>);</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>==</span><span> familyDocument</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>throw</span><span> </span><span>new</span><span> </span><span>Exception</span><span>(</span><span>"Cannot open family document"</span><span>);</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>

### Nested Family Symbols

You can filter a Family Document for FamilySymbols to get all of the FamilySymbols loaded into the Family. In this code sample, all the nested FamilySymbols in the Family for a given FamilyInstance are listed.

<table summary="" id="GUID-DC143EB8-43CB-48AB-938E-7ADE3A9D2E63__TABLE_2EBB4BE77E4C4D0E890F1236C7290DFC"><tbody><tr><td><b>Code Region 13-4: Getting nested Family symbols in a Family</b></td></tr><tr><td><pre><code><span>public</span><span> </span><span>void</span><span> </span><span>GetLoadedSymbols</span><span>(</span><span>Autodesk</span><span>.</span><span>Revit</span><span>.</span><span>DB</span><span>.</span><span>Document</span><span> document</span><span>,</span><span> </span><span>FamilyInstance</span><span> familyInstance</span><span>)</span><span>
</span><span>{</span><span>
        </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> familyInstance</span><span>.</span><span>Symbol</span><span>)</span><span>
        </span><span>{</span><span>
                </span><span>// Get family associated with this</span><span>
                </span><span>Family</span><span> family </span><span>=</span><span> familyInstance</span><span>.</span><span>Symbol</span><span>.</span><span>Family</span><span>;</span><span>

                </span><span>// Get Family document for family</span><span>
                </span><span>Document</span><span> familyDoc </span><span>=</span><span> document</span><span>.</span><span>EditFamily</span><span>(</span><span>family</span><span>);</span><span>
                </span><span>if</span><span> </span><span>(</span><span>null</span><span> </span><span>!=</span><span> familyDoc </span><span>&amp;&amp;</span><span> familyDoc</span><span>.</span><span>IsFamilyDocument</span><span> </span><span>==</span><span> </span><span>true</span><span>)</span><span>
                </span><span>{</span><span>
                        </span><span>String</span><span> loadedFamilies </span><span>=</span><span> </span><span>"FamilySymbols in "</span><span> </span><span>+</span><span> family</span><span>.</span><span>Name</span><span> </span><span>+</span><span> </span><span>":\n"</span><span>;</span><span>
                        </span><span>FilteredElementCollector</span><span> collector </span><span>=</span><span> </span><span>new</span><span> </span><span>FilteredElementCollector</span><span>(</span><span>document</span><span>);</span><span>
                        </span><span>ICollection</span><span>&lt;</span><span>Element</span><span>&gt;</span><span> collection </span><span>=</span><span> 
                                collector</span><span>.</span><span>OfClass</span><span>(</span><span>typeof</span><span>(</span><span>FamilySymbol</span><span>)).</span><span>ToElements</span><span>();</span><span>
                        </span><span>foreach</span><span> </span><span>(</span><span>Element</span><span> e </span><span>in</span><span> collection</span><span>)</span><span>
                        </span><span>{</span><span>
                                </span><span>FamilySymbol</span><span> fs </span><span>=</span><span> e </span><span>as</span><span> </span><span>FamilySymbol</span><span>;</span><span>
                                loadedFamilies </span><span>+=</span><span> </span><span>"\t"</span><span> </span><span>+</span><span> fs</span><span>.</span><span>Name</span><span> </span><span>+</span><span> </span><span>"\n"</span><span>;</span><span>
                        </span><span>}</span><span>

                        </span><span>TaskDialog</span><span>.</span><span>Show</span><span>(</span><span>"Revit"</span><span>,</span><span>loadedFamilies</span><span>);</span><span>
                </span><span>}</span><span>
        </span><span>}</span><span>
</span><span>}</span></code></pre></td></tr></tbody></table>
