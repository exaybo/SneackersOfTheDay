using MongoDB.Bson;

namespace SneackersWebViewer.Models
{
    public class Attempt
    {
        public ObjectId Id { get; set; }
        public int CountToLoad { get; set; }
        public int CountOfLoaded { get; set; }
        public DateTime Date { get; set; }
        public string Source { get; set; }
        public List<string> ErrorList { get; set; }
    }
}
