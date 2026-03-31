using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Revit.SDK.Samples.CoordinationModels.CS
{
   public partial class CategoriesForm : Form
   {
      public List<string> SelectedCategories { get; private set; }

      public CategoriesForm(IList<string> categories)
      {
         InitializeComponent();

         Categories.Items.AddRange(categories.ToArray());
      }

      private void OK_Click(object sender, EventArgs e)
      {
         SelectedCategories = new List<string>();
         foreach (var item in Categories.SelectedItems)
         {
            SelectedCategories.Add(item.ToString());
         }

         Close();
      }

      private void Cancel_Click(object sender, EventArgs e)
      {
         Close();
      }
   }
}
