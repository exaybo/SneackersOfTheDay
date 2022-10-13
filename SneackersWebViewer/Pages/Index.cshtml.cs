using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using SneackersWebViewer.Controllers;
using SneackersWebViewer.Models;

namespace SneackersWebViewer.Pages
{
    public class IndexModel : PageModel
    {
        private readonly ILogger<IndexModel> _logger;
        private readonly ISneackersContext _sneackersContext;

        public IndexModel(ILogger<IndexModel> logger, ISneackersContext sneackersContext)
        {
            _logger = logger;
            _sneackersContext = sneackersContext;
        }

        string GetRandomImageUri()
        {
            Random random = new Random();
            var snkList = _sneackersContext.GetAllSneackers();
            if(snkList.Count() == 0)
                return string.Empty;
            int idsnk = random.Next(snkList.Count());
            Sneacker snk = snkList[idsnk];
            if (snk.ImgUriList.Count() == 0)
                return string.Empty;
            int idimg = random.Next(snk.ImgUriList.Count());

            return snk.ImgUriList[idimg];
        }


        public void OnGet()
        {

        }

        public IActionResult OnGetRandomImg()
        { 
            return new JsonResult(GetRandomImageUri());
        }
    }
}