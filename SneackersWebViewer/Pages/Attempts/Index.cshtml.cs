using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using SneackersWebViewer.Controllers;
using SneackersWebViewer.Models;

namespace SneackersWebViewer.Pages.Attempts
{
    public class IndexModel : PageModel
    {
        public List<Attempt> Attempts {get { return _sneackersContext.GetAllAttempts(); } }

        private readonly ISneackersContext _sneackersContext;
        public IndexModel(ISneackersContext sneackersContext)
        {
            _sneackersContext = sneackersContext;
        }
        public Attempt? CurrentAttempt{ get; set; } = default;
        public void OnGet()
        {

        }

        public void OnGetSetCurrent(string id)
        {
            CurrentAttempt = Attempts.FirstOrDefault(s => s.Id.ToString() == id);
            // code goes here 
            //RedirectToPage();
        }
    }
}
