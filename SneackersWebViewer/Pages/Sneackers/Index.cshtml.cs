using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using MongoDB.Bson;
using SneackersWebViewer.Controllers;
using SneackersWebViewer.Models;

namespace SneackersWebViewer.Pages.Sneackers
{
    public class IndexModel : PageModel
    {
        private readonly ISneackersContext _sneackersContext;

        public IndexModel(ISneackersContext sneackersContext)
        {
            _sneackersContext = sneackersContext;

        }

        public List<Sneacker> Sneackers { get { return _sneackersContext.GetAllSneackers(); } }
        public Sneacker? CurrentSneacker { get; set; } = default;
        public void OnGet()
        {

        }

        public void OnGetSetCurrent( string id )
        {
            CurrentSneacker = Sneackers.FirstOrDefault(s => s.Id.ToString() == id);
            // code goes here 
            //RedirectToPage();
        }

        public async Task<IActionResult> OnPostSetCurrentAsync(string id)
        {
            

            return RedirectToPage();
        }
    }
}
